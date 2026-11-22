#!/usr/bin/env python3
"""Reproduce the explicit three-object category models of orientable surfaces.

The construction is for odd r >= 3. Integer incidence, prescribed
free-face collapses, vertex links, and coherent orientation are checked.
Finite tests corroborate but do not replace the uniform topological proof.
"""
from collections import defaultdict
import json

def model(g):
    assert isinstance(g, int) and g>=1
    r=2*g+1
    # Index nonidentity morphisms as f_i (0->1), g_j (1->2),
    # h_k (0->2) for 0<=indices<r, then distinct leaf morphisms.
    h_index={}
    for j in range(r):
        for i in range(r):
            if i==j:
                h_index[(i,j)]=j
            elif i==(j+1)%r:
                h_index[(i,j)]=(j-1)%r
            else:
                h_index[(i,j)]=r+len([x for x in h_index.values() if x>=r])
    c=len(set(h_index.values()))
    assert c==r*(r-1)
    triangles=[]
    for j in range(r):
        for i in range(r):triangles.append((i,j,h_index[(i,j)]))
    remaining=[];collapses=[]
    for i,j,k in triangles:
        if k>=r:
            assert sum(x[2]==k for x in triangles)==1
            collapses.append((i,j,k))
        else: remaining.append((i,j,k))
    assert len(collapses)==r*(r-2)
    assert len(remaining)==2*r
    for j in range(r):
        assert (j,j,j) in remaining
        assert ((j+1)%r,j,(j-1)%r) in remaining
    # Count incidents for each surviving edge.
    incident_f=defaultdict(list);incident_g=defaultdict(list);incident_h=defaultdict(list)
    for i,j,k in remaining:
        incident_f[i].append((i,j,k));incident_g[j].append((i,j,k));incident_h[k].append((i,j,k))
    assert all(len(incident_f[i])==len(incident_g[i])==len(incident_h[i])==2 for i in range(r))
    # Links of all 3 vertices: connected 2-regular bipartite graphs.
    def link_graph(edges,left,right):
        adj=defaultdict(list)
        for x,y in edges:
            adj[('L',x)].append(('R',y));adj[('R',y)].append(('L',x))
        assert len(adj)==left+right
        assert all(len(z)==2 for z in adj.values())
        seen=set(); component_counts=[]
        for v in adj:
            if v in seen:continue
            stack=[v];seen.add(v);n=0
            while stack:
                u=stack.pop();n+=1
                for w in adj[u]:
                    if w not in seen:seen.add(w);stack.append(w)
            component_counts.append(n)
        assert component_counts==[left+right],component_counts
    link_graph([(i,k) for i,j,k in remaining],r,r) # vertex 0
    link_graph([(i,j) for i,j,k in remaining],r,r) # vertex 1
    link_graph([(j,k) for i,j,k in remaining],r,r) # vertex 2
    # Coherent fundamental cycle +sum A_j -sum B_j, oriented (0,1,2).
    boundary=defaultdict(int)
    for i,j,k in remaining:
        sign=1 if i==j else -1
        boundary[('f',i)]+=sign
        boundary[('g',j)]+=sign
        boundary[('h',k)]-=sign
    assert len(boundary)==3*r and all(v==0 for v in boundary.values())
    faces=(3,r+r+c,r*r)
    reduced_faces=(3,3*r,2*r)
    assert faces[0]-faces[1]+faces[2]==2-2*g
    assert reduced_faces[0]-reduced_faces[1]+reduced_faces[2]==2-2*g
    # Sink graph: b=r nodes g_j, c nodes h_k, E=r*r edges;
    # its core is the 2r-cycle and it has r(r-2) leaves.
    assert r*r-(r+c)+1==1
    return {'genus':g,'r':r,'objects':3,'adjacent_morphisms':(r,r),
            'long_morphisms':c,'nonidentity_morphisms':2*r+c,
            'initial_face_vector':faces,'free_face_pairs':len(collapses),
            'remaining_face_vector':reduced_faces,
            'vertex_links':'three connected 2-regular graphs',
            'integral_fundamental_cycle':'verified',
            'Euler_characteristic':2-2*g}

if __name__=='__main__':
    tests=[model(g) for g in range(1,13)]
    for t in tests: print(json.dumps(t,sort_keys=True,separators=(',',':')))
    print('ALL_12_PARAMETER_TESTS_PASSED')
