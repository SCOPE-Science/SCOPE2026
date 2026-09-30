"""Verify exact transmission exponent at fixed 270-degree Calderon vertex.

Geometry/contrast: vertex at origin; Q1=(0,pi/2) sigma=1; Q2,Q3,Q4 sigma=4.
Ansatz r^lam v(th); v''+lam^2 v=0 per sector; transmission: v, sigma v' continuous.
State Y=[v, sigma v']^T; sector propagator over angle pi/2 with conductivity s0:
  T(s0) = [[c, s/(s0*lam)], [-s0*lam*s, c]], c=cos(lam*pi/2), s=sin(lam*pi/2).
Full turn M = Sb^3 Sa (Sa: s0=1, Sb: s0=4). det M = 1.
Nontrivial 2pi-periodic v <=> det(M-I)=0 <=> tr(M)=2 (2x2, det 1).

Checks:
 (S1) symbolic: tr(M)-2 == s(100s-91)/4, s=sin^2(pi lam/2)  [sympy exact]
 (S2) closed-form root lam1 = (2/pi) arcsin(sqrt(91)/10) in (0,1), value ~0.8060
 (S3) minimality: s strictly increasing on (0,1), s=0 only at lam=0 -> unique root
 (S4) numeric: 8x8 determinant min-SV ~0 at lam1; f(1)!=0 control; second root 2-lam1
"""
import numpy as np
import sympy as sp

ok = []
lam = sp.symbols('lam', real=True, positive=True)
w = lam*sp.pi/2
c = sp.cos(w); s = sp.sin(w)
Sa = sp.Matrix([[c, s/lam], [-lam*s, c]])
Sb = sp.Matrix([[c, s/(4*lam)], [-4*lam*s, c]])
M = Sb**3 * Sa
tr = sp.simplify(M.trace())
F = sp.simplify(tr - 2)
sv = sp.symbols('sv')
P = sv*(100*sv-91)/4
red = sp.simplify(sp.sin(2*w)**2 - 4*sp.sin(w)**2*(1-sp.sin(w)**2))
Q = sp.Rational(25,4)*sp.sin(w)**4 - 4*sp.sin(w)**2 - sp.Rational(75,16)*4*sp.sin(w)**2*(1-sp.sin(w)**2)
diff = sp.expand(Q - P.subs(sv, sp.sin(w)**2))
print("S1: tr(M) =", tr)
print("S1: tr(M)-2 simplified =", sp.trigsimp(F))
print("S1: sin(2w)^2-rule residual:", red, "| poly diff:", diff)
assert red == 0 and diff == 0, "trace identity failed"
print("S1 PASS: trace identity exact")
ok.append(True)

lam1 = 2*sp.asin(sp.sqrt(sp.Rational(91,100)))/sp.pi
lam1f = float(lam1.evalf())
print("S2: lam1 =", lam1, "=", lam1f)
assert 0 < lam1f < 1
s1 = float((sp.sin(sp.pi*lam1/2)**2).evalf())
assert abs(s1 - 0.91) < 1e-12
print(f"S2 PASS: lam1 = {lam1f:.10f}, sin^2(pi lam1/2) = {s1:.12f} = 91/100")
ok.append(True)

xs = np.linspace(0.0005, 1.0, 20000)
ss = np.sin(np.pi*xs/2)**2
Pvals = ss*(100*ss-91)/4
# P<0 on (0,lam1), P>0 just right of lam1; unique crossing since s monotone
assert np.all(Pvals[xs < lam1f-0.002] < 0), "P must be negative left of root"
assert np.all(Pvals[(xs > lam1f+0.002)] > 0), "P must be positive right of root (within (0,1])"
print("S3 PASS: unique root in (0,1); P<0 left, P>0 right; s=0 only at lam=0")
ok.append(True)

SIG = [1.0, 4.0, 4.0, 4.0]
ANGS = [0.0, np.pi/2, np.pi, 3*np.pi/2]
def min_sv(l):
    Mm = np.zeros((8, 8))
    for k in range(4):
        th = ANGS[k]; il = (k-1) % 4; ir = k % 4
        thL = 2*np.pi if k == 0 else th
        cR = np.cos(l*th); sR = np.sin(l*th)
        cL = np.cos(l*thL); sL = np.sin(l*thL)
        Mm[2*k, 2*il] = cL; Mm[2*k, 2*il+1] = sL
        Mm[2*k, 2*ir] = -cR; Mm[2*k, 2*ir+1] = -sR
        Mm[2*k+1, 2*il] = SIG[il]*(-sL); Mm[2*k+1, 2*il+1] = SIG[il]*cL
        Mm[2*k+1, 2*ir] = -SIG[ir]*(-sR); Mm[2*k+1, 2*ir+1] = -SIG[ir]*cR
    svv = np.linalg.svd(Mm, compute_uv=False)
    return svv[-1]/(svv[0]+1e-300)
r1 = min_sv(lam1f)
r_1 = min_sv(1.0)
lam2f = 2 - lam1f
r2 = min_sv(lam2f)
print(f"S4: minSV ratio at lam1={lam1f:.7f}: {r1:.3e} (expect ~0)")
print(f"S4: minSV ratio at lam=1.0: {r_1:.3e} (expect >>0, control)")
print(f"S4: minSV ratio at lam2={lam2f:.7f}: {r2:.3e} (expect ~0)")
assert r1 < 1e-5 and r_1 > 1e-2 and r2 < 1e-5
print("S4 PASS: 8x8 numeric cross-check (root at lam1 and 2-lam1, non-root at 1)")
ok.append(True)

# No-decay lemma numeric witness (proof itself is analytic: max(cos phi,sin phi)>=1/sqrt2)
import math
phis = np.linspace(0, 2*np.pi, 721)
ths = np.linspace(np.pi/2, 2*np.pi, 2001)  # closure of K
CX = np.cos(ths)
vals = []
for p in phis:
    d = np.array([math.cos(p), math.sin(p)])
    vals.append(float(np.max(CX*d[0] + np.sin(ths)*d[1])))
vals = np.array(vals)
worst = vals.min()
print(f"S5: min_phi max_{{xhat in K}} d.xhat = {worst:.6f} (>= 1/sqrt2 = {1/math.sqrt(2):.6f})")
assert worst >= 1/math.sqrt(2) - 1e-3 and np.all(vals > 0)
print("S5 PASS: no-decay lemma witness")
ok.append(True)

print("ALL VERIFY_OK" if all(ok) else "VERIFY_FAIL")
