---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Explicit ε<min[1/(2(1+cd)),1/(2d),1/(2(1+d))] makes the positive rectangle invariant. For r=x/y and T=1/y, exact recurrences r_next−r = r*y[(1−c)−(1+d)r]/(1−y+dx), T_next−T=(1−dr)/(1−y+dx). x decreases by logistic comparison; y→0 by eventually weak predator forcing, but y_next≥y(1−y) implies Σy diverges. For c<1, r contracts toward r*=(1−c)/(1+d), yielding both n limits. For c≥1, r→0 and T/n→1. For c>1 a polynomial upper bound for r makes Σx finite and Σ|y−1/n| finite; log x_n+c log n converges, yielding L>0. For c=1 exact w=y/x satisfies w_next−w=(1+d)y/(1−x−y). First w~(1+d)log n, then reciprocal T=n−[d/(1+d)]n/log n+O(n loglog n/log² n), and the resulting summable difference correction gives w−(1+d)log n−d loglog n→C. Checked four defining rational identities by direct derivation from map; inspected symbolic checker, which tests finite trajectories but cannot prove infinite limits.

## originality

PASS

The exact biological map, up to swapping species, was analyzed by Satoh–Aihara (1990) numerically and Al-Kaff et al. (2024) for fixed points and bifurcations. The accessible full 2024 analysis does not provide simultaneous unit-growth all-orbit asymptotic clocks or critical loglog coefficient. Earlier 1990 and 2018 primary full texts remain plausible priority risks, not automatic originality failure.

## value

PASS

At simultaneous neutral growth multipliers a previously studied ecological map has a quantitative dynamical phase boundary and a second-order loglog extinction clock. The sharp dependence on coupling c and d in a natural nonhyperbolic boundary problem is useful for separating asymptotic population regimes, beyond routine Jacobian stability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
