"""Reproduce frozen-star-swap counts of proper words. Python 3 standard library only.

A word is proper when consecutive symbols differ. A star swap exchanges
position zero and one later position; a word is frozen if no nontrivial
star swap keeps it proper. This verifier uses exact integer arithmetic.
"""
from collections import Counter, defaultdict
from itertools import product
from math import comb


def is_frozen(word):
    n = len(word)
    assert n >= 3
    assert all(word[i] != word[i + 1] for i in range(n - 1))
    for j in range(1, n):
        if word[j] == word[0]:
            continue
        other = list(word)
        other[0], other[j] = other[j], other[0]
        if all(other[i] != other[i + 1] for i in range(n - 1)):
            return False
    return True


def brute_histogram(q, n):
    histogram = Counter()
    for word in product(range(q), repeat=n):
        if any(word[i] == word[i + 1] for i in range(n - 1)):
            continue
        if is_frozen(word):
            histogram[tuple(word.count(i) for i in range(q))] += 1
    return histogram


def grammar_histogram(q, n):
    """Coefficient extraction from the rational composition enumerator."""
    ans = Counter()
    for a in range(q):
        for b in range(q):
            if a == b:
                continue
            cset = [c for c in range(q) if c not in (a, b)]
            others = [c for c in range(q) if c != a]
            # Each block follows one 'a' and ends at the next 'a'.
            blocks = [(x, a) for x in others]
            blocks += [(x, y, a) for x in others for y in others if x != y]
            blocks += [(x, b, y, a) for x in cset for y in cset]
            # Tail has no 'a'.
            tails = [()] + [(x,) for x in others] + [(x, b) for x in cset]
            states = {(a, b, a): 1}
            # Index states by complete word here; this is an independent
            # combinatorial expansion of the multivariate rational series.
            frontier = { (a,b,a): 1 }
            while frontier:
                nxt = {}
                for word, mult in frontier.items():
                    if len(word) > n:
                        continue
                    for t in tails:
                        if len(word)+len(t) == n:
                            full = word+t
                            ans[tuple(full.count(k) for k in range(q))] += mult
                    for block in blocks:
                        v=word+block
                        if len(v)<=n:
                            nxt[v]=nxt.get(v,0)+mult
                frontier=nxt
    return ans


def formula_total(q, max_n):
    # F(z) = q(q-1) z^3 [1+(q-2)z] /
    #        [1-z-(q-2)z^2-(q-2)^2 z^3].
    f=[0]*(max_n+1)
    b=q-2
    for n in range(3,max_n+1):
        f[n]=(f[n-1] if n>=1 else 0)
        if n>=2: f[n]+=b*f[n-2]
        if n>=3: f[n]+=b*b*f[n-3]
        if n==3: f[n]+=q*(q-1)
        if n==4: f[n]+=q*(q-1)*b
    return f


def check():
    checks=0
    for q,top in [(2,9),(3,10),(4,8),(5,7)]:
        totals=formula_total(q,top)
        for n in range(3,top+1):
            brute=brute_histogram(q,n)
            from_series=grammar_histogram(q,n)
            assert brute==from_series, (q,n,brute-from_series,from_series-brute)
            assert sum(brute.values())==totals[n],(q,n,brute,totals[n])
            checks+=1
    # Sharp ternary equal-composition threshold and exact initial counts.
    for m,expected in [(1,0),(2,0),(3,6),(4,30),(5,126),(6,504)]:
        # Gram formula is evaluated at length 3m without exponential search.
        if m==1:
            value=0
        else:
            B = {(1,0):1,(0,1):1,(1,1):2,(1,2):1}
            T = {(0,0):1,(1,0):1,(0,1):1,(1,1):1}
            p={(0,0):1}
            for _ in range(m-2):
                d=defaultdict(int)
                for (i,j),v in p.items():
                    for (x,y),w in B.items(): d[i+x,j+y]+=v*w
                p=dict(d)
            value=6*sum(v*p.get((m-1-i,m-j),0) for (i,j),v in T.items())
        assert value==expected,(m,value,expected)
        assert value==(6*comb(2*m-3,m) if m>=2 else 0)
    # Balanced ternary constructive family.
    for m in range(3,25):
        a,b,c=0,1,2
        word=(a,b,a,c,b,c,a)+((c,b,a)*(m-3))+(c,b)
        assert len(word)==3*m
        assert all(word.count(i)==m for i in range(3))
        assert is_frozen(word)
    print('PASS: %d brute/series/composition cases, exact recurrence, 6 balanced coefficients, 22 constructive lengths'%checks)

if __name__=='__main__': check()
