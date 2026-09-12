import sympy as sp

# 1. Quadric smoothness via determinants
M1 = sp.Matrix([[0,0,0,sp.Rational(1,2)],[0,0,sp.Rational(-1,2),0],[0,sp.Rational(-1,2),0,0],[sp.Rational(1,2),0,0,0]])
M2 = sp.Matrix([[1,0,0,sp.Rational(-1,2)],[0,1,sp.Rational(-1,2),0],[0,sp.Rational(-1,2),1,0],[sp.Rational(-1,2),0,0,1]])
print("det M1 =", M1.det(), " det M2 =", M2.det())

# 2. E in Segre coords: B=(s0^2+s1^2)(t0^2+t1^2)-2 s0 s1 t0 t1 ; smoothness on P1xP1
s0,s1,t0,t1 = sp.symbols('s0 s1 t0 t1')
B = (s0**2+s1**2)*(t0**2+t1**2) - 2*s0*s1*t0*t1
# check bidegree (2,2) and smoothness in the 4 affine charts
for (sv,tv) in [(1,1),(1,0),(0,1),(0,0)]:
    pass
# chart s1=t1=1
s,t = sp.symbols('s t')
b = (s**2+1)*(t**2+1) - 2*s*t
bs, bt = sp.diff(b,s), sp.diff(b,t)
G = sp.groebner([b, bs, bt, s*t-1], s, t, order='lex')  # placeholder; do resultants below
print("b =", b)
# resultant in t of (b, bt): common zeros in this chart
res = sp.resultant(b, bt, t)
print("Res_t(b,db/dt) =", sp.factor(res))
# resultant in s of (b, bs)
res2 = sp.resultant(b, bs, s)
print("Res_s(b,db/ds) =", sp.factor(res2))
# charts at infinity: s1=0 or t1=0
# s1=0: B| = s0^2(t0^2+t1^2); with s0=1: t0^2+t1^2=0 -> points; check gradient nonzero there
print("B(s0,0,t0,t1) =", sp.expand(B.subs({s1:0})))
print("dB/ds1 at (1,0,t0,t1) =", sp.diff(B,s1).subs({s0:1,s1:0}))
