#!/usr/bin/env python3
"""Standalone exact certificate checker for a single-edge Kneser neighborhood complex.
Usage: python3 verify.py [CERTIFICATE.json]. Requires only Python 3 stdlib.
"""
import sys,json,itertools
from collections import defaultdict,deque
from pathlib import Path

def check(cond,msg):
    if not cond:raise AssertionError(msg)

def graph_neighborhoods(vs,deleted):
    neigh=[]
    for i,u in enumerate(vs):
        mask=0
        for j,v in enumerate(vs):
            if not set(u).intersection(v) and sorted((i,j))!=deleted:
                mask|=1<<j
        neigh.append(mask)
    return neigh

def complex_faces(neighborhoods):
    faces=set()
    for mask in neighborhoods:
        x=mask
        while x:
            faces.add(x)
            x=(x-1)&mask
    return faces

def fvector(F):
    return [sum(m.bit_count()==k for m in F) for k in range(1,7)]

def cofaces_in(S,f):
    return [t for t in S if t.bit_count()==f.bit_count()+1 and t&f==f]

def replay_free(S,pairs,relative=False):
    S=set(S)
    for j,(f,t) in enumerate(pairs):
        check(f in S and t in S and f.bit_count()+1==t.bit_count() and f&t==f, 'invalid free pair '+str(j))
        check(cofaces_in(S,f)==[t], 'not a free incidence '+str(j))
        # Every higher-dimensional coface would force additional codimension-one cofaces.
        S.remove(f);S.remove(t)
    return S

def check_morse(S,pairs,expected):
    S=set(S); used=set();matched={}
    for j,(low,high) in enumerate(pairs):
        check(low in S and high in S and low not in used and high not in used,'invalid Morse cell '+str(j))
        check(high.bit_count()==low.bit_count()+1 and high&low==low,'invalid Morse incidence '+str(j))
        used.update([low,high]);matched[(low,high)]=True
    check(sorted(S-used)==sorted(expected),'wrong critical faces')
    adjacency={x:[] for x in S}
    indegree={x:0 for x in S}
    for upper in S:
        x=upper
        while x:
            bit=x&-x;x-=bit
            lower=upper^bit
            if lower not in S:continue
            src,dst=(lower,upper) if (lower,upper) in matched else (upper,lower)
            adjacency[src].append(dst); indegree[dst]+=1
    q=deque(x for x in S if indegree[x]==0);seen=0
    while q:
        x=q.popleft();seen+=1
        for y in adjacency[x]:
            indegree[y]-=1
            if indegree[y]==0:q.append(y)
    check(seen==len(S),'cyclic Morse vector field')
    counts=defaultdict(int)
    for m in S-used:counts[m.bit_count()-1]+=1
    check(dict(counts)=={0:1,2:17},'incorrect critical Morse dimensions')
    return counts

def relative_differential(T):
    edges=sorted(x for x in T if x.bit_count()==2)
    tris=sorted(x for x in T if x.bit_count()==3)
    check(len(edges)==2 and len(tris)==4 and len(T)==6,'wrong relative cells')
    M=[]
    for t in tris:
        v=[j for j in range(15) if t>>j&1]
        row=[]
        for e in edges:
            coeff=0
            for j in range(3):
                if (t^(1<<v[j]))==e:coeff=(-1)**j
            row.append(coeff)
        M.append(row)
    check(M==[[-1,0],[-1,0],[0,-1],[0,-1]],'relative integral boundary not the unit-pair matrix')
    return M

def main(path):
    data=json.loads(Path(path).read_text('utf8'))
    check(data['schema_version']==1,'schema')
    vs=list(itertools.combinations(range(1,7),2))
    check(data['vertex_order']==[str(i)+str(j) for i,j in vs],'vertex indexing')
    edge=data['deleted_graph_edge_vertex_indices']
    check(edge==[0,9],'graph edge')
    F=complex_faces(graph_neighborhoods(vs,[-1,-1]))
    D=complex_faces(graph_neighborhoods(vs,edge))
    check(D.issubset(F),'fault not inclusion')
    check(fvector(F)==data['full_f_vector']==[15,105,260,225,90,15],'intact fvector')
    check(fvector(D)==data['damaged_f_vector']==[15,103,244,205,80,13],'fault fvector')
    residual=replay_free(D,data['absolute_free_pairs'])
    check(len(data['absolute_free_pairs'])==268 and len(residual)==124,'absolute collapses')
    critical=data['absolute_critical_faces']
    check_morse(residual,data['absolute_morse_pairs'],critical)
    check(len(data['absolute_morse_pairs'])==53,'absolute Morse count')
    relative=F-D
    check(len(relative)==50,'relative face count')
    remaining=replay_free(relative,data['relative_free_pairs'],relative=True)
    check(len(data['relative_free_pairs'])==22,'relative collapse count')
    check(sorted(remaining)==sorted(data['relative_critical_faces']),'relative critical faces')
    M=relative_differential(remaining)
    print('PASS: complete faces, 268 absolute collapses, acyclic 53-pair Morse matching,')
    print('      critical cells (1 vertex, 17 triangles), 22 relative collapses,')
    print('      two primitive integral relative H_2 classes, no relative H_1/H_3.')
    print('      face counts',fvector(F),fvector(D),'relative boundary',M)

if __name__=='__main__':
    path=sys.argv[1] if len(sys.argv)>1 else str(Path(__file__).with_name('CERTIFICATE.json'))
    main(path)
