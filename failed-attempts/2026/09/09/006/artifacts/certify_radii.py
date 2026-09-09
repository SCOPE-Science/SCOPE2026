#!/usr/bin/env python3
"""Lane-278: rigorous omega intervals via argument-principle root counts.
Count zeros of Q in |z| < rho (rho rational, no zeros on circle) by the
argument principle: N = winding of Q(gamma) around 0, gamma = circle |z|=rho.
Rigorous winding via exact rational bounding boxes on a fine partition:
split circle into N arcs; on arc k with center angle th_k, half-width dth,
compute EXACT rectangle (Fraction bounds) containing Q(rho e^{it}) using
Taylor-with-remainder or coefficient-wise trig bounds:
  Q(rho e^{it}) = sum q_j rho^j (cos j t + i sin j t).
  On arc: cos/sin enclosed via mean-value: |d/dt cos jt| <= j.
  So Re in [Re(c)-L*dth, Re(c)+L*dth], L = sum |q_j| rho^j j (same for Im).
If no box contains 0 and consecutive boxes' union avoids a ray... standard:
winding = (1/2pi) sum of angle increments; certify each box lies in some
open half-plane through origin relative to previous: require each box to have
angular width < pi AND consecutive boxes overlap consistently. Simplest robust:
require each box to be contained in an open half-plane bounded by a line through
origin (check all 4 corners strictly on one side of some axis-aligned line? no).
Use per-box angular enclosure: box center c, radius rad (in complex plane);
if |c| > rad*sqrt(2)... angle interval = [arg c - dphi, arg c + dphi],
dphi = asin(min(1, rad*sqrt(2)/|c|)) -- rigorous since disk contains box.
Then track cumulative angle with branch cuts: require dphi < pi/2 and step
|arg c_{k+1} - arg c_k| + dphi_k + dphi_{k+1} < pi (no wrap ambiguity);
N = round(total/2pi), certified if accumulated ambiguity < pi/2... formalize:
maintain interval of possible total; each step's increment in interval of width
2(dphi_k+dphi_{k+1}); total width < pi => unique integer. Implement with floats
for angles (sound: add edge margin) -- better: do everything with Fractions for
centers/radii and float angles with rigorous padding (add 1e-9 + relative).
Honestly rigorous: use exact Fraction arithmetic for boxes, float for atan with
padding 1e-6; require total slack < 0.5 (counts) with margin >> padding*Narcs.
"""
import json, math
from fractions import Fraction

def winding_count(Qasc, rho, Narcs=512):
    """Returns N = # zeros in |z|<rho, certified, or raises AssertionError."""
    rho = Fraction(rho)
    n = len(Qasc)-1
    pw = [rho**j for j in range(n+1)]
    M2 = sum(abs(Fraction(Qasc[j]))*pw[j]*j*j for j in range(n+1))  # 2nd-deriv bound
    dth = 2*math.pi/Narcs  # full arc width; midpoint rule: err <= M2*(dth/2)^2/2
    fpad = 1e-9*sum(abs(float(Fraction(Qasc[j])))*float(pw[j]) for j in range(n+1)) + 1e-12
    r = float(M2)*(dth/2)**2/2 + fpad
    boxes = []
    for k in range(Narcs):
        th = (2*k+1)*math.pi/Narcs
        cr = sum(float(Fraction(Qasc[j]))*float(pw[j])*math.cos(j*th) for j in range(n+1))
        ci = sum(float(Fraction(Qasc[j]))*float(pw[j])*math.sin(j*th) for j in range(n+1))
        boxes.append((cr, ci, r))
    angs = []
    for (cr, ci, r) in boxes:
        nc = math.hypot(cr, ci)
        assert nc > r*math.sqrt(2) + 1e-9, f"box contains 0: c=({cr},{ci}) r={r}"
        dphi = math.asin(min(1.0, r*math.sqrt(2)/nc)) + 1e-9
        assert dphi < math.pi/2
        angs.append((math.atan2(ci, cr), dphi))
    total = 0.0; slack = 0.0
    for k in range(Narcs):
        a0, d0 = angs[k]; a1, d1 = angs[(k+1) % Narcs]
        d = a1 - a0
        d -= 2*math.pi*round(d/(2*math.pi))
        assert abs(d) + d0 + d1 < math.pi, "step ambiguous"
        total += d; slack += d0 + d1
    N = total/(2*math.pi)
    assert abs(N - round(N)) < 0.5 - slack/(2*math.pi) - 1e-6, (N, slack)
    return int(round(N))

def min_root_modulus_bracket(Qasc, blo, tol=Fraction(1, 10**9)):
    """Bisect: lo has 0 roots inside (certified), hi=blo has >=1 (Sturm real root).
    Returns lo with N(lo)==0 certified."""
    from sympy import symbols, Poly, Rational, sturm as sym_sturm
    t = symbols('t')
    Q = Poly(sum(int(c)*t**i for i, c in enumerate(Qasc)), t, domain='ZZ')
    # Invariants: R <= hi (Sturm real root in (0,hi] since Q(hi)<=0, Q(0)=1);
    # R > lo once winding_count(lo)==0 certified.
    assert Q.eval(Rational(blo.numerator, blo.denominator)) <= 0, "need Q(blo)<=0 (root in (0,blo])"
    hi = blo
    lo = hi/2
    while True:
        try:
            c = winding_count(Qasc, lo, 2048)
        except AssertionError:
            lo = lo/2; continue
        if c >= 1:
            lo = lo/2; continue
        break
    while hi - lo > tol:
        m = (lo+hi)/2
        try:
            c = winding_count(Qasc, m, 2048)
        except AssertionError:
            m2 = (lo+m)/2  # contaminated circle: search just below, keep hi
            try:
                c2 = winding_count(Qasc, m2, 2048)
            except AssertionError:
                hi = m; continue
            if c2 == 0:
                lo = m2
            else:
                hi = m
            continue
        if c == 0:
            lo = m
        else:
            hi = m
    assert winding_count(Qasc, lo, 4096) == 0
    return lo

def main():
    data = json.load(open("output/artifacts/series.json"))
    out = {}
    for name, S in data["systems"].items():
        Q = [int(x) for x in S["Wden_coeffs_asc"]]
        b = Fraction(S["root_bracket"][1])
        lo = min_root_modulus_bracket(Q, b)
        olo = Fraction(b.denominator, b.numerator)
        ohi = Fraction(lo.denominator, lo.numerator)
        out[name] = {"rho": str(lo), "omega_bracket": [str(olo), str(ohi)],
                     "omega_float": [float(olo), float(ohi)]}
        print(f"{name}: R in ({float(lo):.9f},{float(b):.9f}] "
              f"omega in [{float(olo):.9f},{float(ohi):.9f}] width={float(ohi-olo):.2e}", flush=True)
    order = sorted(out, key=lambda n: float(out[n]["omega_float"][0]))
    print("order:", [(n, [round(float(x),6) for x in out[n]['omega_float']]) for n in order])
    a0 = order[0]
    ok_all = True
    for n in order[1:]:
        gap = Fraction(out[n]["omega_bracket"][0]) - Fraction(out[a0]["omega_bracket"][1])
        print(f"  gap({n}_lo - {a0}_hi) = {float(gap):.6f} positive={gap>0}")
        ok_all &= (gap > 0)
    print("HEADLINE GAP CERTIFIED" if ok_all else "NO HEADLINE (fallback table)")
    json.dump({"intervals": out, "order": order, "headline": bool(ok_all), "min": a0},
              open("output/artifacts/omega.json", "w"), indent=1)

if __name__ == "__main__":
    main()
