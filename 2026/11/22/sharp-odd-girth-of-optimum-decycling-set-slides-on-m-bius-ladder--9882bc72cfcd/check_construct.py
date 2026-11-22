"""Independent parametric certificate for optimal FVS token-slide odd cycles.
Python 3.9+, standard library only. Run: python check_construct.py
"""

def make(n):
    # (layer, rung) with layer 0=a, 1=b. Twisted closure.
    e = set()
    def add(u,v): e.add(frozenset((u,v)))
    for i in range(n):
        add((0,i),(1,i))
        if i<n-1:
            add((0,i),(0,i+1)); add((1,i),(1,i+1))
    add((0,n-1),(1,0));add((1,n-1),(0,0))
    return e

def forest(n, edges, removed):
    vertices={(layer,i) for layer in (0,1) for i in range(n)}-removed
    parent={v:v for v in vertices}
    def root(x):
        while parent[x]!=x:
            x=parent[x]
        return x
    for e in edges:
        if e<=vertices:
            x,y=tuple(e)
            x,y=root(x),root(y)
            if x==y:return False
            parent[x]=y
    return True

def certificate(n):
    assert n>=4 and n%2==0
    e=make(n)
    s={(0,i) for i in range(0,n-2,2)}|{(0,n-1),(1,n-2)}
    initial=frozenset(s);states=[initial]
    def move(a,b):
        assert a in s and b not in s and frozenset((a,b)) in e
        s.remove(a);s.add(b)
        states.append(frozenset(s))
    move((1,n-2),(1,n-3))
    for i in range(n-4,1,-2): move((0,i),(0,i-1))
    move((1,n-3),(0,n-3))
    move((0,0),(1,n-1))
    move((1,n-1),(1,n-2))
    for i in range(n-3,2,-2): move((0,i),(0,i-1))
    move((0,1),(0,0))
    assert len(states)==n+2 and len(set(states[:-1]))==n+1
    assert states[0]==states[-1]
    for t in states:
        assert len(t)==n//2+1
        empty=[i for i in range(n) if (0,i) not in t and (1,i) not in t]
        assert all((i+1)%n not in empty for i in empty)
        assert sum(edge<=t for edge in e)<=1
        assert forest(n,e,set(t))
    return n+1

if __name__=='__main__':
    for n in range(4,102,2):
        assert certificate(n)==n+1
    print('PASS: 49 even rung orders 4..100; every move, minimum size, distinct intermediate state, induced forest, and exact cycle length')
