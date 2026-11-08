"""Exact finite tests of multi-factor nilpotent-product probabilities.

Run: python verify_nil_product.py
Requires Python 3 standard library only. The program directly enumerates ring
multiplication and counts products with dynamic programming; it never assumes
the probability formula in its counting step.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import product


def matrices(n, q, upper=False):
    slots = [(i,j) for i in range(n) for j in range(n) if not upper or i<=j]
    for entries in product(range(q), repeat=len(slots)):
        matrix=[0]*(n*n)
        for (i,j),v in zip(slots,entries):
            matrix[i*n+j]=v
        yield tuple(matrix)


def multiply(a,b,n,q):
    return tuple(sum(a[i*n+k]*b[k*n+j] for k in range(n))%q
                 for i in range(n) for j in range(n))


def is_nilpotent(a,n,q):
    power=a
    zero=(0,)*(n*n)
    for _ in range(n):
        if power==zero:
            return True
        power=multiply(power,a,n,q)
    return power==zero


def run_matrix_case(n,q,upper,max_factors):
    ring=list(matrices(n,q,upper))
    zero=(0,)*(n*n)
    idmat=tuple(int(i==j) for i in range(n) for j in range(n))
    nil={x for x in ring if is_nilpotent(x,n,q)}
    counts={idmat:1}
    for k in range(1,max_factors+1):
        new=defaultdict(int)
        for a,weight in counts.items():
            for b in ring:
                new[multiply(a,b,n,q)]+=weight
        counts=new
        count=sum(multiplicity for x,multiplicity in counts.items() if x in nil)
        actual=Fraction(count,len(ring)**k)
        predicted=(1-(1-Fraction(1,q))**k)**n if upper else 1-(1-Fraction(1,q**n))**k
        assert actual==predicted,(n,q,upper,k,actual,predicted)
        print(f"OK {('UT' if upper else 'M')}_{n}(F_{q}) k={k} pairs_or_tuples={len(ring)**k} nilpotent={count} P={actual}")


def run_product_example():
    matrix_ring=list(matrices(2,2))
    direct_product=[(c,a) for c in range(2) for a in matrix_ring]
    nilset={x for x in matrix_ring if is_nilpotent(x,2,2)}
    counts={(1,(1,0,0,1)):1}
    for k in range(1,5):
        new=defaultdict(int)
        for (c,a),w in counts.items():
            for d,b in direct_product:
                new[(c*d,multiply(a,b,2,2))]+=w
        counts=new
        good=sum(w for (c,a),w in counts.items() if c==0 and a in nilset)
        actual=Fraction(good,len(direct_product)**k)
        predicted=(1-(1-Fraction(1,2))**k)*(1-(1-Fraction(1,4))**k)
        assert actual==predicted
        print(f"OK F_2 x M_2(F_2) k={k} nilpotent={good} / {len(direct_product)**k} P={actual}")


def main():
    cases=[(1,2,False,4),(1,3,False,4),
           (2,2,False,4),(2,3,False,3),(2,5,False,2),
           (3,2,False,3),
           (2,2,True,4),(2,3,True,3),(3,2,True,4)]
    for n,q,upper,kmax in cases:
        run_matrix_case(n,q,upper,kmax)
    run_product_example()
    print('VERIFY_OK: 9 directly enumerated rings and 31 matrix-ring tests, plus 4 directly enumerated product-ring tests')

if __name__=='__main__':
    main()
