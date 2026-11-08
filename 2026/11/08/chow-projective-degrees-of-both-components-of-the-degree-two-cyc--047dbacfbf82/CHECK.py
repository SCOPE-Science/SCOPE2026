"""Exact arithmetic certificates for Chow-embedded degree-two cycle loci.
No third-party packages required; use: python3 CHECK.py.
"""
from fractions import Fraction
from math import comb, factorial, prod
from itertools import combinations

def grass_degree(k,N):
    d=k*(N-k)
    a=factorial(d)*prod(factorial(i) for i in range(k))
    b=prod(factorial(N-k+i) for i in range(k))
    assert a % b == 0
    return a//b

def pair_degree(p,n):
    k=p+1;N=n+1;d=k*(N-k)
    a=comb(2*d,d)*grass_degree(k,N)**2
    assert a%2==0
    return a//2

def quad_degree_localization(p,n, start=0, step=1):
    assert 1<=p<=n-1
    N=n+1;K=p+2;g=K*(N-K);r=K*(K+1)//2;D=g+r-1
    weights=[start+i*step for i in range(N)]
    result=Fraction(0)
    for I in combinations(range(N),K):
        a=[-weights[i] for i in I]
        roots=[a[i]+a[j] for i in range(K) for j in range(i,K)]
        seg=[1]+[0]*g
        for z in roots:
            for t in range(1,g+1):seg[t]-=z*seg[t-1]
        h=sum(a)
        num=sum(comb(D,r-1+j)*(2*h)**(g-j)*seg[j] for j in range(g+1))
        denom=prod(weights[j]-weights[i] for i in I for j in range(N) if j not in I)
        result+=Fraction(num,denom)
    assert result.denominator==1, (p,n,result)
    return result.numerator

def poly_degree_coefficient(p,n):
    """Independent Grassmannian Vandermonde top-coefficient method."""
    N=n+1;K=p+2;g=K*(N-K);r=K*(K+1)//2;D=g+r-1
    target=tuple(N-1-i for i in range(K));zero=(0,)*K
    one={zero:1}
    def add(A,B,coef=1):
        C=A.copy()
        for e,v in B.items():
            z=C.get(e,0)+coef*v
            if z:C[e]=z
            else:C.pop(e,None)
        return C
    def mul(A,B):
        C={}
        for a,v in A.items():
            for b,w in B.items():
                e=tuple(x+y for x,y in zip(a,b))
                if any(x>y for x,y in zip(e,target)):continue
                C[e]=C.get(e,0)+v*w
        return {e:v for e,v in C.items() if v}
    vars_=[{tuple(int(j==i) for j in range(K)):1} for i in range(K)]
    h={}
    for var in vars_:h=add(h,var)
    pow2h=[one]
    for i in range(g):pow2h.append(mul(pow2h[-1],{e:2*v for e,v in h.items()}))
    seg=[one]+[{} for _ in range(g)]
    for i in range(K):
        for j in range(i,K):
            root=add(vars_[i],vars_[j])
            for t in range(1,g+1):seg[t]=add(seg[t],mul(root,seg[t-1]),-1)
    F={}
    for t in range(g+1):
        term=mul(pow2h[g-t],seg[t]);F=add(F,term,comb(D,r-1+t))
    Vand=one
    for i in range(K):
        for j in range(i+1,K):Vand=mul(Vand,add(vars_[i],vars_[j],-1))
    return mul(F,Vand).get(target,0)

def main():
    expected={
        (1,3):(8,92,8,140),
        (1,4):(11,6620,12,11550),
        (2,4):(13,2865,12,11550),
        (1,5):(14,437024,16,1261260),
        (2,5):(17,5557335,18,42882840),
        (3,6):(24,6522193496,24,288592936632)
    }
    for (p,n),(dq,expected_q,dr,expected_r) in expected.items():
        K=p+2;N=n+1;r=K*(K+1)//2
        assert dq==K*(N-K)+r-1 and dr==2*(p+1)*(n-p)
        assert quad_degree_localization(p,n)==expected_q
        assert pair_degree(p,n)==expected_r
        assert quad_degree_localization(p,n,3,2)==expected_q
        print(f'p={p} n={n}: quadric_degree={expected_q} pair_degree={expected_r} localization_weights_2x_OK')
    for p,n in [(1,3),(1,4),(2,4),(1,5),(2,5)]:
        a=quad_degree_localization(p,n);b=poly_degree_coefficient(p,n)
        assert a==b, (p,n,a,b)
        print(f'p={p} n={n}: independent_Grassmann_coefficient_OK')
    for p in range(1,6):
        for n in range(p+2,8):
            lhs=2*(p+1)*(n-p)-((p+2)*(n-p-1)+(p+2)*(p+3)//2-1)
            assert lhs*2==p*(2*n-3*p-3)
    print('CHOW_COMPONENT_DEGREE_CERTIFICATE_OK')

if __name__=='__main__':main()
