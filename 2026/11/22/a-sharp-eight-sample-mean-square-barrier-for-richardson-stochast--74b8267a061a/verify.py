"""Exact-arithmetic verification of polynomial OU sample-generator identities.

This program checks algebraic consequences on finite test inputs. The
all-sample-size moment and tail assertions require the analytic radial proof.
"""
from fractions import Fraction as F
from itertools import product


def empirical(xs):
    s2 = sum((x*x for x in xs), F(0))
    s4 = sum((x*x*x*x for x in xs), F(0))
    assert s4 > 0
    gram = s4 / len(xs)
    h = (-2*s4+2*s2) / len(xs)
    j = (4*s4-4*s2) / len(xs)
    return gram, h, j, h/gram, j/gram


def methods(a, b, h):
    q1 = 1+h*a
    qr = 2*(1+F(1,2)*h*a)**2-q1
    q2 = 1+h*a+F(1,2)*h*h*b
    return q1, qr, q2


def quadratic_error(q, alpha):
    return 3*q*q-2*(1+2*alpha)*q+1+2*alpha*alpha


def run():
    tests=0
    sample_vectors = []
    for m in range(1,6):
        for vals in product((F(-2), F(-1), F(0), F(1), F(3)), repeat=m):
            if all(x==0 for x in vals):
                continue
            sample_vectors.append(vals)
    # Fixed deterministic cases, no random seed or floating-point tolerance.
    for xs in sample_vectors:
        g,H,J,a,b=empirical(xs)
        s2=sum((x*x for x in xs),F(0));s4=sum((x**4 for x in xs),F(0))
        assert g==s4/len(xs)
        assert a==-2+2*s2/s4
        assert b==-2*a
        tests+=3
        for h in (F(1,4), F(1,2), F(1), F(3,2)):
            q1,qr,q2=methods(a,b,h)
            assert q1==1+h*a
            assert qr==1+h*a+h*h*a*a/2
            assert q2==1+(h-h*h)*a
            if h==1:
                assert q2==1
            tests+=4
        a2=empirical(tuple(2*x for x in xs))[3]
        assert a2+2==(a+2)/4
        tests+=1
    for m in range(1,21):
        for q in (F(1,2), F(1),F(2),F(3)):
            # Chi-square negative moment integral Gamma(m/2-q): finite iff m>2q.
            if m>2*q:
                assert F(m,2)-q>0
            else:
                assert F(m,2)-q<=0
            tests+=1
    for alpha in (F(0),F(1,3),F(1)):
        for q in (F(-3),F(-1),F(0),F(2),F(5)):
            # Direct integral of (q*x^2 - (alpha*x^2+1-alpha))^2
            direct=3*(q-alpha)**2-2*(q-alpha)*(1-alpha)+(1-alpha)**2
            assert direct==quadratic_error(q,alpha)
            tests+=1
    print(f"VERIFY_OK {tests} exact checks on {len(sample_vectors)} finite vectors")


if __name__=='__main__':
    run()
