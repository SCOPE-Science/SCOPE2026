"""Arithmetic and finite-trajectory checks for the two-patch rescue theorem.

Run: python verify.py
Only Python's standard library is required. These finite checks support, but do not
replace, the analytical global-manifold proof in RESULT.md.
"""
from fractions import Fraction as Q
from math import sqrt, log, exp, isfinite

checks = 0

# Algebraic cancellation for u' / u + p v' / v, sampled at rational points.
for s_i in (2, 3, 5):
    for d_i in (1, 2, 4):
        s, d = Q(s_i, 3), Q(d_i, 5)
        p, B = d / (s + d), s * d / (s + d)
        for e_i in (2, 4, 7):
            e = Q(e_i, 8)
            for h_i in (1, 3, 7):
                h = Q(h_i, 6)
                for m_i in (1, 2, 5):
                    m = Q(m_i, 7)
                    for u_i in (1, 3, 9):
                        u = Q(u_i, 10)
                        for v_i in (2, 5, 11):
                            v = Q(v_i, 4)
                            Lu = u/(m+u) - e - (h+d)*u + d*v
                            Lv = s + d*u - (s+d)*v
                            f = u/(m+u) - (e-B) - (h+B)*u
                            assert Lu + p*Lv == f
                            checks += 1

def ode_coeff(s, d, e, h, m):
    B = s*d/(s+d)
    L, E, p = h+B, e-B, d/(s+d)
    assert B < e < min(s, 1) and m < (1-sqrt(E))**2/L
    bb = m*L+E-1
    discriminant = bb*bb-4*L*m*E
    lo = (-bb-sqrt(discriminant))/(2*L)
    hi = (-bb+sqrt(discriminant))/(2*L)
    vlow = (s+d*lo)/(s+d)
    return B, L, E, p, lo, hi, vlow

def compute_curve(s, d, e, h, m):
    global checks
    B,L,E,p,lo,hi,vlow = ode_coeff(s,d,e,h,m)
    assert 0 < lo < hi
    for u in (lo, hi):
        v=(s+d*u)/(s+d)
        assert abs(u/(m+u)-E-L*u) < 5e-13
        J11=u*(m/(m+u)**2-(h+d))
        J12=d*u
        J21=d*v
        J22=-(s+d)*v
        determinant=J11*J22-J12*J21
        assert abs(determinant+(s+d)*u*v*(m/(m+u)**2-L))<1e-12
        checks += 2
    J11=lo*(m/(m+lo)**2-(h+d))
    J12=d*lo
    J21=d*vlow
    J22=-(s+d)*vlow
    tr=J11+J22
    det=J11*J22-J12*J21
    assert det < 0
    stable=(tr-sqrt(tr*tr-4*det))/2
    slope=-J12/(J11-stable)  # negative u displacement / positive v displacement
    assert slope<0
    checks += 2
    vstart=vlow+1e-7
    u=lo+slope*1e-7
    x=log(vstart)
    target=[1e2,1e3,1e4,1e5,1e6,1e7]
    observed={}
    def dudx(x,y):
        v=exp(x)
        fu=y*(y/(m+y)-e-(h+d)*y+d*v)
        fv=v*(s+d*y-(s+d)*v)
        return v*fu/fv
    for vtarget in target:
        xend=log(vtarget)
        steps=3000
        dx=(xend-x)/steps
        for i in range(steps):
            if i in (0,steps//4,steps//2,steps-1):
                assert u>0 and u<lo and isfinite(u)
                checks+=1
            x_new=x+dx
            k1=dudx(x,u)
            k2=dudx(x+dx/2,u+dx*k1/2)
            k3=dudx(x+dx/2,u+dx*k2/2)
            k4=dudx(x_new,u+dx*k3)
            u +=dx*(k1+2*k2+2*k3+k4)/6
            x=x_new
        x=xend
        observed[vtarget]=u*vtarget**p
    assert all(v in observed for v in target)
    hlast=observed[1e7]
    C=hlast*exp(E/((s+d)*1e7))
    assert C>lo*vlow**p
    # The implied limit of v*(1-u(v)*v**p/C) is E/(s+d).
    for v in (1e4,1e5,1e6):
        approx=v*(1-observed[v]/C)
        assert abs(approx-E/(s+d))<0.7*(v**(-p)), (v,approx,E/(s+d))
        checks+=1
    # Ratios at a decade apart should approach 10^(-p).
    for v in (1e4,1e5):
        observed_u1=observed[v]/v**p
        observed_u2=observed[10*v]/(10*v)**p
        assert abs(observed_u2/observed_u1-10**(-p))<0.002
        checks+=1
    print('parameters',s,d,e,h,m,'p',round(p,8),'C',round(C,11),'observed H at v=1e6',round(observed[1e6],11))

for pars in ((.8,.4,.5,.3,.2),(.9,.2,.45,.5,.1),(1.2,.5,.62,.35,.15)):
    compute_curve(*pars)
print('VERIFY_OK',checks,'exact rational and numerical checks')
