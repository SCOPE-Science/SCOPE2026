"""Finite cellular verification for cyclic fixed spaces of finite subsets of the two-sphere.
The topological proof (not the computation) establishes the parameter-uniform assertion.
"""
from collections import defaultdict
from itertools import combinations
import sympy as sp

POLES = ('N','S')


def cell_complex(m, k):
    if not (m>=3 and 1<=k<2*m):
        raise ValueError('outside range')
    vertices=[('polar','N'), ('polar','S')]
    if k>=2:
        vertices.append(('polar','NS'))
    edges=[]; triangles=[]
    for p in [(),('N',),('S',),('N','S')]:
        if m+len(p)>k: continue
        label=''.join(p) or 'none'
        top=('polar', ''.join(sorted(set(p)|{'N'})) )
        bottom=('polar', ''.join(sorted(set(p)|{'S'})) )
        assert top in vertices and bottom in vertices
        for j in range(3): vertices.append((label,j))
        for j in range(3):
            edges.extend([
                ((label,j),(label,(j+1)%3),label,'eq',j),
                (top,(label,j),label,'top',j),
                (bottom,(label,j),label,'bottom',j)])
        for j in range(3):
            triangles.extend([
                (label,'top',j), (label,'bottom',j)])
    vmap={v:i for i,v in enumerate(vertices)}
    emap={(e[2],e[3],e[4]):i for i,e in enumerate(edges)}
    d1=sp.zeros(len(vertices),len(edges))
    for j,e in enumerate(edges):
        d1[vmap[e[0]],j]-=1; d1[vmap[e[1]],j]+=1
    d2=sp.zeros(len(edges),len(triangles))
    for j,(label,side,i) in enumerate(triangles):
        a=emap[(label,'eq',i)]
        b=emap[(label,side,i)]
        c=emap[(label,side,(i+1)%3)]
        if side=='top': d2[a,j]+=1;d2[b,j]+=1;d2[c,j]-=1
        else: d2[a,j]-=1;d2[b,j]-=1;d2[c,j]+=1
    assert d1*d2==sp.zeros(d1.rows,d2.cols)
    return vertices,edges,triangles,d1,d2


def predicted(m,k):
    if k==1: return (2,0,0)
    if k<m:return (3,0,0)
    if k==m:return (2,0,1)
    if k==m+1:return (1,1,3)
    return (1,2,4)


def run():
    cases=0; maxcells=0
    for m in range(3,12):
        for k in range(1,2*m):
            vs,es,fs,d1,d2=cell_complex(m,k)
            rank1=d1.rank();rank2=d2.rank()
            bettis=(len(vs)-rank1,len(es)-rank1-rank2,len(fs)-rank2)
            assert bettis==predicted(m,k),(m,k,bettis,predicted(m,k))
            assert len(vs)-len(es)+len(fs)==sum((1,-1,1)[i]*b for i,b in enumerate(bettis))
            assert sum((1,-1,1)[i]*b for i,b in enumerate(bettis))==(2 if k==1 else 3)
            cases+=1;maxcells=max(maxcells,len(vs)+len(es)+len(fs))
    print(f'ALL_VERIFY_OK cases={cases} max_total_cells={maxcells}')

if __name__=='__main__':run()
