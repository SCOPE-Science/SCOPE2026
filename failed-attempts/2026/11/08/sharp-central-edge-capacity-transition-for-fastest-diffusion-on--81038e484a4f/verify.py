"""Exact rational replay of the centered-edge capacity theorem.

Run: python3 verify.py
No third-party dependencies are required. Finite checks complement the general proof.
"""
from fractions import Fraction as F

checks = 0

def check(condition, description):
    global checks
    if not condition:
        raise AssertionError(description)
    checks += 1

def threshold(m, B):
    return F(3*m, 4*m*m - 1) * B

def Q(m, r):
    a = m - 1
    return 1 + 2*a*r*(r + F(2*m - 1, 3))/(r + F(a, 2))

def design(m, B, r, u=None):
    assert m >= 2 and B > 0 and r >= F(1, 2)
    if u is None:
        u = B / Q(m, r)
    if r == F(1, 2):
        lam = F(6, m*(4*m*m-1))*B
    else:
        lam = 2*u*r/(m*(r+F(m-1,2)))
    left = [lam*i*(r+m-F(i+1,2)) for i in range(1,m)]
    mid = lam*m*(r+F(m-1,2))/(2*r)
    weights = left + [mid] + list(reversed(left))
    x = [-r-(m-i) for i in range(1,m+1)]
    x += [-v for v in reversed(x)]
    return lam, weights, x

def replay(m, B, r, u):
    lam, w, x = design(m,B,r,u)
    n = 2*m
    check(len(w)==n-1 and len(x)==n, 'sizes')
    check(sum(w)==B, 'budget')
    check(all(a>0 for a in w), 'strict conductances')
    check(w[m-1]<=u, 'capacity')
    check(sum(x)==0 and all(x[j+1]>x[j] for j in range(n-1)), 'centered monotone vector')
    check(w[m-1]==u if r>F(1,2) else w[m-1]==threshold(m,B), 'center condition')
    for i in range(n):
        l = w[i-1]*(x[i]-x[i-1]) if i>0 else F(0)
        rr = w[i]*(x[i]-x[i+1]) if i<n-1 else F(0)
        check(l+rr==lam*x[i], f'exact eigenvalue relation m={m} i={i}')
    energy=sum(w[i]*(x[i+1]-x[i])**2 for i in range(n-1))
    check(energy==lam*sum(v*v for v in x),'Rayleigh equality')
    check(energy==B+(4*r*r-1)*w[m-1], 'one-edge gap energy')
    # Leading-principal-minor Sturm sequence at the candidate eigenvalue:
    # p_0=1, p_k=det((L-lambda I)[:k,:k]).
    diagonals=[(w[i-1] if i>0 else F(0))+(w[i] if i<n-1 else F(0)) for i in range(n)]
    polys=[F(1)]
    polys.append(diagonals[0]-lam)
    for k in range(2,n+1):
        polys.append((diagonals[k-1]-lam)*polys[k-1]-w[k-2]**2*polys[k-2])
    check(polys[-1]==0 and all(v!=0 for v in polys[:-1]), 'simple Sturm root')
    changes=sum((polys[i]<0)!=(polys[i+1]<0) for i in range(n-1))
    check(changes==1, 'exact Sturm count: precisely one lower eigenvalue')
    # Eigenvector forces every edge weight uniquely by prefix flux.
    prefix=F(0)
    for i in range(n-1):
        prefix+=x[i]
        expected=-lam*prefix/(x[i+1]-x[i])
        check(expected==w[i],f'uniqueness flux m={m} edge={i}')
    return checks

def run():
    for m in list(range(2,17))+[20,25]:
        B=F(19,3)
        u0=threshold(m,B)
        for u in [u0,2*u0, B, 2*B]:
            lam,w,x=design(m,B,F(1,2))
            check(w[m-1] <= u, 'uncapped feasible')
            replay(m,B,F(1,2),u)
        for r in [F(3,5),F(7,10),F(1),F(3,2),F(2),F(11,3),F(17,2)]:
            u=B/Q(m,r)
            check(F(0)<u<u0, 'strict capacity phase')
            check(Q(m,r)==B/u,'implicit root')
            replay(m,B,r,u)
    # A small transparent example: six vertices, B=19, middle cap 3.
    lam,w,x=design(3,F(19),F(1),F(3))
    check(lam==1 and w==[F(3),F(5),F(3),F(5),F(3)],'six-vertex witness')
    check(x==[F(-3),F(-2),F(-1),F(1),F(2),F(3)],'witness Fiedler vector')
    print('VERIFY_OK',checks)

if __name__=='__main__':
    run()
