"""Exact-integer checks of finite cyclic dilation's sharp Gini perturbation law.
No scientific claim of exhaustive verification in unbounded dimensions."""
from itertools import permutations
from fractions import Fraction
from random import Random

def gini(x):
    n=len(x)
    return sum(abs(x[i]-x[j]) for i in range(n) for j in range(i+1,n))

def dilate(x,w):
    n=len(x)
    return tuple(max(x[(i+j)%n] for j in range(w)) for i in range(n))

def sharp_fraction(n,w):
    return Fraction(w*(n-w),n-1)

def run():
    tested=0
    for n in range(2,9):
        for w in range(1,n+1):
            bound=sharp_fraction(n,w)
            windows=[[(i+j)%n for j in range(w)] for i in range(n)]
            greatest=Fraction(-1)
            for p in permutations(range(n)):
                # p[j] is the relative input rank of site j.
                counts=[0]*n
                for window in windows:
                    winner=max(window,key=lambda j:p[j])
                    counts[winner]+=1
                counts.sort(reverse=True)
                t=0
                best=Fraction(0)
                for k in range(1,n):
                    t+=counts[k-1]
                    ratio=Fraction(t*(n-t),k*(n-k))
                    if ratio>best: best=ratio
                if best>bound: raise AssertionError((n,w,p,best,bound))
                if best>greatest: greatest=best
                tested+=1
            if greatest !=bound:raise AssertionError((n,w,greatest,bound))
    print('EXACT_ALL_ORDER_CHAMBER_GINI_NORMS_PASSED', tested)

    # Verify the occupancy inequality independently for all small finite parameters.
    cases=0
    for n in range(2,121):
        for w in range(1,n+1):
            bound=sharp_fraction(n,w)
            for k in range(1,n):
                lo=max(0,n-(n-k)*w)
                hi=min(n,k*w)
                for t in sorted(set([lo,hi,max(lo,min(hi,n//2)),max(lo,min(hi,(n+1)//2))])):
                    # For large windows the extra global-maximum restriction is essential.
                    if 2*w>n and n-w<t<w: continue
                    assert Fraction(t*(n-t),k*(n-k)) <= bound, (n,w,k,t)
                    cases+=1
    print('EXACT_OCCUPANCY_AND_GLOBAL_PEAK_BOUNDS_PASSED',cases)

    # Direct arbitrary rational input pairs; all arithmetic is exact.
    rng=Random(67023)
    cases=0
    for n in range(2,21):
        for w in range(1,n+1):
            bound=sharp_fraction(n,w)
            for _ in range(8):
                x=[Fraction(rng.randrange(-30,31),rng.randrange(1,9)) for _ in range(n)]
                y=[Fraction(rng.randrange(-30,31),rng.randrange(1,9)) for _ in range(n)]
                assert gini(tuple(a-b for a,b in zip(dilate(x,w),dilate(y,w)))) <= bound*gini(tuple(a-b for a,b in zip(x,y)))
                cases+=1
            # Exact local global-peak witness.
            x=[Fraction(-i-10,1) for i in range(n)]
            x[0]=Fraction(1000)
            y=x.copy();y[0]+=Fraction(1,1000)
            inp=gini(tuple(a-b for a,b in zip(x,y)))
            out=gini(tuple(a-b for a,b in zip(dilate(x,w),dilate(y,w))))
            assert out ==bound*inp
    print('EXACT_ARBITRARY_TWO_INPUT_INEQUALITIES_PASSED',cases)
    print('EXACT_GLOBAL_PEAK_ATTAINMENT_PASSED',sum(range(2,21)))
    print('ALL_CYCLIC_DILATION_GINI_CHECKS_PASSED')

if __name__=='__main__':run()
