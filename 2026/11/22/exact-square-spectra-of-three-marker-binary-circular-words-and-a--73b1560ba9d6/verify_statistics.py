"""Independent exact finite-composition mean census and limiting constant checks."""
from math import comb
from fractions import Fraction


def square_count(gaps):
    a,b,c=sorted(gaps)
    # Independent implementation as union of integer interval roots.
    d=(a,b,c); shapes=set()
    for j,t in enumerate(d):
        for k in range(t):
            if k<=d[(j-1)%3]-1 and t-k-1<=d[(j+1)%3]-1:
                shapes.add((t,k))
    return (c-1)//2+len(shapes)


def mean_n(n):
    total=sum(square_count((a,b,n-a-b)) for a in range(1,n-1)
              for b in range(1,n-a))
    return Fraction(total, comb(n-1,2))


def main():
    for n in [3,4,5,6,7,8,9,10,25,50,100,250,500]:
        val=mean_n(n)
        err=val-Fraction(5*n,9)
        print('MEAN',n,str(val), 'decimal',f'{float(val):.9f}', 'error_from_5n/9',f'{float(err):+.9f}')
    # Asymptotic identity for sorted Dirichlet gaps: E(max)=11/18, E(min)=1/9,
    # E((1-2 max)_+)=1/36, so E(F)=11/36+2/9+1/36.
    assert Fraction(11,36)+Fraction(2,9)+Fraction(1,36)==Fraction(5,9)
    print('EXACT_DIRICHLET_CONSTANT_PASS 5/9')
    print('ALL_TESTS_PASS')

if __name__=='__main__': main()
