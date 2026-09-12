import sympy as sp

# --- Z: 8 points proof numeric check ---
# s values with s^4+1=0 (s1=1): zeta_k
import cmath
zetas = [cmath.exp(1j*cmath.pi/4 + k*1j*cmath.pi/2) for k in range(4)]
print("zeta^4+1:", [z**4+1 for z in zetas])
for z in zetas:
    A = z**2
    # (A+1)(t^2+1)-2 z t=0
    a=(A+1); b=-2*z; c=(A+1)
    disc = b**2-4*a*c
    t1=(-b+cmath.sqrt(disc))/(2*a); t2=(-b-cmath.sqrt(disc))/(2*a)
    print(f"s={z:.4f} A={A:.4f} t1={t1:.4f} t1^4+1={t1**4+1:.2e} t2={t2:.4f} t2^4+1={t2**4+1:.2e}")

# --- gradient check at one Z point (affine x3=1): x=(i,zeta,zeta,1) ---
x0,x1,x2 = sp.symbols('x0 x1 x2')
F1 = x0*1 - x1*x2
F2 = x0**2+x1**2+x2**2+1 - x0*1 - x1*x2
G = x0**4+x1**4+x2**4+1
z = sp.exp(sp.I*sp.pi/4)  # symbolic? use root of x^4+1: represent via sqrt
# use explicit radix: (1+i)/sqrt(2)
s = (1+sp.I)/sp.sqrt(2)
pt = {x0: sp.I, x1: s, x2: s}
print("F1(pt)=", sp.simplify(F1.subs(pt)), "F2(pt)=", sp.simplify(F2.subs(pt)), "G(pt)=", sp.simplify(G.subs(pt)))
dF1 = [sp.diff(F1,v).subs(pt) for v in (x0,x1,x2)]
dF2 = [sp.diff(F2,v).subs(pt) for v in (x0,x1,x2)]
dG = [sp.diff(G,v).subs(pt) for v in (x0,x1,x2)]
print("dF1=", [sp.simplify(x) for x in dF1])
print("dF2=", [sp.simplify(x) for x in dF2])
print("dG =", [sp.simplify(x) for x in dG])
M = sp.Matrix([[sp.simplify(a) for a in dF1],[sp.simplify(a) for a in dF2],[sp.simplify(a) for a in dG]])
print("rank(dF1,dF2,dG) =", M.rank())
# express dG = a dF1 + b dF2 ?
a,b = sp.symbols('a b')
sol = sp.Matrix([[dF1[0],dF2[0]],[dF1[1],dF2[1]]]).LUsolve(sp.Matrix([dG[0],dG[1]]))
print("coeffs a,b =", [sp.simplify(x) for x in sol])
print("check 3rd:", sp.simplify(sol[0]*dF1[2]+sol[1]*dF2[2]-dG[2]))
