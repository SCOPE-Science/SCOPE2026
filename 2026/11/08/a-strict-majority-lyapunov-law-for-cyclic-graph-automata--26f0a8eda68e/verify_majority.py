from itertools import product
from random import Random

def step(col, adj, theta, k):
    nxt=list(col)
    moved=[]
    for v,neighbors in enumerate(adj):
        if sum(col[w]==(col[v]+1)%k for w in neighbors)>=theta[v]:
            nxt[v]=(col[v]+1)%k
            moved.append(v)
    return tuple(nxt),moved

def pot(col,adj):
    return sum(col[v]==col[w] for v,adjv in enumerate(adj) for w in adjv if w>v)

def verify(adj,k,states):
    theta=[len(neigh)//2+1 for neigh in adj]
    m=sum(map(len,adj))//2
    num_states=0
    for state in states:
        num_states+=1
        col=tuple(state)
        nchange=0
        for t in range(m+1):
            nex,moved=step(col,adj,theta,k)
            if not moved: break
            inc=pot(nex,adj)-pot(col,adj)
            margin=sum(2*theta[v]-len(adj[v]) for v in moved)
            assert inc>=margin>0,(adj,k,col,nex,moved,inc,margin)
            nchange+=len(moved)
            assert nchange<=m
            col=nex
        else: raise AssertionError('did not fixate')
    return num_states

def adj_from_mask(n,mask):
    adj=[[] for _ in range(n)]
    ix=0
    for i in range(n):
        for j in range(i+1,n):
            if mask&(1<<ix):adj[i].append(j);adj[j].append(i)
            ix+=1
    return adj

def tripartite(m):
    n=3*m
    return [[j for j in range(n) if j//m!=i//m] for i in range(n)]

def moore(L):
    adj=[]
    for x in range(L):
        for y in range(L):
            arr={( ((x+dx)%L)*L+(y+dy)%L) for dx in (-1,0,1) for dy in (-1,0,1) if (dx,dy)!=(0,0)}
            adj.append(sorted(arr))
    return adj

def main():
    rng=Random(1804)
    graphs=0; total_states=0
    for n in range(2,6):
        for mask in range(1<<(n*(n-1)//2)):
            adj=adj_from_mask(n,mask)
            graphs+=1
            for k in (3,4):
                count=verify(adj,k,product(range(k),repeat=n))
                total_states+=count
    print('ALL finite graphs n=2..5 for k=3,4: graphs',graphs,'trajectories',total_states)
    for n in (8,12,18,30):
        for _ in range(100):
            adj=adj_from_mask(n,rng.getrandbits(n*(n-1)//2))
            verify(adj,3,[tuple(rng.randrange(3) for _ in range(n)) for __ in range(7)])
    print('Random graph, random configuration tests passed')
    for L in (3,4,5,7):
        adj=moore(L)
        assert all(len(a)==8 for a in adj)
        count=verify(adj,3,[tuple(rng.randrange(3) for _ in range(L*L)) for __ in range(400)])
        print('Moore',L, 'random configurations',count,'pass')
    for m in (1,2,3,7):
        adj=tripartite(m)
        c=tuple(i//m for i in range(3*m))
        for k in range(3):
            nex,moved=step(c,adj,[m]*len(adj),3)
            assert len(moved)==len(adj)
            assert nex==tuple((i//m+k+1)%3 for i in range(3*m))
            c=nex
        assert c==tuple(i//m for i in range(3*m))
    print('Sharp majority-bound examples K_m,m,m passed')
    for m in (1,2,3):
        adj=[[j for j in range(2*m) if j//m!=i//m] for i in range(2*m)]
        c=tuple(i//m for i in range(2*m))
        for i in range(2):
            c,mov=step(c,adj,[m]*len(adj),2)
            assert len(mov)==2*m
        assert c==tuple(i//m for i in range(2*m))
    print('Binary counterexample K_m,m passed')

if __name__=='__main__':main()

def verify_partial_subsets():
    checked=0
    for n in (2,3,4):
        for mask in range(1<<(n*(n-1)//2)):
            adj=adj_from_mask(n,mask)
            theta=[len(q)//2+1 for q in adj]
            for col in product(range(3),repeat=n):
                col=tuple(col)
                proposed,moving=step(col,adj,theta,3)
                for selected_mask in range(1,1<<len(moving)):
                    subset={moving[i] for i in range(len(moving)) if selected_mask&(1<<i)}
                    nxt=tuple((c+1)%3 if v in subset else c for v,c in enumerate(col))
                    increment=pot(nxt,adj)-pot(col,adj)
                    margin=sum(2*theta[v]-len(adj[v]) for v in subset)
                    assert increment>=margin>0
                    checked+=1
    print('All eligible nonempty partial synchronous update subsets on all graphs with n=2..4:',checked,'pass')

if __name__=='__main__':verify_partial_subsets()
