#!/usr/bin/env python3
"""Reproduce symbolic and numerical checks for a two-visit Poisson occupancy model.

Requires Python >= 3.10, SymPy, and mpmath. This diagnostic is not a replacement
for the analytical proof of identifiability or the uniform asymptotic optimum.
"""
import random
import sympy as sp
import mpmath as mp

count = 0

def check(flag, description='assertion'):
    global count
    if not flag:
        raise AssertionError(description)
    count += 1

p, a, l = sp.symbols('p a l', positive=True)
raw_moments = [
    a+p*l,
    a*a+p*(2*a*l+l*l),
    a**3+p*(3*a*a*l+3*a*l*l+l**3),
]
Jm = sp.Matrix(raw_moments).jacobian([p,a,l])
check(sp.simplify(Jm.det()-l**4*p*(p-1))==0,'moment Jacobian')
x = sp.symbols('x', real=True)
shape = x*x*(1-x)**2*(1-2*x)**2
check(sp.simplify(shape.diff(x).subs(x,(1-1/sp.sqrt(3))/2))==0,'universal short split')
check(sp.simplify(shape.subs(x,(1-1/sp.sqrt(3))/2)-sp.Rational(1,108))==0,'maximum shape')
check(sp.factor(shape.diff(x))== 2*x*(x-1)*(2*x-1)*(6*x*x-6*x+1), 'factorized derivative')

mp.mp.dps=70

def survival(p,a,l,t):
    return (1-p)*mp.exp(-a*t)+p*mp.exp(-(a+l)*t)

def gradients(p,a,l,t):
    e0=mp.exp(-a*t); e1=mp.exp(-(a+l)*t)
    return mp.matrix([e1-e0, -t*survival(p,a,l,t), -p*t*e1])

def histories(p,a,l,u,v):
    m=lambda z:survival(p,a,l,z)
    return [m(u+v), m(v)-m(u+v), m(u)-m(u+v),1-m(u)-m(v)+m(u+v)]

def det_info(p,a,l,u,v,compare=False):
    T=u+v
    rows=[list(gradients(p,a,l,z)) for z in (u,v,T)]
    J=mp.det(mp.matrix(rows))
    h=histories(p,a,l,u,v)
    val=J**2/mp.fprod(h)
    if compare:
        gu,gv,gT=(gradients(p,a,l,z) for z in (u,v,T))
        ghs=[gT,gv-gT,gu-gT,-gu-gv+gT]
        I=mp.matrix(3)
        for prob,g in zip(h,ghs):
            I+=g*g.T/prob
        check(mp.almosteq(mp.det(I),val,rel_eps=mp.mpf('1e-45'),abs_eps=mp.mpf('1e-45')),
              'Fisher determinant from independent probability derivatives')
    return val

rnd=random.Random(169244)
for i in range(375):
    p=mp.mpf(str(.05+.9*rnd.random()))
    a=mp.mpf(str(.05+3*rnd.random()))
    l=mp.mpf(str(.1+4*rnd.random()))
    T=mp.mpf(str(.1+4*rnd.random()))
    fraction=mp.mpf(str(.02+.46*rnd.random()))
    u=T*fraction;v=T-u
    probs=histories(p,a,l,u,v)
    check(all(0<z<1 for z in probs),'history probabilities')
    check(abs(sum(probs)-1)<mp.mpf('1e-60'),'normalization')
    D=det_info(p,a,l,u,v,compare=True)
    check(D>0,'positive full Fisher information')
    check(mp.almosteq(D,det_info(p,a,l,v,u),rel_eps=mp.mpf('1e-45')),'symmetry')
    check(abs(det_info(p,a,l,T/2,T/2))<mp.mpf('1e-110'),'equal visit rank defect')

xstar=(1-1/mp.sqrt(3))/2
cases=[('.3','.5','1.2'),('.8','.2','2.8'),('.4','1.5','.5')]
for ps,al,la in cases:
    p,a,l=map(mp.mpf,(ps,al,la))
    mu1=a+p*l; mu2=a*a+p*(2*a*l+l*l)
    coeff=p*p*(1-p)**2*l**8/(144*mu1*mu1*mu2)
    for t in ('.1','.025','.005'):
        T=mp.mpf(t)
        exact=det_info(p,a,l,T*xstar,T*(1-xstar))
        approx=coeff*T**8/108
        check(abs(exact/approx-1)<mp.mpf('8')*(a+l)*T,'leading exact Fisher coefficient')
    for t in ('.08','.02'):
        T=mp.mpf(t)
        root=mp.findroot(lambda zz:mp.diff(lambda y:mp.log(det_info(p,a,l,T*y,T*(1-y))),zz), (mp.mpf('.18'),mp.mpf('.24')))
        check(abs(root-xstar)<2*T*T,'short budget optimizer diagnostics')

print('PASS', count, 'symbolic/numerical assertions')
print('universal shorter fraction:',mp.nstr(xstar,18))
