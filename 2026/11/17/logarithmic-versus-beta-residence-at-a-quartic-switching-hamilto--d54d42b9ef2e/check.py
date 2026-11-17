"""Independent numerical and algebraic checks for a piecewise quartic Hamiltonian center.
Uses mpmath, sympy, and Python's standard library.
Run: python check.py
"""
import mpmath as mp
mp.mp.dps = 50

def quantities(a,b,E):
    a,b,E=map(mp.mpf,(a,b,E))
    m=4*a*E
    K=mp.ellipk(-m); Q=mp.ellipe(-m)
    tp=2*K
    ap=4*E*((1+1/m)*K-Q/m)
    u2=(-1+mp.sqrt(1+16*b*E))/(4*b)
    u=mp.sqrt(u2)
    c=2*b*u2
    tm=2*mp.quad(lambda phi: 1/mp.sqrt(1+c*(1+mp.sin(phi)**2)),[0,mp.pi/6,mp.pi/3,mp.pi/2])
    am=2*u2*mp.quad(lambda phi: mp.cos(phi)**2*mp.sqrt(1+c*(1+mp.sin(phi)**2)),[0,mp.pi/6,mp.pi/3,mp.pi/2])
    return tp,tm,ap,am,u

def numerical_suite():
    a=mp.mpf('0.6'); b=mp.mpf('1.75'); B1=mp.beta(mp.mpf('0.25'),mp.mpf('0.5')); B2=mp.beta(mp.mpf('0.25'),mp.mpf('1.5'))
    for E in [1,10,1000,1000000]:
        E=mp.mpf(E)
        tp,tm,ap,am,u=quantities(a,b,E)
        # Independent direct integral for upper period and area.
        t_direct=2*mp.quad(lambda phi: 1/mp.sqrt(1+4*a*E*mp.sin(phi)**2),[0,mp.pi/6,mp.pi/3,mp.pi/2])
        a_direct=4*E*mp.quad(lambda phi: mp.cos(phi)**2/mp.sqrt(1+4*a*E*mp.sin(phi)**2),[0,mp.pi/6,mp.pi/3,mp.pi/2])
        assert mp.almosteq(tp,t_direct,rel_eps=mp.mpf('1e-40'))
        assert mp.almosteq(ap,a_direct,rel_eps=mp.mpf('1e-40'))
        # Action/time derivative identity (independent numerical differentiation).
        dA=mp.diff(lambda e: quantities(a,b,e)[2],E)
        assert abs(dA/tp-1)<mp.mpf('1e-37')
        dA=mp.diff(lambda e: quantities(a,b,e)[3],E,addprec=30)
        assert abs(dA/tm-1)<mp.mpf('1e-34')
        print('energy',mp.nstr(E,8),'periods',mp.nstr(tp,12),mp.nstr(tm,12),'areas',mp.nstr(ap,12),mp.nstr(am,12))
        if E>100:
            upperT=mp.log(E)/(2*mp.sqrt(a*E))
            lowerT=(mp.sqrt(2)/4)*b**(-mp.mpf('0.25'))*E**(-mp.mpf('0.25'))*B1
            upperA=mp.sqrt(E/a)*mp.log(E)
            lowerA=(mp.sqrt(2)/2)*b**(-mp.mpf('0.25'))*E**(mp.mpf('0.75'))*B2
            print('  leading-law ratios',*[mp.nstr(x,12) for x in (tp/upperT,tm/lowerT,ap/upperA,am/lowerA)])
            print('  time/area share ratio',mp.nstr((tp/(tp+tm))/(ap/(ap+am)),12))
        assert tp>0 and tm>0 and ap>0 and am>0
    assert mp.almosteq(B2/B1,mp.mpf(2)/3)
    # Exact Hamiltonian energy for the upper and lower vector fields.
    import sympy as sp
    x,y,aS,bS=sp.symbols('x y a b',real=True)
    hp=(x*x+y*y)/2+aS*x*x*y*y
    hm=(x*x+y*y)/2+bS*y**4
    assert sp.simplify(sp.diff(hp,x)*(-sp.diff(hp,y))+sp.diff(hp,y)*sp.diff(hp,x))==0
    assert sp.simplify(sp.diff(hm,x)*(-sp.diff(hm,y))+sp.diff(hm,y)*sp.diff(hm,x))==0
    assert sp.expand(hp.subs(y,0)-hm.subs(y,0))==0
    # Conditional upper-side logarithmic level profile for very large energy.
    E=mp.mpf(10)**50
    tp,tm,ap,am,u=quantities(a,b,E)
    for v in [mp.mpf('0.25'),mp.mpf('0.5'),mp.mpf('0.75')]:
        phi=mp.asin(E**(v/2)/mp.sqrt(2*E))
        F=2*mp.quad(lambda q: 1/mp.sqrt(1+4*a*E*mp.sin(q)**2),[0,phi])/tp
        FA=4*E*mp.quad(lambda q: mp.cos(q)**2/mp.sqrt(1+4*a*E*mp.sin(q)**2),[0,phi])/ap
        print('upper log CDF at',mp.nstr(v,4),': time',mp.nstr(F,9), 'area',mp.nstr(FA,9))
        assert abs(F-v)<mp.mpf('0.04') and abs(FA-v)<mp.mpf('0.04')
    # Lower-side conditional distribution, compared to its Beta limit.
    E=mp.mpf(10)**10
    tp,tm,ap,am,u=quantities(a,b,E)
    c=2*b*u*u
    for z in [mp.mpf('0.3'),mp.mpf('0.7')]:
        phi=mp.asin(z)
        F=2*mp.quad(lambda q: 1/mp.sqrt(1+c*(1+mp.sin(q)**2)),[0,phi])/tm
        target=mp.betainc(mp.mpf('0.25'),mp.mpf('0.5'),0,z**4,regularized=True)
        FA=2*u*u*mp.quad(lambda q: mp.cos(q)**2*mp.sqrt(1+c*(1+mp.sin(q)**2)),[0,phi])/am
        targetA=mp.betainc(mp.mpf('0.25'),mp.mpf('1.5'),0,z**4,regularized=True)
        assert abs(F-target)<mp.mpf('0.005') and abs(FA-targetA)<mp.mpf('0.005')
    print('QUARTIC_SWITCHING_LOG_BETA_AREA_CHECK_OK')
if __name__=='__main__': numerical_suite()
