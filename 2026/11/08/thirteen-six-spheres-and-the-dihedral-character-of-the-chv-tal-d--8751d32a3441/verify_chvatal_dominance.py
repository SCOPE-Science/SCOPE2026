#!/usr/bin/env python3
"""Finite, standard-library-only verification of a Chvatal-graph dominance complex.

The proof uses Forman's acyclic-matching theorem. This program checks its finite
hypotheses by exhaustive enumeration, and computes the exact automorphism character
by signed simplicial Lefschetz numbers. No other files are needed.
"""
from collections import Counter, deque
from itertools import combinations

EDGES = [
    (0,1),(0,4),(0,6),(0,9),
    (1,2),(1,5),(1,7),
    (2,3),(2,6),(2,8),
    (3,4),(3,7),(3,9),
    (4,5),(4,8),
    (5,10),(5,11),
    (6,10),(6,11),
    (7,8),(7,11),
    (8,10),
    (9,10),(9,11),
]
N=12
FULL=(1<<N)-1
PIVOT_ORDER=(10,4,3,6,11,7,0,2,8,9,1,5)
R=(4,0,9,10,5,1,3,6,11,8,7,2)
S=(0,4,3,2,1,5,9,8,7,6,11,10)

def graph():
    neigh=[0]*N
    assert len(EDGES)==24 and len(set(EDGES))==24
    for a,b in EDGES:
        assert 0<=a<b<N
        neigh[a]|=1<<b
        neigh[b]|=1<<a
    assert all(x.bit_count()==4 for x in neigh)
    assert sum(((neigh[a]>>b)&1) * ((neigh[b]>>c)&1) * ((neigh[c]>>a)&1)
               for a in range(N) for b in range(N) for c in range(N))==0
    alpha=max(s.bit_count() for s in range(1<<N) if all(
        (neigh[v]&s)==0 for v in range(N) if (s>>v)&1))
    assert alpha==4
    return neigh

def is_face_by_forbidden(s,closed):
    return all((s & nbr)!=nbr for nbr in closed)

def is_face_by_domination(s,closed):
    selected=(~s)&FULL
    for v in range(N):
        if not (closed[v]&selected):return False
    return True

def get_faces(closed):
    a=set()
    for s in range(1,FULL+1):
        ok=is_face_by_forbidden(s,closed)
        assert ok==is_face_by_domination(s,closed)
        if ok:a.add(s)
    assert len(a)==3098
    assert Counter(s.bit_count()-1 for s in a)=={0:12,1:66,2:220,3:495,4:780,5:840,6:544,7:141}
    assert sum((-1)**(s.bit_count()-1) for s in a)==14
    return a

def matching(faces):
    alive=set(faces)
    pairs=[]
    for v in PIVOT_ORDER:
        b=1<<v
        for small in sorted(alive,key=lambda x:(x.bit_count(),x)):
            if small not in alive or small&b:continue
            large=small|b
            if large in alive:
                alive.remove(small)
                alive.remove(large)
                pairs.append((small,large))
    assert len(set(PIVOT_ORDER))==N
    assert len(pairs)==1542 and len(alive)==14
    assert Counter(t.bit_count()-1 for t in alive)=={0:1,6:13}
    assert len({x for p in pairs for x in p})==2*len(pairs)
    return pairs,alive

def check_acyclicity(faces,pairs):
    # Orient matched covering arrows upward and every other covering arrow downward.
    matched_top_to_bottom={large:small for small,large in pairs}
    out={face:[] for face in faces}
    indeg={face:0 for face in faces}
    covers=0
    for upper in faces:
        t=upper
        while t:
            bit=t&-t;t-=bit
            lower=upper-bit
            if not lower:continue # The empty face is excluded from the face poset.
            assert lower in faces
            src,dst=((lower,upper) if matched_top_to_bottom.get(upper)==lower
                     else (upper,lower))
            out[src].append(dst)
            indeg[dst]+=1
            covers+=1
    assert covers==16648
    q=deque(f for f in faces if indeg[f]==0)
    processed=0
    while q:
        f=q.popleft();processed+=1
        for g in out[f]:
            indeg[g]-=1
            if indeg[g]==0:q.append(g)
    assert processed==len(faces),f"directed cycle: {processed}/{len(faces)}"
    return covers

def rank_f2(cols):
    pivots={}
    for c in cols:
        while c:
            p=c.bit_length()-1
            if p not in pivots:
                pivots[p]=c
                break
            c ^= pivots[p]
    return len(pivots)

def homology_mod2(faces):
    by_dim={d:sorted(s for s in faces if s.bit_count()==d+1) for d in range(8)}
    ranks={}
    for d in range(1,8):
        rowidx={v:i for i,v in enumerate(by_dim[d-1])}
        columns=[]
        for f in by_dim[d]:
            x=0;t=f
            while t:
                bit=t&-t;t-=bit
                x^=1<<rowidx[f-bit]
            columns.append(x)
        ranks[d]=rank_f2(columns)
    betti={d:len(by_dim[d])-ranks.get(d,0)-ranks.get(d+1,0) for d in by_dim}
    assert betti=={0:1,1:0,2:0,3:0,4:0,5:0,6:13,7:0},betti
    return ranks,betti

def compose(p,q):return tuple(p[q[i]] for i in range(N))
def power(p,k):
    z=tuple(range(N))
    for _ in range(k):z=compose(p,z)
    return z

def auts_backtracking(neigh):
    # Exhaustive signed-adjacency backtracking, independent of the specified generators.
    found=[];mapping={};used=set()
    calls=0
    def rec():
        nonlocal calls
        calls+=1
        if len(mapping)==N:
            found.append(tuple(mapping[i] for i in range(N)))
            return
        choices=[]
        for i in range(N):
            if i in mapping:continue
            admissible=[j for j in range(N) if j not in used and all(
                bool((neigh[i]>>k)&1)==bool((neigh[j]>>mapping[k])&1)
                for k in mapping)]
            if not admissible:return
            choices.append((len(admissible),-sum(bool((neigh[i]>>k)&1) for k in mapping),i,admissible))
        _,_,i,candidates=min(choices)
        for j in candidates:
            mapping[i]=j;used.add(j)
            rec()
            used.remove(j);del mapping[i]
    rec()
    assert len(found)==8, (len(found),calls)
    assert len(set(found))==8
    for p in found:
        assert all(bool((neigh[a]>>b)&1)==bool((neigh[p[a]]>>p[b])&1)
                   for a in range(N) for b in range(N))
    return set(found),calls

def parity_of_restricted_permutation(s,p):
    selected=[i for i in range(N) if s&(1<<i)]
    image=[p[i] for i in selected]
    if set(selected)!=set(image):return 0
    inversions=sum(image[i]>image[j] for i in range(len(image)) for j in range(i+1,len(image)))
    return -1 if inversions%2 else 1

def trace(p,faces):
    # Reduced Lefschetz number. The empty simplex contributes -1.
    return -1 + sum(((-1)**(f.bit_count()-1))*parity_of_restricted_permutation(f,p)
                    for f in faces)

def verify_group_and_character(neigh,faces):
    full_autos,calls=auts_backtracking(neigh)
    assert power(R,4)==tuple(range(N))
    assert power(S,2)==tuple(range(N))
    assert compose(S,compose(R,S))==power(R,3)
    G={compose(power(R,i),power(S,j)) for i in range(4) for j in range(2)}
    assert len(G)==8 and G==full_autos
    results={(i,j):trace(compose(power(R,i),power(S,j)),faces)
             for i in range(4) for j in range(2)}
    assert results=={(0,0):13,(1,0):-1,(2,0):1,(3,0):-1,
                     (0,1):-3,(1,1):1,(2,1):-3,(3,1):1},results
    irreps={}
    for a in (1,-1):
        for b in (1,-1):
            num=sum(results[i,j]*(a**i)*(b**j) for i in range(4) for j in range(2))
            assert num%8==0
            irreps[f'r={a},s={b}']=num//8
    two_dim=sum(results[i,j]*(2 if i%4==0 else -2 if i%4==2 else 0)
                if j==0 else 0 for i in range(4) for j in range(2))//8
    assert irreps=={'r=1,s=1':1,'r=1,s=-1':2,'r=-1,s=1':1,'r=-1,s=-1':3}
    assert two_dim==3
    assert sum(irreps.values())+two_dim*2==13
    return results,irreps,two_dim,calls

def main():
    neighbors=graph()
    closed=[neighbors[i]|1<<i for i in range(N)]
    faces=get_faces(closed)
    pairs,critical=matching(faces)
    num_covers=check_acyclicity(faces,pairs)
    ranks,betti=homology_mod2(faces)
    traces,irreps,mult2,search_nodes=verify_group_and_character(neighbors,faces)
    print('CHVATAL_GRAPH vertices=12 edges=24 regular=4 triangle_free=true alpha=4 tau=8')
    print('DOMINANCE_NONEMPTY_FACES',len(faces),'DIMENSIONS',dict(sorted(Counter(f.bit_count()-1 for f in faces).items())))
    print('MATCHED_PAIRS',len(pairs),'CRITICAL_DIMENSIONS',dict(sorted(Counter(f.bit_count()-1 for f in critical).items())))
    print('ORIENTED_COVERING_RELATIONS',num_covers,'ACYCLIC=true')
    print('MOD2_BOUNDARY_RANKS',dict(sorted(ranks.items())),'BETTI',dict(sorted(betti.items())))
    print('AUTOMORPHISMS=8 D4_GENERATORS_VERIFIED=true BACKTRACKING_NODES',search_nodes)
    print('TRACE_BY_R_POWER_S_POWER',dict(sorted(traces.items())))
    print('ONE_DIMENSIONAL_IRREPS',irreps,'STANDARD_TWO_DIMENSIONAL_MULTIPLICITY',mult2)
    print('CHVATAL_DOMINANCE_WEDGE_AND_CHARACTER_PASS')
if __name__=='__main__':main()
