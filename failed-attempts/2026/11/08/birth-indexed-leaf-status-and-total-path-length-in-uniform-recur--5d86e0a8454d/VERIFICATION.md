---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

Conditioning leaf j means forbidding all independent future parent selections P_k=j, leaving them independent uniform on k-2 eligible parents. This gives exact conditional recurrence a_(k+1)=k a_k/(k-1)+1-H_(j-1)/(k-1), whose solution a_k-E[T_k]=-(H_(k-1)-H_(j-1)). Multiplying by P(leaf j)=(j-1)/(n-1) gives indexed covariance; summation gives -(n-2)/4; adjacent differences and harmonic approximation give strict concavity and e^-1 limit. Independent enumeration of every recursive tree up to n=7 verified exact conditional means and covariances. This mathematical correctness does not imply originality.

## originality

FAIL

Published November 2, 2026 full RESULT.md An exact leaf–path-length covariance profile in random recursive trees gives precisely the same uniform-parent model, for every n and i, the same conditional expected path-length shift, identical covariance -(i-1)/(n-1)(H_(n-1)-H_(i-1)), the same sum -(n-2)/4, exact adjacent difference and the same asymptotic maximizer at i/n->1/e with limit 1/e. Its proof repeats the same conditioned parent-restriction recurrence. The entire submitted finding is covered, not just a related global moment.

## value

FAIL

The invariant itself is natural and would be worthwhile in isolation, but its exact conditional profile and every claimed corollary are already published with identical quantifiers and proof; the new package supplies no independent mathematical fact, classification or extension.

The dated certificate retains the supplied scientific assessment, sources and limitations.
