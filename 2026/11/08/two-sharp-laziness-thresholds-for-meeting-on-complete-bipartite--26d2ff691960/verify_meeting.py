"""Exact checks for the bipartite synchronous rendezvous phase diagram.
Run with Python >= 3.9. Uses standard library only.
"""
from fractions import Fraction as F


def solve_exact(A, b):
    """Gauss-Jordan exact linear solve; nonsingular matrix required."""
    n = len(b)
    T = [list(map(F, A[i])) + [F(b[i])] for i in range(n)]
    for j in range(n):
        k = next((i for i in range(j, n) if T[i][j]), None)
        assert k is not None, "unexpected singular absorbing chain"
        T[j], T[k] = T[k], T[j]
        pivot = T[j][j]
        for z in range(j, n+1): T[j][z] /= pivot
        for i in range(n):
            if i == j: continue
            fac = T[i][j]
            if fac:
                for z in range(j, n+1): T[i][z] -= fac * T[j][z]
    return [T[i][-1] for i in range(n)]


def formula(a, b, p):
    d = (1-p*p)*(a+b+p-1)
    HA = 2*a*(2*b+p-1)/d if a>1 else None
    HB = 2*b*(2*a+p-1)/d if b>1 else None
    # Formula still algebraically extends to a=1 or b=1; the corresponding
    # unobservable same-part class has zero incoming probability.
    xa = 2*a*(2*b+p-1)/d
    xb = 2*b*(2*a+p-1)/d
    HC = 1/(2*p*(1-p)) + (a-1)*xa/(2*a) + (b-1)*xb/(2*b)
    return HA,HB,HC


def full_pair_means(a, b, p):
    N=a+b
    P=[[F(0) for _ in range(N)] for _ in range(N)]
    for v in range(N):
        P[v][v] = p
        neighbors=range(a,N) if v<a else range(a)
        for w in neighbors: P[v][w] = (1-p)/len(neighbors)
    states=[(u,v) for u in range(N) for v in range(u+1,N)]
    A=[]
    for u,v in states:
        row=[]
        for x,y in states:
            val=P[u][x]*P[v][y] + P[u][y]*P[v][x]
            row.append((F(1) if (u,v)==(x,y) else F(0))-val)
        A.append(row)
    return dict(zip(states,solve_exact(A,[1]*len(states))))


def Fpoly(a,b,p):
    return (2*(a-b)+3)*p*p+(a+5*b-4)*p-(a+b-1)


def check():
    count=0
    for a in range(1,5):
        for b in range(1,5):
            if a==b==1: continue
            for p in [F(1,5),F(1,3),F(2,5),F(1,2),F(4,5)]:
                true=full_pair_means(a,b,p)
                HA,HB,HC=formula(a,b,p)
                for (u,v),z in true.items():
                    expected=HA if u<a and v<a else HB if u>=a and v>=a else HC
                    assert expected is not None
                    assert z==expected,(a,b,p,u,v,z,expected)
                    count+=1
                if a>=2 and b>=2:
                    D=2*p*(1-p*p)*(a+b+p-1)
                    assert HA-HC == Fpoly(a,b,p)/D
                    assert HB-HC == Fpoly(b,a,p)/D
                    assert HA-HB == -2*(a-b)/((p+1)*(a+b+p-1))
                    count+=3
                if a==b and a>=2:
                    if p==F(1,3):
                        assert HA==HB==HC==F(9*a,4)
                        count+=1
    # Cross-check exact phase interval and uniqueness using monotone derivatives
    for m in range(2,101):
        for s in range(1,m+1):
            assert Fpoly(m,s,F(0))<0
            assert Fpoly(m,s,F(1,2))>0
            assert Fpoly(m,s,F(1,3)) <= 0
            assert (Fpoly(m,s,F(1,3)) ==0) == (m==s)
            count+=4
            if s>=2:
                assert Fpoly(s,m,F(0))<0
                assert Fpoly(s,m,F(1,3)) >= 0
                count+=2
    print('VERIFY_OK',count,'exact assertions')

if __name__=='__main__': check()
