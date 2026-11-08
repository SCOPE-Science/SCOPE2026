"""Independent finite-state replay for synchronous three-state CCA and GHM on K_{n,n} minus t disjoint edges."""
from itertools import product


def graph(n,t):
    g=[set() for _ in range(2*n)]
    for i in range(n):
        for j in range(n):
            if i!=j or i>=t:
                g[i].add(n+j);g[n+j].add(i)
    return tuple(tuple(sorted(s)) for s in g)


def step_cca(x,g):
    return tuple((c+1)%3 if any(x[j]==(c+1)%3 for j in g[i]) else c for i,c in enumerate(x))


def step_ghm(x,g):
    return tuple((c+1)%3 if c else (1 if any(x[j]==1 for j in g[i]) else 0) for i,c in enumerate(x))


def formula(n,t):
    return 3*(4**n + 2*3**n - 2**(n+2) + 1 + t*2**(n+1) + t*(t-1))


def check(n,t):
    g=graph(n,t)
    A=B=0
    # Diameter is at most 3, so the source's synchronization theorem gives
    # coalescence within 3 updates. We nevertheless perform 8 updates.
    for x in product(range(3),repeat=2*n):
        a=x;b=x
        for _ in range(8):
            a=step_cca(a,g); b=step_ghm(b,g)
        A += len(set(a))==1
        B += len(set(b))==1
    want=formula(n,t)
    assert A==B==want,(n,t,A,B,want)
    return A

if __name__=='__main__':
    total=0
    for n in (3,4,5):
        for t in range(n+1):
            got=check(n,t)
            total+=3**(2*n)
            print('n=%d t=%d CCA=GHM=%d OK' % (n,t,got))
    print('DYNAMICS_PASS cases=15 initial_states=',total)
