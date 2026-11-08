"""Exact finite tests for single-root spanning-tree degree identification.
Standard library only. Graph counts use matrix-tree cofactors independently
of the factorization used in the proof.
"""
from fractions import Fraction
from itertools import combinations


def partitions(n, lo=1):
    if n == 0:
        yield ()
    else:
        for first in range(lo, n + 1):
            for tail in partitions(n - first, first):
                yield (first,) + tail


def determinant(a):
    a = [list(row) for row in a]
    n = len(a)
    if n == 0:
        return 1
    sign = 1
    prev = 1
    for k in range(n - 1):
        if a[k][k] == 0:
            pivot = next((h for h in range(k+1, n) if a[h][k] != 0), None)
            if pivot is None:
                return 0
            a[k], a[pivot] = a[pivot], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = a[i][j] * pivot - a[i][k] * a[k][j]
                assert numerator % prev == 0
                a[i][j] = numerator // prev
        for i in range(k + 1, n):
            a[i][k] = 0
        prev = pivot
    return sign * a[-1][-1]


def tree_count(parts, root, z):
    n=sum(parts)
    labels=sum(([i] * m for i,m in enumerate(parts)),[])
    L=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(i+1,n):
            if labels[i] != labels[j]:
                w=z if root in (i,j) else 1
                L[i][i] += w
                L[j][j] += w
                L[i][j] -= w
                L[j][i] -= w
    return determinant([row[:-1] for row in L[:-1]])


def expected_value(parts, root_part, z):
    n=sum(parts); r=len(parts)
    product=Fraction(z,1) * Fraction(n-1+z,n)**(r-2)
    for j, nj in enumerate(parts):
        if j != root_part:
            product*=Fraction(n-nj-1+z,n-nj)**(nj-1)
    return product


def pgf_coeffs(values):
    # Newton interpolation at integer arguments 0,1,...,n-1.
    diffs=list(map(Fraction,values))
    a=[]
    while diffs:
        a.append(diffs[0])
        diffs=[diffs[i+1]-diffs[i] for i in range(len(diffs)-1)]
    coeffs=[Fraction(0)]*len(values)
    basis=[Fraction(1)]
    for k,ak in enumerate(a):
        for i, bi in enumerate(basis):
            coeffs[i]+=ak*bi
        # basis for next k = falling factorial x(x-1).../ k!
        next_basis=[Fraction(0)]*(len(basis)+1)
        for i,b in enumerate(basis):
            next_basis[i] += -Fraction(k,k+1)*b
            next_basis[i+1]+=Fraction(1,k+1)*b
        basis=next_basis
    return coeffs


def divided_by_linear(coeffs, root):
    # Polynomial division by (x-root); low-degree-first coefficients.
    n=len(coeffs)-1
    q=[Fraction(0)]*n
    q[-1]=coeffs[-1]
    for j in range(n-2,-1,-1):
        q[j]=coeffs[j+1]+root*q[j+1]
    rem=coeffs[0]+root*q[0]
    return q,rem


def decode(parts, root_part):
    n=sum(parts);r=len(parts)
    root=sum(parts[:root_part])
    values=[Fraction(tree_count(parts,root,z), tree_count(parts,root,1)) for z in range(n)]
    poly=pgf_coeffs(values)
    # Confirm interpolation in an extra independent evaluation.
    assert sum(c * n**k for k,c in enumerate(poly)) == Fraction(tree_count(parts,root,n),tree_count(parts,root,1))
    cur=list(poly)
    while len(cur)>1 and cur[-1]==0:
        cur.pop()
    multiplicity={}
    for a in range(0,n):
        k=0
        while len(cur)>1:
            nxt, rem=divided_by_linear(cur,-a)
            if rem: break
            cur=nxt;k+=1
        if k: multiplicity[a]=k
    assert len(cur)==1 and cur[0]!=0, (parts,root_part,cur)
    global_root=n-1
    rec_r=multiplicity.get(global_root,0)+2
    assert rec_r==r, (parts,root_part,rec_r,multiplicity)
    other=[]
    for a,k in multiplicity.items():
        if a==global_root: continue
        # For original root z, factor n-j-1+z; zero of root z=-(n-j-1)
        # The root z=0 always includes the mandatory z prefactor.
        if a==0:
            k-=1
        if k==0:
            continue
        part_size=n-a-1
        assert part_size >= 2
        assert k>=0 and k%(part_size-1)==0,(parts,root_part,k,part_size)
        other.extend([part_size]*(k//(part_size-1)))
    # For a=0, the standard prefactor z may occur without a 0-root factor
    if 0 not in multiplicity: raise AssertionError('every degree >=1')
    other.extend([1]*(rec_r-1-len(other)))
    own=n-sum(other)
    assert own>=1,(parts,root_part,other)
    return tuple(sorted(other+[own]))


def main():
    total=0
    count=0
    seen={}
    for n in range(2,10):
        for part in partitions(n):
            if len(part)<2: continue
            seen.setdefault(n,{})
            for i in range(len(part)):
                root=sum(part[:i]); normal=tree_count(part,root,1)
                assert normal>0
                for z in range(n+1):
                    expected=expected_value(part,i,z)
                    actual=Fraction(tree_count(part,root,z),normal)
                    assert actual==expected,(part,i,z,actual,expected)
                    total+=1
                recovered=decode(part,i)
                assert recovered==part,(part,i,recovered)
                count+=1
                signature=tuple(Fraction(tree_count(part,root,z),normal) for z in range(n+1))
                former=seen[n].get(signature)
                assert former is None or former==part, (former,part,i)
                seen[n][signature]=part
    print('VERIFY_OK', 'matrix_tree_point_assertions',total,'reconstructions',count)

if __name__ == '__main__':
    main()
