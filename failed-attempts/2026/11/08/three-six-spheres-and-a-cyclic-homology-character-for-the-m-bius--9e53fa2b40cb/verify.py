#!/usr/bin/env python3
"""Exact finite verification for the two-independence complex of the Moebius-Kantor graph.
Requires Python >=3.9, standard library only. No files or network access needed.
"""
from collections import Counter, deque

N = 8
V = 2*N
PIVOTS = (4,0,6,11,2,9,14,8,12,13,3,15,7,10,1,5)

def graph():
    adj=[0]*V
    def add(a,b):
        assert a!=b
        adj[a]|=1<<b;adj[b]|=1<<a
    for i in range(N):
        add(i,(i+1)%N)
        add(i,N+i)
        add(N+i,N+(i+3)%N)
    assert all(a.bit_count()==3 for a in adj)
    assert sum(a.bit_count() for a in adj)==48
    assert all((adj[i]>>j&1)==(adj[j]>>i&1) for i in range(V) for j in range(V))
    return adj

def degree_one_check(mask,adj):
    return all((mask & adj[v]).bit_count()<=1 for v in range(V) if mask>>v&1)

def component_check(mask,adj):
    remaining=mask
    while remaining:
        v=(remaining & -remaining).bit_length()-1
        seen=1<<v
        frontier=seen
        while frontier:
            nxt=0
            while frontier:
                b=frontier & -frontier
                frontier^=b
                u=b.bit_length()-1
                nxt |= adj[u]&mask&~seen
            seen |= nxt
            frontier=nxt
        if seen.bit_count()>2:
            return False
        remaining &= ~seen
    return True

def enumerate_faces(adj):
    all_masks=set(range(1<<V))
    brute={s for s in all_masks if degree_one_check(s,adj)}
    grow={0}
    for v in range(V):
        additions=set()
        for s in grow:
            t=s | (1<<v)
            if component_check(t,adj):
                additions.add(t)
        grow |= additions
    assert brute==grow
    return sorted(brute)

def matching(faces):
    left=set(faces)
    pairs=[]
    for v in PIVOTS:
        bit=1<<v
        for s in sorted(left):
            if not s&bit and s|bit in left:
                left.remove(s);left.remove(s|bit)
                pairs.append((s,s|bit))
    return pairs,left

def topo_check(faces,pairs):
    index={s:i for i,s in enumerate(faces)}
    matched=set(pairs)
    indeg=[0]*len(faces)
    arcs=[[] for _ in faces]
    incidences=0
    for t in faces:
        rem=t
        while rem:
            b=rem & -rem;rem-=b;s=t^b
            if s not in index:continue
            if (s,t) in matched:source,target=index[s],index[t]
            else:source,target=index[t],index[s]
            arcs[source].append(target)
            indeg[target]+=1
            incidences+=1
    ready=deque(i for i in range(len(faces)) if indeg[i]==0)
    seen=0
    while ready:
        p=ready.popleft();seen+=1
        for q in arcs[p]:
            indeg[q]-=1
            if indeg[q]==0:ready.append(q)
    assert seen==len(faces),('directed-cycle',seen,len(faces))
    return incidences,seen

def gf2_rank(columns):
    pivots={}
    for c in columns:
        while c:
            p=c.bit_length()-1
            if p not in pivots:
                pivots[p]=c
                break
            c^=pivots[p]
    return len(pivots)

def mod2_homology(faces):
    by_dimension={j:[f for f in faces if f.bit_count()==j+1] for j in range(8)}
    ranks={}
    for j in range(1,8):
        rid={f:i for i,f in enumerate(by_dimension[j-1])}
        cols=[]
        for s in by_dimension[j]:
            t=s;c=0
            while t:
                b=t & -t;t-=b
                c^=1<<rid[s^b]
            cols.append(c)
        ranks[j]=gf2_rank(cols)
    betti=[len(by_dimension[j])-ranks.get(j,0)-ranks.get(j+1,0) for j in range(8)]
    assert betti==[1,0,0,0,0,0,3,0]
    return ranks,betti

def permute(mask,k):
    ans=0
    while mask:
        b=mask&-mask;mask-=b
        i=b.bit_length()-1
        ans |= 1<<((i+k)%8 if i<8 else 8+(i-8+k)%8)
    return ans

def signed_action_on_face(mask,k):
    arr=[]
    for i in range(V):
        if mask>>i&1:
            arr.append((i+k)%8 if i<8 else 8+(i-8+k)%8)
    inv=sum(x>y for j,x in enumerate(arr) for y in arr[j+1:])
    return -1 if inv%2 else 1

def characters(faces,adj):
    # Verify every canonical rotation is an automorphism.
    for k in range(8):
        for i in range(V):
            image=(i+k)%8 if i<8 else 8+(i-8+k)%8
            assert permute(adj[i],k)==adj[image]
    char=[]
    for k in range(8):
        tr=-1  # correction from ordinary to reduced H_0
        for s in faces:
            if not s or permute(s,k)!=s:continue
            tr += (-1 if s.bit_count()%2==0 else 1) * signed_action_on_face(s,k)
        char.append(tr)
    assert char==[3,-1,-1,-1,3,-1,-1,-1]
    eps=[1 if k%2==0 else -1 for k in range(8)]
    v4=[2,0,-2,0,2,0,-2,0]
    assert char==[a+b for a,b in zip(eps,v4)]
    assert sum(char)==0
    return char

def main():
    adj=graph()
    faces=enumerate_faces(adj)
    counts=Counter(s.bit_count()-1 for s in faces)
    assert [counts[j] for j in range(-1,8)]==[1,16,120,512,1324,2064,1840,816,120]
    assert len(faces)==6813
    face_set=set(faces)
    maximal=[s for s in faces if s and all((s|(1<<v)) not in face_set for v in range(V) if not s>>v&1)]
    assert Counter(s.bit_count()-1 for s in maximal)=={6:96,7:120}
    pairs,critical=matching(faces)
    assert len(pairs)==3405
    assert len(critical)==3
    assert critical=={29834,50474,57514}
    assert (0,16) in pairs
    ordinary_pairs=[(a,b) for a,b in pairs if a!=0]
    ordinary_faces=[s for s in faces if s!=0]
    ordinary_critical={s for s in ordinary_faces if s not in {v for a,b in ordinary_pairs for v in (a,b)}}
    assert ordinary_critical==critical|{16}
    ordinary_incidences,ordinary_sorted=topo_check(ordinary_faces,ordinary_pairs)
    assert (ordinary_incidences,ordinary_sorted)==(35104,6812)
    incidences,sorted_count=topo_check(faces,pairs)
    assert incidences==35120 and sorted_count==6813
    ranks,betti=mod2_homology(faces)
    char=characters(faces,adj)
    print('graph_vertices=16 graph_edges=24')
    print('faces_including_empty=6813')
    print('maximal_faces_dim6=96_dim7=120')
    print('face_vector_with_empty=' + ','.join(str(counts[j]) for j in range(-1,8)))
    print('augmented_matched_pairs=3405 ordinary_matched_pairs=3404')
    print('critical_masks=' + ','.join(str(x) for x in sorted(critical)))
    print('critical_dimensions=6,6,6;empty_face_paired=yes')
    print('Hasse_incidences=%d acyclic_sorted=%d' % (incidences, sorted_count))
    print('ordinary_Hasse_incidences=%d ordinary_acyclic_sorted=%d' % (ordinary_incidences,ordinary_sorted))
    print('mod2_boundary_ranks=' + ','.join(str(ranks[j]) for j in range(1,8)))
    print('mod2_betti=' + ','.join(str(x) for x in betti))
    print('cyclic_rational_H6_character=' + ','.join(str(x) for x in char))
    print('cyclic_invariant_dimension=' + str(sum(char)//8))
    print('ALL_CHECKS_PASS')
if __name__=='__main__':main()
