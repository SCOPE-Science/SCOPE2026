"""Reproducibility checks for the two-rate complex-time Gaussian semigroup theorem.
These finite tests illustrate exact formulas and asymptotics; the infinite claims
are proved analytically in RESULT.md.
"""
import math
from fractions import Fraction

P=4.0
K=2*math.sqrt(P-1)/abs(P-2)
PI=math.pi


def boundary(s, alpha, beta, k=K):
    return max(math.asinh(abs(math.sin(alpha*s))/k)/alpha,
               math.asinh(abs(math.sin(beta*s))/k)/beta)


def intersection_length(intervals_a, intervals_b):
    i=j=0
    total=0.0
    while i<len(intervals_a) and j<len(intervals_b):
        left=max(intervals_a[i][0],intervals_b[j][0])
        right=min(intervals_a[i][1],intervals_b[j][1])
        total+=max(0.,right-left)
        if intervals_a[i][1]<intervals_b[j][1]: i+=1
        else: j+=1
    return total


def rational_density(m,n,omega,t,k=K):
    period=PI/omega
    def segments(rate):
        a=k*math.sinh(rate*t)
        if a>=1: return [(0., period)]
        radius=math.asin(a)/rate
        r=round(rate/omega)
        seg=[]
        for j in range(r+1):
            x=j*PI/rate
            lo=max(0.,x-radius); hi=min(period,x+radius)
            if hi>lo: seg.append((lo,hi))
        return seg
    return intersection_length(segments(m*omega), segments(n*omega))/period


def irrational_density(alpha,beta,t,k=K):
    return (2/PI*math.asin(min(1,k*math.sinh(alpha*t)))) * (2/PI*math.asin(min(1,k*math.sinh(beta*t))))

# Exact periodicity check of rational rates for a nontrivial family.
period_tests=0
for m,n in [(1,2),(2,3),(3,5),(5,8)]:
    assert math.gcd(m,n)==1
    for t in [0.0, 0.01,0.13,0.8]:
        for i in range(-50,51):
            s=i/13
            assert abs(boundary(s,m,n)-boundary(s+PI,m,n)) < 1e-13
            period_tests+=1

# Rational first-order density coefficient for primitive rate pairs.
rational_tests=0
for m,n in [(1,1),(2,3),(3,5),(5,8)]:
    for t in [1e-3,5e-4,2e-4]:
        d=rational_density(m,n,1.,t)
        predicted=2*K*t/PI
        assert abs(d/predicted-1) < 2e-3, (m,n,t,d,predicted)
        rational_tests+=1

# Irrational second-order density coefficient.
irrational_tests=0
for beta in [math.sqrt(2),(1+math.sqrt(5))/2,math.pi]:
    for t in [0.005,0.002,0.0005]:
        dens=irrational_density(1,beta,t)
        predicted=4*K*K*beta*t*t/(PI*PI)
        assert abs(dens/predicted-1) < 2e-4, (beta,t,dens,predicted)
        irrational_tests+=1

# The golden-ratio sharp contact constant, with convergent denominators.
beta=(1+math.sqrt(5))/2
predicted=PI**2/(2*K*beta*math.sqrt(5))
fib=[1,1]
for _ in range(22): fib.append(fib[-1]+fib[-2])
contact_tests=0
for m in fib[9:20]:
    n=round(m*beta)
    s=PI/2*(m+n/beta)
    observed=s*boundary(s,1.,beta)
    tol=max(2./m,2e-6)
    assert abs(observed/predicted-1) < tol, (m, observed, predicted)
    contact_tests+=1

# Epigraph boundary: exact monotonicity and membership either side, avoiding very small scales.
threshold_tests=0
for alpha,beta in [(1.,math.sqrt(2)),(2.,3.),(math.pi,math.sqrt(3))]:
    for i in range(1,200):
        s=i*.073
        h=boundary(s,alpha,beta)
        below=h-1e-7
        above=h+1e-7
        assert all(abs(math.sin(r*s)) <= K*math.sinh(r*above)+1e-12 for r in (alpha,beta))
        assert any(abs(math.sin(r*s)) > K*math.sinh(r*below) for r in (alpha,beta))
        threshold_tests+=1
print('PASS: %d periodicity, %d rational-density, %d irrational-density, %d golden-contact, %d epigraph tests.' %
      (period_tests,rational_tests,irrational_tests,contact_tests,threshold_tests))
print('Golden limiting contact coefficient: %.15f' % predicted)
