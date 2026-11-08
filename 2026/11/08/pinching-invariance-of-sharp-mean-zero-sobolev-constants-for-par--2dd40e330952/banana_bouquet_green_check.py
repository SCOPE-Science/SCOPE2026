"""Exact-rational independent Poisson solve for metric bouquet/banana Green diagonals.

Uses nodal stiffness after insertion of an observation vertex, and integrates
separate quadratic forcing terms. No use of the theorem's diagonal formulas
in the graph solver.
"""
from fractions import Fraction as F
from sympy import Matrix, Rational


def rr(q):
    return Rational(q.numerator, q.denominator) if isinstance(q,F) else Rational(q)


def make_segments(lengths, graph, edge, s):
    n = len(lengths)
    lengths = [rr(t) for t in lengths]
    s = rr(s)
    assert 0 <= s <= lengths[edge]
    if graph == 'banana':
        segments=[]
        if s == 0: target=0; vertices=2
        elif s == lengths[edge]: target=1; vertices=2
        else: target=2;vertices=3
        for j,L in enumerate(lengths):
            if j==edge and target==2:
                segments.extend([(0,2,s),(2,1,L-s)])
            else:
                segments.append((0,1,L))
    else:
        assert graph=='bouquet'
        target=0 if s==0 or s==lengths[edge] else edge+1
        vertices=n+1
        segments=[]
        for j,L in enumerate(lengths):
            z=s if j==edge and target else L/2
            segments.extend([(0,j+1,z),(j+1,0,L-z)])
    return vertices,segments,target


def exact_diagonal(lengths,graph,edge,s):
    n,segments,target=make_segments(lengths,graph,edge,s)
    T=sum((length for _,_,length in segments), Rational(0))
    L=Matrix.zeros(n)
    mass=Matrix.zeros(n,1)
    cubes=Rational(0)
    for u,v,length in segments:
        assert u!=v and length>0
        g=1/length
        L[u,u]+=g;L[v,v]+=g;L[u,v]-=g;L[v,u]-=g
        mass[u]+=length/(2*T);mass[v]+=length/(2*T)
        cubes+=length**3
    b=Matrix([-mass[j]+(1 if target==j else 0) for j in range(n)])
    w=L[1:,1:].inv()*b[1:,:]
    base=Matrix([0]+list(w))
    offset=cubes/(12*T*T) - (mass.T*base)[0]
    return (base+Matrix([offset]*n))[target]


def claim_diagonal(lengths,graph,edge,s):
    lengths=[rr(t) for t in lengths]
    s=rr(s)
    T=sum(lengths,Rational(0)); c=sum([1/x for x in lengths],Rational(0))
    C=sum([x**3 for x in lengths],Rational(0))/(12*T*T)
    L=lengths[edge]
    v=C+(1/L-1/T)*s*(L-s)
    if graph=='banana':
        v+=(s/L-Rational(1,2))**2/c
    return v


def main():
    tests=0
    families=[(1,1),(1,3),(1,2,3),(1,1,1),(1,2,2,5),(1,3,4,6,7),(F(1,3),F(3,2),F(7,5),F(1,2))]
    for lengths in families:
        T=sum((rr(x) for x in lengths),Rational(0))
        C=sum((rr(x)**3 for x in lengths),Rational(0))/(12*T*T)
        K=C+max(rr(x)*(T-rr(x)) for x in lengths)/(4*T)
        for typ in ('banana','bouquet'):
            for i,L0 in enumerate(lengths):
                L=rr(L0)
                for s in (Rational(0),L/4,L/2,3*L/4,L):
                    got=exact_diagonal(lengths,typ,i,s)
                    want=claim_diagonal(lengths,typ,i,s)
                    assert got==want,(lengths,typ,i,s,got,want)
                    assert got<=K,(lengths,typ,i,s,got,K)
                    tests+=1
            max_i=max(range(len(lengths)),key=lambda j: rr(lengths[j]))
            assert exact_diagonal(lengths,typ,max_i,rr(lengths[max_i])/2)==K
    print('EXACT_NODAL_POISSON_GREEN_CHECKS_PASSED',tests)
    print('ALL_BANANA_BOUQUET_SHARP_CONSTANT_CHECKS_PASSED')

if __name__=='__main__':
    main()
