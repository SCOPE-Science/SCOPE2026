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

Under independent sites and Poisson counts the failure probability is the product of Laplace transforms. The negative log transform has strictly negative second derivative at t>0 by nondegeneracy and tilted variance, extends strictly concavely to zero, and gives the unique balanced allocation. For a real count x the exponent's derivative is -h((H+c)/x-c), with h(t)=(t+c)φ'(t)-φ(t), h(0)>0 and h strictly decreasing. Subtract λ0t to obtain ψ(t)=o(t). For q>0, ψ tends to -log q and integrability of its decreasing derivative gives tψ'(t)→0. For q=0, ψ diverges: if the nondecreasing gap ψ-tψ' were bounded, integrating (ψ/t)' from t to infinity would bound ψ, a contradiction. These limits prove the exact one-site criterion including strict finite-time optimality at equality and the λ0=0 and q=0 cases. Otherwise the unique root gives the continuous target. Adjacent feasible integer differences are negative at their feasibility endpoints, strictly increasing in H by strict decrease of φ', and eventually positive. At a tie strict concavity and the mean-value theorem put the continuous target strictly between the two counts, giving disjoint ordered threshold brackets, no skipped counts, and the count asymptotic. The two-rate example was separately recomputed and matches the stated dwell and detection probabilities. VERIFICATION.md and checker.py were inspected, not executed; the reported 10,469 numerical assertions are not needed for the analytic conclusions.

## originality

PASS

Balancing under concavity, the cost-adjusted count optimization, and special cases of a finite preferred dwell are adjacent to, or covered by, earlier survey/restart optimization and an exact two-atom catalogue analogue. The distinct contribution supported here is the lower-endpoint atom criterion for arbitrary stated rate laws, with equality and atomless cases, together with the universal deadline-indexed, non-skipping strict threshold sequence in the rotation phase.

## value

PASS

The exact contrast between a positive rate floor with an atom and the same floor without one resolves when a fixed overhead can suppress rotation for all horizons. Combined with the discrete thresholds it describes both a qualitative experimental-design boundary and the order and location of all changes in optimal effort. The result is about the idealized iid at-least-one objective, not empirical model validity or detection-rate estimation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
