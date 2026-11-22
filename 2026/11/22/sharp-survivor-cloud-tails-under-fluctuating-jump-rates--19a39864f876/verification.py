"""Numerical checks for fixed-time tails in an absorbed, random-clock nearest-neighbor walk.

No random sampling and no external network access. Requires scipy/numpy.
The examples employ one Pareto-distributed rate during a unit observation interval.
"""
from math import gamma, pi
from scipy.integrate import quad
from scipy.special import ive
from math import comb


def free_pmf(k, alpha, upper_log_rate=17.0):
    # A=Lambda with P(Lambda>z)=z**(-alpha), z>=1; Poisson-clock SSRW.
    # e**(-A) I_k(A) = P(W_{Pois(A)}=k).
    return quad(lambda log_a: alpha * __import__('math').exp(-alpha*log_a)
                * ive(abs(k), __import__('math').exp(log_a)), 0,
                upper_log_rate, epsabs=4e-12, epsrel=2e-9, limit=300)[0]


def killed_pmf_deterministic(j, n, m):
    def binom(k):
        if n+k < 0 or (n+k) % 2 or abs(k)>n:
            return 0
        return comb(n, (n+k)//2) / 2**n
    return binom(j-m)-binom(j+m)


def main():
    tests=0
    for m in (1,2,3):
        for n in range(21):
            first=sum(j*killed_pmf_deterministic(j,n,m) for j in range(1,n+m+1))
            assert abs(first-m)<1e-10, (m,n,first)
            tests+=1
    for alpha in (.3, .7):
        kconst=alpha * 2**alpha * gamma(alpha+.5) / pi**.5
        for k in (12,32,64):
            p=free_pmf(k,alpha)
            ratio=p/(kconst*k**(-2*alpha-1))
            assert .97<ratio<1.03,(alpha,k,ratio)
            tests+=1
        m=2
        pref=2*m*kconst
        for h in (20,40,80):
            crossing=sum(free_pmf(j,alpha) for j in range(h-m+1,h+m+1))
            ratio=crossing/(pref*h**(-2*alpha-1))
            assert .95<ratio<1.07, (alpha,h,ratio)
            tests+=1
    print(f'PASS: {tests} exact-martingale, free-density and reflected-tail checks')

if __name__=='__main__':
    main()
