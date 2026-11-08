"""Exact rational checks of finite-coordinate inverse identities for geometrically damped bilateral shifts."""
from fractions import Fraction


def weight(q, k):
    return Fraction(1) if k <= 0 else q ** k


def gamma(q, j):
    return q ** (j * (j - 1) // 2)


def evaluate(q, x, n):
    y = {j-n: value / __import__('functools').reduce(
        lambda acc, k: acc * weight(q, k), range(j-n, j), Fraction(1))
         for j, value in x.items()}
    lhs = sum((abs(v)**2 for v in y.values()), Fraction(0))
    negative = sum((abs(v)**2 for j, v in x.items() if j <= 0), Fraction(0))
    in_window = sum((abs(v/gamma(q,j))**2 for j,v in x.items()
                     if 1 <= j <= n), Fraction(0))
    tail = sum((abs(v/gamma(q,j))**2 * gamma(q,j-n)**2
                for j,v in x.items() if j > n), Fraction(0))
    return lhs, negative + in_window + tail


def main():
    checks=0
    for q in [Fraction(1,2), Fraction(2,3), Fraction(3,4)]:
        for top in range(2, 13):
            x={j:Fraction((1 if j % 2 == 0 else -1), abs(j)+3) for j in range(-4,top+1)}
            for n in range(0, 13):
                lhs,rhs=evaluate(q,x,n)
                assert lhs==rhs,(q,top,n,lhs,rhs)
                checks+=1
    print(f'MBEKHTA_CORE_EXACT_FINITE_OK {checks}')

if __name__=='__main__':
    main()
