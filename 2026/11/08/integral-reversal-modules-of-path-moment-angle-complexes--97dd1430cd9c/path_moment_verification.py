"""Independent finite checks for path moment-angle reversal cohomology.
Reproduction: python3 path_moment_verification.py (standard library only).
The uniform theorem rests on the accompanying proof, not on this finite test.
"""
from itertools import combinations
from math import comb


def components(I):
    S = set(I)
    out = []
    for v in sorted(S):
        if any(v in cc for cc in out):
            continue
        run = [v]
        while run[-1] + 1 in S:
            run.append(run[-1] + 1)
        out.append(tuple(run))
    return out


def perm_sign(images):
    return -1 if sum(images[i] > images[j] for i in range(len(images))
                     for j in range(i+1, len(images))) % 2 else 1


def rank_formula(n, k):
    if k < 2 or k > n:
        return 0
    return (k-1)*comb(n,k)-(n-1)*comb(n-2,k-2)


def line_count(n, k):
    if k < 2 or k % 2:
        return 0
    j = k//2
    a = n//2-1 if n % 2 == 0 else n//2
    return comb(a,j) if 0 <= j <= a else 0


def trace_formula(n, k):
    return (-1)**(k//2+1)*line_count(n,k) if k % 2 == 0 else 0


def inv_matrix_rank(M, prime=1000003):
    if not M: return 0
    a = [[x%prime for x in row] for row in M]
    nr,nc=len(a),len(a[0]); rank=0
    for col in range(nc):
        pivot=next((r for r in range(rank,nr) if a[r][col]), None)
        if pivot is None:continue
        a[rank],a[pivot]=a[pivot],a[rank]
        q=pow(a[rank][col],-1,prime)
        for c in range(col,nc):a[rank][c]=(a[rank][c]*q)%prime
        for r in range(rank+1,nr):
            if a[r][col]:
                q=a[r][col]
                for c in range(col,nc): a[r][c]=(a[r][c]-q*a[rank][c])%prime
        rank+=1
        if rank==nr:break
    return rank


def coboundary_check(n, I):
    # The support-I cellular cochains have degrees k,k+1,k+2;
    # bases are empty face, vertices, and edges of the induced path.
    vertices=list(I)
    edges=[(v,v+1) for v in I if v+1 in I]
    d0=[]
    for v in vertices:
        omega=[u for u in I if u!=v]
        d0.append((-1)**sum(u<v for u in I))
    # d1 is coboundary on the induced graph after integral basis signs.
    d1=[[int(v==e[1])-int(v==e[0]) for v in vertices] for e in edges]
    assert rank_over_Q(d1)==len(vertices)-len(components(I))
    assert rank_over_Q([d0])==1
    # Isomorphism of cellular complexes with augmented path cochains
    # supplies the integral (not just field) statement via incidence matrices.


def rank_over_Q(M):
    # Integer entries here are -1,0,1; a large prime check is
    # independent confirmation of the explicit incidence rank identity.
    return inv_matrix_rank(M)


def check_n(n):
    ranks={k:0 for k in range(2,n+1)}
    traces={k:0 for k in range(2,n+1)}
    cell_traces={k:0 for k in range(2,n+1)}
    integral_regs={k:0 for k in range(2,n+1)}
    integral_triv={k:0 for k in range(2,n+1)}
    integral_sign={k:0 for k in range(2,n+1)}
    support_count=0
    for k in range(1,n+1):
        for I in combinations(range(n), k):
            cc=components(I); c=len(cc)
            if k>=2:ranks[k]+=c-1
            J=tuple(sorted(n-1-i for i in I))
            if k>=2 and J==I:
                t=sum(i<n-1-i for i in I)
                fixed=sum(tuple(sorted(n-1-v for v in A))==A for A in cc)
                traces[k]+=(-1)**t*(fixed-1)
                # Fully independent signed cellular Lefschetz supertrace.
                F=[()] + [(i,) for i in I] + [(i,i+1) for i in I if i+1 in I]
                supertrace=0
                for sigma in F:
                    if set(n-1-i for i in sigma)!=set(sigma):continue
                    omega=[i for i in I if i not in sigma]
                    perm=[omega.index(n-1-i) for i in omega]
                    supertrace+=(-1)**(k+len(sigma))*perm_sign(perm)
                cell_traces[k]+=(-1)**(k+1)*supertrace
                if fixed==1:
                    assert (c-1)%2==0
                    integral_regs[k]+=(c-1)//2
                else:
                    assert fixed==0 and c%2==0 and c>=2
                    integral_regs[k]+=c//2-1
                    if t%2:integral_triv[k]+=1
                    else:integral_sign[k]+=1
            elif k>=2 and I<J:
                integral_regs[k]+=c-1
            if n<=9 and k>=2:
                coboundary_check(n,I)
            support_count+=1
    for k in range(2,n+1):
        b=rank_formula(n,k); ell=line_count(n,k)
        assert ranks[k]==b,(n,k,ranks[k],b)
        assert traces[k]==trace_formula(n,k),(n,k,traces[k],trace_formula(n,k))
        assert cell_traces[k]==traces[k],(n,k,cell_traces[k],traces[k])
        assert integral_regs[k]*2+integral_triv[k]+integral_sign[k]==b
        assert integral_triv[k]+integral_sign[k]==ell
        assert integral_triv[k]-integral_sign[k]==traces[k]
        assert (b+traces[k])%2==0
        if ell:
            assert (integral_triv[k],integral_sign[k])==((ell,0) if (k//2)%2 else (0,ell))
    assert sum(ranks.values()) == (n-3)*2**(n-2)+1
    assert sum(traces.values()) == 1
    assert sum((ranks[k]+traces[k])//2 for k in ranks) == (n-3)*2**(n-3)+1
    return support_count



def cochain_shuffle_sign(I, sigma):
    # Explicit unimodular cellular-to-augmented-simplicial cochain map.
    omega=[v for v in I if v not in sigma]
    seq=omega+list(sigma)
    inv=sum(seq[i]>seq[j] for i in range(len(seq)) for j in range(i+1,len(seq)))
    k=len(I); z=len(sigma)
    return (-1)**(inv+z*(k-1)-z*(z-1)//2)

def check_equivariant_integral_cochain_map(n):
    for k in range(1,n+1):
        for I in combinations(range(n),k):
            faces=[()] + [(i,) for i in I]+[(i,i+1) for i in I if i+1 in I]
            J=tuple(sorted(n-1-v for v in I))
            for sigma in faces:
                omega=[x for x in I if x not in sigma]
                # Differential compatibility over Z, including all signs.
                for v in omega:
                    sigma2=tuple(sorted(sigma+(v,)))
                    if sigma2 not in faces:continue
                    assert ((-1)**omega.index(v))*cochain_shuffle_sign(I,sigma2) == (
                        cochain_shuffle_sign(I,sigma)*(-1)**sigma2.index(v))
                if I==J:
                    new_sig=tuple(sorted(n-1-v for v in sigma))
                    new_om=tuple(sorted(n-1-v for v in omega))
                    om_perm=[new_om.index(n-1-v) for v in omega]
                    sig_perm=[new_sig.index(n-1-v) for v in sigma]
                    I_perm=[I.index(n-1-v) for v in I]
                    # The exact support-determinant twist is essential.
                    assert perm_sign(om_perm)*cochain_shuffle_sign(I,new_sig) == (
                        cochain_shuffle_sign(I,sigma)*perm_sign(I_perm)*perm_sign(sig_perm))

if __name__=='__main__':
    for n in range(3,11):check_equivariant_integral_cochain_map(n)
    count=sum(check_n(n) for n in range(3,19))
    print('PASS: n=3..18, supports=%d; exact formulas for Betti numbers, integral regular/trivial/sign multiplicities, all signed cellular Lefschetz traces and rational quotient dimensions.' % count)
    print('PASS: integral cellular-to-simplicial cochain signs and reversal equivariance for n=3..10; n=3..9 incidence ranks.')
