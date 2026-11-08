"""Reproducible numerical checks for the fixed-n tangent-area Pareto law.

Uses the standard library plus numpy/scipy for quadrature; not an infinite-proof certificate.
"""
import math
import numpy as np

TAU=2*math.pi

def support(theta,model):
    if model == 'circle':
        return 1.0 + 0*theta
    if model == 'ellipse':
        return np.sqrt(1.5**2*np.cos(theta)**2+0.8**2*np.sin(theta)**2)
    if model == 'constant_width':
        return 1.0 + 0.06*np.cos(3*theta)
    raise ValueError(model)

def rho(theta,model):
    if model == 'circle':
        return 1.0 + 0*theta
    if model == 'ellipse':
        h=support(theta,model)
        return (1.5*0.8)**2/h**3
    if model == 'constant_width':
        return 1.0 - 0.48*np.cos(3*theta)
    raise ValueError(model)

def model_formula(model,n,num=40000):
    theta=np.linspace(0,TAU,num+1)
    dt=TAU/num
    r=rho(theta[:-1],model)
    L=dt*np.sum(r)
    f=r/L
    # H is complementary semicircle mass: integral theta+pi..theta+2pi.
    # Circulant sliding window computes complementary semicircle mass.
    anti_arr=np.r_[f,f]
    cs=np.r_[0,np.cumsum(anti_arr)]*dt
    H=cs[np.arange(num)+num]-cs[np.arange(num)+num//2] +dt*(f-np.roll(f,-num//2))/2
    w=support(theta[:-1],model)+support(theta[:-1]+math.pi,model)
    fpi=np.roll(f,-num//2)
    pb=1-n*np.mean(f*H**(n-1))*TAU
    coefficient=n*(n-1)*TAU*np.mean(f*fpi*H**(n-2)*w**2)/(2*pb)
    return pb,coefficient

def intersection_polygon_area(theta,model):
    theta=np.sort(np.asarray(theta,float))
    ns=np.column_stack((np.cos(theta),np.sin(theta)))
    hs=np.asarray(support(theta,model))
    nxt=np.roll(np.arange(len(theta)),-1)
    v=np.linalg.solve(np.stack([ns,ns[nxt]],axis=1),np.stack([hs,hs[nxt]],axis=1)[...,None])[...,0]
    return abs(np.sum(v[:,0]*np.roll(v[:,1],-1)-v[:,1]*np.roll(v[:,0],-1))/2)


def check_singular():
    for model in ('circle','ellipse','constant_width'):
        theta=0.31
        predicted=float((support(theta,model)+support(theta+math.pi,model))**2/2)
        x=[]
        for d in (0.008,0.002,0.0005):
            angles=[theta,theta+math.pi-d,theta+math.pi+0.28,theta+1.45*math.pi]
            a=intersection_polygon_area(angles,model)
            x.append(a*d)
        assert abs(x[-1]/predicted-1)<0.005,(model,predicted,x)
        print('singular',model,'limit',round(predicted,9),'dA',x)


def check_circle_formula():
    for n in (3,4,5,8):
        pb,c=model_formula('circle',n)
        expect_pb=1-n/2**(n-1)
        expect_c=2*n*(n-1)/(math.pi*(2**(n-1)-n))
        assert abs(pb-expect_pb)<1.e-10
        assert abs(c-expect_c)<1.e-10
        print('circle',n,'Pbounded',pb,'Cconditional',c)


def check_constant_width():
    eta=.48
    pb,c=model_formula('constant_width',3)
    target_pb=.25-eta**2/(6*math.pi**2)
    target_c=(3/math.pi)*(1-eta**2/2)/target_pb
    assert abs(pb-target_pb)<2.e-8,(pb,target_pb)
    assert abs(c-target_c)<2.e-7,(c,target_c)
    print('constant_width n=3 exact',target_pb,target_c)


def sample_and_check(model, count=350000, seed=7235):
    rng=np.random.default_rng(seed)
    # Grid inverse transform for arclength-uniform boundary samples.
    m=20000
    grid=np.linspace(0,TAU,m+1)
    rr=rho(grid,model)
    cdf=np.r_[0,np.cumsum((rr[1:]+rr[:-1])/2*TAU/m)]
    cdf/=cdf[-1]
    th=np.sort(np.interp(rng.random((count,3)),cdf,grid),axis=1)
    delta=np.diff(np.concatenate([th,th[:,:1]+TAU],axis=1),axis=1)
    bounded=(np.max(delta,axis=1)<math.pi)
    th=th[bounded]
    h=support(th,model)
    g=np.diff(np.concatenate([th,th[:,:1]+TAU],axis=1),axis=1)
    hn=np.roll(h,-1,axis=1)
    beta=(hn-h*np.cos(g))/np.sin(g)
    x=h*np.cos(th)-beta*np.sin(th)
    y=h*np.sin(th)+beta*np.cos(th)
    area=np.abs(np.sum(x*np.roll(y,-1,axis=1)-y*np.roll(x,-1,axis=1),axis=1))/2
    pb,C=model_formula(model,3)
    obs=np.mean(bounded)
    assert abs(obs-pb)<0.004,(model,obs,pb)
    print('random_check',model,'n',count,'bounded',obs,'formula',pb)
    for t in (80,160,320):
        mass=np.sum(area>t)/count
        target=pb*C/t
        print('tail',model,'t',t,'t_mass',t*mass,'asymptotic',pb*C,'relative',mass/target)
        assert abs(mass-target)<max(0.15*target,0.001)

if __name__ == '__main__':
    check_singular();check_circle_formula();check_constant_width()
    for model in ('ellipse','constant_width'):
        for n in (3,4,5):
            print('curved',model,n,model_formula(model,n))
    sample_and_check('circle')
    sample_and_check('ellipse')
    sample_and_check('constant_width')
    print('VERIFY_OK')
