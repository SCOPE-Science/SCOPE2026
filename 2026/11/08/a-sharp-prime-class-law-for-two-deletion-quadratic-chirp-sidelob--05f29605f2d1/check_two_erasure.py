"""Reproducible checks for the two-point deletion cyclic chirp energy theorem.

Run: python3 check_two_erasure.py
Only Python standard library required. Direct correlation is independent of the
closed character-sum formula, and no floating tests serve as proof.
"""
import cmath
import math


def primes_to(n):
    return [p for p in range(3,n+1,2) if all(p%d for d in range(2, math.isqrt(p)+1))]


def legendre(a,p):
    v=pow(a%p,(p-1)//2,p)
    assert v in (1,p-1)
    return 1 if v==1 else -1


def energy_direct(p,u,d,a=0):
    values=[cmath.exp(-1j*math.pi*u*k*(k+1)/p) for k in range(p)]
    values[a%p]=values[(a+d)%p]=0j
    return sum(abs(sum(values[(n+k)%p]*values[n].conjugate() for n in range(p)))**2
               for k in range(1,p))


def energy_exact(p,u,d):
    r=(u*d*d*pow(4,-1,p))%p
    assert r!=0
    chi=legendre(r,p)
    base=4*p-22-8*math.cos(8*math.pi*r/p)
    if p%4==1:
        return base +4*math.sqrt(p)*chi*(1+math.cos(2*math.pi*r/p))
    return base +4*math.sqrt(p)*chi*math.sin(2*math.pi*r/p)


def run():
    cases=0
    for p in primes_to(17):
        for u in range(1,p):
            for d in range(1,p):
                expected=energy_exact(p,u,d)
                assert expected>=-5e-10,(p,u,d,expected)
                for a in [0, (p-1)//2]:
                    observed=energy_direct(p,u,d,a)
                    assert abs(observed-expected)<4e-9,(p,u,d,a,observed,expected)
                    cases+=1
    fourth_cases=0
    for p in primes_to(17):
        for u in range(1,p):
            for d in (1, p-1):
                y=[cmath.exp(-1j*math.pi*u*n*(n+1)/p) for n in range(p)]
                y[0]=0j
                y[d]=0j
                fft=[sum(y[n]*cmath.exp(-2j*math.pi*m*n/p) for n in range(p)) for m in range(p)]
                fourth=sum(abs(z)**4 for z in fft)/p-(p-2)**2
                assert abs(fourth-energy_exact(p,u,d))<6e-9,(p,u,d,fourth)
                fourth_cases+=1
    for p in primes_to(53):
        for d in (1,2,p-1):
            table=sorted(energy_exact(p,u,d) for u in range(1,p))
            base=sorted(energy_exact(p,u,1) for u in range(1,p))
            assert max(abs(x-y) for x,y in zip(table,base))<1e-9,p
    large=[]
    for p in (101,103,197,199,401,409,1009,1013):
        m=min(energy_exact(p,u,1) for u in range(1,p))
        gamma=8 if p%4==1 else 4
        barrier=4*p-30-gamma*math.sqrt(p)
        assert m>=barrier-1e-8
        large.append((p,round(m-barrier,7)))
    print('DOUBLE_ERASURE_CHIRP_PASS direct_cases=%d fourth_moment_cases=%d spacing_primes=%d asymptotic_samples=%s'%(cases,fourth_cases,len(primes_to(53)),large))

if __name__=='__main__':
    run()
