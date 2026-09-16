"""Recovery/uniformity audit for the twisted second moment target.

Computes, for representative general moduli q (q not = 2 mod 4):
- tau(q), phi*(q) = sum_{d|q} mu(q/d) phi(d), and ratio phi*(q)/q,
- the divisor-modulus family {d : d|q, mu(q/d)!=0} that survives Mobius inversion
  in the primitive-character orthogonality,
- the smallest surviving moduli (which carry no q-aspect averaging),
- a proxy Weil-only off-diagonal term budget: sum_{d|q} phi(d)/phi*(q) * d^{1/2} * (MN)^{1/2}/(MN)^{1/2}
  simplified to sum phi(d)/phi*(q) d^{1/2}, showing small-d terms contribute O(1), not O(q^{-delta}),
  i.e. Weil alone cannot give power saving uniformly.

This is diagnostic evidence for the blocking obstacle, not a proof of the target.
"""
import sympy as sp

def audit(q):
    ds = sp.divisors(q)
    contrib = [d for d in ds if sp.mobius(q // d) != 0]
    phi_star = sum(sp.mobius(q // d) * sp.totient(d) for d in ds)
    assert phi_star > 0
    weil_proxy = sum(float(sp.totient(d)) / float(phi_star) * float(d) ** 0.5 for d in contrib)
    small = sorted(d for d in contrib if d < q ** 0.5)
    return {
        "q": q, "tau": len(ds), "n_contrib": len(contrib),
        "phi_star": int(phi_star), "phi_star_over_q": float(phi_star) / q,
        "n_small_moduli": len(small), "smallest": small[:12],
        "weil_proxy": weil_proxy,
    }

qs = [72, 3**6, 2**10, 2**8 * 3**5, 3 * 5 * 7 * 11 * 13,
      3 * 5 * 7 * 11 * 13 * 17, 2**4 * 3**2 * 5 * 7 * 11, 9 * 25 * 49 * 121]
for q in qs:
    if q % 4 == 2:
        continue
    r = audit(q)
    print(f"q={r['q']:>8} tau={r['tau']:>3} ndiv={r['n_contrib']:>3} "
          f"phi*/q={r['phi_star_over_q']:.4f} nsmall={r['nsmall_moduli'] if False else r['n_small_moduli']:>3} "
          f"smallest={r['smallest']} weil_proxy={r['weil_proxy']:.3f}")
