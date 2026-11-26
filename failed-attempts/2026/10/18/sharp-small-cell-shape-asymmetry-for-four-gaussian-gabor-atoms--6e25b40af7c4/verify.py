"""Reproduce numerical and algebraic checks for four Gaussian coherent-state corners.
The infinite and asymptotic claims are proved analytically in RESULT.md.
Requires sympy and mpmath.
"""
import sympy as s
import mpmath as mp

x, y, z = s.symbols('x y z', nonzero=True)
G = s.Matrix([
    [1, x, y, x*y],
    [x, 1, x*y*z, y*z],
    [y, x*y/z, 1, x/z],
    [x*y, y/z, x*z, 1],
])
exact = ((1-x*x)*(1-y*y))**2 - x*x*y*y*(2-z-1/z)**2
assert s.factor(G.det()-exact)==0, s.factor(G.det()-exact)
print('symbolic Gram identity verified')

mp.mp.dps=65
pi=mp.pi

def f(v):
    return (-(mp.expm1(-v))/v)**2-mp.exp(-v)

def Q(v):
    return v**3+2*v+4-2*mp.exp(v)-2*(v+1)*mp.exp(-v)

y0=mp.findroot(Q,(mp.mpf('2.1'),mp.mpf('2.8')))
C=pi**4*f(y0)
A=mp.sqrt(y0/pi)
print('y_star',mp.nstr(y0,28))
print('a_star',mp.nstr(A,28))
print('coefficient',mp.nstr(C,28))
assert abs(y0-mp.mpf('2.3826641667'))<mp.mpf('3e-8')
assert Q(y0)==0 or abs(Q(y0))<mp.mpf('1e-55')
assert all(f(y0)>f(k/10) for k in list(range(1,23))+list(range(25,400)))

def D(a,b):
    pp=mp.exp(-pi*a*a); qq=mp.exp(-pi*b*b)
    return ((1-pp)*(1-qq))**2-16*pp*qq*mp.sin(pi*a*b/2)**4

def numerical_det(a,b):
    zz=[mp.mpc(0),mp.mpc(a),mp.j*b,mp.mpc(a, b)]
    gram=mp.matrix(4)
    for i in range(4):
        for j in range(4):
            gram[i,j]=mp.exp(-pi*(abs(zz[i])**2+abs(zz[j])**2)/2+pi*mp.conj(zz[i])*zz[j])
    return mp.re(mp.det(gram))

for a,b in [('.2','.15'),('.8','.0125'),('1.2','2'),('3','.5'),('.1','.1'),('1','1'),('0.4','2.3')]:
    a,b=mp.mpf(a),mp.mpf(b)
    expected=D(a,b)
    observed=numerical_det(a,b)
    assert abs(observed-expected)<mp.mpf('1e-55'),(a,b,observed,expected)
print('7 independent coherent Gram determinants matched')

for area in ['0.1','0.03','0.01','0.003','0.001']:
    t=mp.mpf(area)
    long = D(A,t/A)/t**4
    square = D(mp.sqrt(t),mp.sqrt(t))/t**6
    print('area',area,'thin ratio',mp.nstr(long,18),'square ratio',mp.nstr(square,18))
    assert 0<long<C
    assert abs(long-C)<12*t*t
    assert abs(square-pi**6/3)<(pi**7)*t
    assert D(A,t/A)>D(mp.sqrt(t),mp.sqrt(t))
print('asymmetric advantage and asymptotic scalings verified')

# Direct high-precision scanning supports but cannot prove the global compactness step.
for area in ['0.01','0.03','0.1']:
    t=mp.mpf(area)
    values=[(D(mp.exp(mp.mpf(j)/100),t/mp.exp(mp.mpf(j)/100)),j) for j in range(-220,221)]
    best=max(values)
    assert best[0]>D(mp.sqrt(t),mp.sqrt(t))
print('3 grid optimization comparisons verified')
