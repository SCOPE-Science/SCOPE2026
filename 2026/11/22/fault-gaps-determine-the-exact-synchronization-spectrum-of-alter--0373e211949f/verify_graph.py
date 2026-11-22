"""Exhaustive graph-based checker for periodically switched NOR; Python 3 stdlib.
Run: python3 verify_graph.py
"""
from itertools import combinations
from math import gcd


def nor(x, n, edges):
    adj=[0]*n
    for u,v in edges:
        adj[u] |= 1<<v
        adj[v] |= 1<<u
    z=0
    for i in range(n):
        if x&adj[i] == 0:
            z |= 1<<i
    return z


def edges(m):
    a=[(2*j,2*j+1) for j in range(m)]
    b=[(2*j-1 if j else 2*m-1,2*j) for j in range(m)]
    return a,b


def gap_lengths(m, mask):
    s=[j for j in range(m) if (mask>>j)&1]
    return [(s[(i+1)%len(s)]-s[i])%m or m for i in range(len(s))]


def first_hit(m, mask, x):
    a,b=edges(m)
    b=[edge for j,edge in enumerate(b) if not (mask>>j)&1]
    full=(1<<(2*m))-1
    state=x
    for t in range(m+1):
        if state==full:return t
        state=nor(nor(state,2*m,a),2*m,b)
    raise AssertionError(('failed to converge',m,mask,x))


def run():
    graphcases=0; tested=0
    for m in range(2,7):
        a,b=edges(m)
        for mask in range(1,1<<m):
            gs=gap_lengths(m,mask)
            L=max(gs)
            q=lambda t:sum(max(g-t,0) for g in gs)
            observed=[0]*(m+1)
            for x in range(1<<(2*m)):
                observed[first_hit(m,mask,x)]+=1
            expected=[1]+[4**(m-q(t))-4**(m-q(t-1)) for t in range(1,m+1)]
            assert observed == expected,(m,mask,gs,observed,expected)
            assert max(t for t,v in enumerate(observed) if v)>0
            assert max(t for t,v in enumerate(observed) if v)==L
            tested += 1<<(2*m);graphcases+=1
        # No-fault group: independently classify all states using direct graph updates
        visited=set();orbit_counts={}
        for x in range(1<<(2*m)):
            if x in visited:continue
            orbit=[];z=x
            while z not in visited:
                visited.add(z);orbit.append(z)
                z=nor(nor(z,2*m,a),2*m,b)
            assert z==x
            orbit_counts[len(orbit)]=orbit_counts.get(len(orbit),0)+1
        def mob(n):
            ps=[];d=2
            while d*d<=n:
                if n%d==0:
                    ps.append(d)
                    while n%d==0:n//=d
                d+=1
            if n>1:ps.append(n)
            return 0 if len(set(ps))<len(ps) else (-1)**len(ps)
        def mu(n):
            # small enough that subset-free divisor-lattice recursion suffices
            if n==1:return 1
            return -sum(mu(d) for d in range(1,n) if n%d==0)
        expected_counts={d:sum(mu(d//e)*4**e for e in range(1,d+1) if d%e==0)//d for d in range(1,m+1) if m%d==0}
        assert orbit_counts==expected_counts,(m,orbit_counts,expected_counts)
    print('PASS: all nonempty fault sets for m=2..6;',graphcases,'fault patterns;',tested,'phase-zero initial states.')
    print('PASS: fault-free complete orbit populations for m=2..6.')
if __name__=='__main__':run()
