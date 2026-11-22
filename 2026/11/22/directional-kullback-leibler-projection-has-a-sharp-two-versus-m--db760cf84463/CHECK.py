"""Standalone checks for exact KL projections of equally spaced circular Poisson sources.
Run: python3 CHECK.py. Diagnostic samples do not prove the global theorem.
"""
import math

def critical_q(m):
    assert m>=3
    return math.exp((m-1)*math.log(m-1)-0.5*m*math.log(m)-0.5*(m-2)*math.log(m-2))

def critical_t(m):
    return math.sqrt(m*(m-2))/(m-1)

def log_obj(m,q,t):
    return 2*math.log1p(-q*t**m)-math.log1p(-t*t)

def shape(m,t):
    return t**(m-2)*(m-(m-1)*t*t)

def outer_stationary(m,q):
    assert m>=3 and q>=critical_q(m)*(1-1e-11)
    l=math.sqrt((m-2)/(m-1)); h=1.0
    for _ in range(90):
        mid=(l+h)/2
        if q*shape(m,mid)>1: l=mid
        else: h=mid
    return (l+h)/2

def integrand_density(r,theta):
    return (1-r*r)/(1+r*r-2*r*math.cos(theta))

def numerical_kl(m,r,t,phi,N=4096):
    q=r**m
    total=0.0
    for k in range(N):
        th=2*math.pi*(k+0.5)/N
        p=integrand_density(t,th-phi)
        Q=integrand_density(q,m*th)
        total+=p*math.log(p/Q)
    return total/N

def formula_kl(m,r,t,phi):
    q=r**m
    a=complex(math.cos(m*phi), math.sin(m*phi))*q*t**m
    return -math.log1p(-t*t)-math.log1p(-q*q)+2*math.log(abs(1-a))

count=0
for m in range(2,61):
    if m==2:
        q_star=0.5
        for q in [0.01,0.25,0.49,0.5,0.5001,0.60,0.8,0.999]:
            pred=0.0 if q<=0.5 else math.sqrt(2-1/q)
            for j in range(2001):
                x=j/2001
                assert log_obj(m,q,x)>=log_obj(m,q,pred)-3e-12
                count+=1
    else:
        qc=critical_q(m); tc=critical_t(m)
        assert 0<qc<1
        assert abs(qc*shape(m,tc)-1)<2e-12, (m,qc*shape(m,tc))
        assert abs(log_obj(m,qc,tc))<4e-12
        for q in [0.1*qc,0.8*qc,qc*0.999,qc,qc+0.001*(1-qc),0.5*(1+qc),0.99]:
            t0=0 if q<=qc else outer_stationary(m,q)
            for j in range(1201):
                t=j/1201
                assert log_obj(m,q,t)>=log_obj(m,q,t0)-1e-10,(m,q,t,t0)
                count+=1
for m in range(2,9):
    for r in [0.2,0.51,0.84]:
        for t in [0.0,0.17,0.55,0.81]:
            for phi in [0.0,0.2,0.7]:
                diff=abs(numerical_kl(m,r,t,phi,4096)-formula_kl(m,r,t,phi))
                assert diff<1e-10,(m,r,t,phi,diff)
                count+=1
for m in [3,4,5,10,20,50,1000,10000]:
    qc=critical_q(m); rc=qc**(1/m)
    assert 0<rc<1
    print('m=',m,'qcrit=',format(qc,'.15g'),'rcrit=',format(rc,'.15g'),
          'tjump=',format(critical_t(m),'.15g'))
print('PASS',count,'finite diagnostics')
