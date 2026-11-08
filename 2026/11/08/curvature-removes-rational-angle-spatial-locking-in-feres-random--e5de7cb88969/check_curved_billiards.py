"""Finite illustrative checks for curvature-dependent random circular billiards.

This is NOT a proof of irrationality or of asymptotic convergence.
Uses angle transitions and probabilities of the Feres four-map system.
"""
import math
import numpy as np

pi=math.pi

def phase(x,r,kind):
    q=math.sin(x)
    if kind == 'hyperbolic':
        den=math.sqrt(1+math.sinh(r)**2*math.cos(x)**2)
    elif kind == 'spherical':
        den=math.sqrt(1-math.sin(r)**2*math.cos(x)**2)
    else:
        den=1
    v=2*math.asin(min(1,max(-1,q/den)))
    return v if x<=pi/2 else 2*pi-v

def prob(x,al):
    c=math.cos(2*al)
    def u(a,z):return .5*(1+math.tan(a)/math.tan(z))
    if x<al:
        return [1.,0.,0.,0.]
    elif x<2*al:
        return [u(al,x),0.,0.,u(al,-x)]
    elif x<3*al:
        return [u(al,x),0.,2*c*u(2*al,-x),u(al,-x)-2*c*u(2*al,-x)]
    elif x<pi-3*al:
        return [u(al,x),0.,u(al,-x),0.]
    elif x<pi-2*al:
        return [2*c*u(2*al,x),u(al,x)-2*c*u(2*al,x),u(al,-x),0.]
    elif x<pi-al:
        return [0.,u(al,x),u(al,-x),0.]
    return [0.,0.,1.,0.]

def nexts(x,a):
    return [x+2*a,-x+2*pi-4*a,x-2*a,-x+4*a]

def chain(n,fract):
    a=pi/n;theta=fract*a
    states=[theta]
    for x in states:
        for y,p in zip(nexts(x,a),prob(x,a)):
            if p>1.e-10 and not any(abs(y-z)<1.e-9 for z in states):
                if not 0<y<pi:raise AssertionError(('bad state',x,y))
                states.append(y)
    assert len(states)==n,(n,states)
    P=np.zeros((n,n))
    for i,x in enumerate(states):
        for y,p in zip(nexts(x,a),prob(x,a)):
            if p>1e-11:
                j=min(range(n),key=lambda j:abs(states[j]-y))
                assert abs(states[j]-y)<1e-9
                P[i,j]+=p
        assert abs(sum(P[i])-1)<1e-10
    return states,P

checks=0
for n in [7,8,9,10,11,13]:
    a=pi/n
    for fract in [.25,.5,.73]:
        th=fract*a;v=2*a-th;w=4*a-th;b=2*a+th
        # positive edges for the two different two-step returns
        assert prob(v,a)[0]>0 and prob(w,a)[2]>0
        assert prob(v,a)[3]>0 and prob(b,a)[3]>0
        checks+=4
        state,P=chain(n,fract)
        checks+=n
        for kind,r in [('hyperbolic',.2),('hyperbolic',1.0),('hyperbolic',3.0),('spherical',.2),('spherical',.7),('spherical',1.3)]:
            d=phase(w,r,kind)-phase(b,r,kind)
            assert d>0
            # weak spectral evidence: individual finite Fourier modes only
            for k in range(1,7):
                PK=P*np.exp(1j*k*np.array([phase(t,r,kind) for t in state]))[None,:]
                ev=np.linalg.eigvals(PK)
                sr=max(abs(ev))
                assert sr<1-1.e-10,(n,fract,kind,r,k,sr)
                checks+=1
        for xx in [v,b,w,pi-w]:
            assert abs(phase(xx,0.,'hyperbolic')-2*xx)<1e-12
            checks+=1
print('supporting finite checks passed:',checks)
