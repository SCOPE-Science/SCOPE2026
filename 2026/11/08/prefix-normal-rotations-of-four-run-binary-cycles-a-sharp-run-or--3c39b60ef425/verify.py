"""Reproducibility checks for prefix-normal rotations of four-run binary cycles.

Run with Python 3.9+: python verify.py
The mathematical proof is independent of these finite computations.
"""
from itertools import product
from random import Random


def stats(w):
    length = len(w)
    doubled = w + w
    prefix = [0]
    for ch in doubled:
        prefix.append(prefix[-1] + (ch == "1"))
    maximum = [max(prefix[s + k] - prefix[s] for s in range(length))
               for k in range(1, length + 1)]
    defects = []
    for s in range(length):
        defects.append(max(maximum[k-1] - (prefix[s+k]-prefix[s])
                           for k in range(1, length+1)))
    return maximum, defects


def word(a,b,c,d):
    return "1"*a + "0"*b + "1"*c + "0"*d


def predicted_start_defect(a,b,c,d):
    assert a>=c
    return min(c,max(0,b-d))


def count_by_parameters(n):
    success, failure = 0, 0
    for a in range(1,n-2):
        for b in range(1,n-a-1):
            for c in range(1,n-a-b):
                d=n-a-b-c
                if d<1: continue
                if (a-c)*(b-d)<=0:
                    if a>=c and b<=d: success+=1
                else:
                    if a>c and b>d: failure+=1
    return success,failure


def series_count(n,failed=False):
    # Coefficients of z^(4+2*failed) / ((1-z)^2(1-z^2)^2).
    k=n-4-2*failed
    if k<0: return 0
    return sum((j+1)*(k-2*j+1) for j in range(k//2+1))


def main():
    tested=0
    for a,b,c,d in product(range(1,8),repeat=4):
        w=word(a,b,c,d)
        M, defects=stats(w)
        assert len(M)==len(w)
        if a>=c:
            assert defects[0]==predicted_start_defect(a,b,c,d),(a,b,c,d,defects[0])
        assert (min(defects)==0)==((a-c)*(b-d)<=0),(a,b,c,d,defects)
        distinct_normal={w[i:]+w[:i] for i,delta in enumerate(defects) if delta==0}
        assert len(distinct_normal)==int((a-c)*(b-d)<=0)
        if a>=c:
            assert max(M[a+b-1]-(a),0)==predicted_start_defect(a,b,c,d)
        tested+=1

    for n in range(4,36):
        actual=count_by_parameters(n)
        expected=(series_count(n),series_count(n,True))
        assert actual==expected,(n,actual,expected)
        assert actual[1]==series_count(n-2)

    rng=Random(20261107)
    larger=0
    for _ in range(650):
        a,b,c,d=(rng.randrange(1,51) for _ in range(4))
        M,defects=stats(word(a,b,c,d))
        if a>=c:
            assert defects[0]==predicted_start_defect(a,b,c,d)
        else:
            assert defects[a+b]==predicted_start_defect(c,d,a,b)
        assert (min(defects)==0)==((a-c)*(b-d)<=0)
        larger+=1
    print("VERIFY_OK: exhaustive quadruples",tested,
          "; larger seeded quadruples",larger,
          "; all 32 length-specific necklace counts")


if __name__=="__main__":
    main()
