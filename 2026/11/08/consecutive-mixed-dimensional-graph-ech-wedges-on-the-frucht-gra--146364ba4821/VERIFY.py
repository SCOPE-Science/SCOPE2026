#!/usr/bin/env python3
"""Exact finite verification of the Frucht graph's graph-Cech nerves at scales 3,4.
Run: python3 VERIFY.py (Python 3 standard library only).
"""
import json
from collections import Counter, defaultdict, deque
from functools import lru_cache
N=12
EDGES=[(0,1),(0,6),(0,7),(1,2),(1,7),(2,3),(2,8),(3,4),(3,9),(4,5),(4,9),(5,6),(5,10),(6,10),(7,11),(8,9),(8,11),(10,11)]
def vertices(mask):
    while mask:
        bit=mask&-mask; yield bit.bit_length()-1;mask-=bit

def graph():
    a=[set() for _ in range(N)]
    for u,v in EDGES:a[u].add(v);a[v].add(u)
    assert len(EDGES)==18 and all(len(x)==3 for x in a)
    return a

def distances(adj):
    out=[]
    for s in range(N):
        row=[-1]*N;row[s]=0;q=deque([s])
        while q:
            u=q.popleft()
            for v in adj[u]:
                if row[v]==-1:row[v]=row[u]+1;q.append(v)
        assert -1 not in row;out.append(row)
    alt=[[0 if i==j else 1 if j in adj[i] else 999 for j in range(N)] for i in range(N)]
    for k in range(N):
        for i in range(N):
            for j in range(N):alt[i][j]=min(alt[i][j],alt[i][k]+alt[k][j])
    assert out==alt
    return out

def witness_facets(dist,r):
    k=r//2
    if r%2:
        return {sum(1<<v for v in range(N) if min(dist[u][v],dist[w][v])<=k) for u,w in EDGES}
    return {sum(1<<v for v in range(N) if dist[u][v]<=k) for u in range(N)}

def face_methods(dist,r,facets):
    faces={0}
    for f in facets:
        sub=f
        while sub:faces.add(sub);sub=(sub-1)&f
    # Independent test of every vertex subset using the defining ball-intersection witness.
    direct={0}
    for mask in range(1,1<<N):
        if any(mask&f==mask for f in facets):direct.add(mask)
    assert faces==direct
    # Every listed facet must be maximal for the two scales in the theorem.
    assert all(not (f!=g and f&g==f) for f in facets for g in facets)
    return faces

def signed_facets(face):
    i=0;rest=face
    while rest:
        bit=rest&-rest;yield face^bit,1 if i%2==0 else -1
        rest-=bit;i+=1

def match(faces,reverse):
    unmatched=set(faces)-{0};pairs={}
    for v in (range(N-1,-1,-1) if reverse else range(N)):
        bit=1<<v
        for low in sorted(x for x in unmatched if not x&bit and x|bit in unmatched):
            high=low|bit
            if low in unmatched and high in unmatched:
                unmatched.remove(low);unmatched.remove(high);pairs[low]=high
    assert len(faces)-1==2*len(pairs)+len(unmatched)
    return pairs,unmatched

def acyclic(faces,pairs):
    nodes=set(faces)-{0}; indeg={x:0 for x in nodes};out={x:[] for x in nodes};inc=0
    for upper in nodes:
        for lower,_ in signed_facets(upper):
            if lower==0:continue
            if pairs.get(lower)==upper:src,dst=lower,upper
            else:src,dst=upper,lower
            indeg[dst]+=1;out[src].append(dst);inc+=1
    q=deque(x for x in nodes if indeg[x]==0);seen=0
    while q:
        x=q.popleft();seen+=1
        for y in out[x]:
            indeg[y]-=1
            if indeg[y]==0:q.append(y)
    assert seen==len(nodes)
    return inc

def integer_morse_differential(pairs,critical):
    up_to_low={h:l for l,h in pairs.items()}
    @lru_cache(None)
    def project(face):
        if face in critical:return {face:1}
        if face in up_to_low:return {}
        assert face in pairs
        upper=pairs[face]
        incidence=dict(signed_facets(upper))[face]
        result=defaultdict(int)
        for other,sign in signed_facets(upper):
            if other==face:continue
            for crit,coefficient in project(other).items():result[crit]-=incidence*sign*coefficient
        return {x:c for x,c in result.items() if c}
    rows=[]
    for high in sorted(critical):
        if high.bit_count()<2:continue
        result=defaultdict(int)
        for face,sign in signed_facets(high):
            for crit,coefficient in project(face).items():result[crit]+=sign*coefficient
        rows.append((high,{x:c for x,c in result.items() if c}))
    return rows

def mod2_ranks(faces):
    bydim={}
    for x in faces:
        if x:bydim.setdefault(x.bit_count()-1,[]).append(x)
    for k in bydim:bydim[k].sort()
    ranks=[0]
    for k in range(1,max(bydim)+1):
        index={x:j for j,x in enumerate(bydim[k-1])};piv={}
        for high in bydim[k]:
            col=0
            for low,_ in signed_facets(high):col^=1<<index[low]
            while col:
                i=col.bit_length()-1
                if i not in piv:piv[i]=col;break
                col^=piv[i]
        ranks.append(len(piv))
    betti=[len(bydim[k])-ranks[k]-(ranks[k+1] if k+1<len(ranks) else 0) for k in range(len(ranks))]
    return ranks,betti

def main():
    adj=graph();dist=distances(adj)
    assert max(map(max,dist))==4
    report={'graph':'Frucht graph','vertices':N,'edges':len(EDGES),'diameter':4}
    for r,expected_faces,expected_pairs,expected_critical in [(3,424,209,{0:1,2:2,3:2}),(4,2085,1040,{0:1,3:2,4:1})]:
        all_witnesses=witness_facets(dist,r)
        facets={f for f in all_witnesses if all(f==g or f&g!=f for g in all_witnesses)}
        faces=face_methods(dist,r,facets)
        assert len(faces)==expected_faces
        pairs,critical=match(faces,True)
        dims=dict(sorted(Counter(x.bit_count()-1 for x in critical).items()))
        assert len(pairs)==expected_pairs and dims==expected_critical
        incidences=acyclic(faces,pairs)
        diff=integer_morse_differential(pairs,critical)
        assert all(not boundary for _,boundary in diff),diff
        ranks,betti=mod2_ranks(faces)
        assert betti==([1,0,2,2,0,0] if r==3 else [1,0,0,2,1,0,0,0,0,0])
        # Independent second ordering, with a distinct Morse boundary and acyclicity check.
        other_pairs,other_critical=match(faces,False)
        other_incidences=acyclic(faces,other_pairs)
        other_diff=integer_morse_differential(other_pairs,other_critical)
        fvector=[sum(x.bit_count()==k+1 for x in faces) for k in range(max(x.bit_count() for x in faces))]
        report['scale_'+str(r)]={'faces_with_empty':len(faces),'maximal_facets':len(facets),'face_vector':fvector,
            'matched_pairs':len(pairs),'critical':dims,'Hasse_incidences':incidences,
            'integral_Morse_boundary_nonzero_entries':sum(len(b) for _,b in diff),
            'mod2_boundary_ranks':ranks,'mod2_Betti':betti,
            'second_matching_pairs':len(other_pairs),'second_matching_critical':dict(sorted(Counter(x.bit_count()-1 for x in other_critical).items())),
            'second_Hasse_incidences':other_incidences,'second_nonzero_boundary_rows':[{str(c):{str(k):v for k,v in b.items()}} for c,b in other_diff if b]}
    report['marker']='FRUCHT_INTRINSIC_CECH_MIXED_WEDGES_VERIFIED'
    print(json.dumps(report,sort_keys=True,separators=(',',':')))
if __name__=='__main__':main()
