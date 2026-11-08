"""Reference arithmetic, independent of the exhaustive C++ implementation.

Uses Fraction-weighted carry transitions and direct binary digit calculations.
Run: python3 reference_check.py
"""
from fractions import Fraction
from itertools import product
from random import Random


def density(t):
    k=t.bit_count()
    states={(0,0): Fraction(1)}
    for i in range(t.bit_length()):
        next_states={}
        digit=(t>>i)&1
        for (carry, count), mass in states.items():
            for nbit in (0,1):
                new_carry=(carry+digit+nbit)//2
                new_count=count+new_carry
                if new_count<=k:
                    key=(new_carry,new_count)
                    next_states[key]=next_states.get(key,Fraction(0))+mass/2
        states=next_states
    result=Fraction(0)
    for (carry,count),mass in states.items():
        result+=mass if not carry else mass*(1-Fraction(1,2**(k-count+1)))
    return result


def from_gaps(gaps):
    n=1
    position=0
    for gap in gaps:
        position+=gap
        n+=1<<position
    return n


def main():
    table={
        1:(Fraction(3,4),[1]),
        2:(Fraction(5,8),[5]),
        3:(Fraction(19,32),[11,13]),
        4:(Fraction(73,128),[27]),
        5:(Fraction(9,16),[107]),
        6:(Fraction(567,1024),[219]),
        7:(Fraction(2239,4096),[439,475]),
        8:(Fraction(8839,16384),[951]),
    }
    checked=0
    for k in range(1,6):
        optimum=Fraction(2)
        minimizers=[]
        for gaps in product(range(1,k+2), repeat=k-1):
            t=from_gaps(gaps)
            c=density(t)
            checked+=1
            if c<optimum:
                optimum=c
                minimizers=[t]
            elif c==optimum:
                minimizers.append(t)
        want,ints=table[k]
        assert optimum==want and sorted(minimizers)==ints,(k,optimum,minimizers)
    print("INDEPENDENT_EXHAUSTION_OK k=1..5 count=",checked)

    rng=Random(105)
    long_gap_cases=0
    for k in range(2,9):
        for _ in range(30):
            gaps=[rng.randrange(1,k+14) for i in range(k-1)]
            small=[min(g,k+1) for g in gaps]
            assert density(from_gaps(gaps))==density(from_gaps(small))
            long_gap_cases+=1
    print("INDEPENDENT_GAP_COMPRESSION_OK random_cases=",long_gap_cases)
    for k,(want,ints) in table.items():
        for t in ints:
            assert density(t)==want
            for a in (0,1,3):
                assert density(t<<a)==want
    # Direct finite-prefix frequency checks converge to the exact density;
    # use a sufficiently long dyadic block to make the carry tail negligible.
    checks=0
    for t in (5,11,13,27,107,219,439,475,951):
        q=1<<16
        count=sum((n+t).bit_count()>=n.bit_count() for n in range(q))
        assert abs(Fraction(count,q)-density(t))<Fraction(1,1<<12)
        checks+=1
    print("INDEPENDENT_DIGIT_SUM_CHECK_OK count=",checks)
    print("REFERENCE_VERIFY_OK")


if __name__=="__main__": main()
