"""Exact modular tests for Walsh-coordinate control on binary cubes.
No external packages, internet, or other files are needed.
The algebraic all-dimensional theorem is established in RESULT.md; these are tests.
"""
from itertools import combinations
from math import comb
P = 1000003

def masks(d, j):
    return [sum(1<<i for i in c) for c in combinations(range(d), j)]

def rank_mod(A):
    if not A: return 0
    a = [row[:] for row in A]
    m,n=len(a),len(a[0]); r=0
    for col in range(n):
        pivot=next((i for i in range(r,m) if a[i][col]%P),None)
        if pivot is None: continue
        a[r],a[pivot]=a[pivot],a[r]
        inv=pow(a[r][col]%P,-1,P)
        for i in range(r+1,m):
            if a[i][col]%P:
                z=a[i][col]*inv%P
                rowi,rowr=a[i],a[r]
                for j in range(col,n):
                    rowi[j]=(rowi[j]-z*rowr[j])%P
        r+=1
        if r==m: break
    return r

def testing(d,rows):
    assert len(set(rows))==len(rows)
    result=[]
    for j in range(d+1):
        cols=masks(d,j)
        A=[[1 if ((s&t).bit_count()%2==0) else P-1 for t in cols] for s in rows]
        rank=rank_mod(A)
        assert rank==len(cols), ('rank deficiency',d,j,rank,len(cols))
        result.append((j,rank))
    return result

def harmonic_action_test():
    # Explicit harmonic vector formed from ell disjoint coordinate pairs.
    # On a j-subset T, its lift is product of paired-membership differences.
    checks=0
    for d in (3,5,7,9):
        k=d//2
        rows=masks(d,k)
        for ell in range(k+1):
            def lift(t):
                z=1
                for i in range(ell):
                    z*=((t>>(2*i))&1)-((t>>(2*i+1))&1)
                return z
            for j in range(ell,k+1):
                cols=masks(d,j)
                alpha=(-2)**ell*(-1)**((j-ell)//2)*comb(k-ell,(j-ell)//2)
                for s in rows:
                    lhs=sum((1 if ((s&t).bit_count()%2)==0 else -1)*lift(t) for t in cols)
                    assert lhs==alpha*lift(s),(d,ell,j,s,lhs,alpha*lift(s))
                    checks+=1
    print('Passed:',checks,'exact integer harmonic intertwining comparisons.')

def main():
    num_levels=0
    for d in (1,3,5,7,9):
        k=d//2
        rows=masks(d,k)
        ans=testing(d,rows)
        assert len(rows)==comb(d,k)
        num_levels+=len(ans)
        print('odd d',d,'rows',len(rows),'level ranks',[r for j,r in ans])
    for d in (2,4,6,8):
        k=d//2
        low=masks(d-1,k-1)
        rows=low+[s|(1<<(d-1)) for s in low]
        ans=testing(d,rows)
        assert len(rows)==comb(d,k)
        num_levels+=len(ans)
        print('even d',d,'rows',len(rows),'level ranks',[r for j,r in ans])
        # The tempting central sphere fails at its central eigenspace.
        center=masks(d,k)
        assert len(center)==comb(d,k)
        assert all(((s^((1<<d)-1)).bit_count()==k) for s in center)
        cols=masks(d,k)
        A=[[1 if ((s&t).bit_count()%2==0) else P-1 for t in cols] for s in center]
        actual=rank_mod(A)
        assert actual==len(center)//2,(d,actual)
        print('even central sphere fails: rank',actual,'of',len(center))
    # Leading harmonic scalar, with polynomial coefficient calculated exactly.
    # For odd n=2k+1, alpha_lj=(-2)^l coeff[z^(j-l)] (1-z^2)^(k-l)(1+z).
    count=0
    for k in range(1,25):
        for j in range(k+1):
            for ell in range(j+1):
                t=j-ell
                coeff=(-1)**(t//2)*comb(k-ell,t//2)
                assert coeff!=0
                count+=1
    harmonic_action_test()
    print('Passed:',num_levels,'full-rank PBH eigenspace checks and',count,'symbolic coefficient nonvanishing checks.')

if __name__=='__main__': main()
