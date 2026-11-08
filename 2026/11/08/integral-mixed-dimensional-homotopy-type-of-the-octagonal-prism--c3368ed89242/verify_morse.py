#!/usr/bin/env python3
"""Exact integral discrete-Morse certificate for the octagonal-prism matching complex."""
from collections import Counter,defaultdict,deque
from functools import lru_cache

N=8
ORDER=[0,22,16,3,18,1,13,10,8,4,17,5,11,15,23,7,2,14,12,9,21,19,20,6]

def edges():
    E=set()
    for row in (0,1):
        for i in range(N):
            E.add(tuple(sorted((row*N+i,row*N+(i+1)%N))))
    for i in range(N): E.add((i,N+i))
    return sorted(E)

def generate():
    E=edges(); used=[(1<<u)|(1<<v) for u,v in E]
    cells=[0]
    for i,vertices in enumerate(used):
        cells += [x|(1<<i) for x in cells if all(not(vertices&used[j]) for j in range(i) if x>>j&1)]
    return sorted(cells)

def match(cells):
    remaining=set(cells)
    pairs=[]
    for i in ORDER:
        bit=1<<i
        for a in sorted(remaining):
            b=a|bit
            if not a&bit and b in remaining:
                remaining.remove(a);remaining.remove(b);pairs.append((a,b))
    return remaining,pairs

def codim(cell):
    for j in range(cell.bit_length()):
        if cell>>j&1: yield cell^(1<<j),(-1)**((cell & ((1<<j)-1)).bit_count())

def verify_acyclic(cells,pairs):
    S=set(cells); P=dict(pairs)
    adj=defaultdict(list);indeg=dict.fromkeys(cells,0);num=0
    for b in cells:
        for a,_ in codim(b):
            if a not in S: continue
            u,v=(a,b) if P.get(a)==b else (b,a)
            adj[u].append(v);indeg[v]+=1;num+=1
    q=deque(x for x in cells if indeg[x]==0);visited=0
    while q:
        u=q.popleft();visited+=1
        for v in adj[u]:
            indeg[v]-=1
            if indeg[v]==0:q.append(v)
    assert visited==len(cells), ('directed matching cycle',visited,len(cells))
    return num

def morse_matrix(cells,critical,pairs):
    # Signed boundary via finite gradient-path recursion in dimension 4/5.
    critical4=sorted(x for x in critical if x.bit_count()==5)
    critical5=sorted(x for x in critical if x.bit_count()==6)
    down={a:b for a,b in pairs if a.bit_count()==5}
    critset=set(critical4)
    visiting=set()
    @lru_cache(None)
    def reduce(face):
        if face in critset:return {face:1}
        if face not in down:return {}
        if face in visiting:raise AssertionError('cyclic gradient recursion')
        visiting.add(face)
        coface=down[face]
        boundary=dict(codim(coface))
        pivot=boundary[face]
        assert abs(pivot)==1
        accum=Counter()
        for other,coef in boundary.items():
            if other==face:continue
            for crit,m in reduce(other).items(): accum[crit]-=coef*pivot*m
        visiting.remove(face)
        return {k:v for k,v in accum.items() if v}
    matrix=[]
    for b in critical5:
        accum=Counter()
        for a,coef in codim(b):
            for crit,m in reduce(a).items():accum[crit]+=coef*m
        matrix.append([accum[c] for c in critical4])
    return critical4,critical5,matrix,reduce.cache_info()

if __name__=='__main__':
    cells=generate();E=edges();crit,pairs=match(cells)
    print('edges',len(E),'all_faces_including_empty',len(cells),'matched_pairs',len(pairs),'critical',Counter(x.bit_count()-1 for x in crit))
    print('codimension_one_incidences',verify_acyclic(cells,pairs))
    c4,c5,mat,info=morse_matrix(cells,crit,pairs)
    print('critical_4_cells',len(c4),'critical_5_cells',len(c5))
    print('signed_morse_boundary_rows:',mat)
    print('distinct_columns',len(set(tuple(r) for r in mat)))
    assert len(c4)==4 and len(c5)==8
    nonzero=[row for row in mat if any(row)]
    assert len(nonzero)==3
    pivot=next(row for row in nonzero if any(row))
    assert 1 in [abs(v) for v in pivot] # unit entry: image primitive
    assert all(row==pivot or row==[-v for v in pivot] for row in nonzero)
    print('integer_smith_invariants', [1,0,0,0])
    # Independent simplicial mod-two chain ranks, without a Morse matching.
    faces_by_size=defaultdict(list)
    for f in cells:
        if f: faces_by_size[f.bit_count()].append(f)
    ranks={}
    for sz in range(2, max(faces_by_size)+1):
        row_index={f:i for i,f in enumerate(faces_by_size[sz-1])}
        pivots={}
        for face in faces_by_size[sz]:
            v=0
            for sub,_ in codim(face):v ^= 1<<row_index[sub]
            while v:
                top=v.bit_length()-1
                if top in pivots:v ^= pivots[top]
                else:pivots[top]=v;break
        ranks[sz]=len(pivots)
    betti={sz-1:len(fs)-ranks.get(sz,0)-ranks.get(sz+1,0)-(sz==1)
           for sz,fs in faces_by_size.items()}
    assert {d:b for d,b in betti.items() if b}=={4:3,5:7},betti
    print('independent_mod2_betti',sorted((d,b) for d,b in betti.items() if b))
    print('OCTAGONAL_PRISM_INTEGRAL_MORSE_OK')
