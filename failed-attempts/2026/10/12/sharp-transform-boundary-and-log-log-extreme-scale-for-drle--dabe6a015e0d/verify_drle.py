import math

def params(alpha,beta):
    lam=alpha/beta
    q=math.exp(-lam)
    c=lam/(beta-1.0)
    A=1.0-q*(1.0+c)
    B=c*(1.0-q)
    return lam,q,c,A,B

def S(n,alpha,beta):
    lam,q,c,A,B=params(alpha,beta)
    return (1.0+c*n)*math.exp(-lam*n)

def p(n,alpha,beta):
    return S(n,alpha,beta)-S(n+1,alpha,beta)

def hazard_exact(n,alpha,beta):
    lam,q,c,A,B=params(alpha,beta)
    return 1.0-q-q*c/(1.0+c*n)

def q_asym(u,alpha,beta):
    L=math.log(1.0/u)
    return (beta/alpha)*(L+math.log(L)-math.log(beta-1.0))

for alpha,beta in [(1.2,3.0),(1.8,4.0),(0.7,2.0),(5.0,6.0)]:
    lam,q,c,A,B=params(alpha,beta)
    assert A>0 and B>0
    total=A/(1-q)+B*q/(1-q)**2
    assert abs(total-1.0)<1e-12

    # Exact hazard identity checked where direct probabilities are safe.
    for n in (1,10,100):
        h_direct=p(n,alpha,beta)/S(n,alpha,beta)
        h_formula=hazard_exact(n,alpha,beta)
        assert abs(h_direct-h_formula)<1e-12

    # Terminal rate uses the exact formula, avoiding floating underflow.
    n=100000
    scaled=n*((1-q)-hazard_exact(n,alpha,beta))
    assert abs(scaled/q-1.0)<3e-4

    # PMF tail constant at a moderate n.
    n2=300
    pn=p(n2,alpha,beta)
    approx=B*n2*math.exp(-lam*n2)
    assert abs(pn/approx-1.0)<0.05

# MGF: below the boundary the series stabilizes.
alpha,beta=1.2,3.0
lam,q,c,A,B=params(alpha,beta)
t_below=0.5*lam
def partial_mgf(t,N):
    return sum(math.exp(t*n)*p(n,alpha,beta) for n in range(N))
m1=partial_mgf(t_below,200)
m2=partial_mgf(t_below,400)
assert abs(m2-m1)<1e-10

# At the boundary, terms equal A+Bn up to floating error.
for n in (10,50,100):
    term=math.exp(lam*n)*p(n,alpha,beta)
    assert abs(term/(A+B*n)-1.0)<1e-10

# Exact lattice upper quantiles stay within bounded distance of the asymptotic formula.
def quantile_upper(u,alpha,beta):
    lo,hi=0,1
    while S(hi+1,alpha,beta)>u:
        hi*=2
    while lo<hi:
        mid=(lo+hi)//2
        if S(mid+1,alpha,beta)<=u:
            hi=mid
        else:
            lo=mid+1
    return lo

for alpha,beta in [(1.2,3.0),(1.8,4.0)]:
    residuals=[]
    for k in (8,12,18,26,36):
        u=10.0**(-k)
        qn=quantile_upper(u,alpha,beta)
        residuals.append(qn-q_asym(u,alpha,beta))
    assert max(abs(x) for x in residuals)<5.0, residuals

print("VERIFY_OK")
