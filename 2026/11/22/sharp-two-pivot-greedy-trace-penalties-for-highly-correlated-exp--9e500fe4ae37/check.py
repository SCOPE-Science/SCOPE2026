"""Independent rational finite-kernel checks and continuum limit sampling.
Run: python check.py  (Python 3 standard library only).
"""
from fractions import Fraction as F
import math


def residual_formula(n, rho, i, j):
    """Trace of residual of rank-two Nyström on AR(1), with 0<=i<j<n."""
    assert 0 <= i < j < n and 0 < rho < 1
    t = rho * rho
    d = j - i
    return (sum(1-t**a for a in range(1, i+1))
            + sum(1-t**b for b in range(1, n-j))
            + sum((1-t**s)*(1-t**(d-s))/(1-t**d)
                  for s in range(1, d)))


def direct_schur_trace(n, rho, i, j):
    """Independent 2x2 block inverse and Schur diagonal calculation."""
    q = rho**(j-i)
    den = 1-q*q
    total = F(0)
    for k in range(n):
        a, b = rho**abs(k-i), rho**abs(k-j)
        prediction_variance = (a*a+b*b-2*q*a*b)/den
        total += 1-prediction_variance
    return total


def greedy_second(n, i):
    """Both farthest endpoints are valid in a geometric tie."""
    return [j for j in (0,n-1) if j!=i and abs(i-j)==max(i,n-1-i)]


def discrete_objectives(n, t):
    assert 0<t<1
    def E(i,j):
        if i>j:i,j=j,i
        d=j-i
        return (sum(1-t**a for a in range(1,i+1))
                + sum(1-t**b for b in range(1,n-j))
                + sum((1-t**s)*(1-t**(d-s))/(1-t**d) for s in range(1,d)))
    vals=[(E(i,j),i,j) for i in range(n) for j in range(i+1,n)]
    gr=[(E(min(i,j),max(i,j)),i,j) for i in range(n) for j in greedy_second(n,i)]
    return min(vals),min(gr),max(gr)


def limiting_objective(x,y):
    return x*x/2+(1-y)*(1-y)/2+(y-x)*(y-x)/6


def run():
    tests=0
    for n in range(3,12):
        for rho in (F(1,5),F(1,2),F(3,4),F(9,10)):
            for i in range(n):
                for j in range(i+1,n):
                    assert residual_formula(n,rho,i,j)==direct_schur_trace(n,rho,i,j)
                    tests+=1
            for i in range(n):
                t=rho*rho
                scores=[(1-t**abs(i-j),j) for j in range(n) if j!=i]
                maxima=[j for s,j in scores if s==max(z[0] for z in scores)]
                assert sorted(maxima)==sorted(greedy_second(n,i))
                tests+=1
    assert limiting_objective(.2,.8)==.10000000000000002 or abs(limiting_objective(.2,.8)-.1)<1e-12
    assert abs(limiting_objective(.25,1)-.125)<1e-12
    assert abs(limiting_objective(0,1)-1/6)<1e-12
    print('Exact Schur / Markov and pivot checks:',tests)
    for n in (20,40,80,160):
        # gamma=(1-t) n -> 0; avoid loss of precision of t**j.
        t=math.exp(-1/n**3)
        opt,best,worst=discrete_objectives(n,t)
        print('n=',n,'(best greedy)/opt=',round(best[0]/opt[0],8),
              '(worst greedy)/opt=',round(worst[0]/opt[0],8),
              'opt sites=',(opt[1],opt[2]),
              'best first=',best[1], 'worst first=',worst[1])
    print('Targets: 1.25 and 1.666666666667')

if __name__=='__main__': run()
