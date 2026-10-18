import cmath, math, random

def roots(alpha,theta,beta,lam):
    m=alpha-theta*lam
    A=1-beta*lam+m
    d=A*A-4*m
    s=cmath.sqrt(d)
    return m, (A+s)/2, (A-s)/2

def jury(alpha,theta,beta,lam):
    m=alpha-theta*lam
    return abs(m)<1 and beta*lam>0 and beta*lam<2*(1+m)

def phase(alpha,theta,beta,lam):
    m,r1,r2=roots(alpha,theta,beta,lam)
    if m < 0:
        return 'opposite'
    if abs(m) < 1e-14:
        return 'zero-product'
    x=beta*lam
    lo=(1-math.sqrt(m))**2
    hi=(1+math.sqrt(m))**2
    if x < lo-1e-11:
        return 'positive-real'
    if x > hi+1e-11:
        return 'negative-real'
    if lo+1e-11 < x < hi-1e-11:
        return 'complex'
    return 'boundary'

random.seed(34036)
for _ in range(5000):
    alpha=random.random()
    theta=0.8*random.random()
    beta=1.5*random.random()+1e-4
    lam=0.1+4.9*random.random()
    m,r1,r2=roots(alpha,theta,beta,lam)
    stable=max(abs(r1),abs(r2)) < 1-1e-10
    j=jury(alpha,theta,beta,lam)
    # avoid samples numerically almost on a boundary
    if min(abs(abs(m)-1), abs(beta*lam-2*(1+m))) > 1e-7:
        assert stable == j, (alpha,theta,beta,lam,m,r1,r2,stable,j)
    if j and abs(m)>1e-8:
        ph=phase(alpha,theta,beta,lam)
        if ph=='opposite':
            assert abs(r1.imag)<1e-9 and abs(r2.imag)<1e-9 and r1.real*r2.real<0
        elif ph=='positive-real':
            assert abs(r1.imag)<1e-9 and abs(r2.imag)<1e-9 and min(r1.real,r2.real)>=-1e-8
        elif ph=='negative-real':
            assert abs(r1.imag)<1e-9 and abs(r2.imag)<1e-9 and max(r1.real,r2.real)<=1e-8
        elif ph=='complex':
            assert abs(r1.imag)>1e-8 and abs(r2.imag)>1e-8

for _ in range(1000):
    mu=0.1+random.random()
    L=mu+0.2+4*random.random()
    alpha=random.random()
    theta=random.random()/L
    beta=2*random.random()/L
    endpoint=(alpha-theta*mu<1 and L*(beta+2*theta)<2*(1+alpha))
    grid=all(jury(alpha,theta,beta,mu+(L-mu)*i/400) for i in range(401))
    if min(abs(alpha-theta*mu-1), abs(L*(beta+2*theta)-2*(1+alpha)))>1e-7:
        assert endpoint==grid, (mu,L,alpha,theta,beta,endpoint,grid)

mu,L,alpha,theta,beta=1.0,4.0,0.9,0.2,0.1
assert alpha-theta*mu < 1
assert L*(beta+2*theta) < 2*(1+alpha)
for i in range(401):
    lam=mu+(L-mu)*i/400
    assert jury(alpha,theta,beta,lam)
m,r1,r2=roots(alpha,theta,beta,L)
assert abs(m-0.1)<1e-12
assert phase(alpha,theta,beta,L)=='positive-real'
assert max(abs(r1),abs(r2))<1
print('VERIFY_OK')
