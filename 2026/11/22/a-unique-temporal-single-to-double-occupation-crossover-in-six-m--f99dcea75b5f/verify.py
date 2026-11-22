#!/usr/bin/env python3
"""Standalone exact finite-state certificate for one-site sequential covering.

Usage: python3 rsc_hexamer_verifier.py
Needs Python 3 standard library only. Integer arithmetic is exact.
"""
from fractions import Fraction
from itertools import permutations
from math import factorial

EXPECTED = {
    2: [Fraction(0),Fraction(2,3),Fraction(1,3)],
    3: [Fraction(0),Fraction(173,315),Fraction(253,630),Fraction(31,630)],
    4: [Fraction(0),Fraction(617,1260),Fraction(10723,25200),Fraction(1007,12600),Fraction(41,8400)],
    5: [Fraction(0),Fraction(629,1386),Fraction(294797,675675),Fraction(76931,772200),Fraction(347,35100),Fraction(179,491400)],
    6: [Fraction(0),Fraction(38729,90090),Fraction(8026379,18162144),Fraction(10270963,90810720),Fraction(3667,258720),Fraction(559,635040),Fraction(19,873180)],
}


def incidence(k):
    starts=list(range(-2*(k-1), k))
    support=[sum(1 << (j+2*(k-1)) for j in range(s,s+k)) for s in starts]
    target=sum(1 << i for i,s in enumerate(starts) if -k+1 <= s <= 0)
    return starts,support,target


def backward(k):
    """Last-attempt recurrence: remove one element from an attempted subset."""
    starts,support,target=incidence(k)
    n=len(starts)
    dp=[[0]*(k+1) for _ in range(1<<n)]; dp[0][0]=1
    union=[0]*(1<<n)
    for mask in range(1,1<<n):
        b=mask&-mask
        union[mask]=union[mask^b] | support[b.bit_length()-1]
        rest=mask
        while rest:
            bit=rest&-rest; rest^=bit
            previous=mask^bit
            j=bit.bit_length()-1
            accepted=bool((bit&target) and (support[j]&union[previous]) != support[j])
            for m in range(k+1-int(accepted)):
                dp[mask][m+int(accepted)]+=dp[previous][m]
    return dp


def forward(k):
    """Independent first-to-last dynamic enumeration by adding each next attempt."""
    starts,support,target=incidence(k)
    n=len(starts); full=(1<<n)-1
    dp=[[0]*(k+1) for _ in range(1<<n)]; dp[0][0]=1
    union=[0]*(1<<n)
    for mask in range(1,1<<n):
        b=mask&-mask
        union[mask]=union[mask^b]|support[b.bit_length()-1]
    for mask in range(1<<n):
        unused=full^mask
        while unused:
            bit=unused&-unused; unused^=bit
            j=bit.bit_length()-1
            a=int(bool((bit&target) and (support[j]&union[mask]) != support[j]))
            row=dp[mask]; nxt=dp[mask|bit]
            for m in range(k+1-a):nxt[m+a]+=row[m]
    return dp


def brute(k):
    """Direct enumeration of chronological permutations (small cases only)."""
    starts,support,target=incidence(k)
    counts=[0]*(k+1)
    for order in permutations(range(len(starts))):
        covered=0; multiplicity=0
        for j in order:
            this=support[j]
            if covered&this!=this:
                if (1<<j)&target:multiplicity+=1
                covered|=this
        counts[multiplicity]+=1
    return counts


def finite_time(k,dp,q):
    n=3*k-2
    probs=[Fraction(0) for _ in range(k+1)]
    for mask,row in enumerate(dp):
        m=mask.bit_count()
        weight=q**m*(1-q)**(n-m)/factorial(m)
        for j,count in enumerate(row):probs[j]+=weight*count
    return probs


def dominance_coefficients(k, dp):
    """Coefficients of (1+x)^(3k-2)*(pi1-pi2), with x=q/(1-q)."""
    n=3*k-2
    counts=[0]*(n+1)
    for mask,row in enumerate(dp):
        counts[mask.bit_count()] += row[1]-row[2]
    return [Fraction(counts[m],factorial(m)) for m in range(n+1)]


def evaluate_coefficients(coeff,x):
    out=Fraction(0)
    for c in reversed(coeff):out=out*x+c
    return out


def main():
    checks=0
    for k in range(2,7):
        a=backward(k); b=forward(k)
        assert a[-1]==b[-1]; checks+=k+1
        n=3*k-2
        assert sum(a[-1]) == factorial(n); checks+=1
        probs=[Fraction(x,factorial(n)) for x in a[-1]]
        assert probs == EXPECTED[k]; checks+=k+1
        assert sum(probs)==1; checks+=1
        assert sum(j*p for j,p in enumerate(probs))==Fraction(2*k,k+1); checks+=1
        if k<=3:
            assert brute(k)==a[-1]; checks+=k+1
        coeff=dominance_coefficients(k,a)
        assert coeff[0]==0; checks+=1
        if k<=5:
            assert all(c>0 for c in coeff[1:]); checks+=n
        else:
            expected_signs=[1]*7+[-1]*9
            signs=[(c>0)-(c<0) for c in coeff[1:]]
            assert signs==expected_signs; checks+=16
            expected_scaled=[544864320,4086482400,14529715200,30648618000,
                             40774013280,33629732136,13788094320,-3565311750,
                             -10052042000,-8498073584,-4774499184,-1989374660,
                             -612115280,-131167560,-17489008,-1093063]
            assert [c*90810720 for c in coeff[1:]]==expected_scaled;checks+=16
            lo=Fraction(577764,1000000);hi=Fraction(577765,1000000)
            assert evaluate_coefficients(coeff,lo/(1-lo))>0; checks+=1
            assert evaluate_coefficients(coeff,hi/(1-hi))<0; checks+=1
            # Verify the displayed sixfold temporal polynomial by 17 exact
            # sample points; both sides have degree <=16 in z, so agreement
            # is a polynomial identity, not merely numerical interpolation.
            for iz in range(17):
                z=Fraction(iz,16); q=1-z
                lhs=finite_time(6,a,q)[6]
                coeffs=[76,456,1596,4256,9576,19152,20405,25740,28545,26950,18480]
                rhs=q**6*sum(Fraction(v)*z**j for j,v in enumerate(coeffs))/3492720
                assert lhs==rhs;checks+=1
        for q in [Fraction(0),Fraction(1,3),Fraction(1,2),Fraction(1)]:
            p=finite_time(k,a,q)
            assert sum(p)==1; checks+=1
            assert p[0]==(1-q)**k; checks+=1
            expected_mean=(Fraction(2*k,k+1)-k*(1-q)**k+Fraction(k*(k-1),k+1)*(1-q)**(k+1))
            assert sum(j*v for j,v in enumerate(p))==expected_mean; checks+=1
        print('k=',k,'n=',n,'counts=',a[-1],'terminal probabilities=',[str(p) for p in probs])
    print('PASS: '+str(checks)+' independent exact identity/group checks')


if __name__=='__main__':main()
