"""Direct two-step chip-firing verification; Python standard library only.
Enumerates nonisomorphic small trees by canonicalizing all Prufer words.
This is a finite check, not a proof of the infinite theorem.
"""
import heapq
from itertools import product

def tree(n,word):
    deg=[1]*n
    for x in word:deg[x]+=1
    q=[i for i in range(n) if deg[i]==1];heapq.heapify(q)
    adj=[set() for _ in range(n)]
    for x in word:
        v=heapq.heappop(q);adj[v].add(x);adj[x].add(v)
        deg[v]-=1;deg[x]-=1
        if deg[x]==1:heapq.heappush(q,x)
    v=heapq.heappop(q);w=heapq.heappop(q)
    adj[v].add(w);adj[w].add(v)
    return [tuple(sorted(a)) for a in adj]

def canonical(adj):
    n=len(adj);degree=[len(a) for a in adj]
    leaves=[i for i,d in enumerate(degree) if d<=1]
    remain=n
    while remain>2:
        remain-=len(leaves);nxt=[]
        for v in leaves:
            for w in adj[v]:
                degree[w]-=1
                if degree[w]==1:nxt.append(w)
        leaves=nxt
    def encode(v,p):
        return '('+''.join(sorted(encode(w,v) for w in adj[v] if w!=p))+')'
    return min(encode(v,-1) for v in leaves)

def types(n):
    found={}
    for word in product(range(n),repeat=n-2):
        adj=tree(n,word)
        key=canonical(adj)
        if key not in found:found[key]=adj
    return list(found.values())

def update(adj,c):
    d=[len(a) for a in adj]
    f=[int(c[i]>=d[i]) for i in range(len(adj))]
    return tuple(c[i]-d[i]*f[i]+sum(f[j] for j in adj[i]) for i in range(len(adj)))

def enumerate_2cycles(adj):
    cnt=0
    for c in product(*(range(2*len(x)) for x in adj)):
        t=update(adj,c)
        if t!=c and update(adj,t)==c:cnt+=1
    return cnt

def weighted_cut(adj):
    return sum(__import__('math').prod(sum(x[v]!=x[w] for w in adj[v]) for v in range(len(adj))) for x in product((0,1),repeat=len(adj)))

def path(n):
    return [tuple(j for j in (i-1,i+1) if 0<=j<n) for i in range(n)]

def star(n):
    return [tuple(range(1,n))]+[(0,) for _ in range(n-1)]

if __name__=='__main__':
    total=0
    for n in range(2,8):
        arr=[]
        for adj in types(n):
            a=enumerate_2cycles(adj)
            assert a==weighted_cut(adj),(n,adj,a)
            arr.append(a);total+=1
        print('ALL_TREES',n,len(arr),min(arr),max(arr))
    for n in (8,9,10):
        for tag,adj in [('PATH',path(n)),('STAR',star(n))]:
            val=enumerate_2cycles(adj)
            assert val==weighted_cut(adj)
            print(tag,n,val);total+=1
    for name,adj in [('TRIANGLE',((1,2),(0,2),(0,1))),('SQUARE',((1,3),(0,2),(1,3),(0,2))),('K4',((1,2,3),(0,2,3),(0,1,3),(0,1,2)))]:
        a=enumerate_2cycles(adj)
        assert a==weighted_cut(adj)
        print(name,a);total+=1
    print('DIRECT_STATES_OK',total)
