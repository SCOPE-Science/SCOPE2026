import sympy as sp
import mpmath as mp

lam, x = sp.symbols('lam x')
y = sp.symbols('y')

C4 = sp.factor(sp.gegenbauer(4, lam, x))
C5 = sp.factor(sp.gegenbauer(5, lam, x))

P4 = 4*(lam+2)*(lam+3)*y**2 - 12*(lam+2)*y + 3
P5 = 4*(lam+3)*(lam+4)*y**2 - 20*(lam+3)*y + 15

assert sp.simplify(C4.subs(x**2, y) - lam*(lam+1)/6 * P4) == 0
assert sp.simplify(C5/x - lam*(lam+1)*(lam+2)/15 * P5.subs(y, x**2)) == 0

z4sq = (3 + sp.sqrt(3*(2*lam+3)/(lam+2))) / (2*(lam+3))
z5sq = (5 + sp.sqrt(5*(2*lam+3)/(lam+3))) / (2*(lam+4))
assert sp.simplify(P4.subs(y, z4sq)) == 0
assert sp.simplify(P5.subs(y, z5sq)) == 0

mp.mp.dps = 50

def F4(s):
    return mp.sqrt((3 + mp.sqrt(6*(s+1)/(s+mp.mpf('1.5'))))/2)

def rho4(t):
    return mp.sqrt(mp.sqrt(3*(mp.mpf('2.5')-t)/(mp.mpf('1.5')-t))-3)/(2*mp.pi*t)

def F5(s):
    return mp.sqrt((5 + mp.sqrt(10*(s+1)/(s+mp.mpf('2.5'))))/2)

def rho5(t):
    return mp.sqrt(mp.sqrt(15*(mp.mpf('3.5')-t)/(mp.mpf('2.5')-t))-5)/(2*mp.pi*t)

def rep4(s):
    return mp.sqrt(mp.mpf('2.5')) + mp.quad(lambda t: s/(s+t)*rho4(t), [1, mp.mpf('1.5')])

def rep5(s):
    return mp.sqrt(mp.mpf('3.5')) + mp.quad(lambda t: s/(s+t)*rho5(t), [1, mp.mpf('2.5')])

for s in (mp.mpf('0.1'), mp.mpf('1'), mp.mpf('10')):
    assert abs(F4(s)-rep4(s)) < mp.mpf('1e-25')
    assert abs(F5(s)-rep5(s)) < mp.mpf('1e-25')

print('C4 and C5 zero formulas: verified')
print('Endpoint CBF integral representations: verified at s = 0.1, 1, 10')
