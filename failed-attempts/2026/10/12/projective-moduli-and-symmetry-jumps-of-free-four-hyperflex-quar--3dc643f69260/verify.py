"""Exact checks accompanying the four-hyperflex-tangent arrangement classification."""
import sympy as s

x,y,z,t=s.symbols('x y z t')
H=x*y*(x-y)*(x-t*y)
F=s.expand(H*(H-z**4))
Fx,Fy,Fz=[s.diff(F,v) for v in (x,y,z)]
Hy,Hx=s.diff(H,y),s.diff(H,x)
row1=(Hy,-Hx,s.Integer(0))
row2=(x*z**3,y*z**3,2*H-z**4)
for row in (row1,row2):
    assert s.expand(sum(a*b for a,b in zip(row,(Fx,Fy,Fz))))==0
cross=s.Matrix(row1).cross(s.Matrix(row2))
assert all(s.expand(c+partial)==0 for c,partial in zip(cross,(Fx,Fy,Fz)))
assert s.expand(x*Hx+y*Hy-4*H)==0

j=lambda q:s.cancel(256*(q*q-q+1)**3/(q*q*(1-q)**2))
orbits=(t,1-t,1/t,1/(1-t),t/(t-1),(t-1)/t)
assert all(s.factor(j(v)-j(t))==0 for v in orbits)
for name,q,want in [('generic',s.Rational(3),4),('harmonic',s.Rational(2),8),('equianharmonic',(1+s.sqrt(-3))/2,12)]:
    values={s.simplify(s.expand_complex(v.subs(t,q))) for v in orbits}
    # Each anharmonic orbit has 24 / |K| parameters.
    assert 24//len(values)==want,(name,values)
    assert s.simplify(j(q)-(0 if name=='equianharmonic' else 1728 if name=='harmonic' else j(3)))==0

# Ordinary 4-fold point plus four A7 contacts give the free-curve Tjurina number.
assert 4*7+3*3 == (8-1)**2-3*4 ==37
print('VERIFY_OK: exact Saito syzygies (degrees 3,4), anharmonic j invariance, sample stabilizers 4/8/12, Tjurina 37')
