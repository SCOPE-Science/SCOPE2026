"""Reproducible algebra and numerical spot checks for the Int2 copula criterion.
Analytical inequalities and the infinite domain are established in RESULT.md.
"""
import math
import random
import sympy as s
import mpmath as mp

x, y, a, g = s.symbols('x y a g', positive=True)
C=x*(1+x**a*(1/y-1))**(-x**(-g))
w=x**a*(1/y-1)
k=x**(-g)
L=1+a-g+g*k*s.log(1+w)-a*(k+1)*w/(1+w)
Cy=s.diff(C,y)
# Differentiate ln C_y rather than expanding C_xy; exact independent identity.
log_Cy=s.log(x)+s.log(k)+s.log(x**a)-2*s.log(y)-(k+1)*s.log(1+w)
assert s.simplify(s.diff(log_Cy,x)-L/x)==0
assert s.simplify(s.diff(C,y)- x*k*x**a*y**(-2)*(1+w)**(-k-1))==0
print('symbolic mixed derivative factor identity: PASS')
mp.mp.dps=65
alpha_max=1/(1-mp.log(2))
def H(alpha,gamma):return 1-alpha+gamma*mp.log(2*alpha/gamma)
def G(alpha):
    assert 1<alpha<alpha_max
    return mp.findroot(lambda z:H(alpha,z), (alpha,1+alpha))
print('alpha_max=',mp.nstr(alpha_max,45))
for alpha in [mp.mpf('1.0001'),mp.mpf('1.5'),mp.mpf('2'),mp.mpf('3'),mp.mpf('3.25')]:
    root=G(alpha)
    assert alpha<root<1+alpha
    assert abs(H(alpha,root))<mp.mpf('1e-54')
    print('Gamma(',alpha,')=',mp.nstr(root,42))

def feasible(alpha,gamma):
    if gamma<0: return False
    if gamma==0: return abs(alpha)<=1
    if alpha<=0: return -1<alpha<=0 and gamma<=alpha+1
    if gamma<alpha: return False
    if alpha<=1: return gamma<=1+alpha
    if alpha>alpha_max: return False
    return gamma<=G(alpha) if alpha<alpha_max else gamma==alpha

def L_formula(alpha,gamma,k,w):
    return 1+alpha-gamma+gamma*k*math.log1p(w)-alpha*(k+1)*w/(1+w)

def exact_min(alpha,gamma):
    if gamma==0: return 1-abs(alpha)
    if gamma<0:return -math.inf
    if alpha<=0:return 1+alpha-gamma
    if gamma<alpha:return -math.inf
    if gamma>=2*alpha:return 1+alpha-gamma
    return 1-alpha+gamma*math.log(2*alpha/gamma)

rng=random.Random(1729)
points=[(-1,0),(1,0),(-0.5,0.4),(-0.5,0.6),(0.2,0.1),(0.2,0.3),(0.5,1.2),(0.5,1.6),(1,1),(1,2),(1,2.1),(2,2),(2,2.4),(2,2.8),(3.2,3.2),(3.5,3.5),(-0.3,-0.1),(0.3,-0.5)]
for alpha, gamma in points:
    curmin=math.inf
    for i in range(1400):
        k=1+math.expm1(rng.random()*min(15., 10+abs(alpha)+abs(gamma))) if gamma>0 else (0.05 + rng.random()*0.94 if gamma<0 else 1)
        w=math.expm1(rng.random()*18)
        curmin=min(curmin,L_formula(alpha,gamma,k,w))
    if gamma>=0 and (alpha<=0 or gamma>=alpha):
        floor=exact_min(alpha,gamma)
        assert curmin+2e-12>=floor,(alpha,gamma,curmin,floor)
    print(f'alpha={alpha}, gamma={gamma}, predicted={feasible(alpha, gamma)}; symbolic infimum={exact_min(alpha,gamma):.9g}; sampled infimum={curmin:.9g}')
# Independent derivative numerical checks in interior.
for alpha,gamma in [(.5,.5),(.6,1.4),(-.3,.2),(1.8,2.2),(2.2,2.6)]:
 for i in range(25):
    xx=0.05+0.9*rng.random(); yy=0.05+0.9*rng.random()
    func=lambda u,v: u*(1+u**alpha*(1/v-1))**(-u**(-gamma))
    md=mp.diff(func, (mp.mpf(xx),mp.mpf(yy)), (1,1))
    ww=xx**alpha*(1/yy-1); kk=xx**(-gamma)
    dy=xx*kk*xx**alpha/(yy**2)*(1+ww)**(-kk-1)
    fact=dy/xx*L_formula(alpha,gamma,kk,ww)
    assert abs(float(md)-fact)<2e-9*max(1,abs(fact)), (alpha,gamma,xx,yy)
print('numeric sampled factorization and lower-bound checks: PASS')
