"""Exact checks and a formal-series certificate for the Motzkin covariance theorem.

Run: python3 verify_motzkin.py
Requires Python 3 and SymPy for the formal-series certificate.
"""
from fractions import Fraction
from functools import lru_cache
from math import isclose

@lru_cache(None)
def paths(n, height=0):
    if n == 0:
        return ((),) if height == 0 else ()
    out = []
    for step, h in (('H', height), ('U', height + 1), ('D', height - 1)):
        if h < 0 or h > n - 1:
            continue
        for suffix in paths(n - 1, h):
            out.append((step,) + suffix)
    return tuple(out)

def moments(n):
    counts = [0, 0, 0, 0, 0, 0]
    for w in paths(n):
        level = 0
        r = h = p = 0
        for i, step in enumerate(w):
            if step == 'H':
                h += 1
                r += (level == 0)
            elif step == 'U':
                level += 1
                p += (i + 1 < n and w[i + 1] == 'D')
            else:
                level -= 1
        assert level == 0
        for i, v in enumerate((1, r, h, p, r * h, r * p)):
            counts[i] += v
    return counts

def recurrences(N):
    M = [0] * (N + 1)
    W = [0] * (N + 1)
    V = [0] * (N + 1)
    R = [0] * (N + 1)
    RW = [0] * (N + 1)
    RV = [0] * (N + 1)
    M[0] = 1
    for n in range(1, N + 1):
        a = sum(M[i] * M[n - 2 - i] for i in range(n - 1)) if n >= 2 else 0
        b = sum(M[i] * W[n - 2 - i] for i in range(n - 1)) if n >= 2 else 0
        c = sum(M[i] * V[n - 2 - i] for i in range(n - 1)) if n >= 2 else 0
        M[n] = M[n - 1] + a
        W[n] = W[n - 1] + M[n - 1] + 2 * b
        V[n] = V[n - 1] + 2 * c + (M[n - 2] if n >= 2 else 0)
        R[n] = sum(M[i] * M[n - 1 - i] for i in range(n))
        RW[n] = R[n] + 2 * sum(M[i] * W[n - 1 - i] for i in range(n))
        RV[n] = 2 * sum(M[i] * V[n - 1 - i] for i in range(n))
    return M, R, W, V, RW, RV

def formal_certificate():
    import sympy as s
    t = s.symbols('t', positive=True)
    z = (1 - t*t) / 3
    Delta = s.sqrt((1-3*z)*(1+z))
    M = (1-z-Delta)/(2*z*z)
    P = z*z*M/Delta
    H = z*M/Delta
    R = z*M*M
    RP = 2*z*M*P
    RH = R + 2*z*M*H
    functions = {'M': M, 'R': R, 'P': P, 'RP': RP, 'H': H, 'RH': RH}
    expected = {
       'M': (s.Rational(3,2)*s.sqrt(3), s.Rational(-39,16), s.Rational(2665,512)),
       'R': (3*s.sqrt(3), s.Rational(-75,16), s.Rational(8785,512)),
       'P': (s.sqrt(3)/6, s.Rational(-7,16), s.Rational(-23,512)),
       'RP': (s.sqrt(3)/3, s.Rational(-43,16), s.Rational(1489,512)),
       'H': (s.sqrt(3)/2, s.Rational(-15,16), s.Rational(505,512)),
       'RH': (s.sqrt(3), s.Rational(-3,16), s.Rational(-3455,512)),
    }
    def expansion_factor(alpha, j):
       a = alpha
       c0 = 1/s.gamma(-a)
       if j == 0: return c0
       if j == 1: return c0 * a*(a+1)/2
       if j == 2: return c0 * a*(a+1)*(a+2)*(3*a+1)/24
       raise ValueError(j)
    rows = {}
    for key,f in functions.items():
       fs = s.series(f, t, 0, 7).removeO().expand()
       k = s.Rational(1,2) if key in ('M','R') else s.Rational(-1,2)
       raw = []
       for j in range(3):
          coefficient = 0
          for ell in range(j+1):
             a = k + ell
             coefficient += fs.coeff(t, 2*a)*expansion_factor(a, j-ell)
          raw.append(s.simplify(coefficient*s.sqrt(s.pi)))
       got=(raw[0], s.simplify(raw[1]/raw[0]), s.simplify(raw[2]/raw[0]))
       assert all(s.simplify(x-y) == 0 for x,y in zip(got,expected[key])), (key,got)
       rows[key]=got
    a,m1,m2=rows['M']; b,r1,r2=rows['R']; c,p1,p2=rows['P']; d,d1,d2=rows['RP']
    h,h1,_=rows['H']; rh,rh1,_=rows['RH']
    assert s.simplify(d/a-b*c/a**2)==0
    assert s.simplify((d/a)*(d1-m1)-(b*c/a**2)*(r1+p1-2*m1))==0
    coef=s.simplify((d/a)*(d2-m2+m1*m1-m1*d1) - (b*c/a**2)*(
        r2-m2+m1*m1-m1*r1+p2-m2+m1*m1-m1*p1+(r1-m1)*(p1-m1)))
    cv_rh=s.simplify((rh/a)*(rh1-m1) - (b*h/a**2)*(r1+h1-2*m1))
    assert coef == -1,coef
    assert cv_rh == 2,cv_rh
    return rows

def main():
    arrays=recurrences(250)
    checks=0
    for n in range(0, 13):
       actual=moments(n)
       given=[col[n] for col in arrays]
       assert actual==given,(n,actual,given)
       checks+=6
    M,R,H,P,RH,RP=arrays
    for n in range(1,251):
       assert M[n]>=1 and R[n]>=0 and H[n]>=0 and P[n]>=0
       checks+=4
    for n in (50, 100, 150, 200, 250):
       covariance_rp=Fraction(RP[n]*M[n]-R[n]*P[n],M[n]*M[n])
       covariance_rh=Fraction(RH[n]*M[n]-R[n]*H[n],M[n]*M[n])
       print('n=',n,'n Cov(R,P)=',round(n*float(covariance_rp),8),
             'Cov(R,H)=',round(float(covariance_rh),8))
       assert n*float(covariance_rp)<-0.89
       assert 1.85<float(covariance_rh)<2
       checks+=2
    rows=formal_certificate()
    checks+=18
    print('formal table:', rows)
    print('passed:',checks,'checks')

if __name__=='__main__':
    main()
