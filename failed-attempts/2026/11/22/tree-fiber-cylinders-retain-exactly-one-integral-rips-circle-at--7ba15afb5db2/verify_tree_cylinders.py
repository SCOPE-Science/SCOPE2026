"""Exact finite checks for graph-metric Rips complexes of tree cylinders.
Uses only the Python standard library. Finite checks are evidence, not an all-case proof.
"""
from collections import defaultdict, deque
from itertools import combinations


def tree_distances(n, edges):
    nb = [[] for _ in range(n)]
    for a,b in edges:
        nb[a].append(b); nb[b].append(a)
    assert len(edges) == n-1
    d = [[999]*n for _ in range(n)]
    for s in range(n):
        q=deque([s]); d[s][s]=0
        while q:
            v=q.popleft()
            for w in nb[v]:
                if d[s][w] == 999:
                    d[s][w]=d[s][v]+1;q.append(w)
    assert all(x<999 for row in d for x in row)
    return d


def face_sets(n, t, tree_edges):
    td=tree_distances(t,tree_edges)
    size=n*t
    neigh=[0]*size
    for i in range(size):
        for j in range(size):
            if i != j and min(abs(i//t-j//t),n-abs(i//t-j//t)) + td[i%t][j%t] <= 2:
                neigh[i] |= 1<<j
    face={1<<i for i in range(size)}
    frontier=list(face)
    while frontier:
        mask=frontier.pop()
        biggest=mask.bit_length()-1
        choices=neigh[biggest] & ~((1<<(biggest+1))-1)
        for i in range(biggest):
            if mask>>i & 1:
                choices &= neigh[i]
        while choices:
            bit=choices&-choices;choices-=bit
            child=mask|bit
            assert child not in face
            face.add(child); frontier.append(child)
    return face,neigh


def betti_mod2(faces):
    levels=defaultdict(list)
    for m in faces:levels[m.bit_count()-1].append(m)
    level_sizes=[len(levels[k]) for k in range(max(levels)+1)]
    ranks=[]
    for d in range(1,len(level_sizes)):
        rows={m:i for i,m in enumerate(levels[d-1])}; pivots={}
        for simplex in levels[d]:
            v=0; x=simplex
            while x:
                bit=x&-x;x-=bit
                v ^=1<<rows[simplex^bit]
            while v:
                i=v.bit_length()-1
                if i not in pivots:pivots[i]=v;break
                v^=pivots[i]
        ranks.append(len(pivots))
    return [level_sizes[i]-(ranks[i-1] if i>0 else 0)-(ranks[i] if i<len(ranks) else 0) for i in range(len(level_sizes))],level_sizes


def strip_dismantles(k,t,tree_edges):
    td=tree_distances(t,tree_edges)
    alive={(i,j) for i in range(k) for j in range(t)}
    def adjacent(x,y):return abs(x[0]-y[0])+td[x[1]][y[1]]<=2
    # Independent original-square-power vertex-dominance test.
    removed=[]
    while len(alive)>1:
        found=None
        for u in sorted(alive):
            nearu={w for w in alive if adjacent(u,w)}
            for v in sorted(alive):
                if u!=v and nearu <= {w for w in alive if adjacent(v,w)}:
                    found=(u,v);break
            if found:break
        if not found:
            return False,len(alive),removed
        alive.remove(found[0]);removed.append(found)
    return True,len(alive),removed



def explicit_leaf_sequence(k,t,edges):
    # Replays precisely the leaf-pole domination pattern in the proof,
    # not a greedy search for any possible matching.
    d=tree_distances(t,edges)
    alive={(i,v) for i in range(k) for v in range(t)}
    remains=set(range(t))
    tree_nb=[set() for _ in range(t)]
    for u,v in edges:tree_nb[u].add(v);tree_nb[v].add(u)
    while len(remains)>1:
        leaf=next(v for v in sorted(remains) if len(tree_nb[v]&remains)==1)
        parent=next(iter(tree_nb[leaf]&remains))
        if k==1: moves=[((0,leaf),(0,parent))]
        elif k==2: moves=[((0,leaf),(1,parent)),((1,leaf),(0,parent))]
        else: moves=[((0,leaf),(1,parent)),((2,leaf),(1,parent)),((1,leaf),(1,parent))]
        for x,y in moves:
            assert x in alive and y in alive
            n_x={z for z in alive if abs(z[0]-x[0])+d[z[1]][x[1]]<=2}
            n_y={z for z in alive if abs(z[0]-y[0])+d[z[1]][y[1]]<=2}
            assert n_x<=n_y,(k,leaf,parent,x,y,n_x-n_y)
            alive.remove(x)
        remains.remove(leaf)
    assert len(alive)==k
    # The remaining P_k is a full simplex at radius two.
    return True


def square_cycles_independent(n,t,edges):
    # Graph edges in C_n square T (scale one).
    e=[]
    for i in range(n):
        for v in range(t):e.append(tuple(sorted((i*t+v,((i+1)%n)*t+v))))
        for a,b in edges:e.append(tuple(sorted((i*t+a,i*t+b))))
    positions={x:i for i,x in enumerate(e)}
    assert len(positions)==len(e)
    vectors=[]
    for i in range(n):
        j=(i+1)%n
        for a,b in edges:
            sides=[(i*t+a,j*t+a),(i*t+b,j*t+b),(i*t+a,i*t+b),(j*t+a,j*t+b)]
            val=0
            for s in sides:val ^=1<<positions[tuple(sorted(s))]
            vectors.append(val)
    pivots={}
    for val in vectors:
        while val:
            p=val.bit_length()-1
            if p not in pivots: pivots[p]=val;break
            val ^=pivots[p]
    return len(pivots),len(e),len(vectors)


def verify(n,t,edges):
    faces,adj=face_sets(n,t,edges)
    windows=[{(i+j)%n for j in (-1,0,1)} for i in range(n)]
    for f in faces:
        columns={i//t for i in range(n*t) if f>>i&1}
        assert any(columns<=w for w in windows),('uncovered',n,t,columns)
    for k in (1,2,3):
        ok,remain,_=strip_dismantles(k,t,edges)
        assert ok and remain==1,(n,t,k,remain)
        assert explicit_leaf_sequence(k,t,edges)
    betti,counts=betti_mod2(faces)
    assert betti == [1,1]+[0]*(len(betti)-2),(n,t,betti)
    rank,edgenum,num=square_cycles_independent(n,t,edges)
    assert rank == n*(t-1) and num==n*(t-1) and edgenum==n*(2*t-1)
    print('PASS n=%d tree_vertices=%d faces=%d f_vector=%s betti_F2=%s square_rank=%d' %
          (n,t,len(faces),counts,betti,rank))


def main():
    shapes=[('point',1,[]),('path2',2,[(0,1)]),('path3',3,[(0,1),(1,2)]),
        ('star4',5,[(0,i) for i in range(1,5)]),
        ('broom',6,[(0,1),(1,2),(2,3),(2,4),(4,5)])]
    for n in (7,8,9,10):
        for label,t,edges in shapes:
            verify(n,t,edges)
    print('VERIFY_OK 20 all-face and chain complex tests; every strip k<=3 dismantled; primitive square basis mod two')
if __name__ == '__main__':main()
