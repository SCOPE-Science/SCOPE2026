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

# Verification and scope

The algebraic proof in `RESULT.md` establishes all-order and all-partition statements without empirical extrapolation. The standalone `verify.py` uses Python 3 standard-library rational arithmetic and independently compares directly formed matrix polynomials against the three entry formulas. Invocation: `python3 verify.py`. Observed output:

`VERIFY_OK exact_matrix_entry_and_cubic_identity_checks= 430180 partitions= 247`

The matrices cover every ordered complete multipartite partition of \(2\le n\le8\), Taylor orders \(1\le p\le8\), and four rational normalized steps per case. Exact cubic identities are additionally tested for every \(3\le n<100\) and each nonsingleton part size at four rational arguments. The program also checks row sums exactly, all even-order test-point sign equivalences, and the simplified cubic criterion. These are finite tests, not independent verification of the infinite analytic proof.

The underlying projector identities, scalar Taylor integral remainder, convexity and positive-kernel interpolation argument are stated explicitly in `RESULT.md`. At an even-order cutoff a cross-part entry is exactly zero and subsequently strictly negative; for odd orders each diagonal and each existing within-part off-diagonal has a unique and permanent crossing. No positive-time reentry is asserted or used.

Scientific limitations and a full-text access risk are recorded in `RESULT.md` and `REVIEW.md`. Independent audit has not been performed.
