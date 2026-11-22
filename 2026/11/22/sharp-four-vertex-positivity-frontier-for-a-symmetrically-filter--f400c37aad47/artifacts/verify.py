"""Independent exact-arithmetic diagnostics for filtered-Euler graph heat maps.

Requires Python 3 and SymPy. Run: python artifacts/verify.py
Finite diagnostics supplement, but do not replace, the accompanying proofs.
"""
import sympy as S

h = S.symbols('h', positive=True)

def path(n):
    L = S.zeros(n)
    for i in range(n-1):
        L[i,i] += 1
        L[i+1,i+1] += 1
        L[i,i+1] -= 1
        L[i+1,i] -= 1
    return L

def filt_first(L, x):
    I = S.eye(L.rows)
    J = (I + x*L/2).inv()
    return I-x*J*L*J

def check_equal(a, b):
    if isinstance(a, S.MatrixBase):
        assert all(S.cancel(t)==0 for t in a-b)
    else:
        assert S.cancel(a-b)==0

L4 = path(4)
M4 = filt_first(L4, h)
D = 2*(h+1)**2*(h**2+4*h+2)**2
formulas = {
 (0,1): -h*(h+2)*(h**3-6*h**2-10*h-4)/D,
 (0,2): h**2*(3*h**3+12*h**2+18*h+8)/D,
 (0,3): h**3*(5*h**2+12*h+6)/D,
 (1,2): h*(h+2)*(h**3+2*h**2+6*h+4)/D,
}
for (i,j), expected in formulas.items():
    check_equal(M4[i,j], expected)
    check_equal(M4[3-i,3-j], expected)
check_equal(M4*S.ones(4,1), S.ones(4,1))

M3 = filt_first(path(3),h)
check_equal(M3[0,1], 4*h/(3*h+2)**2)
check_equal(M3[0,2], 16*h*h*(h+1)/((h+2)**2*(3*h+2)**2))
check_equal(M3[1,2], 4*h/(3*h+2)**2)
M2 = filt_first(path(2),h)
check_equal(M2[0,1], h/(h+1)**2)

Ltriangle = S.Matrix([[2,-1,-1],[-1,2,-1],[-1,-1,2]])
Mt = filt_first(Ltriangle,h)
check_equal(Mt[0,1], h/(1+3*h/2)**2)
check_equal(Mt[0,2], h/(1+3*h/2)**2)

P4 = h**3-6*h**2-10*h-4
assert S.factor(M4[0,1].subs(h,S.Rational(8))) == -S.Rational(440,194481)
assert M4[0,1].subs(h,S.Rational(7)) > 0
assert S.nroots(P4)[0].as_real_imag()[0] > 7
# Verify one positive root by exact Descartes coefficients and signed interval.
assert S.Poly(P4,h).all_coeffs() == [1,-6,-10,-4]
assert P4.subs(h,7) < 0 and P4.subs(h,8) > 0

for n in range(2,10):
    L = path(n)
    P = S.ones(n,n)/n
    K = (L+P).inv()-P  # Exact Moore-Penrose pseudoinverse.
    check_equal(K[0,1], S.Rational((n-1)*(2*n-7),6*n))
    check_equal(L*K, S.eye(n)-P)
    for x in [S.Rational(1,3),S.Rational(4),S.Rational(9)]:
        M = filt_first(L,x)
        check_equal(M*S.ones(n,1), S.ones(n,1))
        check_equal(M, M.T)

# General-order filter: verify exact algebraic large-h leading coefficient.
t = S.symbols('t', positive=True)
lmb = S.symbols('lambda', positive=True)
c = S.symbols('c', positive=True)
for p in range(1,9):
    x = t*c*lmb/2
    r = 1-(x/(1+x))**p
    check_equal(S.limit(t*(t*lmb*r**2),t,S.oo),4*p*p/(c*c*lmb))

print('VERIFY_OK')
