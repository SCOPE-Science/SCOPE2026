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

In the one-edge tree a mark gains A=L−D/2 by 1/2 on attachment to itself and loses 1 on attachment to a neighboring leaf, at rates D/T and L/T in discrete time. This remains valid at the seed edge. The drift is −A/T, and the conditional second moment of the increment is (D/4+L)/T. Iterating the resulting squared-state recursion with E[D]=O(sqrt(n)) gives E[A²]=O(sqrt(n)). In the exponential-clock embedding the edge count and a marked degree after birth are Yule processes of per-capita rates 2 and 1. Each rescaled limit is positive and finite by the one-particle Yule law; their independence is not needed. Evaluating at the edge-count hitting times gives the F∞-measurable positive W. The drift-compensated A/b has b∼c n^{-1/2}. The leading rescaled diagonal bracket is n^{-3/2} sum (3D_j/(8c²)), giving W/(4c²); the linear and quadratic errors before normalization are O(n^{5/4}) and O(sqrt(n)) in L¹. When both marks cease to be leaves, their raw increments cannot occur together, so the centered cross term is −A_u A_v/T²; the exceptional prefix is a.s. finite and the remaining normalized sum is O(n^{-1}) in L¹. For the stable martingale array one may start at a common deterministic size after all births: the rows use the same nested tree filtrations, initial terms vanish, and the n^{-3/4}-scaled increments have deterministic maximum O(n^{-1/4}). Conditional Lindeberg follows; if using the realized-variation formulation, the difference from the predictable variation also tends to zero in L² by bounding its variance by the squared maximal jump times the uniformly bounded expected scaled bracket. Cramér–Wold with bounded F∞ test weights thus gives the asserted stable Gaussian kernel. Rescaling by n^{1/2}b and studentizing by the a.s. positive degree limits gives diagonal 1/4 covariance and independent limiting coordinates.

## originality

PASS

The supported distinction is the mixed Gaussian limit stable with respect to tree growth for finitely many fixed labels and its independent realized-degree studentization. Neither the center nor the coefficient 1/4 is novel as a population asymptotic. The distinct uniform half-degree result controls the same statistic but does not identify its fixed-label law at the sharp fluctuation scale.

## value

PASS

This supplies the sharp fluctuation scale and conditional law for a natural degree–leaf composition statistic in a classical growth model. It separates dependent random hub sizes from asymptotically independent local noise and identifies a universal Gaussian normalization using an observed degree, beyond a population variance or simultaneous upper bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
