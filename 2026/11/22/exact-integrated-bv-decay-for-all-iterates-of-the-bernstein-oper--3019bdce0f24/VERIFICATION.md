---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

RESULT.md lines 5–55 hold for real pointwise Jordan-BV data, not a.e. classes. For a nodal unit jump the binomial martingale expresses its defect as two signed interior-state sums. Dominating their weights by the appropriate first- or last-cell step gives an integrated bound, strict for every interior step because both sums are positive on (0,1). Reflection equalizes the two endpoint integrals. The endpoint residuals have opposite signs throughout the open interval, hence equality requires only the two endpoint increments, with product nonpositive, and no variation beyond the nodal sum. For n=2 the empty interior restriction and the opposite-sign test still apply. The beta integral gives a uniform state at time one, so reflection makes the norm half the surviving mass after r−1 further transitions. One-step absorption makes it strictly decrease. The positive eigenvector h=x(1−x) gives λ=(n−1)/n; normalizing the Perron projection by p·h and using Σh=(n²−1)/(6n) gives λ^r/(12a_n) at fixed n. The frozen checker was inspected, not run. Separate exact-rational evidence: 56 formula/integral comparisons and 17,640 endpoint tests for n=2–8, r=1–8, and positive left eigenvector checks for n=2–6; replay evidence in /workspace/branches/7bfec47a-991a-477e-b34c-8b0442ffea76/record1_independent_check.txt and record1_perron_check.txt. These finite checks do not establish the universal result; the proof does.

## originality

PASS

In the compared sources, the exact sharp finite-iterate integrated endpoint-interpolation defect and its equality class are distinct; neither Bernstein iteration convergence nor the Bernstein eigenstructure is claimed new. The amplitude is the consequence of the sharp norm identity combined with prior spectral theory.

## value

PASS

An exact operator norm, its full equality class, and a sharp convergence amplitude answer a natural quantitative question left open by qualitative endpoint convergence. The strict endpoint dominance explains why genuinely interior jumps cannot be worst cases, and supplies a useful general method rather than just a numerical decay rate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
