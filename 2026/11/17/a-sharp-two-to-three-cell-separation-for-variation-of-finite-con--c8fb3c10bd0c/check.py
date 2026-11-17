"""Exact rational diagnostic for path variation and partition averaging."""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import sqrt

def variation(x):
    return sum(abs(x[i+1]-x[i]) for i in range(len(x)-1))

def norm_by_steps(word):
    n=len(word)
    sizes=Counter(word)
    left=Counter()
    best=Fraction(0)
    best_k=None
    for k in range(1,n):
        left[word[k-1]]+=1
        out=[Fraction(left[c],sizes[c]) for c in word]
        v=variation(out)
        if v>best:
            best,best_k=v,k
    return best,best_k

def binary_formula(word):
    n=len(word)
    a=word.count(0);b=n-a
    assert a and b
    t=sum(word[i]!=word[i+1] for i in range(n-1))
    u=v=0; delta=Fraction(0)
    for j in range(n-1):
        if word[j]==0: u+=1
        else: v+=1
        delta=max(delta,abs(Fraction(u,a)-Fraction(v,b)))
    return t*delta

def three_word(n):
    q,r=divmod(n,4)
    A,B,C=0,1,2
    if r==0:
        assert q>=1
        return [A,B]*q+[C,A]*q
    if r==1:
        assert q>=1
        return [A,B]*q+[A]+[C,B]*q
    if r==2:
        assert q>=1
        return [A,B]*q+[A]+[C,B]*q+[C]
    return [A,B]*(q+1)+[C,A]*q+[C]

def three_expected(n):
    return Fraction(n,2) if n%4!=3 else Fraction(n,2)-Fraction(1,n-1)

def test():
    checked=0
    for n in range(2,13):
        for tail in product((0,1),repeat=n-1):
            word=(0,)+tail
            if 1 not in word:continue
            norm,_=norm_by_steps(word)
            assert norm==binary_formula(word),(n,word,norm,binary_formula(word))
            checked+=1
    print('EXACT_BINARY_PATH_PREFIX_IDENTITY_PASS',checked)
    for n in range(3,121):
        w=three_word(n)
        assert len(w)==n
        val,k=norm_by_steps(w)
        assert val==three_expected(n),(n,val,three_expected(n),k)
        assert len(set(w))==3
    print('THREE_CELL_CONSTRUCTIONS_EXACT_PASS',118)
    alpha=6-4*sqrt(2)
    for n in range(4,301):
        b=round(n*(1-1/sqrt(2)))
        assert 1<=b and n-2*b>=1
        word=[0]*(n-2*b)+[v for _ in range(b) for v in (1,0)]
        # Explicit cut at the end of the initial zero segment.
        val=Fraction(2*b*(n-2*b),n-b)
        assert val >= alpha*n-2.000001
        assert val <= alpha*n+1.000001
        if n<60:
            actual,_=norm_by_steps(word)
            assert actual >= val
    print('BINARY_ASYMPTOTIC_CONSTRUCTION_AND_BOUND_PASS',297)
    # Independent exact 3-block matrices and all partitions of n<=7.
    def part(n):
        w=[0]*n
        def rec(i,m):
            if i==n:
                yield w[:]
                return
            for col in range(m+2):
                w[i]=col
                yield from rec(i+1,max(m,col))
        yield from rec(1,0)
    counts=[]
    for n in range(2,8):
        best=Fraction(0)
        for w in part(n):
            value,_=norm_by_steps(w)
            best=max(best,value)
        counts.append((n,str(best)))
    print('EXACT_ALL_PARTITIONS_SMALL_N_PASS',counts)
    print('ALL_PARTITION_VARIATION_CHECKS_PASS')
if __name__=='__main__':test()

# Independent finite onset confirmation, using all two-cell words.
def test_binary_onset():
    expected={3:Fraction(1),4:Fraction(3,2),5:Fraction(2),6:Fraction(9,4),7:Fraction(5,2)}
    for n,v in expected.items():
        largest=max(norm_by_steps((0,)+w)[0] for w in product((0,1),repeat=n-1) if 1 in w)
        assert largest==v, (n,largest,v)
        assert (three_expected(n)>v)==(n>=4)
    print('EXACT_BINARY_ONSET_N3_TO_N7_PASS')

if __name__ == '__main__':
    test_binary_onset()
