"""Exact finite checks for the prime-power follow-up theorem.

The infinite assertions in RESULT.md are proved mathematically; this script
checks finite instances and is not an exhaustive proof for all N.
Run: python3 checker.py
"""
from fractions import Fraction
from math import gcd, lcm, isqrt


def prime_powers(N):
    result=[]
    for q in range(2,N+1):
        div=[p for p in range(2,q+1) if q%p==0 and all(p%d for d in range(2,isqrt(p)+1))]
        if len(div)==1:
            result.append(q)
    return result


def visits_denom(N):
    return [(q, Fraction(1,q)) for q in prime_powers(N)]


def transit_exact(k,t):
    return (k*t).denominator==1


def transit_with_tolerance(k,t,eps):
    return any(abs(t-Fraction(j,k)) <= eps for j in range(1,k))


def signature(k,times,eps=None):
    if eps is None:
        return tuple(int(transit_exact(k,t)) for t in times)
    return tuple(int(transit_with_tolerance(k,t,eps)) for t in times)


def check():
    assertions=0
    for N in range(2,151):
        pps=prime_powers(N)
        times=[t for _,t in visits_denom(N)]
        assert len(pps)==len(times); assertions+=1
        sigs=[signature(k,times) for k in range(1,N+1)]
        assert len(set(sigs))==N; assertions+=1
        for q in pps:
            pp=next(p for p in range(2,q+1) if q%p==0 and all(p%d for d in range(2,isqrt(p)+1)))
            smaller=q//pp
            # The q coordinate is forced by this adjacent prime-power pair.
            for d in range(2,N+1):
                if transit_exact(q,Fraction(1,d))!=transit_exact(smaller,Fraction(1,d)):
                    assert d==q; assertions+=1
            assert signature(q,times) != signature(smaller,times); assertions+=1
        H=1
        for k in range(1,N+1): H=lcm(H,k)
        assert all(H%q==0 for q in pps); assertions+=1
        if N<=22:
            eps=Fraction(1,3*N*N)
            eps_sigs=[signature(k,times,eps) for k in range(1,N+1)]
            assert eps_sigs==sigs; assertions+=1
    for N,expected,H in [(6,4,60),(12,8,27720),(38,19,5342931457063200)]:
        assert len(prime_powers(N))==expected; assertions+=1
        g=1
        for k in range(1,N+1):g=lcm(g,k)
        assert g==H; assertions+=1
        assert len([p for p in prime_powers(N) if all(p%d for d in range(2,isqrt(p)+1))]) <= expected; assertions+=1
    # Direct finite-rational separation of primitive phases.
    for N in range(2,31):
        phases=sorted({Fraction(j,q) for q in prime_powers(N) for j in range(1,q) if gcd(j,q)==1})
        for a,b in zip(phases,phases[1:]):
            assert b-a>=Fraction(1,N*N); assertions+=1
    print(f"PASS: {assertions} exact assertions; exact 0 and finite-tolerance signatures, prime-power witness necessity, grid constants, rational separation.")


if __name__=='__main__': check()
