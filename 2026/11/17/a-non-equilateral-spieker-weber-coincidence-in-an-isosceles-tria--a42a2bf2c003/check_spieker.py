"""Reproducible interval certificate for a triangle-center coincidence.

Requires Python 3.10+, sympy 1.14, mpmath 1.3.
All certificate inputs are integers; intervals are rounded outwards.
"""
import sympy as sp
from mpmath import iv, mp

h = sp.symbols('h', positive=True)
s = sp.sqrt(1+h*h)
y = h*s/(2*(1+s))
G = 2*y*sp.asinh(1/y) + 2*(
    h/s*(sp.sqrt(1+y*y) - h + y)
    - (h-y)/(s*s)*(sp.asinh(h)+sp.asinh((1+h*y)/(h-y)))
)
DG = sp.diff(G,h)
iv.dps = 50
asinh_iv = lambda x: iv.log(x+iv.sqrt(1+x*x))
mods = [{'sqrt':iv.sqrt, 'asinh':asinh_iv}, 'math']
G_iv = sp.lambdify(h,G,modules=mods)
DG_iv = sp.lambdify(h,DG,modules=mods)
a = G_iv(iv.mpf(7)/10)
b = G_iv(iv.mpf(4)/5)
assert a.b < 0, a
assert b.a > 0, b
min_lower = iv.mpf(1)
for k in range(100):
    left = iv.mpf(700+k)/1000
    right = iv.mpf(701+k)/1000
    interval = iv.mpf([left.a, right.b])
    z = DG_iv(interval)
    assert z.a > iv.mpf(9)/100, (k,z)
    if z.a < min_lower.a: min_lower=z.a

# Independent evaluation: direct high-precision integration of each segment.
mp.dps = 50
for height in [mp.mpf('0.7'),mp.mpf('0.75'),mp.mpf('0.8'),mp.sqrt(3)]:
    leg = mp.sqrt(1+height*height)
    yy = height*leg/(2*(1+leg))
    g_direct = mp.quad(lambda x: yy/mp.sqrt(x*x+yy*yy), [-1,1])
    g_direct += 2*leg*mp.quad(lambda t: (yy-height*t)/mp.sqrt((1-t)**2+(yy-height*t)**2), [0,1])
    g_closed = sp.lambdify(h,G,modules='mpmath')(height)
    assert abs(g_direct-g_closed) < mp.mpf('1e-40'), (height,g_direct,g_closed)

root=mp.findroot(sp.lambdify(h,G,modules='mpmath'), (mp.mpf('0.7'),mp.mpf('0.8')))
assert mp.mpf('0.7') < root < mp.mpf('0.8')
print('SPIEKER_WEBER_COINCIDENCE_OK')
print('g(0.7) interval',a)
print('g(0.8) interval',b)
print('g_derivative_certified_strictly_gt',mp.mpf('0.09'))
print('isolated_root_approx',mp.nstr(root,30))
