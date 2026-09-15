"""Recovery/bounded-viability test for the inhomogeneous critical-exponent target.

Two checks, both reproducible with `python3 recovery_test.py`:
 (1) Algebra: the only theta-uniform He-Liao lower bound (Thm 1.2, (1.5))
     cannot reach s(tau) under the mandatory beta<1.
 (2) Geometry: the homogeneous 1/(q q') separation used in Cases 3B-5B
     (Lemma 4.1 + absolute decaying, theta=0 only) fails for shifted
     rationals (p+theta)/q with theta not in Z.
"""
import math

delta = math.log(6) / math.log(7)
print(f"delta = log 6 / log 7 = {delta:.10f}")
print("Check 1: required beta for (1.5) to equal s(tau)")
print("  s(tau)=delta+2/(1+tau)-1; sharpness needs "
      "beta*delta >= s(tau)*(tau+1)  [s=delta-x vs delta-x*s'/...]")
ok = True
for tau in (1.01, 1.05, 1.10, 1.20, 1.50):
    s = delta + 2.0 / (1.0 + tau) - 1.0
    req = s * (tau + 1.0) / delta
    feas = "FEASIBLE" if req < 1.0 else "IMPOSSIBLE (beta<1 required)"
    if req < 1.0:
        ok = False
    print(f"  tau={tau:5.2f}  s={s:.6f}  req_beta={req:.6f}  {feas}")
print("  => (1.5) can never reach s(tau); result:", "BLOCKED" if ok else "route open")

print("Check 2: inhomogeneous separation failure")
theta = math.sqrt(2) - 1
Q = 50
pts = []
for q in range(1, Q + 1):
    for p in range(0, Q + 1):
        v = (p + theta) / q
        if 0.0 <= v <= 1.0:
            pts.append((v, p, q))
pts.sort()
viol = None
for i in range(len(pts) - 1):
    v1, p1, q1 = pts[i]
    v2, p2, q2 = pts[i + 1]
    gap = v2 - v1
    sep = 1.0 / (q1 * q2)
    if gap < sep / 2:
        viol = (gap, sep, p1, q1, p2, q2, v1, v2)
        break
print(f"  theta={theta:.8f} (irrational, not in Z), Q={Q}")
print(f"  adjacent shifted rationals: {(viol[4], viol[3]), (viol[5], viol[2])} "
      f"values {viol[6]:.8f}, {viol[7]:.8f}")
print(f"  gap={viol[0]:.3e} < sep/2={viol[1] / 2:.3e} "
      f"(homogeneous Lemma 4.1 allows at most ONE rational per Q^-2 interval)")
for k in range(1, Q + 1):
    d = abs(k * theta - round(k * theta))
    if d < 0.02:
        print(f"  clustering witness: k={k}, ||k theta||={d:.5f}, "
              f"pair gap ~ {d / Q ** 2:.2e} << 1/Q^2 = {1 / Q ** 2:.2e}")
        break
print("  => Cases 3B-5B simplex step has no theta-uniform analogue; result: BLOCKED")
