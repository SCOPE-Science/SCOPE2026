"""Exact reproducibility checks for two independent synchronous walks on K_{n,n}."""
from collections import defaultdict
from fractions import Fraction
from math import comb, factorial

def coupon(n, seeded, draws):
    """Probability draws visit every one of n-seeded fixed targets."""
    if draws < n-seeded:
        return Fraction(0)
    return sum(((-1)**j*comb(n-seeded,j)*Fraction((n-j)**draws,n**draws)
                for j in range(n-seeded+1)), Fraction(0))

def prediction(n, t, starts):
    side_a = sum(x<n for x in starts)
    side_b = 2-side_a
    if t%2 == 0:
        samples_a=samples_b=t
    else:
        samples_a=t-1+side_b
        samples_b=t-1+side_a
    # For two walkers, each side receives t samples at even deadlines
    # and t+number of walkers starting in the other part at odd deadlines.
    seen_a=len({x for x in starts if x<n})
    seen_b=len({x for x in starts if x>=n})
    return coupon(n,seen_a,samples_a)*coupon(n,seen_b,samples_b)

def exact_walk(n,t,starts):
    fullmask=(1<<(2*n))-1
    states={(starts[0],starts[1],(1<<starts[0])|(1<<starts[1])):1}
    for _ in range(t):
        new=defaultdict(int)
        for (x,y,mask),count in states.items():
            candx=range(n,2*n) if x<n else range(n)
            candy=range(n,2*n) if y<n else range(n)
            for a in candx:
                for b in candy:
                    new[(a,b,mask|(1<<a)|(1<<b))]+=count
        states=new
    num=sum(v for (_,_,mask),v in states.items() if mask==fullmask)
    return Fraction(num,n**(2*t))

def surj(N,k):
    if k<0 or k>N:return 0
    if N==0:return int(k==0)
    if k==0:return 0
    return sum((-1)**j*comb(k,j)*(k-j)**N for j in range(k+1))

def main():
    tests=0
    for n in range(2,5):
        # Same part, split, and duplicate starts; start positions all explicit.
        for starts in ((0,1),(0,n),(0,0)):
            for t in range(0,9):
                a=exact_walk(n,t,starts)
                b=prediction(n,t,starts)
                assert a==b,(n,t,starts,a,b)
                tests+=1
    # Cover probability inequalities over all parameter cases, without floats.
    inequalities=0
    for n in range(2,18):
        for k in range(0,21):
            N=2*k
            even_split=coupon(n,1,N)**2
            even_same=coupon(n,2,N)*coupon(n,0,N)
            assert even_split>=even_same
            assert (even_split>even_same)==(N>=n-1)
            odd_same=coupon(n,2,N)*coupon(n,0,N+2)
            odd_split=coupon(n,1,N+1)**2
            assert odd_same>=odd_split
            assert (odd_same>odd_split)==(N>=n-2)
            inequalities+=2
    # Independent integer verification of the ordered-Stirling coefficient identity.
    stirling_checks=0
    for N in range(1,28):
        coeff=[0]+[surj(N,j) for j in range(1,N+1)]+[0]
        for j in range(1,N+1):
            assert coeff[j]**2>=coeff[j-1]*coeff[j+1]
            stirling_checks+=1
    # Smallest illustrative instance K_{2,2}, first two deadlines.
    assert prediction(2,1,(0,1))==Fraction(1,2)
    assert prediction(2,1,(0,2))==Fraction(1,4)
    assert prediction(2,2,(0,1))==Fraction(1,2)
    assert prediction(2,2,(0,2))==Fraction(9,16)
    print('CHECK_OK', {'full_labeled_state_vs_coupon':tests,'strict_deadline_checks':inequalities,'ordered_stirling_checks':stirling_checks})
if __name__=='__main__':main()
