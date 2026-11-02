"""Reproduce Hasse--Witt coefficient and rank computations for X^4+Y^4+XZ^3.
Uses only Python's standard library. Algebraic proof for every prime appears in RESULT.md.
"""
from math import factorial

ALPHA = ((2, 1, 1), (1, 2, 1), (1, 1, 2))

def primes_to(bound):
    return [p for p in range(5, bound + 1) if all(p % d for d in range(2, int(p ** 0.5) + 1))]

def multinomial(n, a, b, c):
    return factorial(n) // (factorial(a) * factorial(b) * factorial(c))

def from_exponents(p):
    """Enumerate all triples in (X^4+Y^4+XZ^3)^(p-1)."""
    coeffs = {}
    for a in range(p):
        for b in range(p - a):
            c = p - 1 - a - b
            key = (4*a+c, 4*b, 3*c)
            coeffs[key] = multinomial(p-1, a, b, c) % p
    return tuple(tuple(coeffs.get(tuple(p*t - s for t,s in zip(u,v)),0)
                       for v in ALPHA) for u in ALPHA)

def by_solved_diophantine(p):
    """Second route: solve the three exponent equations entry by entry."""
    out=[]
    for u in ALPHA:
        row=[]
        for v in ALPHA:
            e = tuple(p*t-s for t,s in zip(u,v))
            if e[1]%4 or e[2]%3:
                row.append(0)
                continue
            b,c=e[1]//4,e[2]//3
            if (e[0]-c)%4:
                row.append(0)
                continue
            a=(e[0]-c)//4
            if min(a,b,c)<0 or a+b+c!=p-1:
                row.append(0)
                continue
            row.append(multinomial(p-1,a,b,c)%p)
        out.append(tuple(row))
    return tuple(out)

def rank(m,p):
    a=[list(row) for row in m]
    n=len(a)
    rank=0
    for j in range(n):
        pivot=next((i for i in range(rank,n) if a[i][j]%p),None)
        if pivot is None: continue
        a[rank],a[pivot]=a[pivot],a[rank]
        inv=pow(a[rank][j],-1,p)
        a[rank]=[x*inv%p for x in a[rank]]
        for i in range(rank+1,n):
            f=a[i][j]
            a[i]=[(x-f*y)%p for x,y in zip(a[i],a[rank])]
        rank+=1
    return rank

def multiply(x,y,p):
    return tuple(tuple(sum(x[i][k]*y[k][j] for k in range(3))%p for j in range(3)) for i in range(3))

def expected(p):
    r=p%12
    return {1:3,5:2,7:1,11:0}[r]

def main():
    for p in primes_to(109):
        h=from_exponents(p)
        assert h==by_solved_diophantine(p),(p,'methods',h)
        r=rank(h,p)
        assert r==expected(p),(p,'rank',r,h)
        assert rank(multiply(h,h,p),p)==r,(p,'stable',h)
        assert rank(multiply(multiply(h,h,p),h,p),p)==r,(p,'stable3',h)
        support={(i,j) for i in range(3) for j in range(3) if h[i][j]}
        supports={1:{(0,0),(1,1),(2,2)},5:{(0,2),(2,0)},7:{(1,1)},11:set()}
        assert support==supports[p%12],(p,'support',support)
    for p in (5,7,11,13):
        print(f'p={p}, H={from_exponents(p)}, stable_rank={expected(p)}')
    print(f'VERIFY_OK: all primes 5..109, two independent coefficient constructions, stable Frobenius ranks')

if __name__=='__main__':
    main()
