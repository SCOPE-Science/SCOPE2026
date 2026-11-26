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

The four-dimensional moment image of the TV unit ball is compact and spans the moment space (use four distinct nodes). Separation gives attained duality over bounded real cubics, and weak-star compactness gives primal attainment. Both nonzero amplitudes force the sign interpolation p(a)=1, p(b)=−1 for optimality; interior contact also forces p′(a)=p′(b)=0. These determine a unique cubic, namely T₃((t−c)/Δ) with c=(a+b)/2 and Δ=b−a. Since |T₃|≤1 exactly on [−1,1] over the reals, the test is Δ≥max(1+c,1−c). Failure implies a strictly lower attained TV, not just a second minimizer. At a feasible pair the saturation set has at most four nodes, the two interior sites and possibly one or both endpoints. Any minimizer is supported on these nodes; four monomial moments are injective there by Vandermonde rank. For uniformly sorted sites, at center c the half-gap ranges up to 1−|c| and must be at least (1+|c|)/2. Using Jacobian 2 gives recovery area 1/3 out of ordered area 2. At |c|=1/3 there are in fact no feasible interior pairs, consistent with the stated exclusion for |c|>1/3. These checks are exact; the source checker was inspected, not run, and grid diagnostics are not needed for the result.

## originality

PASS

Credit the established TV duality and Chebyshev certificates. The supported distinct claim is a complete feasible-location criterion at degree three for independently moving, oppositely signed interior sites, including strict failure and uniqueness even when the certificate also touches at an endpoint. Neither the exact symmetric instance nor the general sufficient separation/certificate results inspected settle this location classification.

## value

PASS

At the four-moment budget, exact invertibility of a sparse model and success of unrestricted TV minimization are genuinely different questions. The threshold classifies when TV succeeds, certifies strict failure everywhere else irrespective of amplitudes, and settles the equality case that strict-certificate theorems cannot cover. This is useful as a sharp benchmark for low-degree recovery; the probability is a consequence, not the reason for acceptance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
