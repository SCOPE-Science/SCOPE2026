"""Finite direct checks of complete compact fair allocations on bicliques.

The counted objects are assignments of distinguishable vertices to labeled agents.
The graph-distance predicate is computed from induced adjacency, not from the
structural formulas being tested.
"""
from functools import lru_cache
from itertools import combinations
from math import comb, factorial, sqrt


def coefficient_count(n, q, a):
    if a < n or a > n * (q - 1):
        return 0
    c = [0] * (a + 1)
    c[0] = 1
    for _ in range(n):
        d = [0] * (a + 1)
        for k, v in enumerate(c):
            if v:
                for j in range(1, q):
                    if k + j <= a:
                        d[k + j] += v * comb(q, j)
        c = d
    # The coefficient of (sum binom(q,j) x^j)^n, divided by (q!)^n.
    # a! b! is the conversion from exponential to ordinary coefficients.
    return c[a] * factorial(a) * factorial(n * q - a) // factorial(q) ** n


def predicted(n, q, a):
    b = n * q - a
    if not (0 <= a <= n*q):
        return (0, 0, 0)
    if q == 1:
        v = factorial(n)
        return (v, v, v)
    if q == 2:
        v = factorial(n) ** 2 if a == n else 0
        return (v, v, factorial(2*n) // 2**n)
    if n <= a <= n*(q-1) and (a-n) % (q-2) == 0:
        t = (a-n)//(q-2)
        one = comb(n,t)*factorial(a)*factorial(b)//factorial(q-1)**n
    else:
        one = 0
    two = coefficient_count(n,q,a)
    return (one, two, two)


def exhaustive_case(n, q, a):
    m = n*q
    b = m-a
    assert b >= 0
    # Neighborhood graph is rebuilt from the stated two-part item relation.
    adjacency = [sum(1 << j for j in range(m) if (i < a) != (j < a))
                 for i in range(m)]
    @lru_cache(maxsize=None)
    def compact(mask, alpha, beta):
        vertices = [i for i in range(m) if mask & (1 << i)]
        if not vertices:
            return True
        # Breadth-first distances entirely within the induced bundle.
        distances = {}
        for root in vertices:
            D = {root:0}
            layer = [root]
            while layer:
                fresh = []
                for u in layer:
                    for v in vertices:
                        if v not in D and adjacency[u] & (1 << v):
                            D[v] = D[u]+1
                            fresh.append(v)
                layer=fresh
            distances[root]=D
        for r in range(1, min(alpha,len(vertices))+1):
            for centers in combinations(vertices,r):
                if all(any(distances[c].get(v,10**6) <= beta for c in centers)
                       for v in vertices):
                    return True
        return False

    ans = [0,0,0]
    count = 0
    def allocate(remaining, seat, masks):
        nonlocal count
        if seat == n-1:
            subsets = masks+(remaining,)
            count+=1
            if all(compact(x,1,1) for x in subsets):
                ans[0]+=1
            if all(compact(x,1,2) for x in subsets):
                ans[1]+=1
            if all(compact(x,2,1) for x in subsets):
                ans[2]+=1
            return
        verts = [i for i in range(m) if (remaining>>i)&1]
        for c in combinations(verts,q):
            piece=sum(1<<i for i in c)
            allocate(remaining^piece, seat+1,masks+(piece,))
    allocate((1<<m)-1,0,())
    exp = predicted(n,q,a)
    assert tuple(ans)==exp,(n,q,a,ans,exp)
    assert count == factorial(m)//factorial(q)**n,(n,q,a,count)
    return count


def asymptotic_check():
    # Central coefficient of (1+3x/2+x^2)^n, using integer weights (2,3,2).
    data=[]
    for n in (2,4,8,16,32,64):
        c=[0]*(2*n+1)
        c[0]=1
        for _ in range(n):
            d=[0]*(2*n+1)
            for k,v in enumerate(c):
                if v:
                    for j,weight in enumerate((2,3,2)):
                        if k+j<=2*n:
                            d[k+j]+=weight*v
            c=d
        # [x^n](1+1.5x+x^2)^n=c[n]/2^n
        ratio=comb(n,n//2)*2**n/c[n]
        scaled=ratio/(4/7)**n
        data.append((n,float(ratio),float(scaled)))
    return data


def main():
    cases = [(n,q,a) for n,q in [(2,2),(3,2),(2,3),(3,3),(2,4),(3,4),(2,5)]
             for a in range(1,n*q)]
    cases += [(4,3,a) for a in (4,6,8)]
    equitable = 0
    for n,q,a in cases:
        equitable += exhaustive_case(n,q,a)
    print('PASS: direct induced-distance enumeration')
    print('cases:',len(cases),'equitable allocations:',equitable)
    print('K_6,6 with three agents, four goods each:',predicted(3,4,6))
    print('K_8,8 with four agents, four goods each:',predicted(4,4,8))
    print('balanced four-item ratio scaling (limit 4/sqrt(7)):',asymptotic_check())
    print('asymptotic limit:',4/sqrt(7))

if __name__=='__main__':main()
