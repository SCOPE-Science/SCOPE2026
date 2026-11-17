"""Exact certificates for spatially fixed binary minority automata.

Standard-library-only, run as: python3 verify.py.
The spectral inequalities use integer Collatz-Wielandt row bounds.
"""
from math import gcd

BOUNDS = {1:(16180,16181), 2:(16663,16664),
          3:(16576,16577), 4:(16593,16594)}

def graph(r):
    size = 1 << (2*r)
    adjacency = [[] for _ in range(size)]
    for a in range(size):
        central = (a >> (r-1)) & 1
        for v in (0, 1):
            ones = a.bit_count() + v - central
            opposites = ones if central == 0 else 2*r - ones
            if opposites >= r:
                adjacency[a].append(((a << 1) & (size-1)) | v)
    return adjacency

def components(a):
    n=len(a)
    reverse=[[] for _ in range(n)]
    for u,links in enumerate(a):
        for v in links:
            reverse[v].append(u)
    visited=set()
    order=[]
    def dfs(u):
        visited.add(u)
        for v in a[u]:
            if v not in visited: dfs(v)
        order.append(u)
    for v in range(n):
        if v not in visited: dfs(v)
    visited=set()
    result=[]
    def dfs2(u,comp):
        visited.add(u)
        comp.add(u)
        for v in reverse[u]:
            if v not in visited: dfs2(v,comp)
    for v in reversed(order):
        if v not in visited:
            comp=set()
            dfs2(v,comp)
            result.append(comp)
    return sorted(result,key=len,reverse=True)

def period_of_component(a, comp):
    root = min(comp)
    depth = {root:0}
    bfs = [root]
    for u in bfs:
        for v in a[u]:
            if v in comp and v not in depth:
                depth[v] = depth[u]+1
                bfs.append(v)
    assert len(depth) == len(comp)
    period = 0
    for u in comp:
        for v in a[u]:
            if v in comp:
                period=gcd(period,depth[u]+1-depth[v])
    return period

def certificate(a, core, r, steps=50):
    x={u:1 for u in core}
    for _ in range(steps):
        x={u:sum(x[v] for v in a[u] if v in core) for u in core}
    y={u:sum(x[v] for v in a[u] if v in core) for u in core}
    lo,hi=BOUNDS[r]
    assert all(lo*x[u]<10000*y[u]<hi*x[u] for u in core)
    return lo,hi,len(str(max(x.values())))

def direct_fixed(r,n):
    assert n>2*r
    total=0
    for state in range(1<<n):
        stable=True
        for i in range(n):
            bit=(state>>i)&1
            opposite=sum(((state>>((i+j)%n))&1)!=bit
                         for j in range(-r,r+1) if j)
            if opposite<r:
                stable=False
                break
        total+=stable
    return total

def trace_power(a,n):
    result=0
    for initial in range(len(a)):
        x={initial:1}
        for _ in range(n):
            y={}
            for u,count in x.items():
                for v in a[u]:
                    y[v]=y.get(v,0)+count
            x=y
        result+=x.get(initial,0)
    return result

def main():
    for r in (1,2,3,4):
        a=graph(r)
        groups=components(a)
        core=groups[0]
        assert len(core)>1
        assert all(len(c)==1 and u not in a[u] for c in groups[1:] for u in c)
        assert period_of_component(a,core)==1
        lo,hi,digits=certificate(a,core,r)
        tested=[]
        for n in range(2*r+1,min(2*r+5,13)):
            direct=direct_fixed(r,n)
            transfer=trace_power(a,n)
            assert direct==transfer,(r,n,direct,transfer)
            tested.append((n,direct))
        print(f'r={r}; states={len(a)}; edges={sum(map(len,a))}; '
              f'primitive_core={len(core)}; acyclic_states={len(a)-len(core)}; '
              f'10000*rho strictly between {lo} and {hi}; '
              f'max_vector_digits={digits}; direct_vs_transfer={tested}')
    print('PROVED: rho(1) < rho(2) > rho(3) < rho(4) by strict rational enclosures.')
    print('All certificate assertions passed.')

if __name__=='__main__': main()
