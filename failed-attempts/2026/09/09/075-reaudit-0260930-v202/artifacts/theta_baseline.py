"""Lane 434: exact theta(C7) enclosure, zero floats.
T7(x)=64x^7-112x^5+56x^3-7x. T7(x)+1=(x+1)(8x^3-4x^2-4x+1)^2 by exact
coefficient expansion. Hence T7(x)=-1 iff x=-1 or 8x^3-4x^2-4x+1=0.
Since T7(cos t)=cos(7t), zeros give cos(7t)=-1, t=(2k+1)pi/7; distinct
values cos(pi/7)>cos(3pi/7)>cos(5pi/7). Three disjoint certified
sign-change intervals with p''-monotonicity isolate all three roots;
largest = cos(pi/7). f(x)=7x/(1+x) increasing => theta enclosure.
Stdlib only. Prints VERIFY_OK.
"""
from fractions import Fraction


def mul(a, b):
    c = {}
    for d1, v1 in a.items():
        for d2, v2 in b.items():
            c[d1 + d2] = c.get(d1 + d2, 0) + v1 * v2
    return {d: v for d, v in c.items() if v != 0}


def main():
    q = {3: 8, 2: -4, 1: -4, 0: 1}
    f = mul(mul(q, q), {1: 1, 0: 1})
    T7 = {7: 64, 5: -112, 3: 56, 1: -7, 0: 1}
    assert f == T7, "T7+1 factorization failed"
    print("T7+1=(x+1)(8x^3-4x^2-4x+1)^2 exact: OK")
    p = lambda x: 8 * x ** 3 - 4 * x ** 2 - 4 * x + 1
    pp = lambda x: 24 * x ** 2 - 8 * x - 4
    ppp = lambda x: 48 * x - 8
    I1 = (Fraction("-0.62348981"), Fraction("-0.62348980"))
    I2 = (Fraction("0.22252093"), Fraction("0.22252094"))
    I3 = (Fraction("0.9009688678"), Fraction("0.9009688680"))
    for name, (a, b) in [("I1", I1), ("I2", I2), ("I3", I3)]:
        assert (p(a) < 0) != (p(b) < 0), name
        assert (ppp(a) > 0) == (ppp(b) > 0), name + " p'' sign"
        assert ((pp(a) > 0 and pp(b) > 0) or (pp(a) < 0 and pp(b) < 0)), name + " p'"
        print(name, "sign-change + strict mono: OK")
    assert I1[1] < I2[0] and I2[1] < I3[0]
    print("all three roots isolated; largest = cos(pi/7) in I3: OK")
    f7 = lambda x: 7 * x / (1 + x)
    lo, hi = f7(I3[0]), f7(I3[1])
    print("theta in [%s, %s]" % (lo, hi))
    assert lo > Fraction("3.3176") and hi < Fraction("3.3177")
    print("theta(C7) in [3.3176,3.3177] EXACT: OK")
    print("VERIFY_OK")


if __name__ == "__main__":
    main()
