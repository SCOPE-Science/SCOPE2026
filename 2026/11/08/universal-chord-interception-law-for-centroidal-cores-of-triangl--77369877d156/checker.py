"""Numerical Euclidean geometry check for the centroid-core chord formula."""
import math
import random


def F(r):
    if not 0 <= r <= 1:
        raise ValueError('scale must be in [0,1]')
    if r == 1: return 1.0
    t = (1-r)/3
    if r == 0: return 0.0
    return (1-2*t-3*t*t + 2*t*t*math.log(t)
            + 2*t*(2*t-1)*math.log(1-2*t)
            + 2*t*(1-3*t)*math.log(1-t))


def cross(x,y):return x[0]*y[1]-x[1]*y[0]


def hits_polygon_segment(P,Q,V):
    # Clip segment against the three inward halfplanes of a CCW triangle.
    d=(Q[0]-P[0],Q[1]-P[1])
    lo,hi=0.0,1.0
    for j in range(3):
        a=V[j]; b=V[(j+1)%3]
        edge=(b[0]-a[0],b[1]-a[1])
        p0=cross(edge,(P[0]-a[0],P[1]-a[1]))
        pd=cross(edge,d)
        if abs(pd)<1e-14:
            if p0 < -1e-14: return False
            continue
        limit=-p0/pd
        if pd>0: lo=max(lo,limit)
        else: hi=min(hi,limit)
        if lo>hi+1e-12: return False
    return True


def one_run(V,scale,n,seed):
    rng=random.Random(seed)
    sides=[math.dist(V[i],V[(i+1)%3]) for i in range(3)]
    Ptot=sum(sides)
    weights=[z/Ptot for z in sides]
    thresholds=[weights[0],weights[0]+weights[1],1.0]
    centroid=((V[0][0]+V[1][0]+V[2][0])/3,(V[0][1]+V[1][1]+V[2][1])/3)
    T=[(centroid[0]+scale*(p[0]-centroid[0]),centroid[1]+scale*(p[1]-centroid[1])) for p in V]
    successes=0
    for _ in range(n):
        points=[]
        for _ in range(2):
            z=rng.random(); i=next(i for i,t in enumerate(thresholds) if z<t)
            q=V[i]; w=V[(i+1)%3]; frac=rng.random()
            points.append((q[0]+frac*(w[0]-q[0]),q[1]+frac*(w[1]-q[1])))
        successes+=hits_polygon_segment(points[0],points[1],T)
    target=(1-sum(p*p for p in weights))*F(scale)
    got=successes/n
    sigma=(target*(1-target)/n)**0.5
    assert abs(got-target)<=6*sigma+0.0005,(got,target,n,scale)
    return (got,target,sigma)


def main():
    triangles=[[(0.,0.),(1.,0.),(.0,1.)],[(0.,0.),(7.,0.),(.2,.42)],[(0.,0.),(2.,0.),(.35,3.2)]]
    rvals=[.03,.2,.5,.78,.96]
    for i,T in enumerate(triangles):
        for j,r in enumerate(rvals):
            observed,target,se=one_run(T,r,65000,881000+i*111+j)
            print('triangle',i,'scale',r,'observed',round(observed,6),'formula',round(target,6),'z',round((observed-target)/se,2))
    for r in [.001,.01,.25,.5,.9,.999]:
        assert 0<F(r)<1
    print('TRIANGLE_CENTROID_CORE_CHORD_CDF_OK 975000')

if __name__=='__main__':main()
