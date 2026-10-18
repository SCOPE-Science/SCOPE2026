#!/usr/bin/env python3
"""Exhaustive integral discrete-Morse verification of the Petersen matching complex.
All computations use exact Python integers; this program has no external dependencies.
"""
import collections
import heapq

N = 5
EDGES = tuple(sorted({tuple(sorted(e)) for i in range(N)
                      for e in ((i,(i+1)%N),(i,5+i),(5+i,5+(i+2)%N))}))
ORDER = (8,9,4,12,6,14,0,3,7,5,10,1,13,11,2)
assert len(EDGES)==15 and sorted(ORDER)==list(range(15))


def all_faces():
    faces={}
    def rec(start,edge_mask,vertex_mask):
        if edge_mask:
            faces[edge_mask]=edge_mask.bit_count()-1
        for i in range(start,len(EDGES)):
            u,v=EDGES[i]
            if vertex_mask & ((1<<u)|(1<<v)) == 0:
                rec(i+1,edge_mask | 1<<i,vertex_mask | (1<<u)|(1<<v))
    rec(0,0,0)
    return faces


def matching(faces):
    unpaired=set(faces)
    matched=[]
    for i in ORDER:
        b=1<<i
        for a in sorted(unpaired):
            high=a|b
            if not a&b and high in unpaired:
                unpaired.remove(a);unpaired.remove(high)
                matched.append((a,high))
    return unpaired,matched


def signed_boundary(mask):
    # Oriented simplex uses graph-edge IDs in ascending order.
    j=0; out={}
    for i in range(len(EDGES)):
        if mask&(1<<i):
            out[mask^(1<<i)] = -1 if j%2 else 1
            j+=1
    return out


def acyclic_hasse(faces,pairs):
    # Each codimension-one incidence goes high -> low, except paired incidences low -> high.
    inverted={(a,b) for a,b in pairs}
    successors={f:[] for f in faces}
    indegree={f:0 for f in faces}
    count=0
    for high,d in faces.items():
        if d==0:continue
        for low in signed_boundary(high):
            if low not in faces:raise AssertionError('not closed')
            if (low,high) in inverted:
                x,y=low,high
            else:
                x,y=high,low
            successors[x].append(y);indegree[y]+=1;count+=1
    q=[f for f in faces if indegree[f]==0]
    heapq.heapify(q);counted=0
    while q:
        x=heapq.heappop(q);counted+=1
        for y in successors[x]:
            indegree[y]-=1
            if indegree[y]==0:heapq.heappush(q,y)
    assert counted==len(faces),(counted,len(faces))
    return count


def morse_coeff(high,low_critical,lower_pairs):
    # Eliminate all lower faces paired with upper cells of the same dimension.
    # The recurrence is an exact sum over reversed gradient paths.
    d={k:v for k,v in signed_boundary(high).items() if v}
    pivot={a:(b,signed_boundary(b)[a]) for a,b in lower_pairs}
    assert all(abs(s)==1 for _,s in pivot.values())
    todo=[a for a in d if a in pivot and d[a]]
    while todo:
        a=todo.pop()
        z=d.get(a,0)
        if not z:continue
        b,s=pivot[a]
        factor=z*s # since s=+-1
        for x,c in signed_boundary(b).items():
            d[x]=d.get(x,0)-factor*c
            if not d[x]: del d[x]
            elif x in pivot:todo.append(x)
    return [d.get(x,0) for x in low_critical],d


def run():
    faces=all_faces();bydim=collections.Counter(faces.values())
    assert bydim=={0:15,1:75,2:145,3:90,4:6}
    critical,pairs=matching(faces)
    assert len(pairs)==160
    assert collections.Counter(faces[x] for x in critical)=={0:1,2:5,3:5}
    arcs=acyclic_hasse(faces,pairs)
    lows=sorted(x for x in critical if faces[x]==2)
    highs=sorted(x for x in critical if faces[x]==3)
    lower_pairs=[(a,b) for a,b in pairs if faces[a]==2]
    mat=[]
    for b in highs:
        row,residue=morse_coeff(b,lows,lower_pairs)
        assert all((x in critical or x in {bb for aa,bb in pairs}) for x in residue)
        mat.append(row)
    # 5x5 matrix: each column is the boundary of a critical 3-cell.
    matrix=list(map(list,zip(*mat)))
    print('GRAPH_EDGES:',EDGES)
    print('FACE_VECTOR:',[bydim[d] for d in range(5)])
    print('MATCHING_ORDER:',ORDER)
    print('FACE_COUNT:',len(faces),'MATCHED_PAIRS:',len(pairs))
    print('CRITICAL_CELLS:',{d:sum(faces[f]==d for f in critical) for d in range(5)})
    print('DIRECTED_INCIDENCES:',arcs)
    print('CRITICAL_TWO_CELLS:',lows)
    print('CRITICAL_THREE_CELLS:',highs)
    print('SIGNED_MORSE_BOUNDARY:',matrix)
    if any(any(row) for row in matrix):
        print('NONZERO: requires attaching degree treatment')
    else:
        print('ZERO: wedge of five 2-spheres and five 3-spheres')
    return matrix

if __name__=='__main__':run()
