"""Reproducible exact-rational checks of sharp binomial-posterior kernel contraction."""
from fractions import Fraction as Q
from math import comb


def tv(a,b):
    return sum((abs(x-y) for x,y in zip(a,b)),Q(0))/2


def run_case(n, atoms, weights):
    assert n>=1 and len(atoms)==len(weights) and all(Q(0)<=a<=Q(1) for a in atoms)
    assert any(Q(0)<a<Q(1) and w>0 for a,w in zip(atoms,weights))
    basis=[[Q(comb(n,k))*a**k*(1-a)**(n-k) for a in atoms] for k in range(n+1)]
    z=[sum((b*w for b,w in zip(row,weights)),Q(0)) for row in basis]
    assert all(z0>0 for z0 in z)
    post=[[b*w/z0 for b,w in zip(row,weights)] for row,z0 in zip(basis,z)]
    assert all(sum(row)==1 for row in post)
    edge=tv(post[0],post[n]); assert edge<1
    for i in range(n+1):
        for j in range(n+1):
            assert tv(post[i],post[j])<=edge
    for x in [Q(0),Q(1,4),Q(1,2),Q(3,4),Q(1)]:
        for y in [Q(0),Q(1,4),Q(1,2),Q(3,4),Q(1)]:
            px=[sum((Q(comb(n,k))*x**k*(1-x)**(n-k)*post[k][j] for k in range(n+1)),Q(0)) for j in range(len(atoms))]
            py=[sum((Q(comb(n,k))*y**k*(1-y)**(n-k)*post[k][j] for k in range(n+1)),Q(0)) for j in range(len(atoms))]
            assert sum(px)==sum(py)==1
            assert tv(px,py)<=edge
            if x==0 and y==1:assert tv(px,py)==edge
    # The normalized prior is stationary (reversibility on the atomic state space).
    wtotal=sum(weights); prior=[w/wtotal for w in weights]
    for col,a in enumerate(atoms):
        colsum=Q(0)
        for row,x in enumerate(atoms):
            p=sum((Q(comb(n,k))*x**k*(1-x)**(n-k)*post[k][col] for k in range(n+1)),Q(0))
            colsum+=prior[row]*p
        assert colsum==prior[col]
    return edge


def main():
    cases=[([Q(0),Q(1,7),Q(1,3),Q(3,5),Q(1)], [Q(2),Q(3),Q(4),Q(5),Q(1)]),
           ([Q(1,3)], [Q(1)]),
           ([Q(1,5),Q(4,5)], [Q(1),Q(2)]),
           ([Q(0),Q(1,2),Q(1)], [Q(2),Q(1),Q(7)])]
    for n in range(1,7):
        for atoms,weights in cases:
            d=run_case(n,atoms,weights)
            print(f'n={n} support={len(atoms)} exact_TV={d}')
        # Exact integral for uniform base measure:
        # q_0=(n+1)(1-u)^n, q_n=(n+1)u^n; sign crossing at u=1/2.
        f0=Q(1)-Q(1,2)**(n+1)
        fn=Q(1,2)**(n+1)
        assert f0-fn==Q(1)-Q(1,2)**n
        print(f'n={n} uniform_coefficient={f0-fn}')
    print('ALL_EXACT_CHECKS_PASSED')


if __name__=='__main__':main()
