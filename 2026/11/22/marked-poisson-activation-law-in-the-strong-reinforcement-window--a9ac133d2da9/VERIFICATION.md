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

At size t the sum of the outdegrees is t−1, hence the total weight is D_t=t+a(t−1). Given the activation history, each eligible nonroot label has probability 1/D_t; the root is already ineligible at size two and the newborn enters as a leaf. Per step an independent proposal of each nonroot label with probability 1/[a(t−1)] followed by acceptance at rate a(t−1)/D_t for eligible labels exactly reproduces this complete history. The rejection probability is t/(aD_t)+(H_t−1)/D_t with H_t the number of already active vertices including the root. The expectation of H_t−1 is at most (t−2)/a, by counting all earlier positive proposals. The two numerators sum in expectation to at most 2(t−1) over a common denominator aD_t, yielding 2/a² per step, even at t=2; for n=2 the two empty histories agree. This is a total-variation bound on the labelled joint law, not just the count law. In the stated triangular array n/a_n² tends to zero. Taking logs of the independent reference Laplace functional incurs an O(n/a_n²) error, and the mark inside each time slice is uniform on the label grid j/t. The grid Riemann sums converge uniformly away from t/n=0; the bounded integrand and the vanishing relative fraction of early times complete the limit on the compact square including λ=0. The root-star event is exactly zero nonroot activations and its reference probability is (1−1/a_n)^(n−2). The source VERIFICATION.md, checker.py and checker_output.txt were inspected without execution; the reported exact finite checks are source evidence, not independent execution or a certificate of the limit.

## originality

PASS

The complete affine leaf-set occupancy construction in the distinct same-date leaf-repulsion result covers more of the mechanism than a change in seed wording suggests: a ghost-leaf conditioning reduction transfers its exact finite leaf-history law to this model. Credit that overlap fully. The supported distinct increment is the uniform whole-history approximation by a particular independent reference with explicit error 2(n−2)/a² and the joint critical birth-time and birth-label law, rather than the exact finite leaf kernel, the fact that proposals can be taken independently, or the star probability alone. The approximation requires bounding repeat and rate errors; it is not a statement of the exact occupancy theorem. The date supplies no ordering between the two records.

## value

PASS

A quantitative approximation for the full finite birth-labelled experiment is useful for arbitrary joint first-parent queries and need not reconstruct the reinforced tree. Its vanishing-error range a≫√n is broader than the fixed finite-intensity critical window; the critical limit then gives the interpretable independent fractional birth labels and event times. The finite-survival formula and zero-event limit in isolation would support a much smaller contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
