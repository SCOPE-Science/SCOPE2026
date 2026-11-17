"""Finite independent numerical checks of ridge-angle and curvature formulas.
Use: python layered_curvature_checker.py
No external data are needed; SciPy and NumPy are used for geometric comparisons.
"""
from itertools import product,combinations
from math import factorial,acos,pi,sqrt,prod,isclose
import numpy as np
from scipy.spatial import ConvexHull

def analytic(sizes):
    n=sum(sizes); r=len(sizes); s=sum(a==1 for a in sizes)
    vol=2**n*prod(factorial(a) for a in sizes)/factorial(n)
    area=vol*n*sqrt(r)
    k=(r-s)*sqrt(2*r-1)*acos((r-1)/r)+s*sqrt(r-1)*acos((r-2)/r)
    v_nm2=vol*n*(n-1)*k/(4*pi)
    return vol,area,v_nm2

def brute(sizes):
    n=sum(sizes); r=len(sizes)
    offsets=np.cumsum([0,*sizes[:-1]])
    vertices=[]
    for a,off in zip(sizes,offsets):
        for signs in product([-1,1],repeat=a):
            v=np.zeros(n); v[off:off+a]=signs;vertices.append(v)
    vertices=np.array(vertices)
    normals=[]; labels=[]
    for selected in product(*[list(product(range(a),[-1,1])) for a in sizes]):
        nor=np.zeros(n)
        for (j,sgn),off in zip(selected,offsets):nor[off+j]=sgn
        normals.append(nor);labels.append(selected)
    normals=np.array(normals)
    fvol=ConvexHull(vertices).volume
    ridge_count=0; categories={0:0,1:0}; ridge_volumes={0:[],1:[]}; angle_volumes=0.
    for i,j in combinations(range(len(normals)),2):
        hits=np.where(np.isclose(vertices@normals[i],1,atol=1e-9)&np.isclose(vertices@normals[j],1,atol=1e-9))[0]
        if len(hits)<n-1:continue
        v=vertices[hits]
        v0=v[0]; _,sing,vt=np.linalg.svd(v[1:]-v0,full_matrices=False)
        rank=(sing>1e-8).sum()
        if rank!=n-2:continue
        ridge_count+=1
        basis=vt[:rank].T; co=(v-v0)@basis
        if rank==0: rv=1.0
        elif rank==1: rv=co[:,0].max()-co[:,0].min()
        else: rv=ConvexHull(co,qhull_options='QJ').volume
        diff=[k for k,(a,b) in enumerate(zip(labels[i],labels[j])) if a!=b]
        assert len(diff)==1
        typ=int(sizes[diff[0]]==1)
        categories[typ]+=1;ridge_volumes[typ].append(rv)
        exterior=acos(float(normals[i]@normals[j])/r)
        angle_volumes+=rv*exterior/(2*pi)
        ref_angle=acos((r-2 if typ else r-1)/r)
        assert abs(exterior-ref_angle)<1e-9
    F=prod(2*a for a in sizes)
    assert categories[0]==F*sum(a-1 for a in sizes if a>1)
    assert categories[1]==F*sum(a==1 for a in sizes)//2
    av,aa,ak=analytic(sizes)
    assert isclose(fvol,av,rel_tol=1e-7,abs_tol=1e-7),(sizes,fvol,av)
    assert isclose(angle_volumes,ak,rel_tol=2e-6,abs_tol=2e-6),(sizes,angle_volumes,ak)
    return ridge_count

if __name__=='__main__':
    ps=[(1,1),(1,1,1),(2,1),(2,2),(3,1),(2,1,1),(1,1,1,1),(3,2),(2,2,1),(2,1,1,1),(1,1,1,1,1)]
    tot=0
    for p in ps: tot+=brute(p)
    # A second, symbolic normal/ridge multiplicity check for all profiles up to dimension 18:
    examined=0
    for n in range(2,19):
      for mask in range(1<<(n-1)):
       sizes=[]; count=1
       for bit in range(n-1):
        if mask>>bit&1: sizes.append(count);count=1
        else: count+=1
       sizes.append(count)
       if len(sizes)<2: continue
       r=len(sizes);F=prod(2*a for a in sizes)
       c0=F*sum(a-1 for a in sizes if a>1)
       c1=F*sum(a==1 for a in sizes)//2
       assert c0+c1==F*sum(a-1 for a in sizes)+F*sum(a==1 for a in sizes)//2
       examined+=1
    print(f'LAYERED_CURVATURE_PASS numerical_profiles={len(ps)} brute_ridges={tot} profile_identities={examined}')
