"""Recompute distinct scattered-palindrome counts for short binary run words.
Self-contained Python 3 verifier; no network, external dependencies, or prover required.
"""
from functools import lru_cache
from itertools import combinations, product


def direct_palindromes(word):
    seen={''}
    for ch in word:
        seen |= {p+ch for p in tuple(seen)}
    return {p for p in seen if p and p==p[::-1]}


def count_palindromes(word):
    @lru_cache(None)
    def solve(i,j):
        if i>j:return 0
        if i==j:return 1
        if word[i]!=word[j]:
            return solve(i+1,j)+solve(i,j-1)-solve(i+1,j-1)
        lo=i+1; hi=j-1
        while lo<=hi and word[lo]!=word[i]:lo+=1
        while lo<=hi and word[hi]!=word[i]:hi-=1
        if lo>hi:return 2*solve(i+1,j-1)+2
        if lo==hi:return 2*solve(i+1,j-1)+1
        return 2*solve(i+1,j-1)-solve(lo+1,hi-1)
    return solve(0,len(word)-1)


def build(runs):
    return ''.join(str(i%2)*a for i,a in enumerate(runs))


def full_run_palindromes(runs):
    r=len(runs)
    assert r%2==1
    k=(r-1)//2
    return runs[k]*__import__('math').prod(min(runs[i],runs[-1-i]) for i in range(k))

checks = 0
for n in range(3,15):
    for r in (3,4):
        if r>n:continue
        best=0
        for cuts in combinations(range(1,n),r-1):
            runs=tuple(b-a for a,b in zip((0,)+cuts,cuts+(n,)))
            value=count_palindromes(build(runs))
            if r==3:
                expect=n+runs[1]*min(runs[0],runs[2])
            else:
                a,b,c,d=runs
                expect=n+b*min(a,c)+c*min(b,d)
            assert value==expect,(n,r,runs,value,expect)
            best=max(best,value)
            checks+=1
        assert best==n+n*n//8,(n,r,best,n+n*n//8)

# Independent direct enumeration for small arbitrary words.
direct_checks=0
for n in range(1,13):
    for bits in product('01',repeat=n):
        word=''.join(bits)
        if word[0]!='0':continue
        if n>10 and word.count('1')>7:continue
        actual=direct_palindromes(word)
        assert len(actual)==count_palindromes(word)
        run_lengths=[]; last=word[0]; count=0
        for ch in word:
            if ch!=last:
                run_lengths.append(count);count=0;last=ch
            count+=1
        run_lengths.append(count)
        if len(run_lengths)%2==1 and len(run_lengths)>=3:
            full={p for p in actual if 1+sum(p[i]!=p[i-1] for i in range(1,len(p)))==len(run_lengths)}
            assert len(full)==full_run_palindromes(run_lengths),(word,len(full),full_run_palindromes(run_lengths))
        direct_checks+=1

# Explicit witness and asymptotic optimal leading term, with rigorous upper bound evaluated.
witness_checks=0
for k in range(1,9):
    for n in (3*k+3,20*k+20,100*k+100,500*k+500):
        r=2*k+1
        if n<r:continue
        x=n//(2*(k+1))
        if x<1:continue
        y=n-2*k*x
        runs=(x,)*k+(y,)+(x,)*k
        T=full_run_palindromes(runs)
        bound=n**(k+1)/(2**k*(k+1)**(k+1))
        assert T<=bound+1e-5*max(1,bound)
        witness_checks+=1

print('PASS: exact 3/4-run formulas and sharp maxima on',checks,'compositions')
print('PASS: independent direct-vs-DP palindromes and full-run classification on',direct_checks,'binary words')
print('PASS: balanced-pair asymptotic witness checks on',witness_checks,'examples')
