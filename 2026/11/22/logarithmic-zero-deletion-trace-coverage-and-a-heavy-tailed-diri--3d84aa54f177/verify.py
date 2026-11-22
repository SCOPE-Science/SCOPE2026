"""Verify exact fixed-composition conditional deletion cover-time identities."""
from itertools import combinations
from fractions import Fraction
from math import comb, log

def mean_from_words(n, k):
    # Source words are all equally likely. Compute deletion strings literally.
    total = Fraction(0)
    for ones in combinations(range(n), k):
        word = ['1' if j in ones else '0' for j in range(n)]
        counts = {}
        for i, letter in enumerate(word):
            if letter == '0':
                key = ''.join(word[:i] + word[i+1:])
                counts[key] = counts.get(key, 0) + 1
        weights = list(counts.values())
        v = Fraction(0)
        for size in range(1, len(weights)+1):
            for group in combinations(weights, size):
                v += (-1)**(size+1) * Fraction(n-k, sum(group))
        total += v
    return total / comb(n,k)

def mean_closed(n,k):
    m = k+1
    N = n-k
    denom = comb(N+m-1,m-1)
    ans = Fraction(0)
    for s in range(1,m+1):
        a = Fraction(0)
        for t in range(s,N+1):
            if s == m:
                c = comb(N-1,m-1) if t == N and N >= m else 0
            else:
                c = comb(t-1,s-1) * comb(N-t+m-s-1,m-s-1)
            a += Fraction(c,t)
        ans += (-1)**(s+1) * comb(m,s) * a
    return N * ans / denom

def finite_tail_from_words(n,k,t):
    total = Fraction(0)
    for ones in combinations(range(n),k):
        word=['1' if i in ones else '0' for i in range(n)]
        counts={}
        for j,x in enumerate(word):
            if x=='0':
                y=''.join(word[:j]+word[j+1:])
                counts[y]=counts.get(y,0)+1
        vals=list(counts.values())
        q=Fraction(0)
        for s in range(1,len(vals)+1):
            for subset in combinations(vals,s):
                q+=(-1)**(s+1)*Fraction(n-k-sum(subset),n-k)**t
        total+=q
    return total / comb(n,k)

def limit_tail(m,t):
    if t==0: return Fraction(1)
    if t<m: return Fraction(1)
    return Fraction(1)-Fraction(comb(t-1,m-1),comb(t+m-1,m-1))

def asymptotic_mean(n,k):
    m=k+1
    h=lambda q: sum(1/j for j in range(1,q+1))
    return (m*(m-1)*(log(n-k)+0.5772156649015328606-h(m-2))
           +(m-1)*(m-1-m*h(m-1)))

def main():
    checked=0
    for k in (1,2,3):
        for n in range(k+1, min(k+9,13)):
            a,b=mean_from_words(n,k),mean_closed(n,k)
            assert a==b,(n,k,a,b)
            checked+=comb(n,k)
    for n in (2,3,5,8,13):
        if n<2:continue
        exact=mean_closed(n,1)
        N=n-1
        special=Fraction(2*N, N+1)*sum((Fraction(1,j) for j in range(1,N+1)),Fraction(0))-Fraction(N-1,N+1)
        assert exact==special,(n,exact,special)
    # Independent inclusion-exclusion survival checks, including zero-gap cases.
    for k,n in ((1,7),(2,8),(3,9)):
        for t in range(1,7):
            x=finite_tail_from_words(n,k,t)
            assert 0<=x<=1,(k,n,t,x)
    # Two independent derivations of limiting tails: beta moments and uniform compositions.
    for m in range(2,7):
        for t in range(1,16):
            s=Fraction(0)
            for q in range(1,m+1):
                rise=lambda a,t:__import__('math').prod(a+i for i in range(t))
                s+=(-1)**(q+1)*comb(m,q)*Fraction(rise(m-q,t),rise(m,t))
            assert s==limit_tail(m,t),(m,t,s,limit_tail(m,t))
    for k in (1,2,3):
        diffs=[abs(float(mean_closed(n,k))-asymptotic_mean(n,k)) for n in (100,1000)]
        assert diffs[1]<diffs[0],(k,diffs)
    print('VERIFY_OK', 'literal_source_words',checked,'independent_tail_identities',5*15)

if __name__=='__main__':main()
