---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

For orthonormal code vectors e,f, their exterior product has norm one. The matrix element of the multiplicative exterior square of Z_i in e∧f is the determinant of its 2×2 compression, equal to λ_i². The computational wedge basis diagonalizes the exterior square with eigenvalue (−1)^(x_i+y_i); summing gives n−2 times the average Hamming distance subtracted from n, i.e. n−2 E[d_H]. Distinct basis indices guarantee d_H≥1, and nonnegative normalized wedge weights show that saturation is equivalent to support only on pairs at distance one. The two local Z operators send both positive Bell states to negative Bell states, so the Bell two-plane has zero compression for both. Tensoring with one-qubit expectation states realizes (t,…,t,0,0) for any t in [0,1] and hence the full radius interval. At n=2 the construction has no one-qubit factors and the interval is {0}. This is an analytic check, not a numerical or formal replay. No full-vector or full-error-correction claim is certified.

## originality

FAIL

The main all-n theorem is an immediate sharp consequence of the prior precise upper and lower bounds for diagonal tuples in Sun–Cao–Poon–Zeng, Proposition A.1 (A2)–(A4), not merely analogous to a published n=3 formula. Each signed cube-corner inequality contains all but one joint eigenvalue point and gives a valid half-space at rank two, so the prior bound directly gives ∥λ∥₁≤n−2; |λ_i|≤1 then gives the claimed quadratic bound. The very same proposition's lower bound gives the whole radial interval using the two disjoint opposite-diagonal sets on the last-two-coordinate square and free choices of the other cube coordinates. The exterior-square calculation is a different proof, and its Hamming support condition is a deterministic equality check in that alternate identity; neither makes the exact radial invariant distinct from the prior implication.

## value

FAIL

Local Z is a worthwhile family, but the exact radial invariant is already determined by elementary cube geometry in the prior diagonal-tuple bounds. The determinant calculation is a correct alternate proof, and making equality in its nonnegative average explicit is helpful exposition, but the frozen claim does not turn that identity into an independent structural theorem, equality-code classification or another nonmechanical exact invariant. There is no supported surviving result to repair merely by rewriting motivation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
