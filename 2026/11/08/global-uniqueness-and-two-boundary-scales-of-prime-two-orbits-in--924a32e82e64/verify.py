#!/usr/bin/env python3
"""Symbolic and high-precision spot checks of the global two-cycle census.
Requires sympy and mpmath. Finite checks corroborate, but do not replace, the analytic proof.
"""
import sympy as sp
import mpmath as mp

s, p, c, m, u, v = sp.symbols('s p c m u v')
p_s = s*(s-1)*(c+m*s)/(c+m*(2*s-1))
R_s = (c+m*(2*s-1))/((s-1)*(c+m*s)*(c+m*(s-1)))
Q_s = 2*m*s*s+3*(c-m)*s-4*c
S2 = s*s-4*p_s
C2 = 1-s+p_s
checks = {
    'equal_weighted_orbit_equation': sp.factor((u*u*(1-u)*(c+m*u)-v*v*(1-v)*(c+m*v))/(u-v) - (s*(1-s)*(c+m*s)+p*(c+m*(2*s-1))).subs({s:u+v,p:u*v})),
    'weighted_equation_vanishes': sp.factor(s*(1-s)*(c+m*s)+p_s*(c+m*(2*s-1))),
    'sum_orbit_equation': sp.factor(c*(s-s*s+2*p_s)+m*(s*s-s**3+(3*s-2)*p_s)-s/R_s),
    'discriminant': sp.factor(S2+s*Q_s/(c+m*(2*s-1))),
    'complementary_product': sp.factor(C2-(s-1)**2*(c+m*(s-1))/(c+m*(2*s-1))),
}
for k, residual in checks.items():
    if residual != 0:
        raise AssertionError((k,residual))
mp.mp.dps=65
examples=[(1,0),(0,1),(mp.mpf('0.5'),mp.mpf('0.5')),(mp.mpf('.75'),mp.mpf('.25')),(mp.mpf('.2'),mp.mpf('.8')),(mp.mpf('0.9'),mp.mpf('0.01'))]
num=0
for cv,mv in examples:
    cv,mv=mp.mpf(cv),mp.mpf(mv)
    ss=(mp.mpf(4)/3 if mv==0 else (3*(mv-cv)+mp.sqrt(9*(mv-cv)**2+32*mv*cv))/(4*mv))
    def RR(z): return (cv+mv*(2*z-1))/((z-1)*(cv+mv*z)*(cv+mv*(z-1)))
    def ff(z,r): return r*z*(1-z)*(cv+mv*z)
    rc=RR(ss)
    assert 1<ss<2 and rc>0
    for factor in ['1.001','1.01','1.2','2','4','20','1000']:
        r=rc*mp.mpf(factor)
        lo,hi=mp.mpf(1),ss
        for _ in range(235):
            mid=(lo+hi)/2
            if RR(mid)>r: lo=mid
            else: hi=mid
        z=(lo+hi)/2
        pp=z*(z-1)*(cv+mv*z)/(cv+mv*(2*z-1))
        disc=z*z-4*pp
        assert disc>0
        uu=(z-mp.sqrt(disc))/2; vv=(z+mp.sqrt(disc))/2
        assert 0<uu<vv<1
        assert abs(ff(uu,r)-vv)<mp.mpf('1e-40')
        assert abs(ff(vv,r)-uu)<mp.mpf('1e-40')
        num+=1
    for power in [5,9]:
        r=mp.power(10,power)
        if r<=rc:continue
        lo,hi=mp.mpf(1),ss
        for _ in range(340):
            mid=(lo+hi)/2
            if RR(mid)>r:lo=mid
            else:hi=mid
        z=(lo+hi)/2
        pp=z*(z-1)*(cv+mv*z)/(cv+mv*(2*z-1))
        disc=z*z-4*pp
        uu=(z-mp.sqrt(disc))/2; vv=(z+mp.sqrt(disc))/2
        if cv>0:
            assert abs(uu*cv*r-1)<mp.mpf('.005')
            assert abs((1-vv)*cv*(cv+mv)*r*r-1)<mp.mpf('.005')
        else:
            assert abs(uu*mp.sqrt(mv*r)-1)<mp.mpf('.005')
            assert abs((1-vv)*(mv*r)**mp.mpf('1.5')-1)<mp.mpf('.005')
        num+=1
print(f'VERIFY_OK symbolic_identities={len(checks)} high_precision_cycle_and_boundary_cases={num} precision_digits={mp.mp.dps}')
