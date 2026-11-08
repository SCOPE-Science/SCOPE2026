#!/usr/bin/env python3
"""Finite arithmetic consistency checks for a two-speed coupon refresh model.

These checks do not prove any limiting theorem or claim historical priority.
Run: python3 verify.py
"""
from fractions import Fraction
from math import comb, exp, factorial, log

checks = 0

def check(condition, explanation):
    global checks
    if not condition:
        raise AssertionError(explanation)
    checks += 1

def probabilities(m1,m2,a,b,c):
    m=m1+m2
    assert 0<c<m
    wbar=(m1*a+m2*b)/m
    pa=a/(m*wbar)
    pb=b/(m*wbar)
    p=c/m
    return pa,pb,p

def invariant_prob(m1,m2,p,k,l):
    return Fraction(comb(m1,k)*comb(m2,l),1)*p**(k+l)*(1-p)**(m1+m2-k-l)

for a,b in [(Fraction(2,3),Fraction(4,3)),(Fraction(1,2),Fraction(3,2))]:
  for m in (2,4,6,8,10,12):
    m1=m//2; m2=m-m1
    pa,pb,p=probabilities(m1,m2,a,b,Fraction(1,1))
    check(pa*m1+pb*m2==1, 'selection weights must sum to one')
    check(0<p<1 and 0<pa<1 and 0<pb<1, 'model probabilities positive')
    total=Fraction(0)
    for k in range(m1+1):
      for l in range(m2+1):
        pi=invariant_prob(m1,m2,p,k,l)
        total+=pi
        upa=(m1-k)*pa*p
        downa=k*pa*(1-p)
        upb=(m2-l)*pb*p
        downb=l*pb*(1-p)
        check(0<=upa and 0<=downa and 0<=upb and 0<=downb,'transition nonnegative')
        check(upa+downa+upb+downb<=1,'transition row stochastic')
        if k<m1:
          pi_next=invariant_prob(m1,m2,p,k+1,l)
          check(pi*upa==pi_next*(k+1)*pa*(1-p),'first-class detailed balance')
        if l<m2:
          pi_next=invariant_prob(m1,m2,p,k,l+1)
          check(pi*upb==pi_next*(l+1)*pb*(1-p),'second-class detailed balance')
    check(total==1,'stationary law normalizes')

# The limiting stationary vacant-state transition probability equals the
# product of the two independent immigration-death equilibrium kernels.
c=1.4
rho=0.4
a=0.6
b=(1-rho*a)/(1-rho)
C1,C2=c*rho,c*(1-rho)

def mean_series(J=28):
    return sum((C1**j/factorial(j))*(C2**k/factorial(k))/(a*j+b*k)
               for j in range(J+1) for k in range(J+1) if j+k>0)

def mean_integral(n=12000,L=45):
    h=L/n
    def f(t):return exp(C1*exp(-a*t)+C2*exp(-b*t))-1
    return h/3*(f(0)+f(L)+4*sum(f((2*i-1)*h) for i in range(1,n//2+1))
                +2*sum(f(2*i*h) for i in range(1,n//2)))
M=mean_series()
M_queue=M
I=mean_integral()
check(abs(M-I)<4e-9,'queue mean series equals time integral')
check(M>sum(c**j/(factorial(j)*j) for j in range(1,29)),'strict unequal-rate delay penalty')
for t in (.01,.05,.1,.25,.5,1,2,5,12,30):
    check(rho*exp(-a*t)+(1-rho)*exp(-b*t)>exp(-t), 'Jensen heterogeneity gap')

def laplace_formula(s):
    return 1/(s*sum((C1**j/factorial(j))*(C2**k/factorial(k))/(s+a*j+b*k)
                    for j in range(29) for k in range(29)))

def laplace_integral(s,n=16000,L=35):
    h=L/n
    def f(t):return exp(-s*t)*exp(C1*exp(-a*t)+C2*exp(-b*t))
    return 1/(s*(h/3*(f(0)+f(L)+4*sum(f((2*i-1)*h) for i in range(1,n//2+1))
                  +2*sum(f(2*i*h) for i in range(1,n//2)))+exp(-s*L)/s))
for s in (Fraction(1,5),Fraction(1,2),Fraction(3,2),Fraction(4,1)):
    s=float(s)
    check(abs(laplace_formula(s)-laplace_integral(s))<2e-9,'Laplace integral/series')
check(abs(laplace_formula(1e-6)-(1-M*1e-6))<2e-9,'zero-argument transform slope')
check(abs(laplace_formula(1e4)-exp(-c))<1e-3,'Laplace large argument sees atom at zero')

# The Poissonized two-speed ordinary cover time has an exact finite product CDF.
for m in (100,1000,10000):
    m1=int(rho*m);m2=m-m1
    wbar=(m1*a+m2*b)/m
    for x in (-1.0,0.0,1.0):
        t=m/a*(log(m)+x)
        F=(1-exp(-a*t/(m*wbar)))**m1 * (1-exp(-b*t/(m*wbar)))**m2
        limit=exp(-rho*exp(-x))
        check(0<F<1, 'finite coupon CDF well defined')
        if m==10000:
            check(abs(F-limit)<0.001,'cover-time Gumbel CDF diagnostic')


# Exact finite PGF and mean of the stationary-start post-cover delay,
# independently checked by solving an absorbing Markov system on all masks.
def solve_linear(A, y):
    n=len(y)
    A=[list(row)+[v] for row,v in zip(A,y)]
    for j in range(n):
        row=next(i for i in range(j,n) if A[i][j])
        A[j],A[row]=A[row],A[j]
        div=A[j][j]
        for k in range(j,n+1): A[j][k]/=div
        for i in range(n):
            if i==j:continue
            mult=A[i][j]
            if mult:
                for k in range(j,n+1):A[i][k]-=mult*A[j][k]
    return [row[-1] for row in A]

def spectral_pgf_mean(weights,p,z):
    m=len(weights);r=p/(1-p)
    spectral=Fraction(0);delay_mean=Fraction(0)
    for mask in range(1<<m):
        k=mask.bit_count()
        qs=sum((weights[i] for i in range(m) if mask&(1<<i)),Fraction(0))
        spectral+=r**k/(1-z*(1-qs))
        if mask:delay_mean+=r**k/qs
    return 1/((1-z)*spectral), delay_mean

def direct_pgf_mean(weights,p,z):
    m=len(weights);N=1<<m
    target=N-1
    masks=[i for i in range(N) if i!=target]
    index={u:j for j,u in enumerate(masks)}
    A=[[Fraction(int(i==j),1) for j in range(N-1)]for i in range(N-1)]
    B=[Fraction(0) for _ in masks]
    C=[Fraction(1) for _ in masks]
    for old in masks:
        j=index[old]
        for i,w in enumerate(weights):
            for good,prob in [(True,1-p),(False,p)]:
                new=(old|(1<<i)) if good else (old&~(1<<i))
                mass=w*prob
                if new==target:B[j]+=z*mass
                else:A[j][index[new]]-=z*mass
    f=solve_linear(A,B)
    # replace discount z with 1 for mean linear system
    A2=[[Fraction(int(i==j),1) for j in range(N-1)]for i in range(N-1)]
    for old in masks:
        j=index[old]
        for i,w in enumerate(weights):
            for good,prob in [(True,1-p),(False,p)]:
                new=(old|(1<<i)) if good else (old&~(1<<i))
                if new!=target:A2[j][index[new]]-=w*prob
    h=solve_linear(A2,C)
    mass=lambda mask: p**(m-mask.bit_count())*(1-p)**mask.bit_count()
    pgf=mass(target)+sum((mass(mask)*f[index[mask]] for mask in masks),Fraction(0))
    mean=sum((mass(mask)*h[index[mask]] for mask in masks),Fraction(0))
    return pgf,mean

for weights in [
  (Fraction(1,3),Fraction(2,3)),
  (Fraction(1,4),Fraction(3,4)),
  (Fraction(1,6),Fraction(1,3),Fraction(1,2)),
  (Fraction(1,10),Fraction(3,10),Fraction(6,10)),
  (Fraction(1,12),Fraction(1,6),Fraction(1,4),Fraction(1,2)),
  (Fraction(1,4),)*4,
]:
  for p in (Fraction(1,4),Fraction(2,5)):
    for z in (Fraction(1,3),Fraction(2,3)):
      F,M=spectral_pgf_mean(weights,p,z)
      F2,M2=direct_pgf_mean(weights,p,z)
      check(F==F2,'stationary-start PGF equals absorbing-chain solution')
      check(M==M2,'stationary-start mean equals absorbing-chain solution')

# More dispersed selection probabilities strictly increase the post-cover mean.
for p in (Fraction(1,5),Fraction(1,2)):
  m=4
  uniform=tuple(Fraction(1,m) for _ in range(m))
  mild=(Fraction(1,8),Fraction(1,4),Fraction(1,4),Fraction(3,8))
  extreme=(Fraction(1,16),Fraction(1,8),Fraction(1,4),Fraction(9,16))
  means=[spectral_pgf_mean(w,p,Fraction(1,2))[1] for w in (uniform,mild,extreme)]
  check(means[0]<means[1]<means[2], 'strict mean penalty for dispersed sampling')


# The exact spectral expression for the all-present return probability can
# be compared with a brute-force transition matrix for small labeled systems.
for weights in [
 (Fraction(1,3),Fraction(2,3)),
 (Fraction(1,6),Fraction(1,3),Fraction(1,2)),
 (Fraction(1,12),Fraction(1,6),Fraction(1,4),Fraction(1,2)),
]:
    p=Fraction(1,4);m=len(weights);r=p/(1-p)
    N=1<<m;target=N-1
    dist=[Fraction(0) for _ in range(N)];dist[target]=1
    for n in range(7):
        formula=(1-p)**m*sum((r**mask.bit_count()*(1-sum((weights[i] for i in range(m) if (mask>>i)&1),Fraction(0)))**n for mask in range(N)),Fraction(0))
        check(dist[target]==formula,'exact return probability spectral expansion')
        nextdist=[Fraction(0) for _ in range(N)]
        for mask,pm in enumerate(dist):
            if not pm:continue
            for i,w in enumerate(weights):
                nextdist[mask|(1<<i)]+=pm*w*(1-p)
                nextdist[mask&~(1<<i)]+=pm*w*p
        check(sum(nextdist)==1,'brute-force transition preserves mass')
        dist=nextdist

# Cover-time inclusion-exclusion and two separate dispersion inequalities.
def cover_expectation(weights):
    m=len(weights)
    return sum(((-1)**(mask.bit_count()+1) / sum((weights[i] for i in range(m) if mask&(1<<i)), Fraction(0)) for mask in range(1,1<<m)),Fraction(0))
for p in (Fraction(1,5),Fraction(1,2)):
    uniform=(Fraction(1,4),)*4
    mild=(Fraction(1,8),Fraction(1,4),Fraction(1,4),Fraction(3,8))
    extreme=(Fraction(1,16),Fraction(1,8),Fraction(1,4),Fraction(9,16))
    collect=[cover_expectation(q) for q in (uniform,mild,extreme)]
    delayed=[spectral_pgf_mean(q,p,Fraction(1,2))[1] for q in (uniform,mild,extreme)]
    check(collect[0]<collect[1]<collect[2],'ordinary expected cover increases with weight dispersion')
    check(all(collect[i]+delayed[i]<collect[i+1]+delayed[i+1] for i in (0,1)),
          'full clumsy expected completion strictly increases with dispersion')
    check(collect[0]==4*(Fraction(1)+Fraction(1,2)+Fraction(1,3)+Fraction(1,4)),
          'uniform coupon mean recovers harmonic-number identity')

print('PASS: %d deterministic exact/rational/numerical checks'%checks)
print('two-class mean delay=%.12f; uniform benchmark=%.12f'%(M_queue,sum(c**j/(factorial(j)*j) for j in range(1,29))))
print('Laplace at s=1/2=%.12f'%laplace_formula(.5))
