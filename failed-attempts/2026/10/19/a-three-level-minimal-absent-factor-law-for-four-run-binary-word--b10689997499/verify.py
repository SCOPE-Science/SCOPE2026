"""Independent finite checks of minimal absent contiguous factors for four-run binary words.

No finite enumeration is used as a proof of the parameter-uniform classification.
"""
from itertools import product


def predicted(a,b,c,d):
    assert min(a,b,c,d)>=1
    ans={'0'*(max(a,c)+1), '1'*(max(b,d)+1)}
    ans.update('0'+'1'*j+'0' for j in range(1,b))
    ans.update('1'+'0'*j+'1' for j in range(1,c))
    if d>b: ans.add('1'*(b+1)+'0')
    if a>c: ans.add('1'+'0'*(c+1))
    if c>a and d>=b: ans.add('0'*(a+1)+'1'*b+'0')
    if a>=c and d>=b: ans.add('1'+'0'*c+'1'*b+'0')
    if a>c and d>b: ans.add('0'*(c+1)+'1'*(b+1))
    if c>a and b>d: ans.add('0'*(a+1)+'1'*(d+1))
    if a>=c and b>d: ans.add('1'+'0'*c+'1'*(d+1))
    return ans


def overlap_enumeration(w):
    """Enumerate every MAW via intersecting length-(k-1) factor contexts."""
    n=len(w)
    factors={j:{w[i:i+j] for i in range(n-j+1)} for j in range(n+1)}
    ans=set()
    for length in range(2,n+2):
        prior=factors[length-1]
        by_first={}
        for f in prior: by_first.setdefault(f[:-1],set()).add(f[-1])
        for p in prior:
            for last in by_first.get(p[1:],()):
                candidate=p+last
                if candidate not in factors.get(length,set()): ans.add(candidate)
    return ans


def direct_enumeration(w):
    """Check each binary candidate separately, without using factor overlap."""
    ans=set();n=len(w)
    for length in range(2,n+2):
        for tup in product('01',repeat=length):
            s=''.join(tup)
            if s not in w and s[:-1] in w and s[1:] in w: ans.add(s)
    return ans


def run_checks():
    total=0
    for a,b,c,d in product(range(1,8),repeat=4):
        w='0'*a+'1'*b+'0'*c+'1'*d
        got=overlap_enumeration(w)
        want=predicted(a,b,c,d)
        assert got==want, (a,b,c,d,got-want,want-got)
        assert len(got)==b+c+2**((a>c)+(d>b)),(a,b,c,d)
        total+=1
    direct=0
    for a,b,c,d in product(range(1,7),repeat=4):
        if a+b+c+d>11:continue
        w='0'*a+'1'*b+'0'*c+'1'*d
        assert direct_enumeration(w)==predicted(a,b,c,d),(a,b,c,d)
        direct+=1
    import random
    rng=random.Random(20221016)
    for i in range(200):
        a,b,c,d=(rng.randrange(1,16) for j in range(4))
        w='0'*a+'1'*b+'0'*c+'1'*d
        assert predicted(a,b,c,d)==overlap_enumeration(w),(a,b,c,d)
    print('FOUR_RUN_MAW_ALL_CHECKS_PASSED exhaustive_parameters=%d direct_word_checks=%d additional_fixed_seed_cases=200'%(total,direct))

if __name__=='__main__':run_checks()
