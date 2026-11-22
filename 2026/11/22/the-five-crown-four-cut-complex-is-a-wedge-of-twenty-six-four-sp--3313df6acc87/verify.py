#!/usr/bin/env python3
"""Reproduce an integral discrete-Morse certificate for the five-crown four-cut complex.
Requires Python 3 standard library only. No external precomputed results.
"""
import itertools, collections, json
N = 5
V = frozenset(range(2*N))

def adj(u,v):
    return (u<N) != (v<N) and (u % N) != (v % N)

def disconnected(S):
    todo=[next(iter(S))];seen=set(todo)
    while todo:
        u=todo.pop()
        for v in S-seen:
            if adj(u,v):
                seen.add(v);todo.append(v)
    return seen!=S

def faces_of_facets(facets):
    out=set()
    for T in facets:
        for r in range(1,len(T)+1):
            out.update(frozenset(S) for S in itertools.combinations(T,r))
    return out

def verify_morse(faces):
    # Standard successive elementary matchings at vertices 0,1,...,9.
    remaining=set(faces);paired=[]
    for v in sorted(V):
        for S in list(remaining):
            if v not in S and (T:=S|{v}) in remaining:
                remaining.remove(S);remaining.remove(T);paired.append((S,T))
    assert len(remaining)+2*len(paired)==len(faces)
    # Acyclicity checked on the entire reversed-matching Hasse digraph.
    ix={S:i for i,S in enumerate(faces)}
    ups={(ix[S],ix[T]) for S,T in paired}
    succ=[[] for _ in faces];indeg=[0]*len(faces);edge_count=0
    for T in faces:
        if len(T)==1:continue
        for v in T:
            S=T-{v};a,b=ix[S],ix[T]
            u,w=(a,b) if (a,b) in ups else (b,a)
            succ[u].append(w);indeg[w]+=1;edge_count+=1
    queue=collections.deque(i for i,k in enumerate(indeg) if k==0)
    scanned=0
    while queue:
        u=queue.popleft();scanned+=1
        for w in succ[u]:
            indeg[w]-=1
            if indeg[w]==0:queue.append(w)
    assert scanned==len(faces), 'Directed cycle in gradient Hasse graph'
    return {'nonempty_faces':len(faces),'matching_pairs':len(paired),'critical_counts_by_dimension':dict(sorted(collections.Counter(len(S)-1 for S in remaining).items())),'hasse_edges_checked':edge_count,'acyclic':True,'unmatched_faces':sorted([sorted(S) for S in remaining])}

def main():
    quadruples={frozenset(Q) for Q in itertools.combinations(V,4) if disconnected(frozenset(Q))}
    # Structural check performed independently of the homotopy calculation.
    predicted={frozenset(Q) for Q in itertools.combinations(range(N),4)}
    predicted|={frozenset(Q) for Q in itertools.combinations(range(N,2*N),4)}
    predicted|={frozenset((i,j,i+N,j+N)) for i,j in itertools.combinations(range(N),2)}
    predicted|={frozenset((*T,N+i)) for T in itertools.combinations(range(N),3) for i in T}
    predicted|={frozenset((i,*(N+j for j in T))) for T in itertools.combinations(range(N),3) for i in T}
    assert quadruples==predicted
    assert len(quadruples)==80
    facets={V-Q for Q in quadruples}
    assert len(facets)==80 and all(len(F)==6 for F in facets)
    cut=faces_of_facets(facets)
    dual={frozenset(S) for r in range(1,2*N+1) for S in itertools.combinations(V,r) if all(not Q<=frozenset(S) for Q in quadruples)}
    # Independent verification of Alexander dual complement condition, including empty face.
    for r in range(2*N+1):
        for S0 in itertools.combinations(V,r):
            S=frozenset(S0)
            dual_by_definition = not any((V-S)<=F for F in facets)
            assert dual_by_definition == (S in dual or len(S)==0)
    c=verify_morse(cut);d=verify_morse(dual)
    assert c['critical_counts_by_dimension']=={0:1,4:26},c['critical_counts_by_dimension']
    assert d['critical_counts_by_dimension']=={0:1,3:26},d['critical_counts_by_dimension']
    fvec=[sum(len(S)==k for S in cut) for k in range(1,7)]
    dual_fvec=[sum(len(S)==k for S in dual) for k in range(1,7)]
    assert sum((-1)**i*x for i,x in enumerate(fvec))-1 ==26
    assert sum((-1)**i*x for i,x in enumerate(dual_fvec))-1 ==-26
    data={'graph':'K_5,5 with five diagonal matching edges removed','vertices':10,'edges':20,'disconnected_quadruples':80,'cut_facets':80,'cut_f_vector':fvec,'cut_morse':c,'dual_f_vector':dual_fvec,'dual_morse':d,'alexander_duality':'cut H_4 corresponds to dual cohomology H^3; each free rank 26','result':'PASS'}
    print(json.dumps(data,sort_keys=True,indent=2))
if __name__=='__main__':main()
