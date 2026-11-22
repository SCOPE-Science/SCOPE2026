"""Exact finite certificates for shortest-path Rips complexes of a truncated tetrahedral graph after an edge deletion."""
from collections import Counter, deque
from itertools import combinations, permutations

V = tuple((a, b) for a in range(4) for b in range(4) if a != b)
INDEX = {x: i for i, x in enumerate(V)}
EDGES = frozenset((i, j) for i in range(12) for j in range(i + 1, 12)
                  if V[i][0] == V[j][0] or V[i] == (V[j][1], V[j][0]))
FAULTS = {
    'triangle': tuple(sorted((INDEX[(0,1)],INDEX[(0,2)]))),
    'reversal': tuple(sorted((INDEX[(0,1)],INDEX[(1,0)]))),
}
EXPECTED = {
    'triangle': {'diam': 4, 'r1': (12,17,3), 'r2': (12,40,42,10),
                 'core': (12,32,24), 'collapsed':18, 'pi1':21, 'spheres':3},
    'reversal': {'diam': 5, 'r1': (12,17,4), 'r2': (12,37,38,10),
                 'core': (10,23,16), 'collapsed':24, 'pi1':14, 'spheres':2},
}

def graph_distance(edges):
    adj=[set() for _ in range(12)]
    for i,j in edges:
        adj[i].add(j);adj[j].add(i)
    output=[]
    for i in range(12):
        d=[None]*12; d[i]=0; q=deque([i])
        while q:
            a=q.popleft()
            for b in sorted(adj[a]):
                if d[b] is None:
                    d[b]=d[a]+1;q.append(b)
        assert all(x is not None for x in d)
        output.append(tuple(d))
    return tuple(output)

def faces_at(dist, radius):
    out=set()
    for mask in range(1,1<<12):
        vs=[i for i in range(12) if (mask>>i)&1]
        if all(dist[i][j]<=radius for i,j in combinations(vs,2)):
            out.add(mask)
    return out

def fvector(faces):
    tally=Counter(x.bit_count()-1 for x in faces)
    return tuple(tally.get(i,0) for i in range(max(tally)+1))

def free_collapse(faces):
    active=set(faces);ops=[]
    while True:
        immediate={}
        for upper in sorted(active):
            for bit in range(12):
                if upper&(1<<bit):
                    lower=upper^(1<<bit)
                    if lower:
                        immediate.setdefault(lower,[]).append(upper)
        candidates=[(lower,uppers[0]) for lower,uppers in immediate.items()
                    if lower in active and len(uppers)==1]
        if not candidates:break
        # Select highest-dimensional free face; then lowest mask for reproducibility.
        lower,upper=min(candidates,key=lambda z:(-z[0].bit_count(),z[0],z[1]))
        assert lower in active and upper in active
        assert upper.bit_count()==lower.bit_count()+1
        assert (lower&upper)==lower
        assert [u for u in active if u!=lower and u&lower==lower]==[upper]
        active.remove(lower);active.remove(upper)
        ops.append((lower,upper))
    return active,ops

def fgrank(core):
    # Present pi_1 of a two-complex using non-tree oriented edges as generators.
    assert max(x.bit_count() for x in core)<=3
    edges=sorted(x for x in core if x.bit_count()==2)
    faces2=sorted(x for x in core if x.bit_count()==3)
    parent=list(range(12))
    def root(x):
        while parent[x]!=x:x=parent[x]
        return x
    tree=set()
    for e in edges:
        i,j=tuple(k for k in range(12) if (e>>k)&1)
        a,b=root(i),root(j)
        if a!=b:parent[a]=b;tree.add(e)
    assert len(tree)==len([f for f in core if f.bit_count()==1])-1
    gens={e:k+1 for k,e in enumerate(e for e in edges if e not in tree)}
    def reduce_word(w):
        stack=[]
        for x in w:
            if stack and stack[-1]==-x:stack.pop()
            else:stack.append(x)
        while len(stack)>1 and stack[0]==-stack[-1]:stack=stack[1:-1]
        return stack
    words=[]
    for t in faces2:
        ids=[i for i in range(12) if (t>>i)&1]
        word=[]
        for u,v in ((ids[0],ids[1]),(ids[1],ids[2]),(ids[2],ids[0])):
            k=gens.get((1<<u)|(1<<v))
            if k:word.append(k if u<v else -k)
        words.append(reduce_word(word))
    seen=[]
    while True:
        choices=[(len(w),j,abs(w[0])) for j,w in enumerate(words) if len(w)==1]
        if not choices:break
        _,j,pivot=min(choices)
        words=[reduce_word([g for g in w if abs(g)!=pivot])
               for i,w in enumerate(words) if i!=j]
        seen.append(pivot)
    assert len(seen)==len(gens) and not any(words)
    return len(gens),len(seen),len(words)

def gf2_betti(faces):
    groups={k:sorted(f for f in faces if f.bit_count()==k+1) for k in range(12)}
    ranks={0:0}
    for k in range(1,12):
        row={f:i for i,f in enumerate(groups[k-1])}
        pivots={}
        for f in groups[k]:
            x=0
            for i in range(12):
                if f&(1<<i):x^=1<<row[f^(1<<i)]
            while x:
                j=x.bit_length()-1
                if j in pivots:x^=pivots[j]
                else:pivots[j]=x;break
        ranks[k]=len(pivots)
    return tuple(len(groups[k])-ranks.get(k,0)-ranks.get(k+1,0) for k in range(12))

def signed_boundary(faces, dimension):
    higher=sorted(x for x in faces if x.bit_count()==dimension+1)
    lower=sorted(x for x in faces if x.bit_count()==dimension)
    positions={x:i for i,x in enumerate(lower)}
    mat=[[0]*len(higher) for _ in lower]
    for j,f in enumerate(higher):
        ordered=[i for i in range(12) if (f>>i)&1]
        for pos,removed in enumerate(ordered):
            mat[positions[f^(1<<removed)]][j]=1 if pos%2==0 else -1
    return mat,higher

def unit_reduction(matrix):
    # Elementary integral row and column operations with unit pivots.
    m=len(matrix)
    n=len(matrix[0]) if m else 0
    A=[r[:] for r in matrix]
    U=[[int(i==j) for j in range(n)] for i in range(n)]
    rank=0
    while rank<min(m,n):
        pivot=next(((i,j) for i in range(rank,m) for j in range(rank,n)
                    if abs(A[i][j])==1),None)
        if pivot is None:break
        i,j=pivot;k=rank
        A[k],A[i]=A[i],A[k]
        for row in range(m):A[row][k],A[row][j]=A[row][j],A[row][k]
        for row in range(n):U[row][k],U[row][j]=U[row][j],U[row][k]
        sign=A[k][k]
        assert abs(sign)==1
        for row in range(k+1,m):
            factor=A[row][k]*sign
            if factor:
                for col in range(n):A[row][col]-=factor*A[k][col]
        for col in range(k+1,n):
            factor=A[k][col]*sign
            if factor:
                for row in range(m):A[row][col]-=factor*A[row][k]
                for row in range(n):U[row][col]-=factor*U[row][k]
        rank+=1
    # The residual matrix must be all zero. This is an exact certificate
    # for invariant factors all equal to one, not a rational rank proxy.
    assert all(A[i][j]==0 for i in range(rank,m) for j in range(rank,n))
    kernel=[[U[i][j] for j in range(rank,n)] for i in range(n)]
    assert all(sum(matrix[i][j]*kernel[j][c] for j in range(n))==0
               for i in range(m) for c in range(n-rank))
    return rank,kernel

def primitive_fault_map(fault_faces,full_faces):
    d2,triangles=signed_boundary(fault_faces,2)
    rank2,cycles=unit_reduction(d2)
    d3_fault,_=signed_boundary(fault_faces,3)
    rank3,_=unit_reduction(d3_fault)
    full_d3,_=signed_boundary(full_faces,3)
    full_rank3,_=unit_reduction(full_d3)
    full_triangles=sorted(x for x in full_faces if x.bit_count()==3)
    assert len(full_d3)==len(full_triangles)
    pos={face:i for i,face in enumerate(full_triangles)}
    # Columns generate im(d3 of intact) plus all 2-cycles of the fault.
    matrix=[row[:] + [0]*len(cycles[0]) for row in full_d3]
    for i,face in enumerate(triangles):
        for j,v in enumerate(cycles[i]):matrix[pos[face]][len(full_d3[0])+j]=v
    rank_combined,_=unit_reduction(matrix)
    return rank2,rank3,full_rank3,rank_combined,len(cycles[0])

def check_orbits():
    assert len(V)==12 and len(EDGES)==18
    orbit={name:set() for name in FAULTS}
    for p in permutations(range(4)):
        transformed={tuple(sorted((INDEX[(p[V[i][0]],p[V[i][1]])],
                                   INDEX[(p[V[j][0]],p[V[j][1]])])))
                     for i,j in EDGES}
        assert transformed==set(EDGES)
        for name,(i,j) in FAULTS.items():
            x=INDEX[(p[V[i][0]],p[V[i][1]])]
            y=INDEX[(p[V[j][0]],p[V[j][1]])]
            orbit[name].add(tuple(sorted((x,y))))
    assert set.union(*orbit.values())==set(EDGES)
    assert not set.intersection(*orbit.values())
    assert tuple(len(orbit[n]) for n in ('triangle','reversal'))==(12,6)
    return {n:len(x) for n,x in orbit.items()}

def main():
    print('edge_orbits',check_orbits())
    intact=faces_at(graph_distance(EDGES),2)
    assert fvector(intact)==(12,42,48,12)
    full_d2,_=signed_boundary(intact,2)
    full_rank2,_=unit_reduction(full_d2)
    assert full_rank2==31
    for name,edge in FAULTS.items():
        es=EDGES-{edge};d=graph_distance(es);e=EXPECTED[name]
        diam=max(max(row) for row in d)
        assert diam==e['diam']
        f1=faces_at(d,1);f2=faces_at(d,2)
        assert fvector(f1)==e['r1']
        assert fvector(f2)==e['r2']
        core1,collapse1=free_collapse(f1)
        assert max(f.bit_count() for f in core1)<=2
        assert len(collapse1)>=e['r1'][2]
        assert len([f for f in core1 if f.bit_count()==2])-len([f for f in core1 if f.bit_count()==1])+1==(3 if name=='triangle' else 2)
        core2,collapse2=free_collapse(f2)
        assert max(f.bit_count() for f in core2)<=3
        assert fvector(core2)==e['core']
        assert len(collapse2)==e['collapsed']
        generators,killed,remaining=fgrank(core2)
        assert generators==e['pi1'] and killed==generators and remaining==e['spheres']
        euler=sum((-1)**k * z for k,z in enumerate(fvector(core2)))
        assert euler-1==e['spheres']
        br2,br3,fullbr3,combined,zrank=primitive_fault_map(f2,intact)
        expected_lattice={'triangle':(29,10,12,15,13),
                          'reversal':(26,10,12,14,12)}[name]
        assert (br2,br3,fullbr3,combined,zrank)==expected_lattice
        assert len(intact.intersection(f2))==len(f2)
        assert len([x for x in intact if x.bit_count()==3])-full_rank2-fullbr3==5
        betti=gf2_betti(f2)
        assert (betti[0],betti[1],betti[2])==(1,0,e['spheres'])
        for r in range(3,diam):
            f=faces_at(d,r)
            last,ops=free_collapse(f)
            assert fvector(last)==(1,)
            print(name,'r',r,'simplices',len(f),'pairs',len(ops),'collapses_to_vertex')
        print(name,'diam',diam,'r1',e['r1'],'r2',e['r2'],
              'r2_pairs',len(collapse2),'core',fvector(core2),
              'trivialized_pi1_generators',killed,'spheres',e['spheres'],
              'integral_inclusion_rank',combined-fullbr3,
              'primitive_cokernel_rank',5-(combined-fullbr3))
    print('EXACT_RIPS_FAULT_VERIFICATION_OK')

if __name__=='__main__':main()
