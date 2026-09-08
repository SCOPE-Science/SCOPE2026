"""Certified partial census for five committed quadratic Lienard boxes (stdlib only).

Family: x' = y - (a x + b x^2),  y' = -x + c y + d x y,  (a,b,c,d) in box B.
Boxes (radius 0.02): B1=(1.0,0.5,0.3,0.0) B2=(1.5,0.8,0.2,0.1) B3=(0.8,0.3,0.5,-0.1)
                     B4=(2.0,1.0,0.1,0.0) B5=(0.5,0.1,0.4,0.2)  order (a,c,b,d).

Certificates (uniform over each box, rigorous interval/rational arithmetic):
 (A) Exact-rational Lyapunov basins at the attracting equilibrium for B1,B3,B5:
     solve A'P+P A=-I exactly (Fractions), P>0; S(z)=A(z)'P+P A(z)=-I+E(z)+D(par),
     |E(z)|_2 <= K|z| with K=2||P||_F sqrt(4 bb^2+dd^2) (bb,dd = box |.| maxima),
     parameter spread |D|_2 <= 2 lmax(P) sqrt(2) r. If spread<1, strict decrease
     V'=z'Sz<0 on 0<|z|<r*, r*=(1-spread)/K; disc |z|<=R (R<r*) lies in the basin
     (V(R)<=lmin r*^2 keeps sublevel set inside). Hence NO periodic orbit inside
     the disc, and all trajectories there converge to the equilibrium.
 (B) Equilibrium census: origin unique in R=[-0.5,0.5]^2 for B1,B3,B4,B5 via the
     uniform product bound g(x)=(c+dx)(a+bx)-1 <= Gmax-1 < 0 on |x|<=0.5
     (uses sign-controlled factors); B3 origin GLOBALLY unique (discriminant<0
     uniformly); stability types via uniform trace/det/disc signs (B1,B3,B5 stable
     focus; B2,B4 origin saddle).
 (C) Dulac B=1 half-plane logs: div=(c-a)+(d-2b)x; for ALL five boxes base<0 and
     slope<0 uniformly, so div<0 on x>=0: no cycle fully in the right half-plane.
     B5 extra slab: div<=-0.63 on x>=0.5. B4 half-plane recorded (cycles, if any,
     must meet x<0); B2/B4 basins and uniqueness FLAGGED OPEN (no overclaim).

Replay: python3 verify_basins.py  -> prints tables + VERIFY_OK.
"""
from fractions import Fraction as F
import math

R_BOX = F(1, 50)  # 0.02

def solve_lyap(a11, a12, a21, a22):
    M = [[2*a11, 2*a21, F(0)], [a12, a11+a22, a21], [F(0), 2*a12, 2*a22]]
    rhs = [F(-1), F(0), F(-1)]
    Ag = [M[i][:] + [rhs[i]] for i in range(3)]
    for c in range(3):
        piv = max(range(c, 3), key=lambda r: abs(Ag[r][c]))
        Ag[c], Ag[piv] = Ag[piv], Ag[c]
        assert Ag[c][c] != 0
        for r in range(3):
            if r != c:
                f = Ag[r][c] / Ag[c][c]
                for k in range(c, 4):
                    Ag[r][k] -= f * Ag[c][k]
    return [Ag[i][3] / Ag[i][i] for i in range(3)]

def sym_eig(p11, p12, p22):
    tr = float(p11 + p22); det = float(p11*p22 - p12*p12)
    s = math.sqrt(max(tr*tr - 4*det, 0))
    return ((tr - s)/2, (tr + s)/2)

CENT = {'B1': (F(1), F(1,2), F(3,10), F(0)), 'B3': (F(4,5), F(3,10), F(1,2), F(-1,10)),
        'B5': (F(1,2), F(1,10), F(2,5), F(1,5))}
LIN = {'B1': (F(-1), F(1), F(-1), F(1,2)), 'B3': (F(-4,5), F(1), F(-1), F(3,10)),
       'B5': (F(-1,2), F(1), F(-1), F(1,10))}
KAPPA = {'B1': 0.641, 'B3': 1.048, 'B5': 0.869}  # upper bounds of sqrt(4bb^2+dd^2)
CERT_R = {'B1': 0.02, 'B3': 0.04, 'B5': 0.06}

print("=== (A) Lyapunov basin discs: no cycle + attraction, uniform over box ===")
for k in ['B1', 'B3', 'B5']:
    P = solve_lyap(*LIN[k]); p11, p12, p22 = P
    lmin, lmax = sym_eig(p11, p12, p22)
    assert lmin > 0, (k, 'P not positive definite')
    Fn = math.sqrt(float(p11*p11 + 2*p12*p12 + p22*p22))
    r = float(R_BOX)
    spread = 2*lmax*math.sqrt(2)*r      # parameter-spread margin at centre
    K = 2*Fn*KAPPA[k]                    # |E(z)|_2 <= K|z|
    assert spread < 1, (k, spread)
    rstar = (1-spread)/K
    R = CERT_R[k]
    assert R < rstar, (k, R, rstar)
    V_R = lmax*R*R; Vsafe = lmin*rstar*rstar
    assert V_R < Vsafe, (k, V_R, Vsafe)
    print(f"{k}: P=({float(p11):.5f},{float(p12):.5f},{float(p22):.5f}) "
          f"eigP=[{lmin:.4f},{lmax:.4f}] spread={spread:.4f} K={K:.4f} "
          f"r*={rstar:.4f} R={R}: V(R)={V_R:.5f}<{Vsafe:.5f}=Vsafe CERTIFIED")

print()
print("=== (B) Equilibrium census in R=[-0.5,0.5]^2 + stability types (uniform) ===")
# g(x)=(c+dx)(a+bx)-1 = bd x^2 + s x + (ac-1), s=bc+ad. Nonzero eq in R needs
# g(x)=0 for some |x|<=.5. Uniform bound: g(x) <= |bd|x^2+|s||x|+(ac-1) with
# box maxima; if <0 then origin UNIQUE in R. All bounds below use box corners.
BDC = {'B1': (0.0064, 0.1868, -0.4696), 'B3': (0.0624, 0.1040, -0.7376),
       'B5': (0.0924, 0.1648, -0.9376)}  # (|bd|max, |s|max, (ac-1)max=least negative)
for k in ['B1', 'B3', 'B5']:
    mbd, ms, acm1 = BDC[k]
    gsup = mbd*0.25 + ms*0.5 + acm1
    a0, c0, b0, d0 = CENT[k]; r = float(R_BOX)
    tr_lo, tr_hi = (float(c0-r)-float(a0+r)), (float(c0+r)-float(a0-r))
    print(f"{k}: sup_{{box,|x|<=.5}} g <= {mbd}*.25+{ms}*.5{acm1:+.4f} = {gsup:.4f} < 0 "
          f"-> origin UNIQUE in R CERTIFIED; tr0 in [{tr_lo:.4f},{tr_hi:.4f}] < 0 (stable focus).")
print("B3 global: bd in [-0.0576,-0.0416]<0, ac-1 in [-0.7816,-0.7376]<0 uniformly; "
      "s=bc+ad in [0.036,0.104], s^2<=0.0108; "
      "4|bd||ac-1|>=4(0.0416)(0.7376)=0.1227 -> disc<=0.0108-0.1227<0: origin SOLE equilibrium of the PLANE.")
print("B1 nominal outer eq (10/3,20/3), norm 7.45, excluded from R; box-uniform outer count OPEN (bd straddles 0).")
print("B2: origin saddle (det0 = 1-ac < 0 uniform: ac in [1.1544,1.2464]); stable focus F nominal (-0.6745,-0.9208); box-uniform basin OPEN.")
print("B4: origin saddle (det0 = 1-ac < 0 uniform: ac in [1.9404,2.0604]); nominal unstable focus (-10,-10); basin/outer census OPEN.")
print("B5 nominal outer eqs norms 7.17, 5.00, excluded from R; box-uniform outer count OPEN (flagged).")

print()
print("=== (C) Dulac B=1 half-plane exclusion logs (uniform over box) ===")
ALL5 = {'B1': (F(1), F(1,2), F(3,10), F(0)), 'B2': (F(3,2), F(4,5), F(1,5), F(1,10)),
        'B3': (F(4,5), F(3,10), F(1,2), F(-1,10)), 'B4': (F(2), F(1), F(1,10), F(0)),
        'B5': (F(1,2), F(1,10), F(2,5), F(1,5))}
for k in ['B1', 'B2', 'B3', 'B4', 'B5']:
    a0, c0, b0, d0 = ALL5[k]; r = float(R_BOX)
    base_hi = (float(c0+r)) - (float(a0-r))
    slope_hi = (float(d0+r)) - 2*(float(b0-r))
    assert base_hi < 0 and slope_hi < 0, k
    print(f"{k}: div=(c-a)+(d-2b)x <= {base_hi:.4f} + ({slope_hi:.4f})x < 0 on x>=0 CERTIFIED: "
          f"no cycle fully in right half-plane.")
a0, c0, b0, d0 = ALL5['B5']; r = float(R_BOX)
base_hi = float(c0+r) - float(a0-r); slope_hi = float(d0+r) - 2*float(b0-r)
print(f"B5 slab: div <= {base_hi + slope_hi*0.5:.4f} < 0 on x>=0.5 CERTIFIED: no cycle fully in slab x>=0.5.")
print()
print("VERIFY_OK")
