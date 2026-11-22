"""Independent checks for type spectra over one-by-two balanced tripartite 3-graphs.
Run: python3 hypergraph_link_verify.py  (standard library only).
"""
from math import comb
from fractions import Fraction


def polynomial_from_shores(n):
    # The free link-edge count is n(n-1)+n*n-i*j.
    result = [0] * (comb(2*n+1, 2)+1)
    for i in range(n+1):
        for j in range(n+1):
            multiplicity=comb(n,i)*comb(n,j)
            free=n*(n-1)+n*n-i*j
            for v in range(free+1):
                result[i+j+v] += multiplicity*comb(free,v)
    return result


def polynomial_by_forbidden_clauses(n):
    # Independently apply inclusion-exclusion to all old hyperedges.
    N=2*n+1
    pairs=[(a,b) for a in range(N) for b in range(a+1,N)]
    pos={e:k for k,e in enumerate(pairs)}
    clause=[]
    for b in range(1,n+1):
        for c in range(n+1,2*n+1):
            mask=sum(1 << pos[e] for e in [(0,b),(0,c),(b,c)])
            clause.append(mask)
    output=[0] * (len(pairs)+1)
    for k in range(1<<len(clause)):
        union=0
        for t,m in enumerate(clause):
            if (k>>t)&1: union |=m
        h=union.bit_count()
        sign=(-1)**k.bit_count()
        for v in range(len(pairs)-h+1):
            output[h+v] += sign*comb(len(pairs)-h,v)
    return output


def brute(n):
    N=2*n+1
    pairs=[(a,b) for a in range(N) for b in range(a+1,N)]
    pos={e:k for k,e in enumerate(pairs)}
    masks=[]
    for b in range(1,n+1):
        for c in range(n+1,2*n+1):
            masks.append(sum(1<<pos[e] for e in [(0,b),(0,c),(b,c)]))
    result=[0]*(len(pairs)+1)
    for edges in range(1<<len(pairs)):
        if all(edges & c != c for c in masks):
            result[edges.bit_count()]+=1
    return result


def rational_formula(n):
    S=sum((Fraction(comb(n,i)*comb(n,j), 2**(i*j))
           for i in range(n+1) for j in range(n+1)),Fraction(0))
    return S, S*2**(2*n*n-n)


def run():
    for n in range(1,5):
        lhs=polynomial_from_shores(n)
        rhs=polynomial_by_forbidden_clauses(n)
        assert lhs==rhs,(n,'polynomial')
        S,T=rational_formula(n)
        assert sum(lhs)==T and T.denominator==1
        if n<=3:
            assert brute(n)==lhs,(n,'brute')
        # Decompose exact mixed shore profiles into pure, single-side and residual.
        pure=2**(n+1)-1
        single=2*n*((Fraction(3,2)**n)-1)-Fraction(n*n,2)
        residual=sum((Fraction(comb(n,i)*comb(n,j),2**(i*j))
            for i in range(2,n+1) for j in range(2,n+1)),Fraction(0))
        assert S==pure+single+residual
        print('n',n,'types',int(T),'mixed_prob',format(float((S-pure)/S),'.6f'))
    for n in (8,12,20,40,60,100):
        S,_=rational_formula(n)
        mixed=S-(2**(n+1)-1)
        ratio=float(mixed/(2*n*Fraction(3,2)**n))
        print('asymptotic_check',n,format(ratio,'.9f'))
    print('VERIFY_OK')

if __name__=='__main__': run()
