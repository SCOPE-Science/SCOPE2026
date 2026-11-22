"""Standalone diagnostics for a transient Gaussian-pulse Poisson information theorem."""
import math
import random

checks = 0

def check(condition, reason):
    global checks
    if not condition:
        raise AssertionError(reason)
    checks += 1

def g(t, a, D, A, k):
    return A / math.sqrt(t) * math.exp(-k*t - a*a/(4*D*t))

def info(t, a, D, A, b, k):
    s = g(t, a, D, A, k)
    return (a*a/(2*D*D*t*t))*s*s/(b+s)

def derivatives(t, a, D, A, b, k):
    val = []
    for x in (-a, 0., a):
        sig = A/math.sqrt(t)*math.exp(-k*t-(x*x)/(4*D*t))
        val.append((b+sig, sig*x/(2*D*t), sig/A, 1.))
    mat = [[sum(row[i+1]*row[j+1]/row[0] for row in val)
            for j in range(3)] for i in range(3)]
    return mat

def eff(mat):
    m = mat
    det = m[1][1]*m[2][2]-m[1][2]*m[2][1]
    check(det>0, 'nuisance invertibility')
    r = (m[0][1]*(m[2][2]*m[1][0]-m[1][2]*m[2][0])+
         m[0][2]*(-m[2][1]*m[1][0]+m[1][1]*m[2][0]))/det
    return m[0][0]-r

def F(t,a,D,A,b,k):
    s=g(t,a,D,A,k);p=s/(b+s);h=a*a/(4*D)
    return -2+(2-p)*(-.5+h/t-k*t)

def logtime_second(t,a,D,A,b,k):
    h=a*a/(4*D);s=g(t,a,D,A,k);p=s/(b+s)
    lp=-.5-k*t+h/t;lpp=-k*t-h/t
    return (2-p)*lpp-p*(1-p)*lp*lp

def T(h,k,alpha):
    return 2*h/(alpha+math.sqrt(alpha*alpha+4*k*h))

def root(a,D,A,b,k):
    h=a*a/(4*D)
    lo=T(h,k,2.5);hi=T(h,k,1.5)
    for _ in range(100):
        mid=(lo+hi)/2
        if F(mid,a,D,A,b,k)>0:lo=mid
        else:hi=mid
    return (lo+hi)/2

# Exact symbolic example evaluated numerically independently of root finding.
a=2.;D=A=1.;k=0.;b=math.exp(-2)/math.sqrt(2)
check(abs(F(.5,a,D,A,b,k))<1e-13,'exact stationary example')
check(abs(root(a,D,A,b,k)-.5)<1e-13,'example unique root')
check(abs(g(.5,a,D,A,k)-2*b)<1e-13,'example signal/background')

rng=random.Random(37091)
for n in range(2200):
    a=math.exp(rng.uniform(-1.3,1.3))
    D=math.exp(rng.uniform(-1.3,1.3))
    A=math.exp(rng.uniform(-1.5,1.5))
    b=A*math.exp(rng.uniform(-3,3))
    k=0. if n%3==0 else math.exp(rng.uniform(-2.5,1))
    h=a*a/(4*D)
    t=root(a,D,A,b,k)
    check(T(h,k,2.5)<t<T(h,k,1.5),'bracket')
    check(abs(F(t,a,D,A,b,k))<1e-10,'root residual')
    check(logtime_second(t,a,D,A,b,k)<0,'strict logtime concavity')
    check(T(h,k,1.5)/T(h,k,2.5)<=5/3+1e-12,'sharp factor bound')
    check(info(t,a,D,A,b,k)>info(T(h,k,2.5),a,D,A,b,k),'interior vs lower end')
    check(info(t,a,D,A,b,k)>info(T(h,k,1.5),a,D,A,b,k),'interior vs upper end')
    check(root(a,D,A,b*1.2,k)>t,'monotone background effect')
    m=derivatives(t,a,D,A,b,k)
    check(abs(m[0][1])<1e-10*max(1,m[0][0]),'amplitude orthogonality')
    check(abs(m[0][2])<1e-10*max(1,m[0][0]),'background orthogonality')
    val=eff(m)
    check(abs(val-info(t,a,D,A,b,k))<1e-10*max(1,val),'Schur complement')
    # Two arbitrary off-optimal times to test the global strict concavity formula.
    for factor in (0.5, 2.):
        check(logtime_second(t*factor,a,D,A,b,k)<0,'global concavity')

print('VERIFY_OK assertions='+str(checks))
