#!/usr/bin/env python3
"""Independent transfer, maximal-independent-set, and double-cover checks."""
from itertools import product
try:
    import sympy as sp
except ImportError:
    sp = None

ALPHABET = ('T','B','E')
PAIRS=list(product(ALPHABET,repeat=2))

def local(a,b,c):
    if b=='E':
        return (a,c) in (('T','B'),('B','T'))
    return a != b and c != b

def mat():
    return [[int(b==u and local(a,b,v)) for u,v in PAIRS] for a,b in PAIRS]

def multiply(a,b):
    n=len(a)
    ans=[[0]*n for _ in range(n)]
    for i in range(n):
        for k,c in enumerate(a[i]):
            if c:
                for j,d in enumerate(b[k]):
                    ans[i][j] += c*d
    return ans

def trace_power(T,n):
    m=len(T); a=[[int(i==j) for j in range(m)] for i in range(m)]
    while n:
        if n%2: a=multiply(a,T)
        T=multiply(T,T);n//=2
    return sum(a[i][i] for i in range(m))

def luc(n):
    a,b=2,1
    for _ in range(n):a,b=b,a+b
    return a

def closed(n): return luc(n)+(2 if n%3==0 else -1)

def word_count(n):
    return sum(all(local(w[(i-1)%n],w[i],w[(i+1)%n]) for i in range(n))
               for w in product(ALPHABET,repeat=n))

def is_maximal_independent(graph, subset):
    for v,adj in enumerate(graph):
        if (subset>>v)&1:
            if (subset & adj):return False
        elif not (subset&adj):
            return False
    return True

def prism_graph(n):
    graph=[]
    for rail in (0,1):
        for i in range(n):
            graph.append((1<<(rail*n+(i-1)%n)) |
                         (1<<(rail*n+(i+1)%n)) |
                         (1<<((1-rail)*n+i)))
    return graph

def independent_set_count(graph):
    return sum(is_maximal_independent(graph,i) for i in range(1<<len(graph)))

def cover_graph(graph):
    m=len(graph)
    return [(sum(1 << (v+m) for v in range(m) if graph[u]>>v&1)) for u in range(m)] + graph

def check_odd_cover_isomorphism(n):
    assert n >= 3 and n%2 == 1
    def mapped(i,rail,phase):
        j = next(j for j in range(2*n) if j%n==i and j%2==phase)
        return ((j+n*rail)%(2*n),rail)
    image=set(mapped(i,a,t) for i in range(n) for a in range(2) for t in range(2))
    assert len(image)==4*n
    for i in range(n):
        for a in range(2):
            for t in range(2):
                j,b=mapped(i,a,t)
                actual={mapped((i+1)%n,a,1-t),mapped((i-1)%n,a,1-t),mapped(i,1-a,1-t)}
                expected={((j+1)%(2*n),b),((j-1)%(2*n),b),(j,1-b)}
                assert actual==expected,(n,i,a,t,actual,expected)
    return True

if __name__ == '__main__':
    for n in (3,5,7,9,11):assert check_odd_cover_isomorphism(n)
    T=mat()
    if sp:
        t=sp.Symbol('t')
        characteristic=sp.factor(sp.Matrix(T).charpoly(t).as_expr())
        assert characteristic==t**5*(t*t-t-1)*(t*t+t+1)
        print('characteristic polynomial:',characteristic)
    for n in range(3,31):
        assert trace_power(T,n)==closed(n),n
        if n<=9: assert word_count(n)==closed(n),n
    for n in range(3,9):
        graph=prism_graph(n)
        assert independent_set_count(graph)==closed(n),n
    for n in range(3,6):
        graph=prism_graph(n)
        cover=cover_graph(graph)
        m=independent_set_count(cover)
        assert m==(closed(n)**2 if n%2==0 else closed(2*n)),(n,m)
    print('PASS: transfer traces n=3,...,30; independent direct counts n=3,...,8; double-cover direct counts n=3,...,5; odd cover edge isomorphisms n=3,5,7,9,11')
