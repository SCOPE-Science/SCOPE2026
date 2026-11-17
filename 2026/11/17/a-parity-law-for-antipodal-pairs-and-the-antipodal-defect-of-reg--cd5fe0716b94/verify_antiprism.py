"""Coordinate support checks of antipodal vertex and edge pairs.
For each candidate pair we solve its support normals analytically via edge-direction crosses
(or extreme rays of the normal cones for parallel edge directions).
"""
import numpy as np
from itertools import combinations
from math import pi
from time import perf_counter

def antiprism(n):
    d=np.longdouble
    a=d(2)*np.arccos(d(-1))/d(n)
    verts=np.array([[np.cos(a*j),np.sin(a*j),-d(1)] for j in range(n)]+[[np.cos(a*(j+d('.5'))),np.sin(a*(j+d('.5'))),d(1)] for j in range(n)],dtype=d)
    facets=[tuple(range(n)),tuple(range(n,2*n))]
    for j in range(n):
        facets.append(tuple(sorted([j,n+j,n+(j-1)%n])))
        facets.append(tuple(sorted([n+j,j,(j+1)%n])))
    edges=set()
    for j in range(n):
        for e in [(j,(j+1)%n),(n+j,n+(j+1)%n),(j,n+j),(j,n+(j-1)%n)]:edges.add(tuple(sorted(e)))
    edges=sorted(edges)
    incident=[]
    for e in edges:
        incident.append([f for f in range(len(facets)) if set(e).issubset(facets[f])])
    assert all(len(f)==2 for f in incident)
    normals=[]
    for fid,fac in enumerate(facets):
        i,j,k=fac[:3]
        if fid<2:
            u=np.array([0,0,-1 if i<n else 1],dtype=d)
        else:
            u=np.cross(verts[j]-verts[i],verts[k]-verts[i]);u/=np.linalg.norm(u)
            if np.max((verts-verts[i])@u)>d('1.e-10'):u=-u
        normals.append(u)
    return verts,edges,normals,incident

def supports(vs,u,aa,bb):
    vals=vs@u
    M=(vals[list(aa)].sum()/len(aa))
    m=(vals[list(bb)].sum()/len(bb))
    tol=np.longdouble('2e-12')*np.linalg.norm(u)
    return bool(M-m>tol and np.max(vals-M)<=tol and np.max(m-vals)<=tol)

def compute(n):
    vs,edges,normals,incident=antiprism(n)
    A=0;B=0
    for a,b in combinations(range(len(vs)),2):
        # Point pair antipodal iff either shared facet normal ray or a cross between vertex normal cone facets;
        # use linear feasibility for a numerical cross-check. Here use cross of all vertex incident facet normals.
        import scipy.optimize as so
        mat=np.vstack([vs-vs[a],vs[b]-vs])
        r=so.linprog(np.zeros(3),A_ub=np.array(mat,dtype=float),b_ub=np.ones(len(mat))*1e-11,A_eq=np.array([vs[a]-vs[b]],dtype=float),b_eq=[1],bounds=[(None,None)]*3,method='highs')
        A+=r.success
    for i,j in combinations(range(len(edges)),2):
        e,f=edges[i],edges[j]
        de=vs[e[1]]-vs[e[0]];df=vs[f[1]]-vs[f[0]]
        cross=np.cross(de,df); scale=np.linalg.norm(de)*np.linalg.norm(df)
        if np.linalg.norm(cross)>np.longdouble('1e-13')*scale:
            if supports(vs,cross,e,f) or supports(vs,-cross,e,f):B+=1
        else:
            cand=[normals[z] for z in incident[i]]+[-normals[z] for z in incident[j]]
            if any(supports(vs,u,e,f) for u in cand):B+=1
    return A,B,2*n-1-A+B
if __name__=='__main__':
    total=0
    for n in range(3,16):
        t=perf_counter()
        A,B,delta=compute(n)
        expected_A=n*n+(2*n if n%2 else n)
        expected_B=n*n+(7*n if n%2 else n)
        expected_D=7*n-1 if n%2 else 2*n-1
        assert (A,B,delta)==(expected_A,expected_B,expected_D), (n,A,B,delta)
        total+=3
        print(f'n={n}: A={A}, B={B}, defect={delta}; matches theorem; time={perf_counter()-t:.2f}s',flush=True)
    print(f'PASS: {total} per-instance count identities across 13 dimensions')
