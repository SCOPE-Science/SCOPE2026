"""Reproduce finite tests for the median-anchored clipping variation theorem.
Standard library only. Exact rational arithmetic for exhaustive face checks/witnesses.
Finite tests supplement, and do not replace, the general proof.
"""
from fractions import Fraction as Q
from itertools import combinations
from random import Random


def med_center(x, theta=Q(1, 2)):
    n = len(x)
    s = sorted(x)
    if n % 2:
        return s[n // 2]
    return (1-theta)*s[n//2-1] + theta*s[n//2]


def clip_op(x, theta=Q(1, 2), tau=Q(1)):
    c = med_center(x,theta)
    return [min(c+tau,max(c-tau,u)) for u in x]


def variation(x):
    return sum(abs(b-a) for a,b in zip(x,x[1:]))


def proposed(n, theta=Q(1,2)):
    if n % 2: return Q(n-1)
    return max(Q(n-2), 1+Q(n-2)*max(theta,1-theta))


def face_exhaust(n, theta):
    best = Q(0)
    possible = [(i,) for i in range(n)] if n%2 else list(combinations(range(n),2))
    for mid in possible:
        for cut in range(n-1):
            h = [int(i>cut) for i in range(n)]
            c = Q(h[mid[0]]) if n%2 else (1-theta)*h[mid[0]]+theta*h[mid[1]]
            for mask in range(1<<n):
                v = [Q(h[i]) if mask>>i&1 else c for i in range(n)]
                best = max(best,variation(v))
    return best


def witness(n, theta=Q(1,2), which='split'):
    tau=Q(1)
    if n%2:
        median=(0,)
        cut=0
        unclipped={0}|{i for i in range(1,n) if i%2}
    elif which=='same':
        median=(0,1)
        cut=1
        unclipped={0,1}|{i for i in range(2,n) if i%2==0}
    else:
        # Arrange the lower/upper central rank in the spatial order that
        # maximizes the split-centre contrast.
        median=(0,1) if theta<=Q(1,2) else (1,0)
        cut=0
        unclipped={0,1}|{i for i in range(2,n) if i%2==1}
    x=[Q(0)]*n
    if n%2:
        x[0]=Q(0)
        others=list(range(1,n))
    else:
        low,high=median
        x[low]=-Q(1,50)
        x[high]=Q(1,50)
        others=[i for i in range(n) if i not in median]
    half=len(others)//2
    for k,i in enumerate(others):
        sign=-1 if k<half else 1
        magnitude=(Q(1,5)+Q(i,1000)) if i in unclipped else (Q(3)+Q(i,1000))
        x[i]=sign*magnitude
    # All positions in unclipped set should be strictly inside (c-tau,c+tau),
    # and all others strictly outside; the middle order positions are fixed.
    c=med_center(x,theta)
    for i in range(n):
        assert (abs(x[i]-c)<tau) == (i in unclipped), (n,i,x,c,unclipped)
    delta=Q(1,100000)
    h=[int(i>cut) for i in range(n)]
    y=[x[i]+delta*h[i] for i in range(n)]
    assert variation([y[i]-x[i] for i in range(n)])==delta
    z=[a-b for a,b in zip(clip_op(y,theta),clip_op(x,theta))]
    return variation(z)/delta


def main():
    trials=0
    for n in range(2,9):
        for t in ((Q(1,2),) if n%2 else (Q(0),Q(1,4),Q(1,2),Q(3,4),Q(1))):
            b=face_exhaust(n,t)
            assert b==proposed(n,t), (n,t,b,proposed(n,t))
            trials+=1
    print('ALL_PIECEWISE_AFFINE_FACE_MASKS_PASS',trials)
    witnesses=0
    for n in range(2,20):
        for t in ((Q(1,2),) if n%2 else (Q(0),Q(1,10),Q(1,4),Q(1,2),Q(3,4),Q(9,10),Q(1))):
            vals=[witness(n,t,choice) for choice in (('split','same') if n%2==0 and n>=4 else ('split',))]
            assert max(vals)==proposed(n,t),(n,t,vals,proposed(n,t))
            witnesses+=1
    print('EXACT_STRICT_MEDIAN_RANK_AND_CLIPPING_WITNESSES_PASS',witnesses)
    r=Random(44051)
    samples=0
    for n in range(2,29):
        for _ in range(50):
            t=Q(r.randrange(11),10)
            x=[Q(r.randrange(-1000,1001),100) for i in range(n)]
            y=[Q(r.randrange(-1000,1001),100) for i in range(n)]
            dx=[a-b for a,b in zip(x,y)]
            if variation(dx)==0:continue
            dy=[a-b for a,b in zip(clip_op(x,t),clip_op(y,t))]
            assert variation(dy)<=proposed(n,t)*variation(dx)
            assert variation(clip_op(x,t))<=variation(x)
            samples+=1
    print('RANDOM_RATIONAL_TWO_INPUT_AND_ONE_INPUT_STRESS_PASS',samples)
    print('MEDIAN_ANCHORED_CLIPPING_ALL_CHECKS_PASS')

if __name__=='__main__':main()
