"""Independent numerical checks of two-harmonic spectral-power positivity.
Dependencies: Python 3 and mpmath. They supplement, not replace, the exact proof.
"""
import mpmath as m
m.mp.dps = 45

def a(r): return r/(1+r*r/2)
def b(r): return r*r/(4+2*r*r)
def c(r): return m.log(a(r))/m.log(b(r))
def t0(r): return m.log(4)/m.log(4/r)
def ti(t,r): return 1-2*b(r)**t-a(r)**(2*t)/(4*b(r)**t)
def te(t,r): return 1-2*a(r)**t+2*b(r)**t
def tr(r): return m.log(m.log(b(r))/m.log(a(r)))/m.log(a(r)/b(r))
def true_min(t,r): return ti(t,r) if t<=t0(r) else te(t,r)
def root(a0,b0,f):
    assert f(a0)*f(b0)<=0
    for _ in range(130):
        mid=(a0+b0)/2
        if f(a0)*f(mid)<=0:b0=mid
        else:a0=mid
    return (a0+b0)/2
cc=m.findroot(lambda u:2*(1-u)*u**(u/(1-u))-1,(m.mpf('.22'),m.mpf('.24')))
rc=m.findroot(lambda r:c(r)-cc,(m.mpf('.96'),m.mpf('.98')))
assert m.mpf('.9666')<rc<m.mpf('.9667')
assert m.mpf('1.043')<tr(rc)<m.mpf('1.045')
assert abs(te(tr(rc),rc))<m.mpf('1e-35')
for rr in ['.1','.5','.8','.95','.9666','.97','.99','1']:
    r=m.mpf(rr)
    tminus=root(m.mpf('0'),t0(r),lambda t:ti(t,r))
    assert tminus<t0(r)
    for j in range(1,90):
        t=m.mpf(j)/55
        xstar=max(m.mpf('-1'),-a(r)**t/(4*b(r)**t))
        observed=1-2*b(r)**t+2*a(r)**t*xstar+4*b(r)**t*xstar*xstar
        assert abs(observed-true_min(t,r))<m.mpf('1e-36')
        for k in range(65):
            u=-1+m.mpf(k)/32
            val=1-2*b(r)**t+2*a(r)**t*u+4*b(r)**t*u*u
            assert val>=observed-m.mpf('1e-36')
    assert abs(ti(tminus,r))<m.mpf('1e-35')
    if r>rc and r<1:
        z=tr(r)
        l=root(m.mpf('1'),z,lambda t:te(t,r))
        h=root(z,m.mpf('2'),lambda t:te(t,r))
        assert m.mpf('1')<l<z<h and te(z,r)<0
r=m.mpf('1')
assert abs(tr(r)-m.mpf('1.0718636518871572'))<m.mpf('1e-14')
assert abs(root(tr(r),m.mpf('2'),lambda t:te(t,r))-m.mpf('1.14772038123701436'))<m.mpf('1e-14')
print('PASS: exact minimizer tests, roots, transition and sampled polynomial signs')
print('critical_rho',m.nstr(rc,24),'critical_time',m.nstr(tr(rc),24))
