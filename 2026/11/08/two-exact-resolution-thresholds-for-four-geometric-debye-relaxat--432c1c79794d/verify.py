#!/usr/bin/env python3
"""Reproduce algebraic and numerical checks for four equal Debye responses.
Requires sympy and mpmath. Run: python verify.py
"""
import sympy as sp
import mpmath as mp

h,v,z=sp.symbols('h v z',real=True)
Q=sp.expand((1-v)*(v+h*h)**2+(h-2)*(h*h-v)*(v+1)**2)
C=h**3-11*h**2+40*h-52
T=h**7-16*h**6+75*h**5-66*h**4-393*h**3-300*h**2-35*h-34
checks=0

def assert_true(cond, explanation):
    global checks
    if not cond: raise AssertionError(explanation)
    checks+=1

# Algebraic reduction in logarithmic frequency and the critical polynomials.
p=(h-3)/4
var=sp.symbols('w',real=True)
F=var*(1/(var**2+p)+(h-2)/(var**2+p*h*h))
Qactual=sp.together(sp.diff(F,var)*(var**2+p)**2*(var**2+p*h*h)**2)
Qtarget=p**3*Q.subs(v,var**2/p)
assert_true(sp.simplify(Qactual-Qtarget)==0,'Derivative numerator')
assert_true(sp.factor(sp.discriminant(Q,v))==(h-2)*(h-1)**4*(h+1)**2*T,'Discriminant')
assert_true(sp.factor(Q.subs(v,1/p))==(h-2)*(h-1)*(h+1)**2*C/(h-3)**3,'Central curvature')
assert_true(sp.simplify(C.subs(h,z+3)-(z*(z-1)**2-4))==0,'Lower threshold shift')
assert_true(sp.expand(T.subs(h,z+3))==z**7+5*z**6-24*z**5-156*z**4-240*z**3-1488*z**2-7424*z-10048,'Upper threshold shift')
assert_true(C.subs(h,5)<0<C.subs(h,6),'Lower isolation')
assert_true(T.subs(h,9)<0<T.subs(h,10),'Upper isolation')
assert_true(Q.subs({h:10,v:sp.Rational(4,7)})>0,'First witness sign')
assert_true(Q.subs({h:10,v:2})<0,'Second witness sign')
assert_true(Q.subs({h:10,v:20})>0,'Third witness sign')
assert_true(Q.subs({h:10,v:80})<0,'Fourth witness sign')

mp.mp.dps=65
cf=lambda H: H**3-11*H**2+40*H-52
tf=lambda H: H**7-16*H**6+75*H**5-66*H**4-393*H**3-300*H**2-35*H-34
hc=mp.findroot(cf,(mp.mpf('5'),mp.mpf('6')))
hd=mp.findroot(tf,(mp.mpf('9'),mp.mpf('10')))
rr=lambda H: (H-1+mp.sqrt((H-1)**2-4))/2
rc,rd=rr(hc),rr(hd)
assert_true(4<rc<4.1 and 8<rd<8.1,'Critical separations')

def numeric_critical_points(r):
    # Numeric cubic roots from exact coefficients in the scaled coordinate.
    H=mp.mpf(r)+1+1/mp.mpf(r)
    pp=(H-3)/4
    coeff=[1-H, H**3-4*H**2-2*H+5,
           -H**4+2*H**3-2*H**2-H+2,
           H**4+H**3-2*H**2]
    roots=mp.polyroots(coeff,maxsteps=1000,error=False)
    positive=sorted([mp.re(t) for t in roots if abs(mp.im(t))<mp.mpf('1e-35') and mp.re(t)>1/pp],key=float)
    return [mp.acosh(mp.sqrt(pp*t)) for t in positive]

def physical_loss(s,r):
    a=mp.log(r)
    return sum(1/(2*mp.cosh(s-j*a/2)) for j in (-3,-1,1,3))

def physical_derivative(s,r):
    a=mp.log(r)
    return -sum(mp.sinh(s-j*a/2)/(2*mp.cosh(s-j*a/2)**2) for j in (-3,-1,1,3))

for r,count in [(2,0),(4,0),(mp.mpf('4.1'),1),(5,1),(7,1),(8,1),(mp.mpf('8.03'),3),(9,3),(10,3),(30,3)]:
    pts=numeric_critical_points(r)
    assert_true(len(pts)==count, 'Noncentral stationary-point count at r='+str(r))
    for s in pts:
        assert_true(abs(physical_derivative(s,r))<mp.mpf('1e-35'),'Physical derivative at '+str(s))
        assert_true(s>0,'Positive log-frequency root')

# Independent direct numeric sampling of derivative signs on intervals.
for r in [mp.mpf('3'),mp.mpf('5'),mp.mpf('10'),mp.mpf('30')]:
    pts=numeric_critical_points(r)
    ends=[mp.mpf('0')]+pts+[mp.log(r)*2+6]
    for i,(a,b) in enumerate(zip(ends,ends[1:])):
        observed=mp.sign(physical_derivative((a+b)/2,r))
        predicted=(-1)**(i+int(r<rc))
        assert_true(int(observed)==predicted,'Physical interval sign')

def high_critical_points(r):
    H=r+1+1/r
    pp=(H-3)/4
    V0=1/pp
    def evalq(v):
        return (1-v)*(v+H*H)**2+(H-2)*(H*H-v)*(v+1)**2
    def bisect(lo,hi):
        flo=evalq(lo)
        assert_true(flo*evalq(hi)<0,'Bracketing high-r root')
        for _ in range(220):
            mid=(lo+hi)/2
            fm=evalq(mid)
            if flo*fm>0:
                lo,flo=mid,fm
            else: hi=mid
        return (lo+hi)/2
    vv=[bisect(V0,mp.mpf('2')),bisect(H,2*H),bisect(H*H/2,H*H)]
    return [mp.acosh(mp.sqrt(pp*t)) for t in vv]

for r in [mp.mpf('1000'),mp.mpf('10000')]:
    s1,s2,s3=high_critical_points(r)
    a=mp.log(r)
    assert_true(abs(s1-a/2)<mp.mpf('0.05'),'Inner maxima asymptotic')
    assert_true(abs(s2-a)<mp.mpf('0.05'),'Outer minimum asymptotic')
    assert_true(abs(s3-3*a/2)<mp.mpf('0.05'),'Outer maxima asymptotic')
    for s in [mp.mpf('0'),s2]:
        assert_true(abs(physical_loss(s,r)*mp.sqrt(r)/2-1)<mp.mpf('0.08'),'Valley-height asymptotic')

print('VERIFY_OK checks=',checks)
print('h_c=',mp.nstr(hc,24),'r_c=',mp.nstr(rc,24))
print('h_d=',mp.nstr(hd,24),'r_d=',mp.nstr(rd,24))
