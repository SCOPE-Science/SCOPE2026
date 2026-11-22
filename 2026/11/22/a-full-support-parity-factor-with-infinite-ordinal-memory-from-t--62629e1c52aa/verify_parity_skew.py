"""Independent rational interval-cylinder checker for a parity-coded skew tent product.

Public reproducibility: python3 verify_parity_skew.py (standard library only).
"""
from fractions import Fraction as F
from itertools import product


def measure_word(c, word):
    """Exact Lebesgue measure of an up/down comparison word via inverse intervals."""
    u=1/(2-c)
    segments=[(F(0),F(1))]
    for bit in reversed(word):
        lo,hi=(F(0),u) if bit else (u,F(1))
        newer=[]
        for left,right in segments:
            for l,r in ((c*left,c*right),(1-(1-c)*right,1-(1-c)*left)):
                l=max(l,lo);r=min(r,hi)
                if l<r: newer.append((l,r))
        segments=newer
    return sum((r-l for l,r in segments),F(0))


def formula(c,d,n):
    a=1-c;b=1-d;den=(2-c)*(2-d)
    v=(F(1),F(1))
    # row (ab,1) times Q^(n-1), Q=( (0,1),(ab,cd) )
    w=(a*b,F(1))
    for i in range(n-1):
        w=(w[1]*a*b,w[0]+w[1]*c*d)
    return (w[0]+w[1])/den


def main():
    cases=[(F(1,2),F(1,2)),(F(1,3),F(2,3)),(F(1,4),F(3,5)),(F(3,7),F(4,9))]
    counts=0
    for c,d in cases:
        a=1-c;b=1-d;D=(2-c)*(2-d)
        Fs=[]
        for n in range(1,9):
            direct=sum((measure_word(c,w)*measure_word(d,w) for w in product((0,1),repeat=n)),F(0))
            expected=formula(c,d,n)
            assert direct==expected,(c,d,n,direct,expected)
            counts+=1
            Fs.append(expected)
        for i in range(len(Fs)-2):
            n=i+1
            defect=Fs[i]*Fs[i+2]-Fs[i+1]**2
            rhs=(a*b*(c+d-2*c*d)**2/D**2)*(-a*b)**(n-1)
            assert defect==rhs,(c,d,n,defect,rhs)
            assert defect!=0
            counts+=2
        assert Fs[1]==(2*a*b+c*d)/D
        counts+=1
    print(f'PASS: {counts} exact rational interval / recurrence / defect checks across {len(cases)} parameter pairs, lengths through 8.')

if __name__=='__main__': main()
