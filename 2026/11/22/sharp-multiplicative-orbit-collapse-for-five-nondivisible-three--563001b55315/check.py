#!/usr/bin/env python3
"""Independent finite checks for five-adic nondivisibility under small multipliers."""

def digit_ok(n):
    assert n >= 0
    pos=0
    while n:
        d=n%5
        if d > (3 if pos%2==0 else 1): return False
        n//=5;pos+=1
    return True

def pair_language(n,m):
    assert m in (2,3)
    alphabet = (0,1,3) if m==2 else (0,1,2)
    while n:
        if n%25 not in alphabet: return False
        n//=25
    return True

def check():
    asserts=0
    max_n=9*5**6
    val=[0]*(max_n+1)
    def v5(x):
        v=0
        while x and x%5==0:
            x//=5;v+=1
        return v
    # v_5(c(n,3)) difference from (n)c(n)=3(3n-2)c(n-1).
    for n in range(1,max_n+1):
        val[n]=val[n-1]+v5(3*n-2)-v5(n)
        assert val[n]>=0
        asserts+=1
    for n in range(0,5**6):
        for m in (1,2,3,4,9):
            assert (val[m*n]==0)==digit_ok(m*n)
            asserts+=1
        for m in (2,3):
            assert (digit_ok(n) and digit_ok(m*n)) == pair_language(n,m)
            assert not (n>0 and digit_ok(n) and digit_ok(m*n) and digit_ok(m*m*n))
            asserts+=2
    for r in range(0,4):
        for m in (2,3):
            actual=sum(digit_ok(n) and digit_ok(m*n) for n in range(25**r))
            assert actual==3**r,(m,r,actual)
            asserts+=1
    assert digit_ok(2) and digit_ok(8) and digit_ok(32)
    asserts+=1
    # Each pair transition starts without a carry at an even position and finishes without a carry.
    for m,alphabet in ((2,(0,1,3)),(3,(0,1,2))):
        for a in range(4):
            for b in range(2):
                low=m*a
                next_digit=m*b+low//5
                admissible=low%5<=3 and next_digit%5<=1
                assert admissible==(b==0 and a in alphabet)
                asserts+=1
    print('PASS:',asserts,'independent exact assertions; pair counts at depths r=0,1,2,3; triples absent for n<15625; witness n=2 for ratio 4')

if __name__=='__main__':check()
