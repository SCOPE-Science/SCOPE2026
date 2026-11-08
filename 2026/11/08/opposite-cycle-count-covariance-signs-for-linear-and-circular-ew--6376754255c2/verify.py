"""Independent exact finite checks for the one-line/circular Ewens-succession theorem.
The infinite-size theorem is proved separately; enumeration does not certify it.
"""
from fractions import Fraction
from itertools import permutations
from math import factorial


def cycles(p):
    n = len(p)
    seen = set()
    count = 0
    for start in range(n):
        if start in seen:
            continue
        count += 1
        j = start
        while j not in seen:
            seen.add(j)
            j = p[j]
    return count


def exact_formula(n, theta):
    denominator = (theta+n-2)*(theta+n-1)
    lin = (n-1)*(theta*theta+n-2)/denominator
    circ = n*(theta*theta+n-1)/denominator
    a = n-2
    p_lin = (2*a+1)*theta*theta+2*a*a*theta-a*(2*a+1)
    p_circ = (2*a+1)*theta*theta+2*(a*a-1)*theta-(a+1)*(2*a+1)
    return (lin,circ,
            theta*(n-1)*p_lin/denominator**2,
            theta*n*p_circ/denominator**2)


def direct(n, theta):
    weight = Fraction(0)
    S = T = C = CS = CT = Fraction(0)
    for p in permutations(range(n)):
        k = cycles(p)
        l = sum(p[i+1] == p[i]+1 for i in range(n-1))
        r = sum(p[(i+1)%n] == (p[i]+1)%n for i in range(n))
        w = theta**k
        weight += w
        S += w*l
        T += w*r
        C += w*k
        CS += w*k*l
        CT += w*k*r
    return (S/weight,T/weight,CS/weight-(C*S)/weight**2,
            CT/weight-(C*T)/weight**2)


def main():
    cases = 0
    for n in range(3,9):
        for t in (Fraction(1,2), Fraction(1), Fraction(2), Fraction(7)):
            observed = direct(n,t)
            predicted = exact_formula(n,t)
            assert observed == predicted,(n,t,observed,predicted)
            assert observed[0] > 0 and observed[1] > 0
            cases += 1
        at_one = exact_formula(n,Fraction(1))
        assert at_one[2] == Fraction(1,n*n)
        assert at_one[3] == -Fraction(1,(n-1)**2)
        cases += 1
    print(f'VERIFIED {cases} exact finite cases; both expectations/covariances and uniform signs. Infinite assertion requires written proof.')

if __name__ == '__main__':
    main()
