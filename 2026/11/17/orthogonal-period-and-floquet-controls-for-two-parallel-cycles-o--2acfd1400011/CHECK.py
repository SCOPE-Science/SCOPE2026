"""Exact identities and independent high-precision return-integral checks.

Run: python CHECK.py
Requires Python 3, SymPy and mpmath.
The integration checks supplement, but do not replace, the analytic proof.
"""
import sympy as sp
import mpmath as mp

x, y, z, a, p, q, u, v, w, sig = sp.symbols(
    "x y z a p q u v w sig", real=True
)
B = p*x + q*y
f = w + u*x + v*y
P = z*(x*B-a*a*p)/2 + f*y
Q = z*(y*B-a*a*q)/2 - f*x
R = B*(z*z-1)
U = x*x+y*y-a*a
H = U*U+z*z-1
assert sp.expand(2*x*P+2*y*Q-z*B*U) == 0
assert sp.expand(sp.diff(H,x)*P+sp.diff(H,y)*Q+sp.diff(H,z)*R-2*z*B*H) == 0
assert sp.expand(x*Q-y*P+(x*x+y*y)*f-z*a*a*(p*y-q*x)/2) == 0
Aplus = sp.Matrix([u+q/2,v-p/2])
Aminus = sp.Matrix([u-q/2,v+p/2])
BB = sp.Matrix([p,q])
assert sp.simplify(BB.dot(Aplus)-p*u-q*v) == 0
assert sp.simplify(BB.dot(Aminus)-p*u-q*v) == 0
assert sp.simplify(Aplus.dot(Aplus)-Aminus.dot(Aminus)-2*(u*q-v*p)) == 0
print("EXACT_TANGENCY_ANGULAR_AND_SPLITTING_IDENTITIES_OK")

mp.mp.dps=45
cases=[(2,1,0,1,0,5), (2,1,0,0,1,5),
       (mp.mpf('1.5'),mp.mpf('0.4'),mp.mpf('-0.7'),mp.mpf('0.25'),mp.mpf('0.8'),-7),
       (3,mp.mpf('-1.2'),mp.mpf('0.2'),mp.mpf('0.4'),mp.mpf('0.4'),8)]
for a0,p0,q0,u0,v0,w0 in cases:
    for s0 in [-1,1]:
        ax=u0+s0*q0/2
        ay=v0-s0*p0/2
        delta=mp.sqrt(w0*w0-a0*a0*(ax*ax+ay*ay))
        assert delta > 0
        T=2*mp.pi/delta
        logmu=(-2*mp.pi*s0*mp.sign(w0)*a0*a0*(p0*u0+q0*v0)
               /(delta*(abs(w0)+delta)))
        def speed(th):
            return abs(w0+a0*(ax*mp.cos(th)+ay*mp.sin(th)))
        # Split the smooth trigonometric integrals at quadrants.
        pieces=[0,mp.pi/2,mp.pi,3*mp.pi/2,2*mp.pi]
        T_direct=mp.quad(lambda th:1/speed(th),pieces)
        logmu_direct=mp.quad(
            lambda th:s0*a0*(p0*mp.cos(th)+q0*mp.sin(th))/speed(th),pieces)
        assert mp.almosteq(T,T_direct,rel_eps=mp.mpf('1e-35'))
        assert mp.almosteq(logmu,logmu_direct,abs_eps=mp.mpf('1e-35'))
print("EIGHT_ORIGINAL_TIME_AND_FLOQUET_QUADRATURES_OK")

# Concrete independence witnesses, both with two periodic parallels.
a0,p0,q0,w0=2,1,0,5
u0,v0=1,0
for s0 in [-1,1]:
    delta=mp.sqrt(w0*w0-a0*a0*(u0*u0+(v0-s0*p0/2)**2))
    assert mp.almosteq(delta,mp.sqrt(20))
    logmu=-2*mp.pi*s0*a0*a0*p0*u0/(delta*(w0+delta))
    assert (logmu<0)==(s0==1)
u0,v0=0,1
assert p0*u0+q0*v0==0
assert (u0*q0-v0*p0)!=0
print("ORTHOGONAL_CLOCK_AND_STABILITY_WITNESSES_OK")
