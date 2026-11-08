---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility and verification

Run `python3 verify.py` in the same directory as `rational_certificates.tsv` using Python 3.9 or newer. The script requires only the Python standard library and uses `fractions.Fraction` for all expectation calculations and comparisons. It reconstructs the stated rational recurrence for all integers \(2\le a\le11\) and checks each certified numerator/denominator pair against the accompanying tab-separated certificate file.

For each \(3\le a\le11\), it verifies the strict inequalities \(T_B(a)<7/2<T_A(a)\) by exact integer arithmetic, with no floating-point thresholds. For \(2\le a\le6\), it independently builds every labelled blue-subset state, considers every independent simultaneous infection outcome, and solves all transient first-step equations in decreasing blue-set size, then matches the two start states against the compressed recurrence. This independent implementation does not assume part-size symmetry in its transition kernel.

The script also checks the equal-size boundary and the finite starting cases of the dyadic inequalities. The proof in `RESULT.md`, not a bounded loop, establishes the all-parameter comparison for \(a\ge12\), using an explicit geometric waiting-time lower bound and a coupled maximum-of-geometric-clocks upper bound. The same proof gives the asymptotic gap; no simulation or extrapolation is used for the infinite claim.

Historical novelty is assessed against the accessible cited primary literature and indexed published records; these checks cannot certify that no unindexed proof exists. Independent mathematical assessment has not been performed.
