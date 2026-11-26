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

Under the all-coordinate independence specified in the assumptions, W=1−V turns the arc rule into U_i>W_j. The reciprocal kernel has mean 1/4, variance 3/16 and one-index projection g=U(1−W), with variance 7/144. Disjoint pairs are independent; the shared-index term in Var(R_n) has multiplier 6 binom(n,3). An incident reciprocal pair is incompatible with a sink, whereas a disjoint pair and a sink coexist with probability ∫(1−t)^(n−3)((1−t)^2/2)^2 dt=1/[4(n+2)]. Arc reversal handles sources. A same-label sink/source pair uses disjoint coordinates; distinct labels share the constraint U_i<W_j, giving the stated beta integral and strict covariance positivity by the central-binomial bound, including n=2. Omitting self-arcs changes the two full-boundary proxy counts only on exceptional rows/columns, with disagreement probability at most 1/(n+1) each from the expected first spacing. The four endpoints have asymptotically independent unit-rate Poisson limits by the one-index rare-event transform. A boundary count before the first point of the opposite process is geometric with parameter 1/2; truncation to compact windows and the absence of ties justify the mapping. In the reciprocal first-projection CLT the degenerate remainder has variance O(n²). Boundedness of g gives an O(n^−3/2) per-index mixed Laplace–Fourier term on endpoint events of probability O(1/n), which vanishes after multiplication by n and proves independence, not merely pairwise zero covariance. The n^(3/2) normalization gives 7/144 as stated.

## originality

PASS

Prior work gives the exact model and its finite graph law, sink marginal distribution/limit, joint zero probability and arc-count CLT. Do not credit these ingredients as new. The compact reciprocity and cross-covariance formulas and the simultaneous limit of the two extremal counts with the reciprocal-pair CLT are a distinct contribution on inspected evidence.

## value

PASS

Zero directed degree and reciprocal connectivity are different natural network statistics. Explicit finite covariances distinguish positive sink/source association from negative sink/reciprocity and source/reciprocity association. Establishing full independence at their disparate fluctuation scales separates a finite dependence effect from the limiting behavior in an established random graph model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
