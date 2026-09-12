"""Symmetric regular-flower check for hyperbolic Poisson-Voronoi typical cell.

Closed form (derived in DRAFT.md): n symmetric neighbours at hyperbolic radius rho,
angles 2*pi*k/n. Circumcentre of (o, x0, x1) on ray pi/n at distance d with
  coth(d) = coth(rho/2) * cos(pi/n),
admissible iff tanh(rho/2) < cos(pi/n), i.e. rho < 2*artanh(cos(pi/n)).
Disk area A(r) = 2*pi*(cosh(r)-1). Empty-disk probability exp(-lambda*A(d)).
Union-bound flower estimate exp(-lambda*n*A(d)) <= P(empty flower).
Self-avoidance S(x): no non-consecutive symmetric neighbour lies in the
interior of any circumdisk D_i (checked in the Poincare disk model).
Scaling check: rho = s/sqrt(lambda) -> lambda*A(d) -> Euclidean limit.
Pure numpy.
"""
import numpy as np

def max_rho(n):
    return 2.0 * np.arctanh(np.cos(np.pi / n))

def circum_d(rho, n):
    c = 1.0 / np.tanh(rho / 2.0) * np.cos(np.pi / n)
    # c = coth(d) must exceed 1
    return np.arctanh(1.0 / c)

def disk_area(r):
    return 2.0 * np.pi * (np.cosh(r) - 1.0)

def poincare_t(rho):
    return np.tanh(rho / 2.0)

def cosh_dist_poincare(a, b):
    na2 = np.vdot(a, a).real
    d2 = np.vdot(a - b, a - b).real
    return 1.0 + 2.0 * d2 / ((1.0 - na2) * (1.0 - np.vdot(b, b).real))

def check_self_avoidance(n, rho):
    """Return (S, min_margin): S=1 iff no non-consecutive symmetric neighbour
    lies in the interior of any circumdisk D_i. By rotation symmetry it
    suffices to check D_0 against x_2..x_{n-1}."""
    t = poincare_t(rho)
    d = circum_d(rho, n)
    u = poincare_t(d)
    c = u * np.array([np.cos(np.pi / n), np.sin(np.pi / n)])
    rcosh = np.cosh(d)  # circumradius: d(c, o)
    xs = [t * np.array([np.cos(2.0 * np.pi * k / n), np.sin(2.0 * np.pi * k / n)])
          for k in range(n)]
    margins = []
    for j in range(2, n):
        margins.append(cosh_dist_poincare(c, xs[j]) - rcosh)
    return bool(all(m > 1e-12 for m in margins)), min(margins)

def main():
    print("n  rho_max  rho  d  A(d)  P_empty_disk(lam=1)  P_empty_disk(lam=10)")
    for n in [3, 4, 5, 6, 8]:
        rm = max_rho(n)
        for frac in [0.25, 0.5, 0.9]:
            rho = frac * rm
            d = circum_d(rho, n)
            a = disk_area(d)
            print(f"{n}  {rm:.4f}  {rho:.4f}  {d:.4f}  {a:.4f}  "
                  f"{np.exp(-a):.6f}  {np.exp(-10*a):.6f}")
    # scaling: rho = s/sqrt(lam), lam*A(d) -> pi*s^2/(4cos^2(pi/n))? check convergence
    print("\nscaling check n=6, s=1.0:")
    s = 1.0
    n = 6
    euc = np.pi * s**2 / (4.0 * np.cos(np.pi/n)**2)
    for lam in [10, 100, 1000, 10000]:
        rho = s / np.sqrt(lam)
        d = circum_d(rho, n)
        print(f"lam={lam}: lam*A(d)={lam*disk_area(d):.6f}  euc_limit={euc:.6f}")
    # admissibility failure for large rho
    print("\nlarge-rho inadmissibility: n=3, rho=3.0 (> rho_max=%.4f):" % max_rho(3))
    print("coth(rho/2)cos(pi/3) =", 1.0/np.tanh(1.5)*np.cos(np.pi/3), "< 1 => no finite circumcentre")
    # self-avoidance S(x) for the symmetric flowers
    print("\nself-avoidance S(x) (no non-consecutive neighbour in int D_i):")
    for n in [3, 4, 5, 6, 8]:
        rm = max_rho(n)
        for frac in [0.25, 0.5, 0.9]:
            rho = frac * rm
            S, margin = check_self_avoidance(n, rho)
            print(f"n={n}  rho={rho:.4f}  S={int(S)}  min_margin={margin:.6f}")

if __name__ == "__main__":
    main()
