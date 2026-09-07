"""Assemble final audit script verify_envelope.py (self-contained, stdlib+numpy+mpmath)."""
import numpy as np
J01 = 2.4048255577

def J0d(z):
    z = np.asarray(z, dtype=float)
    t = z*z/4.0
    s = np.ones_like(z); term = np.ones_like(z)
    for k in range(1, 14):
        term = term*(-t)/(k*k); s = s + term
    return s

def G(z):
    z = np.asarray(z, dtype=float)
    a = 1 - z**2/8 + 0.004
    b = np.full_like(z, np.inf); m = z > 0
    b[m] = np.sqrt(2/(np.pi*z[m]))*(1 - z[m]**2/40)
    return np.minimum(1.0, np.minimum(a, b))

def Pn(x, n):
    x = np.asarray(x, dtype=float)
    p0 = np.ones_like(x); p1 = x.copy()
    if n == 0: return p0
    if n == 1: return p1
    for k in range(1, n):
        p0, p1 = p1, ((2*k+1)*x*p1 - k*p0)/(k+1)
    return p1

def main():
    worst_margin = 1e9; worst_q = 0.0; arg = None
    slack_new_all = []; slack_old_all = []
    per_n = []
    for n in range(5, 51):
        N = n + 0.5; tmax = J01/N
        th = np.linspace(0, tmax, 40001)
        t = th[1:]
        x = np.cos(t)
        P = np.abs(Pn(x, n))
        S = np.sqrt(t/np.sin(t))
        E = S*G(N*t) + 0.025*t**2
        mg = (E - P).min()
        worst_margin = min(worst_margin, mg)
        # Double precision loses ~n^2*eps/t^2 on the R_n quotient as t->0
        # (cos rounds, amplified by |P_n'|~n^2/2); measure the quotient only where
        # it is numerically meaningful: t >= 2.5e-4*tmax (z >= 6.0e-4).
        # The endpoint layer is covered analytically (Taylor data at 0, Lemma 4.x).
        tcut = 2.5e-4 * tmax
        tq = t[t >= tcut]
        xq = np.cos(tq)
        Sq = np.sqrt(tq/np.sin(tq))
        Rq = Pn(xq, n) - Sq*J0d(N*tq)
        q = (np.abs(Rq)/tq**2).max()
        if q > worst_q: worst_q = q; arg = (n, tq[(np.abs(Rq)/tq**2).argmax()])
        TB = np.minimum(1.0, np.sqrt(2/(np.pi*n*np.sin(t))))
        inn = P > 0.05
        rn = (E[inn]/P[inn]); ro = (TB[inn]/P[inn])
        slack_new_all.append(rn); slack_old_all.append(ro)
        per_n.append((n, mg, q, rn.mean(), float(np.median(rn)), float(np.percentile(rn,90)), rn.max(),
                      ro.mean(), float(np.median(ro)), float(np.percentile(ro,90)), ro.max()))
    rn_all = np.concatenate(slack_new_all); ro_all = np.concatenate(slack_old_all)
    print(f"GRID: 46 lobes x 40000 pts. min(E-|Pn|) = {worst_margin:.3e}")
    print(f"HILB (t>=2.5e-4*tmax; endpoint layer analytic): max|R|/t2 = {worst_q:.5f} at n,theta = {arg} (budget 0.025)")
    for s, name in [(rn_all, 'NEW'), (ro_all, 'OLD textbook')]:
        print(f"{name}: pooled mean={s.mean():.4f} med={float(np.median(s)):.4f} p90={float(np.percentile(s,90)):.4f} max={s.max():.4f}")
    ok = (worst_margin >= 0) and (worst_q <= 0.025)
    print("AUDIT:", "PASS" if ok else "FAIL")
    return per_n, worst_margin, worst_q

if __name__ == "__main__":
    per_n, wm, wq = main()
    import csv
    with open("output/artifacts/slack_table.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["n","min_margin","max_R_over_t2","new_mean","new_med","new_p90","new_max","old_mean","old_med","old_p90","old_max"])
        for r in per_n: w.writerow([r[0], repr(r[1]), repr(r[2])] + [repr(v) for v in r[3:]])
    print("wrote output/artifacts/slack_table.csv")
