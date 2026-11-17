"""Exact algebra checks for multiseason quadratic population return; SymPy required."""
import sympy as s
x,p,q=s.symbols('x p q', real=True)
for d in [2,4,8,16]:
    xc=s.Rational(d-1,2*d-1)
    qc=s.Rational(2*d-1,d*d)
    pc=(s.Rational(2*d-1,2*(d-1))**(d-1))/2
    F=p*(1-q*(1-x)**2)**d
    vals={x:xc,p:pc,q:qc}
    assert s.simplify((F-x).subs(vals)) == 0
    assert s.simplify((s.diff(F,x)-1).subs(vals)) == 0
    assert s.simplify(s.diff(F,x,2).subs(vals)) == 0
    assert s.simplify(s.diff(F,x,3).subs(vals)) == -s.Rational((2*d-1)**3,d*d*(d-1))
    for qv in [s.Rational(1,2),s.Rational(3,4),s.Rational(9,10)]:
        if qv<=qc: continue
        z=s.sqrt((d-1)**2-(2*d-1)*(1/qv-1))
        for t in [(d-1-z)/(2*d-1),(d-1+z)/(2*d-1)]:
            pr=s.simplify(t/(1-qv*(1-t)**2)**d)
            assert s.simplify((F-x).subs({x:t,q:qv,p:pr}))==0
            assert s.simplify((s.diff(F,x)-1).subs({x:t,q:qv,p:pr}))==0
# Exact polynomial Sturm count in the physical interval and numerical multipliers.
w=s.Rational(22,25)*(1-s.Rational(1,2)*(1-x)**2)**4
assert s.polys.polytools.count_roots(w-x,0,1)==3
rr=s.nroots(w-x,maxsteps=200)
real=[float(s.re(z)) for z in rr if abs(float(s.im(z)))<1e-10 and 0<float(s.re(z))<1]
assert len(real)==3
mult=[float(s.diff(w,x).subs(x,z)) for z in real]
assert mult[0]<1 and mult[1]>1 and mult[2]<1
assert max(abs(a-b) for a,b in zip(real,[0.135164498510195,0.412684328499179,0.830532482392202]))<1e-10
print('MULTISEASON_STOCHASTIC_CUSP_OK symbolic_depths=4 exact_witness_roots=3')
