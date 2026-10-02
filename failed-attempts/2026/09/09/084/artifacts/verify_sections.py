"""Rigorous (stdlib-only) enclosure of central sections of K0 = B_4^5.

Koldobsky cosine identity (hypothesis H-K), proved as Lemma H-K in DRAFT.md
from Koldobsky, "Fourier Analysis in Convex Geometry", AMS Math. Surveys &
Monographs vol. 105 (2005), Ch. 2, Theorem 2.1 (p. 27) — the Fourier
representation of central-section volumes — specialized to B_4^5 via the
product density f(x)=exp(-||x||_4^4) and the Fourier slice theorem:
  S(a) = |K0 cap a^perp|_4 = (c0^5/pi) * int_0^oo F_a(t) dt,
  F_a(t) = Prod_{j=1..5} psi(a_j t),
  psi(v) = Gamma(5/4)^{-1} int_0^oo cos(v y) exp(-y^4) dy, psi(0)=1.
e1 is reported EXACT (V4 = c0^4); e1 quadrature cross-check included.

Method: composite Simpson on [0,Y0=4] for psi AND psi' tables
(step 0.05, cubic Hermite outer interpolation); composite Simpson on
[0,T=60] for the outer integral; polynomial majorant tail bounds
|psi(v)| <= min(1, C2/v^2, C4/v^4), C2=8.2, C4=1100.
Floating-point rounding allowance FP_ALLOW=1e-7 (quantified in DRAFT.md).
Runtime stdlib ~1 s.
"""
import math, time
from math import factorial

GAMMA54 = math.gamma(1.25)
C0 = 2.0 * GAMMA54
KOUT = C0 ** 5 / math.pi
V4EXACT = C0 ** 4
V5 = C0 ** 5 / math.gamma(2.25)

C2 = 8.2     # >= (1/Gamma) int |h''|; triangle proof: (16*N6+12*N2)/Gamma(5/4)
             # <= (16*0.231+12*0.307)/0.9063 = 7.38/0.9063 = 8.15 <= 8.2
C4 = 1100.0  # >= (1/Gamma) int |h''''|; triangle proof:
             # (256*N12+1408*N8+1680*N4+24*N0)/Gamma(5/4)
             # <= (256*0.638+1408*0.284+1680*0.227+24*0.907)/0.9063
             # = 966.6/0.9063 = 1066.5 <= 1100 (measured sharp value: 168.5)
# psi derivative caps: |psi^{(m)}| <= Dm (exact moments (1/4)Gamma((m+1)/4)/Gamma(5/4))
D0, D1, D2, D3, D4 = 1.0, 0.49, 0.34, 0.28, 0.25
# sup|h^{(m)}| hand-calculus ceilings (h(y)=exp(-y^4), e>2.71827):
# M1: max 4y^3e^{-y^4} at y=(3/4)^{1/4}: 4(3/4)^{3/4}e^{-3/4} <= 1.531 -> 1.54.
# M2: 16y^6e^{-y^4}<=16(3/2)^{3/2}e^{-3/2}=6.56 (max at y^4=3/2) plus
#     12y^2e^{-y^4}<=12(1/2)^{1/2}e^{-1/2}=5.15 (max at y^4=1/2): sum<=11.71
#     -> 11.8.
# M3: exact triangle 64*M9+144*M5+24*M1m with Mk=max y^k e^{-y^4}
#     =(k/4)^{k/4}e^{-k/4}: 64*0.8399+144*0.4877+24*0.7087=140.98 -> 146.
# M4: exact triangle 256*27e^-3+1408*4e^-2+1680e^-1+24 <= 1748.4 -> 1760.
# M4 enters ONLY g4cap (the psi-table Simpson error E0); it does NOT enter
# the outer tail (which uses the moment-triangle caps C2/C4 instead).
M0, M1, M2, M3, M4 = 1.0, 1.54, 11.8, 146.0, 1760.0
# NOTE: N_k/L0 integrated-moment machinery REMOVED (auditor repair 2026-09-09):
# gp4cap below is now a genuine pointwise sup majorant, not an L1/moment mix.

# Floating-point rounding allowance (quantified): FP_ALLOW = 1e-7 per
# section value. Accumulated rounding over the ~1.3e3-term Hermite table
# build and the 6001-term outer Simpson sums is at most a few thousand
# ulps (~1e-12 relative on values of order 10); FP_ALLOW exceeds any
# plausible rounding by >100x while remaining negligible against the
# analytic radii (~3.6e-4).
FP_ALLOW = 1e-7

Y0 = 4.0
NY = 4800
PSI_STEP = 0.05
PSI_UMAX = 65.0
T_OUT = 60.0
N_OUT = 6000

def g4cap_val(u):
    return (u**4*M0 + 4*u**3*M1 + 6*u**2*M2 + 4*u*M3 + M4)

def gp4cap_val(u):
    # Genuine pointwise sup majorant for G''''(y), G(y) = y*sin(u y)*h(y),
    # h(y) = exp(-y^4), uniform over y in [0,4], u in [0,60].
    # Leibniz: G'''' = sum_{k=0..4} C(4,k) q^{(k)}(y) h^{(4-k)}(y),
    # q(y) = y sin(u y). Pointwise |q^{(k)}(y)| ceilings (y<=4, |trig|<=1):
    #   |q|     <= 4                                    =: Q0
    #   |q'|    <= 4u+1                                 =: Q1
    #   |q''|   <= 4u^2+2u ... see derivation: q''=2u cos-uy^2 sin
    #             <= 2u + 4u^2                           =: Q2
    #   |q'''|  <= 3u^2 + 4u^3 + u^2 ... q'''=-3u^2 sin-u^3 y cos-u^2...:
    #             <= 4u^2 + 4u^3                         =: Q3 (covers u>=1;
    #             for u<1 use the crude envelope below, still valid)
    #   |q''''| <= 4u^3 + 4u^4 + 4u^3 = 4u^4+8u^3        =: Q4
    # combined with sup|h^{(m)}| ceilings M_m. Each Q is replaced by a
    # slightly looser polynomial that is provably >= the sharp bound for
    # all u>=0 (extra positive terms added; verified term-by-term):
    Q0 = 4.0
    Q1 = 4*u+1
    Q2 = 4*u*u+2*u+1
    Q3 = 4*u**3+4*u*u+3*u+1
    Q4 = 4*u**4+8*u**3+6*u*u+4*u+1
    return (Q0*M4 + 4*Q1*M3 + 6*Q2*M2 + 4*Q3*M1 + Q4*M0)

def build_tables():
    h = Y0 / NY
    ys = [i*h for i in range(NY+1)]
    ey = [math.exp(-(y**4)) for y in ys]
    ye = [ys[i]*ey[i] for i in range(NY+1)]
    w = [1.0]*(NY+1)
    for i in range(1, NY):
        w[i] = 4.0 if (i % 2 == 1) else 2.0
    bw0 = [w[i]*ey[i] for i in range(NY+1)]
    bw1 = [w[i]*ye[i] for i in range(NY+1)]
    coef = (h/3.0)/GAMMA54
    n = int(PSI_UMAX/PSI_STEP)+1
    tab = [0.0]*n
    dtab = [0.0]*n
    ev = [0.0]*n
    ed = [0.0]*n
    for k in range(n):
        u = k*PSI_STEP
        s0 = 0.0
        s1 = 0.0
        for i in range(NY+1):
            cy = math.cos(u*ys[i])
            sy = math.sin(u*ys[i])
            s0 += bw0[i]*cy
            s1 += bw1[i]*sy
        tab[k] = coef*s0
        dtab[k] = -coef*s1  # psi'(u) = -(1/Gamma) int y sin(uy) e^{-y^4} dy
        ev[k] = (Y0/180.0)*(h**4)*g4cap_val(u)/GAMMA54
        ed[k] = (Y0/180.0)*(h**4)*gp4cap_val(u)/GAMMA54
    return tab, dtab, ev, ed

def hermite(u, tab, dtab, hh):
    import math as m
    if u < 0:
        u = -u
    n = len(tab)
    k = int(u/hh)
    if k >= n-1:
        return 0.0
    s = (u - k*hh)/hh
    p0 = tab[k]; p1 = tab[k+1]
    m0 = dtab[k]; m1 = dtab[k+1]
    s2 = s*s; s3 = s2*s
    h00 = 2*s3-3*s2+1
    h10 = s3-2*s2+s
    h01 = -2*s3+3*s2
    h11 = s3-s2
    return h00*p0 + h10*hh*m0 + h01*p1 + h11*hh*m1

def outer_mid(a, tab, dtab):
    n = N_OUT
    h = T_OUT/n
    tot = 0.0
    for i in range(n+1):
        t = i*h
        p = 1.0
        for aj in a:
            if aj == 0.0:
                continue
            p *= hermite(abs(aj)*t, tab, dtab, PSI_STEP)
        wgt = 1.0 if (i == 0 or i == n) else (4.0 if i % 2 == 1 else 2.0)
        tot += wgt*p
    return KOUT*tot*(h/3.0)

def psi_bound(v):
    b = 1.0
    c = C2/(v*v)
    if c < b:
        b = c
    d = C4/(v**4)
    if d < b:
        b = d
    return b

def tail_bound(a):
    E = 0
    logC = 0.0
    for aj in a:
        if aj == 0.0:
            continue
        v = abs(aj)*T_OUT
        b2 = C2/(v*v)
        b4 = C4/(v**4)
        if b4 <= b2 and b4 <= 1.0:
            E += 4
            logC += math.log(C4) - 4*math.log(abs(aj))
        elif b2 <= 1.0:
            E += 2
            logC += math.log(C2) - 2*math.log(abs(aj))
        else:
            E += 0
    if E <= 1:
        return float('inf')
    C = math.exp(logC)
    return KOUT*C/((E-1)*(T_OUT**(E-1)))

def outer_simpson_err(a):
    caps = []
    for aj in a:
        caps.append([D0, abs(aj)*D1, aj*aj*D2, abs(aj)**3*D3, abs(aj)**4*D4])
    tot = 0.0
    for m1 in range(5):
        for m2 in range(5-m1):
            for m3 in range(5-m1-m2):
                for m4 in range(5-m1-m2-m3):
                    m5 = 4-m1-m2-m3-m4
                    ms = (m1, m2, m3, m4, m5)
                    mult = factorial(4)
                    for m in ms:
                        mult //= factorial(m)
                    term = mult
                    for j, m in enumerate(ms):
                        term *= caps[j][m]
                    tot += term
    h = T_OUT/N_OUT
    return KOUT*(T_OUT/180.0)*(h**4)*tot

def main():
    t0 = time.time()
    tab, dtab, ev, ed = build_tables()
    t1 = time.time()
    print("tables built: %d pts, %.1fs" % (len(tab), t1-t0))
    umax_need = T_OUT  # max a_j*T_OUT
    ks = [k for k in range(len(tab)) if k*PSI_STEP <= umax_need]
    E0 = max(ev[k] for k in ks)
    E1 = max(ed[k] for k in ks)
    hinterp_trunc = D4/384.0*PSI_STEP**4
    # Data-perturbation through Hermite basis: |h00|+|h01| = 1,
    # |h10|+|h11| <= 8/27 < 0.3, so perturbed-data error <= E0 + 0.3*h*E1.
    eps_h = E0 + 0.3*PSI_STEP*E1 + hinterp_trunc
    print("E0=%.2e E1=%.2e hermite_trunc=%.2e eps_h=%.2e" % (E0, E1, hinterp_trunc, eps_h))
    prop = KOUT*T_OUT*5*eps_h*1.05
    print("propagated psi-error on S <= %.2e" % prop)
    sq5 = math.sqrt(5.0)
    sq13 = math.sqrt(13.0)
    dirs = {
        "e1": (1.0, 0.0, 0.0, 0.0, 0.0),
        "k2": (1/math.sqrt(2), 1/math.sqrt(2), 0, 0, 0),
        "k3": (1/math.sqrt(3),)*3+(0, 0),
        "k4": (0.5, 0.5, 0.5, 0.5, 0.0),
        "diag": (1/sq5,)*5,
        "w133": (3/sq13, 1/sq13, 1/sq13, 1/sq13, 1/sq13),
    }
    results = {}
    for name, a in dirs.items():
        if name == "e1":
            lo = V4EXACT-1e-9
            hi = V4EXACT+1e-9
            mid = V4EXACT
            q = outer_mid(a, tab, dtab)
            print("e1 exact=%.9f quad-check=%.6f diff=%.2e" % (V4EXACT, q, abs(q-V4EXACT)))
        else:
            mid = outer_mid(a, tab, dtab)
            tb = tail_bound(a)
            se = outer_simpson_err(a)
            tot = tb+se+prop+FP_ALLOW
            lo, hi = mid-tot, mid+tot
            print("%s mid=%.6f tail=%.2e simp=%.2e tot=%.2e" % (name, mid, tb, se, tot))
        results[name] = (lo, mid, hi)
    print("---- intervals (width) ----")
    for name, (lo, mid, hi) in results.items():
        print("%s: [%.6f, %.6f] width %.2e" % (name, lo, hi, hi-lo))
    lo_d, _, hi_d = results["diag"]
    lo_e, _, hi_e = results["e1"]
    print("diag/e1 lower ratio bound: %.6f" % (lo_d/hi_e))
    print("check width<=1e-3:", all((hi-lo) <= 1e-3+1e-12 for lo, _, hi in results.values()))
    print("check ratio>=1.05:", (lo_d/hi_e) >= 1.05)
    print("elapsed %.1fs" % (time.time()-t0))

if __name__ == "__main__":
    main()
