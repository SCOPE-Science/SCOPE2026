"""Independent numerical checks for a conditional marked long-distance law in ideal hyperbolic polygons."""
import math
import numpy as np

def chart_specs(t):
    return [
        ('0',0., -1.,0.,1.),
        ('1',1., -1./(t-1.),1.,t/(t-1.)),
        ('t',t,0.,1./(t-1.),1./(t-1.)),
        ('inf',float('inf'),0.,t,t),
    ]

def cusp_point(spec, x01, height):
    name,a,l,r,w=spec
    c=l+w*x01
    if name=='inf': return c+1j*height
    return a-1/(c+1j*height)

def distance(z1,z2):
    return np.arccosh(1+np.abs(z1-z2)**2/(2*z1.imag*z2.imag))

def weights(t):
    sp=chart_specs(t); W=np.zeros((4,4))
    for i in range(4):
        for j in range(4):
            if i==j:continue
            g=1 if 3 in (i,j) else (sp[i][1]-sp[j][1])**2
            W[i,j]=sp[i][4]*sp[j][4]*g
    return W/W.sum()

def sample_polygon(rng,t,n):
    which=rng.integers(0,2,n)
    a=np.where(which==0,0.,1.); b=np.where(which==0,1.,t)
    theta=rng.uniform(0,np.pi/2,n)
    x=a+(b-a)*np.sin(theta)**2
    y=np.sqrt((x-a)*(b-x))/rng.random(n)
    return x+1j*y

def test_exact_area_and_tail():
    rng=np.random.default_rng(84923)
    for t in (2.,3.):
        n=1200000
        x=sample_polygon(rng,t,n);y=sample_polygon(rng,t,n)
        d=distance(x,y)
        C=2*t*t/(math.pi**2*(t-1))
        for T in (8.,10.):
            q=np.mean(d>T); want=C*T*math.exp(-T)
            # O(e^-T) correction means errors at finite threshold are expected.
            print('direct',t,T,round(q,7),round(want,7),round(q/want,4))
            assert 0.5<q/want<1.5
        # chart asymptotic and categorical formula
        W=weights(t); assert abs(W.sum()-1)<1e-12
        assert abs((W[0,2]+W[2,0]+W[1,3]+W[3,1])-0.5)<1e-12
        assert abs(W[0,1]+W[1,0]-1/(4*t))<1e-12
        assert abs(W[0,3]+W[3,0]-(t-1)/(4*t))<1e-12
        print('label weights unordered t=',t, [[round(W[i,j]+W[j,i],6) for j in range(i+1,4)] for i in range(3)])
        specs=chart_specs(t)
        for i,j in [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]:
            H=10.
            u=rng.uniform(5.,13.,3000);v=rng.uniform(5.,13.,3000)
            z1=cusp_point(specs[i],rng.random(len(u)),H*np.exp(u))
            z2=cusp_point(specs[j],rng.random(len(v)),H*np.exp(v))
            g=1 if 3 in (i,j) else (specs[i][1]-specs[j][1])**2
            err=distance(z1,z2)-(u+v+np.log(g*H*H))
            assert np.max(np.abs(err))<1e-2
    print('CUSP_MARKED_DISTANCE_CHECKS_OK')

if __name__=='__main__': test_exact_area_and_tail()

def test_marked_conditional_proposal():
    """Test the exact cusp-chart geometry against the asymptotic conditional product law.

    The proposal conditions on the leading logarithmic-distance surrogate, not the
    exact rare event; this is a consistency experiment, not an exact conditional sampler.
    """
    rng=np.random.default_rng(77471)
    t=3.; T=35.; H=10.; n=160000
    specs=chart_specs(t)
    W=weights(t)
    pairs=np.array([(i,j) for i in range(4) for j in range(4) if i!=j])
    probs=np.array([W[i,j] for i,j in pairs]); assert abs(sum(probs)-1)<1e-12
    k=rng.choice(len(pairs),size=n,p=probs)
    U=np.empty(n);E=np.empty(n);xm=np.empty(n);yv=np.empty(n);iids=np.empty(n,dtype=int);jids=np.empty(n,dtype=int)
    for h,(i,j) in enumerate(pairs):
        idx=np.flatnonzero(k==h);m=len(idx)
        g=1. if 3 in (i,j) else (specs[i][1]-specs[j][1])**2
        b=T-math.log(g*H*H)
        assert b>10
        # Conditional Gamma(2,1) overshoot of its sum above b: mixture of Exp and Gamma(2).
        S=b+rng.exponential(1,m)+np.where(rng.random(m)<1/(b+1),rng.exponential(1,m),0.)
        u=S*rng.random(m);v=S-u
        a=rng.random(m);c=rng.random(m)
        z1=cusp_point(specs[i],a,H*np.exp(u));z2=cusp_point(specs[j],c,H*np.exp(v))
        d=distance(z1,z2)
        # Exact geodesic midpoint in the upper-half-plane.
        coshd=np.cosh(d)
        denom=1/z1.imag+1/z2.imag
        mid=(z1.real/z1.imag+z2.real/z2.imag)/denom+1j*np.sqrt(2+2*coshd)/denom
        charti=mid.imag if i==3 else (-1/(mid-specs[i][1])).imag
        chartj=mid.imag if j==3 else (-1/(mid-specs[j][1])).imag
        dep=np.maximum(np.log(np.maximum(charti,1e-100)),np.log(np.maximum(chartj,1e-100)))/T
        xm[idx]=dep; U[idx]=u/T; E[idx]=d-T; yv[idx]=np.abs(u-v)/(2*T)
        iids[idx]=i;jids[idx]=j
    good=E>0
    print('conditional proposal',round(good.mean(),5),'mean U',round(U[good].mean(),5),'mean E',round(E[good].mean(),5), 'mid-depth discrepancy',round(np.mean(abs(xm[good]-yv[good])),5))
    assert good.mean()>0.97
    expected_u=sum(W[i,j]*(T-math.log((1 if 3 in (i,j) else (specs[i][1]-specs[j][1])**2)*H*H)+1.0)/(2*T) for i,j in pairs)
    assert abs(U[good].mean()-expected_u)<0.01
    assert abs(np.mean(E[good])-1)<0.06
    assert np.mean(abs(xm[good]-yv[good]))<0.02
    print('CUSP_MARKED_CONDITIONAL_GEOMETRY_OK')

if __name__=='__main__': test_marked_conditional_proposal()
