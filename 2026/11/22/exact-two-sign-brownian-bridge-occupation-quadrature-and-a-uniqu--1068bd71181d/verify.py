"""Independent numerical checks of closed two-sign bridge occupation formulas.

Finite-precision checks corroborate, but do not replace, the analytic proof.
"""
import mpmath as mp

mp.mp.dps = 65

def a(s):
    return (mp.sqrt(s) + mp.sqrt(1-s) - 1) / 2

def c(s, t):
    assert 0 < s < t < 1
    return 2/mp.pi * mp.asin(mp.sqrt(s*(1-t)/(t*(1-s))))

def corr(u, v):
    if u == v:
        return mp.mpf(1)
    lo, hi = sorted([u, v])
    return mp.sqrt(lo*(1-hi)/(hi*(1-lo)))

def a_integral(s):
    return (mp.quad(lambda u: mp.asin(corr(u,s)), [0,s]) +
            mp.quad(lambda u: mp.asin(corr(u,s)), [s,1]))/mp.pi

def explained(s,t):
    cc=c(s,t)
    return (a(s)**2+a(t)**2-2*cc*a(s)*a(t))/(1-cc**2)

def symmetric_explained(s):
    return 2*a(s)**2/(1+2/mp.pi*mp.asin(s/(1-s)))

def deriv(s):
    ap=(1/mp.sqrt(s)-1/mp.sqrt(1-s))/4
    cc=2/mp.pi*mp.asin(s/(1-s))
    cp=2/(mp.pi*(1-s)*mp.sqrt(1-2*s))
    return 2*ap/a(s)-cp/(1+cc)

def near(x,y,eps=mp.mpf('1e-28')):
    if abs(x-y)>eps:
        raise AssertionError((mp.nstr(x,45),mp.nstr(y,45),mp.nstr(abs(x-y),35)))

checks=0
for n in [mp.mpf('0.08'),mp.mpf('0.2'),mp.mpf('0.333333333333333'),
          mp.mpf('0.5'),mp.mpf('0.67'),mp.mpf('0.89')]:
    near(a_integral(n),a(n)); checks+=1

for s,t in [(mp.mpf('0.1'),mp.mpf('0.25')),
            (mp.mpf('0.16'),mp.mpf('0.73')),
            (mp.mpf('0.333333333333333'),mp.mpf('0.666666666666667')),
            (mp.mpf('0.4'),mp.mpf('0.9'))]:
    cc=c(s,t)
    al=(a(s)-cc*a(t))/(1-cc*cc)
    be=(a(t)-cc*a(s))/(1-cc*cc)
    near(al+cc*be,a(s)); checks+=1
    near(cc*al+be,a(t)); checks+=1
    near(explained(s,t),al*a(s)+be*a(t)); checks+=1
    assert 0 < explained(s,t) < mp.mpf(1)/12; checks+=1

one_third=mp.mpf(1)/3
two_thirds=2*one_third
near(c(one_third,two_thirds),one_third); checks+=1
tri=(3+mp.sqrt(2)-mp.sqrt(3)-mp.sqrt(6))/4
near(explained(one_third,two_thirds),tri); checks+=1
near(explained(one_third,two_thirds),symmetric_explained(one_third)); checks+=1
single_midpoint=(3-2*mp.sqrt(2))/4
near(a(mp.mpf(1)/2)**2,single_midpoint);checks+=1
assert tri>single_midpoint; checks+=1

root=mp.findroot(deriv,(mp.mpf('.33678'),mp.mpf('.33679')))
assert mp.mpf('.33678')<root<mp.mpf('.33679');checks+=1
near(deriv(root),0);checks+=1
near(symmetric_explained(root),explained(root,1-root));checks+=1
assert symmetric_explained(root)>tri;checks+=1
for ds in [mp.mpf('0.00001'),mp.mpf('0.002'),mp.mpf('0.02'),mp.mpf('0.1')]:
    assert symmetric_explained(root)>symmetric_explained(root-ds);checks+=1
    if root+ds <mp.mpf('.5'):
        assert symmetric_explained(root)>symmetric_explained(root+ds);checks+=1

# Deterministic stress grid verifies bounded conditional-variance formula;
# it is not a substitute for analytic all-pair correctness or uniqueness.
for i in range(2,35):
    for j in range(i+1,39):
        s=mp.mpf(i)/40;t=mp.mpf(j)/40
        cc=c(s,t)
        alpha=(a(s)-cc*a(t))/(1-cc*cc)
        beta=(a(t)-cc*a(s))/(1-cc*cc)
        near(explained(s,t),a(s)*alpha+a(t)*beta);checks+=1
        assert 0 <= explained(s,t) <= mp.mpf(1)/12; checks+=1

print('Checks passed:',checks)
print('symmetric_optimal_s:',mp.nstr(root,50))
print('symmetric_optimal_t:',mp.nstr(1-root,50))
print('explained_variance:',mp.nstr(symmetric_explained(root),50))
print('explained_fraction:',mp.nstr(12*symmetric_explained(root),50))
print('trisection_explained_variance:',mp.nstr(tri,50))
print('trisection_explained_fraction:',mp.nstr(12*tri,50))
print('single_midpoint_explained_fraction:',mp.nstr(12*single_midpoint,50))
