"""Finite checks for threshold-two excitable dynamics and cubic edge coloring."""
from itertools import product

def cubic_ladder(n, twist=False):
    assert n >= 3
    edges=set()
    for i in range(n):
        edges.add(tuple(sorted(((i,0),(i,1)))))
    for i in range(n):
        for r in range(2):
            j=(i+1)%n
            rr=1-r if twist and i==n-1 else r
            edges.add(tuple(sorted(((i,r),(j,rr)))))
    return sorted(edges)

def line_neighbors(edges):
    return [tuple(j for j,f in enumerate(edges) if i!=j and set(e)&set(f)) for i,e in enumerate(edges)]

def iterate(s,nb):
    return tuple(2 if a==1 else 0 if a==2 else (1 if sum(s[j]==1 for j in nb[i])>=2 else 0) for i,a in enumerate(s))

def direct(n, twist):
    edges=cubic_ladder(n,twist)
    nb=line_neighbors(edges)
    assert len(edges)==3*n and all(len(x)==4 for x in nb)
    periodic=0
    for state in product(range(3),repeat=len(edges)):
        a=iterate(state,nb)
        if a==state: continue
        b=iterate(a,nb)
        c=iterate(b,nb)
        if c==state:periodic+=1
    return periodic

def edge_color_count(n, twist):
    edges=cubic_ladder(n,twist)
    adj=line_neighbors(edges)
    color=[-1]*len(edges)
    cnt=0
    def recurse(i):
        nonlocal cnt
        if i==len(edges):cnt+=1;return
        forbid={color[j] for j in adj[i] if color[j]>=0}
        for c in range(3):
            if c not in forbid:color[i]=c;recurse(i+1)
        color[i]=-1
    recurse(0)
    return cnt

def formula(n,twist):
    return 2**n + 3 + (-1 if twist else 5)*(-1)**n

if __name__=='__main__':
    for twist in (False,True):
        for n in range(3,11):
            c=edge_color_count(n,twist)
            assert c==formula(n,twist), (n,twist,c)
            if n <= 4:
                d=direct(n,twist)
                assert d==c, (n,twist,d,c)
                print(f"n={n} seam={'twisted' if twist else 'straight'} direct={d} edge_color={c} exact={formula(n,twist)}")
            else:print(f"n={n} seam={'twisted' if twist else 'straight'} edge_color={c} exact={formula(n,twist)}")
    print('PASS: independent state and edge-colouring enumeration')
