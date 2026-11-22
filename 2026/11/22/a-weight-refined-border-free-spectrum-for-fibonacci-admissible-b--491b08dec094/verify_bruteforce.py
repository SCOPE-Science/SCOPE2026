"""Direct exhaustive test for unbordered words in the golden-mean language.

Usage: python verify_bruteforce.py
"""
from collections import Counter
from functools import lru_cache

@lru_cache(None)
def fib_words(n):
    if n == 0:
        return ('',)
    if n == 1:
        return ('0', '1')
    return tuple('0' + w for w in fib_words(n-1)) + tuple('10' + w for w in fib_words(n-2))

def independently_unbordered(s):
    return all(s[:j] != s[len(s)-j:] for j in range(1, len(s)))

def dict_sum(a,b):
    out=Counter(a)
    for k,v in b.items():out[k]+=v
    return +out

def recurrence(maxn):
    # Exact weight-polynomial coefficient counts from the refined Mahler equation.
    U=[Counter() for _ in range(maxn+1)]
    U[1]=Counter({0:1,1:1})
    # (1-z-tz^2)U(z,t) + U(z^2,t^2) = (1+t)z+t(1+t)z^2(1-z).
    for n in range(2,maxn+1):
        v=Counter(U[n-1])
        if n>=3:
            for j,c in U[n-2].items():v[j+1]+=c
        if n==2:
            v[1]+=1;v[2]+=1
        if n==3:
            v[1]-=1;v[2]-=1
        if n%2==0:
            for j,c in U[n//2].items():v[2*j]-=c
        U[n]=+v
    return U

def main():
    maxn=21
    U=recurrence(maxn)
    for n in range(1,maxn+1):
        words=fib_words(n)
        check=Counter(s.count('1') for s in words if independently_unbordered(s))
        assert check == U[n], (n, check, U[n])
        assert len(words) == len(fib_words(n-1))+len(fib_words(n-2)) if n>=2 else True
        print(f'n={n:2d} admissible={len(words):6d} unbordered={sum(check.values()):6d} weight_coeffs={sorted(check.items())}')
    print('PASS direct enumeration and the weight-refined Mahler recurrence, lengths 1..21')
if __name__=='__main__':main()
