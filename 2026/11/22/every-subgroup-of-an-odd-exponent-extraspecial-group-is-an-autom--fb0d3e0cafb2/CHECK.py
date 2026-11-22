"""Exact finite-field checks for a fixed-subgroup realization theorem.

This code verifies the rank-one group by exhaustive automorphism and subgroup
sets at primes three and five, plus explicit higher-rank symplectic matrices.
No external packages are required.
"""
from itertools import product

def verify_rank_one(p):
    F=range(p)
    els=set(product(F,F,F))
    def omega(x,y): return (x[0]*y[1]-x[1]*y[0])%p
    inv2=pow(2,-1,p)
    def multiply(g,h):
        return ((g[0]+h[0])%p,(g[1]+h[1])%p,(g[2]+h[2]+inv2*omega(g,h))%p)
    Z={(0,0,z) for z in F}
    lines=set()
    for a,b in product(F,F):
        if a or b:
            lines.add(frozenset(((k*a)%p,(k*b)%p) for k in F))
    assert len(lines)==p+1
    V=set(product(F,F))
    group_subgroups={frozenset({(0,0,0)}),frozenset(els)}
    for U in lines|{frozenset({(0,0)}),frozenset(V)}:
        group_subgroups.add(frozenset((a,b,z) for a,b in U for z in F))
    for U in lines:
        nonzero=min(U-{(0,0)})
        for t in F:
            H=frozenset(((k*nonzero[0])%p,(k*nonzero[1])%p,(k*t)%p) for k in F)
            group_subgroups.add(H)
    assert len(group_subgroups)==p*p+2*p+4, (p,len(group_subgroups))
    if p==3:
        for H in group_subgroups:
            assert all(multiply(x,y) in H for x in H for y in H)
    fixed=set()
    for a,b,c,d in product(F,repeat=4):
        det=(a*d-b*c)%p
        if not det: continue
        for u,v in product(F,repeat=2):
            fix=frozenset((x,y,z) for x,y,z in els
                if ((a*x+b*y-x)%p==0 and (c*x+d*y-y)%p==0
                    and ((det-1)*z+u*x+v*y)%p==0))
            fixed.add(fix)
    assert group_subgroups<=fixed, (p, len(group_subgroups-fixed))
    assert group_subgroups==fixed, (p,len(group_subgroups),len(fixed))
    print(f'RANK_ONE_OK p={p} group_order={p**3} subgroups={len(group_subgroups)} fixed_sets={len(fixed)}')

def verify_higher_rank(p):
    # Basis e1,f1,e2,f2, with alternating matrix J=diag(J2,J2).
    J=[[0,1,0,0],[-1,0,0,0],[0,0,0,1],[0,0,-1,0]]
    def matvec(M,v): return [sum(M[i][j]*v[j] for j in range(4))%p for i in range(4)]
    def check(M,lam,U):
        assert all(sum(M[k][i]*J[k][l]*M[l][j] for k in range(4) for l in range(4))%p==lam*J[i][j]%p
                   for i in range(4) for j in range(4)),(p,M,lam)
        fixed={v for v in product(range(p),repeat=4) if matvec(M,v)==list(v)}
        Uset={v for v in product(range(p),repeat=4) if U(v)}
        assert fixed==Uset,(p,len(fixed),len(Uset))
    # Full center-containing representative: U=<e1,e2> (lagrangian).
    M=[[1,1,0,0],[0,1,0,0],[0,0,1,1],[0,0,0,1]]
    check(M,1,lambda v:v[1]==0 and v[3]==0)
    # Symplectic two-dimensional fixed subspace: U=<e1,f1>.
    M=[[1,0,0,0],[0,1,0,0],[0,0,-1,0],[0,0,0,-1]]
    check(M,1,lambda v:v[2]==0 and v[3]==0)
    # One isotropic fixed line U=<e1>; R* f1 sheared, remaining plane -I.
    M=[[1,1,0,0],[0,1,0,0],[0,0,-1,0],[0,0,0,-1]]
    check(M,1,lambda v:v[1]==0 and v[2]==0 and v[3]==0)
    # Center-avoiding (lambda=-1), U=<e1>, nonsingular no-fixed B on E.
    M=[[1,0,0,0],[0,-1,0,0],[0,0,0,1],[0,0,1,1]]
    check(M,-1,lambda v:v[1]==0 and v[2]==0 and v[3]==0)
    # Center-avoiding maximal U=<e1,e2> (two complementary hyperbolic blocks).
    M=[[1,0,0,0],[0,-1,0,0],[0,0,1,0],[0,0,0,-1]]
    check(M,-1,lambda v:v[1]==0 and v[3]==0)
    # Center-avoiding trivial U=0: two B blocks.
    M=[[0,1,0,0],[1,1,0,0],[0,0,0,1],[0,0,1,1]]
    check(M,-1,lambda v:v==(0,0,0,0))
    print(f'HIGHER_RANK_OK p={p} rank=4 six representative symplectic/similitude checks')

if __name__=='__main__':
    verify_rank_one(3)
    verify_rank_one(5)
    verify_higher_rank(3)
    verify_higher_rank(5)
    print('EXTRASPECIAL_FIXED_SUBGROUP_REALIZATION_OK')
