"""Independent finite-state recurrence for fixed states, plus odd-cactus test.
Run: python verify_transfer.py
"""
from itertools import product
from collections import defaultdict

def transfer(n):
    # State consists of current run length 0,1,2, plus left-boundary flag.
    states={(0,False):1}
    for index in range(1,n+1):
        nxt=defaultdict(int)
        for (length,left),count in states.items():
            # append a zero, closing a run
            nxt[(0,False)]+=count*(1 if length in (0,2) or left else 2)
            # append a one, beginning/continuing a run
            if length==0: nxt[(1,index==1)]+=count
            elif length==1 and not left: nxt[(2,False)]+=count
        states=nxt
    return 2*(states.get((0,False),0)+sum(v for (length,left),v in states.items() if length==1 and not (left and n==1)))


def via_matrix(n):
    M=((1,1,0),(2,0,1),(1,0,0))
    def T(k):
        v=(1,0,0)
        for _ in range(k):v=tuple(sum(v[i]*M[i][j] for i in range(3)) for j in range(3))
        return v[0]+v[1]
    return 2*(T(n-1)+(T(n-2) if n>=2 else 0))


def majority_step(x,adj):
    new=0
    for v,neighbors in enumerate(adj):
        ones=sum((x>>u)&1 for u in neighbors)
        bit=((x>>v)&1) if 2*ones==len(neighbors) else int(2*ones>len(neighbors))
        new|=bit<<v
    return new


def cactus(num_cycle, lengths):
    # wedge of disjoint odd cycles (all vertices even degree)
    edges=[]; cur=1
    for length in lengths:
        nodes=[0]+list(range(cur,cur+length-1));cur+=length-1
        for j in range(length):edges.append((nodes[j],nodes[(j+1)%length]))
    adj=[[] for _ in range(cur)]
    for a,b in edges:adj[a].append(b);adj[b].append(a)
    return adj

def run():
    for n in range(1,81):
        a=transfer(n);b=via_matrix(n)
        assert a==b,(n,a,b)
        if n>3: assert a==transfer(n-1)+2*transfer(n-2)+transfer(n-3)
    for lens in ((3,), (5,), (3,3), (3,5), (3,3,3), (5,5)):
        adj=cactus(len(lens),lens)
        F=0;T=0
        for x in range(1<<len(adj)):
            y=majority_step(x,adj)
            F+=x==y
            T+=x==majority_step(y,adj)
        assert F==T,(lens,F,T)
        print('odd-cycle bouquet',lens,'vertices',len(adj),'fixed',F,'two-step',T)
    print('PASS two independent wall-word methods through n=80 and six cactus exhaustions')
if __name__=='__main__':run()
