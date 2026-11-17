"""Exact finite-state and event-level checks for weighted dimer RSA.
Usage: python verify.py (Python 3 stdlib only).
"""
from fractions import Fraction
from functools import lru_cache
from math import comb, exp
from random import Random

COUNT = [0]
def require(condition, text):
    COUNT[0] += 1
    if not condition:
        raise AssertionError(text)


def transitions(a, b, h, weight):
    """Transitions (rate, next state, bridge increment) from vacancy counts."""
    rows = []
    for x, y, is_a in ((a, b, True), (b, a, False)):
        if x < 2:
            continue
        for j in range(3):
            if j > h or 2-j > x-h:
                continue
            rate = Fraction(comb(h, j)*comb(x-h, 2-j))
            if rate:
                state = (x-2, y, h-j) if is_a else (y, x-2, h-j)
                rows.append((rate, state, 0))
    if h:
        rows.append((weight*h, (a-1,b-1,h-1), 1))
    return rows


def exact_pgf(n, weight):
    @lru_cache(None)
    def solve(a,b,h):
        moves=transitions(a,b,h,weight)
        if not moves:
            require(a <= 1 and b <= 1, 'terminal maximality')
            return (Fraction(1),)
        total=sum((r for r,_,_ in moves), Fraction(0))
        coeff=[]
        for rate,state,extra in moves:
            sub=solve(*state)
            while len(coeff) < len(sub)+extra:
                coeff.append(Fraction(0))
            for j,v in enumerate(sub):
                coeff[j+extra]+=rate*v/total
        return tuple(coeff)
    return solve(n,n,n)


def F(a,b,h):
    return Fraction(h,a)+Fraction(h,b) if a and b else Fraction(0)


def check_generator():
    for lam in (Fraction(1,4),Fraction(1,2),Fraction(1),Fraction(3)):
        c=min(Fraction(1),2*lam)
        for a in range(1,16):
            for b in range(1,16):
                for h in range(1,min(a,b)+1):
                    drift=sum((rate*(F(*state)-F(a,b,h)) for rate,state,_ in transitions(a,b,h,lam)),Fraction(0))
                    require(-drift >= c*h, f'Lyapunov drift {a,b,h,lam}')
    print('Lyapunov generator inequality verified for all finite test states.')


def sample_exact_process(n, weight, rng):
    va=list(range(n)); vb=list(range(n)); bridge=0
    while True:
        h=sum(x in set(vb) for x in va)
        ra=len(va)*(len(va)-1)/2
        rb=len(vb)*(len(vb)-1)/2
        total=ra+rb+weight*h
        if total == 0: break
        z=rng.random()*total
        if z<ra:
            i,j=rng.sample(va,2); va.remove(i); va.remove(j)
        elif z<ra+rb:
            i,j=rng.sample(vb,2); vb.remove(i); vb.remove(j)
        else:
            common=list(set(va)&set(vb)); i=rng.choice(common)
            va.remove(i); vb.remove(i); bridge+=1
    require(len(va)+len(vb)==2*((n-bridge)%2), 'exact pathwise parity')
    return bridge


def main():
    check_generator()
    for lam in (Fraction(1,2),Fraction(1),Fraction(2)):
        for n in range(1,9):
            p=exact_pgf(n,lam)
            require(sum(p)==1,'normalization')
            require(all(v>=0 for v in p),'nonnegative')
            for k,v in enumerate(p):
                if v:
                    require(0<=k<=n,'bridge support')
            print('exact', n, str(lam), 'mean', float(sum(k*v for k,v in enumerate(p))))
    rng=Random(20261105)
    # Separate vertex-label simulation, not recurrence simulation.
    for n in (3,4,5):
        lam=Fraction(1,2)
        p=exact_pgf(n,lam)
        trials=1500
        hits=[0]*(n+1)
        for _ in range(trials):
            hits[sample_exact_process(n,float(lam),rng)]+=1
        for k in range(n+1):
            require(abs(hits[k]/trials-float(p[k]))<0.05, 'independent simulation vs exact DP')
    # Fixed lambda Poisson predictions, checked only numerically; proof is analytic.
    lam=0.8
    n=120
    reps=500
    xs=[sample_exact_process(n,lam,rng) for _ in range(reps)]
    mean=sum(xs)/reps
    p_odd=sum(x%2 for x in xs)/reps
    require(abs(mean-lam)<0.25,'bridge Poisson mean diagnostic')
    require(abs(p_odd-(1-exp(-2*lam))/2)<0.10,'Poisson parity diagnostic')
    print('large-n diagnostics', n, reps, 'mean',mean, 'P odd',p_odd)
    print('PASS',COUNT[0], 'checks')

if __name__=='__main__': main()
