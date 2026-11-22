"""Exact generator-moment checks for fixed-speed, full-redraw active harmonic transport.
Runs with Python 3 standard library only; checks are finite diagnostics, not proofs.
"""
from fractions import Fraction as F
from itertools import product


def expected_formula(alpha, sigma2):
    a, s = F(alpha), F(sigma2)
    mean = 1/(1+a)
    var = 2*a*(1+(1+a)*s)/((1+a)**2*(2+a)*(3+a))
    return mean, var


def stationary_moments(alpha, directions, probabilities, degree=4):
    """Solve every state-resolved polynomial generator equation recursively."""
    a = F(alpha)
    p = tuple(F(z) for z in probabilities)
    assert sum(p) == 1 and all(z > 0 for z in p)
    assert all(x*x+y*y == 1 for x, y in directions)
    m = {}
    for i, pi in enumerate(p):
        m[(0,0,i)] = pi
    for n in range(1, degree+1):
        for k in range(n+1):
            j = n-k
            forcing = []
            for i, (ux,uy) in enumerate(directions):
                f = F(0)
                if k: f += k*ux*m[k-1,j,i]
                if j: f += j*uy*m[k,j-1,i]
                forcing.append(f)
            total = sum(forcing)/n
            for i, f in enumerate(forcing):
                m[k,j,i] = (f+a*p[i]*total)/(n+a)
    def moment(k,j):
        return sum(m[k,j,i] for i in range(len(p)))
    return moment(2,0)+moment(0,2), moment(4,0)+2*moment(2,2)+moment(0,4), m


def kernel(t, mu, gamma):
    import math
    m,g=float(mu),float(gamma)
    if abs(g-m)<1e-12:
        return (1+2*m*t)*math.exp(-2*m*t)
    return ((m+g)*math.exp(-2*m*t)-2*m*math.exp(-(m+g)*t))/(g-m)


def variance(m, g, v, s):
    return 2*g*v**4*(s*g+s*m+m)/(m**2*(g+m)**2*(g+2*m)*(g+3*m))




def independent_trajectory_check():
    """Independent exact-clock path simulation, including shared initial heading."""
    import random, math
    rng = random.Random(140112)
    directions = ((1.,0.),(-1.,0.),(0.,1.),(0.,-1.))
    count=40000; lag=0.7; rate=2.0
    sum0=sum1=sum01=0.
    for _ in range(count):
        first=directions[rng.randrange(4)]
        heading=first
        position=[0.,0.]
        age=0.
        while age<18.:
            right=min(18.,age+rng.expovariate(rate))
            weight=math.exp(-age)-math.exp(-right)
            position[0]+=weight*heading[0]
            position[1]+=weight*heading[1]
            age=right
            heading=directions[rng.randrange(4)]
        u0=position[0]**2+position[1]**2
        heading=first
        elapsed=0.
        while elapsed<lag:
            next_t=min(lag,elapsed+rng.expovariate(rate))
            attenuation=math.exp(-(next_t-elapsed))
            position[0]=attenuation*position[0]+(1-attenuation)*heading[0]
            position[1]=attenuation*position[1]+(1-attenuation)*heading[1]
            elapsed=next_t
            heading=directions[rng.randrange(4)]
        u1=position[0]**2+position[1]**2
        sum0+=u0;sum1+=u1;sum01+=u0*u1
    empirical=(sum01/count-(sum0/count)*(sum1/count))/F(1,18)
    target=kernel(lag,1,2)
    assert abs(empirical-target)<.05, (empirical,target)
    print(f'Independent 40,000-path lag check: empirical={empirical:.9f}, exact={target:.9f}')

def verify():
    D = ((F(1),F(0)), (F(-1),F(0)), (F(0),F(1)), (F(0),F(-1)))
    checks = 0
    for a in [F(1,7),F(1,2),F(1),F(3,2),F(2),F(5)]:
        for w in [F(0),F(1,4),F(1,2),F(3,4),F(1)]:
            if w == 1:
                directions = D[:2]; p=(F(1,2),F(1,2))
            else:
                directions = D; p=((1+w)/4,(1+w)/4,(1-w)/4,(1-w)/4)
            mean,m4,_=stationary_moments(a,directions,p)
            s=(1+w*w)/2
            mf,vf=expected_formula(a,s)
            assert mean==mf and m4-mean*mean==vf, (a,w,mean,m4,vf)
            checks+=2
            assert m4>0 and vf>0
            checks+=2
    # Exact rational duality and strict variance distinction
    for mu,gamma,v,s in product([F(1,3),F(1),F(2)], [F(1,5),F(1),F(2)], [F(1),F(2)], [F(1,2),F(1)]):
        mp=(mu+gamma)/2; gp=(3*mu-gamma)/2
        if gp<=0:continue
        assert mu*(mu+gamma)==mp*(mp+gp)
        assert {2*mu,mu+gamma}=={2*mp,mp+gp}
        checks+=2
        vd=variance(mu,gamma,v,s)-variance(mp,gp,v,s)
        assert (vd>0)-(vd<0)==(gamma>mu)-(gamma<mu)
        checks+=1
        for t in [0.0,0.3,1.1,3.0]:
            assert abs(kernel(t,mu,gamma)-kernel(t,mp,gp))<1e-13
            checks+=1
    assert variance(F(1),F(2),F(1),F(1,2))==F(1,18)
    assert variance(F(3,2),F(1,2),F(1),F(1,2))==F(1,63)
    assert abs(kernel(0.3,1,1)-1.6*__import__('math').exp(-0.6))<1e-14
    checks+=3
    independent_trajectory_check()
    print(f'PASS: {checks} exact-rational and analytic-kernel checks plus 1 seeded path check')

if __name__=='__main__':
    verify()
