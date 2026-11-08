#!/usr/bin/env python3
"""Reproducible numeric checks for radial singularities of flat 2-torus Voronoi cells.
Only supplementary experiments: the theorem's all-lattice proof is analytic.
"""
import math
from fractions import Fraction
import numpy as np

def polygon(basis):
    b=np.array(basis,float)
    C=max(np.linalg.norm(b,axis=1))*9
    poly=[np.array(v,float) for v in [(-C,-C),(C,-C),(C,C),(-C,C)]]
    for j in range(-4,5):
      for k in range(-4,5):
       if j==k==0: continue
       v=j*b[0]+k*b[1]
       h=np.dot(v,v)/2
       new=[]
       for i,p in enumerate(poly):
        q=poly[(i+1)%len(poly)]
        x=np.dot(p,v)-h; y=np.dot(q,v)-h
        if x<=1e-9: new.append(p)
        if (x< -1e-9 and y>1e-9) or (x>1e-9 and y< -1e-9):
         new.append(p+(q-p)*(-x/(y-x)))
       poly=new
    vv=[]
    for p in poly:
      if not vv or np.linalg.norm(p-vv[-1])>1e-7: vv.append(p)
    if len(vv)>1 and np.linalg.norm(vv[0]-vv[-1])<1e-7: vv.pop()
    return np.array(vv)

def facets(p):
    n=len(p)
    ff=[]
    for i in range(n):
      u=p[(i+1)%n]-p[i]; mid=(p[(i+1)%n]+p[i])/2
      norm=np.array([u[1],-u[0]])
      if np.dot(norm,mid)<0: norm=-norm
      norm=norm/np.linalg.norm(norm)
      d=np.dot(mid,norm)
      ff.append((d,math.atan2(norm[1],norm[0])))
    return ff

def visible(r,ff):
    intervals=[]
    for d,ang in ff:
      if r<=d: continue
      a=math.acos(min(1,d/r))
      for shift in (-2*math.pi,0,2*math.pi,4*math.pi):
       s=max(0,ang+shift-a);t=min(2*math.pi,ang+shift+a)
       if t>s: intervals.append((s,t))
    if not intervals:return 2*math.pi
    intervals.sort();measure=0.; hi=-1.;start=0.
    for s,t in intervals:
      if s>hi:
        if hi>=0:measure+=hi-start
        start=s;hi=t
      else: hi=max(hi,t)
    if hi>=0:measure+=hi-start
    return max(0,2*math.pi-measure)

def main():
    # Exact reflection and unimodular-basis certificate for Example 3.18.
    u=(Fraction(1),Fraction(0))
    v=(Fraction(1,3),Fraction(1))
    Ru=(-u[0],u[1]); Rv=(-v[0],v[1])
    u2=(-Ru[0],-Ru[1]); v2=(Rv[0]-Ru[0],Rv[1]-Ru[1])
    assert u2 == (Fraction(1),Fraction(0))
    assert v2 == (Fraction(2,3),Fraction(1))
    rng=np.random.default_rng(1463)
    cases=[[[1.,0.],[0.,1.]],[[1.,0.],[0.,1.7]],
       [[1.,0.],[0.5,math.sqrt(3)/2]],[[1.,0.],[.3,1.1]],
       [[1.,0.],[.01,7.]],[[1.,0.],[.29,1.2]],
       [[.8,0],[.3,1.8]]]
    for i in range(10):
      a=rng.uniform(.7,1.4); b=rng.uniform(a,2*a)
      dot=rng.uniform(.01,.45)*a*a/b
      cases.append([[a,0],[dot,b*math.sqrt(1-dot**2/b**2)]])
    total=0; maximum_err=0
    for basis in cases:
      p=polygon(basis)
      ff=facets(p)
      assert len(p) in (4,6),(basis,len(p))
      ds=[]
      for d in sorted(d for d,_ in ff):
       if not ds or abs(d-ds[-1])>1e-8: ds.append(d)
      area=.5*abs(np.dot(p[:,0],np.roll(p[:,1],-1))-np.dot(p[:,1],np.roll(p[:,0],-1)))
      expect=abs(np.linalg.det(basis))
      assert abs(area-expect)<1e-6*expect,(area,expect)
      for d in ds:
       m=sum(abs(df-d)<1e-8 for df,_ in ff)//2
       assert 2*m==sum(abs(df-d)<1e-8 for df,_ in ff)
       eps=1e-10*min(1,d)
       score=(visible(d+eps,ff)-visible(d-eps,ff))/math.sqrt(eps)
       prediction=-4*m*math.sqrt(2/d)
       rel=abs((score-prediction)/prediction)
       maximum_err=max(maximum_err,rel)
       assert rel<.0015,(basis,d,m,score,prediction,rel)
       total+=1
      if len(p)==6:
        lengths=sorted([2*d for d,_ in ff])[::2]
        ss,tt,uu=lengths
        cosang=(ss**2+tt**2-uu**2)/(2*ss*tt)
        assert cosang>0 and cosang<=.5000001,(basis,lengths,cosang)
        reconstructed_area=ss*tt*math.sqrt(1-cosang**2)
        assert abs(reconstructed_area-area)<1e-7
      else:
        lengths=sorted([2*d for d,_ in ff])[::2]
        assert abs(lengths[0]*lengths[1]-area)<1e-7
    # Independent sampling uses only nearest lattice-image distances, not the polygon clipping.
    compares=0; worst_cdf=0.
    for basis in cases[:5]:
      bs=np.asarray(basis)
      p=polygon(basis)
      ff=facets(p)
      area=abs(np.linalg.det(bs))
      theta=np.linspace(0,2*math.pi,60000,endpoint=False)
      dirs=np.stack([np.cos(theta),np.sin(theta)],axis=1)
      rho=np.full(len(theta),np.inf)
      for di,phi in ff:
        cos=np.cos(theta-phi)
        rho=np.minimum(rho,np.divide(di,cos,out=np.full(len(theta),np.inf),where=cos>0))
      dxy=(rng.random((75000,2))-rng.random((75000,2)))@bs
      dist=np.full(len(dxy),np.inf)
      for ix in (-1,0,1):
       for iy in (-1,0,1):
        delta=dxy-ix*bs[0]-iy*bs[1]
        dist=np.minimum(dist,np.linalg.norm(delta,axis=1))
      for r in np.linspace(min(x[0] for x in ff)*.8,max(np.linalg.norm(p,axis=1)),4)[1:-1]:
       cdf_numerical=np.mean(np.minimum(r,rho)**2)*math.pi/area
       cdf_mc=np.mean(dist<=r)
       worst_cdf=max(worst_cdf,abs(cdf_numerical-cdf_mc));compares+=1
       assert abs(cdf_numerical-cdf_mc)<.015,(basis,r,cdf_numerical,cdf_mc)
    print('VERIFY_OK exact_reflection_isometry=1 polygon_cases=%d facet_threshold_groups=%d max_signature_relative_error=%.8g independent_pair_cdf_checks=%d max_cdf_error=%.6g' % (len(cases),total,maximum_err,compares,worst_cdf))
    print('The checks use orientation interval unions; all-lattice validity requires the analytical proof.')
if __name__=='__main__':main()
