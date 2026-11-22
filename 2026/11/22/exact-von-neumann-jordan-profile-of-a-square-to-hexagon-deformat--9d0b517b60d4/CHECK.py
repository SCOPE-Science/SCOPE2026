"""Finite diagnostics for the exact von Neumann--Jordan profile of a three-facet planar norm.
No finite test replaces the analytic proof.
"""
import math
import random

def predicted(t):
    assert t>0
    if t<=0.5:return 2.0
    b=abs(1-1/t)
    return (3+b*b+math.sqrt(b**4+2*b*b+8*b+5))/4

def norm(z,t):return max(abs(z[0]),abs(z[1]),t*abs(z[0]-z[1]))
def ratio(x,y,t):
    nx,ny=norm(x,t),norm(y,t)
    assert nx*nx+ny*ny>0
    return (norm((x[0]+y[0],x[1]+y[1]),t)**2+norm((x[0]-y[0],x[1]-y[1]),t)**2)/(2*(nx*nx+ny*ny))

def exact_vertex_enumeration(t):
    a=1/t-1
    vs=[(1,1),(1,-a),(-a,1),(-1,-1),(-1,a),(a,-1)]
    forms=[(1,0),(0,1),(t,-t)]
    values=[[f[0]*v[0]+f[1]*v[1] for v in vs] for f in forms]
    best=0
    for i in range(3):
        for j in range(3):
            for u in range(6):
                for v in range(6):
                    A=values[i][u];B=values[j][u];C=values[i][v];D=-values[j][v]
                    tr=A*A+B*B+C*C+D*D
                    det=(A*D-B*C)**2
                    eig=(tr+math.sqrt(max(0.0,tr*tr-4*det)))/2
                    best=max(best,eig/2)
    return best

def extremizer(t):
    if t<=0.5:return (1,1),(1,-1)
    b=abs(1-1/t);lam=2*predicted(t)
    k=(lam-2)/(1+b)
    q=1/math.sqrt(1+k*k);p=k*q
    if t<=1:
        # Principal eigenvector here has its larger coordinate first.
        p,q=q,p
        return ((p+q),(p+q)),((p+b*q),-b*(p+b*q))
    else:
        # Principal eigenvector here has its larger coordinate second.
        return ((p+q),b*(p+q)),(b*(b*p+q),(b*p+q))

def run():
    rng=random.Random(2411)
    count=0
    ts=[.1,.25,.5,.50001,.51,.6,.8,1,1.0001,1.1,1.5,2,3,10,100]
    ts += [.5+rng.random()*1.5 for _ in range(120)]
    ts += [2+98*rng.random() for _ in range(35)]
    for t in ts:
        exp=predicted(t);u,v=extremizer(t)
        assert abs(ratio(u,v,t)-exp)<1e-10,(t,u,v,exp,ratio(u,v,t))
        count+=1
        if t>.5:
            got=exact_vertex_enumeration(t)
            assert abs(got-exp)<2e-10,(t,exp,got)
            count+=1
        for _ in range(32):
            u=(rng.uniform(-2,2),rng.uniform(-2,2))
            v=(rng.uniform(-2,2),rng.uniform(-2,2))
            assert ratio(u,v,t)<exp+1e-10,(t,u,v)
            count+=1
    assert abs(predicted(1)-(3+math.sqrt(5))/4)<1e-12
    assert all(predicted(t)<2 for t in [.50001,.7,1,2,5,100])
    print('HEXAGON_DEFORMATION_NJ_DIAGNOSTIC_OK',count)
if __name__=='__main__':run()
