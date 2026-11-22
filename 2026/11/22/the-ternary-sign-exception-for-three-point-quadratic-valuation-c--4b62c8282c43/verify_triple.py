"""Direct integer test of a three-point valuation law; requires only Python 3."""
from collections import Counter

def valuation_clipped(a, p, k):
    j = 0
    while j < k and a % p == 0:
        j += 1
        a //= p
    return j

def expected_counts(p, s, k):
    z = Counter({(0, 0, 0): (p-2) * p**(k-1)})
    for j in range(1, min(s, k)):
        z[(j, j, j)] += 2*(p-1)*p**(k-j-1)
    if k <= s:
        z[(k, k, k)] += 2
    else:
        z[(s, s, s)] += 2*(p-3)*p**(k-s-1)
        for j in range(s+1, k+1):
            cnt = 2*(p-1)*p**(k-j-1) if j < k else 2
            for a in range(3):
                vals = [s, s, s]
                vals[a] = j
                z[tuple(vals)] += cnt
    return +z

def observed_counts(p, s, k, c):
    offsets = (0, p**s, 2*p**s)
    d=Counter()
    for n in range(p**k):
        d[tuple(valuation_clipped((n+h)*(n+h+1)+c,p,k) for h in offsets)] += 1
    return d

def run():
    tests = obs = 0
    for p in (3,5,7,11,13):
        for k in range(1,7):
            if p**k > 65000: continue
            for s in (1,2,3,4):
                for c in (p,2*p,p*p,5*p*p):
                    exp=expected_counts(p,s,k)
                    seen=observed_counts(p,s,k,c)
                    if exp!=seen:
                        print('FAIL',p,s,k,c,'excess observed',seen-exp,'missing',exp-seen)
                        raise SystemExit(1)
                    if sum(exp.values())!=p**k:
                        raise SystemExit('mass discrepancy')
                    tests+=1; obs+=p**k
    print('PASS',tests,'complete histograms;',obs,'index triples')

if __name__=='__main__':
    run()
