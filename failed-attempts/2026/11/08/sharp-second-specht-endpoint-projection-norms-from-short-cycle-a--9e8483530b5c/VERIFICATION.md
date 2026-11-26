---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The unordered-pair permutation representation contains exactly the trivial, standard and (n-2,2) irreducibles for n>=4; subtracting the first two characters gives chi=F(F-3)/2+T_2. Its only negative values are -1 at F=1 or 2 and T_2=0. The mean is zero by orthogonality, so E|chi| is twice the probability of those disjoint events, namely 2q_(n-1)+q_(n-2) after choosing the fixed letters. The full coefficient block is a multiplicity-one regular bimodule. Averaging over both sides cannot increase the norm of a projection onto it and gives precisely the central convolution projector, whose norm is the absolute row mass by a sign choice. Exact equality holds precisely when some row's nonzero kernel entries align with the input at unit modulus and one common phase (a sign over the reals). This also shows that real and complex norms coincide. The relative minimum is absolute here: the host finite sup-norm space is injective by coordinatewise Hahn–Banach. The EGF gives the stated coefficient formula by expanding exp(-z-z^2/2)/(1-z); the numerator is entire and its coefficient tail has the stated bound by Cauchy's estimate for each R>1. The n=4 case is included, with q_3=1/3 and q_2=0 giving 4/3.

## originality

FAIL

The central claim is shown already known, not merely possibly overlapping. A distinct, earlier accessible October 18 record explicitly gives exactly n(n-3)(q_(n-1)+q_(n-2)/2) for the same full (n-2,2) coefficient block, all n>=4, and the same q generating function. Its novelty is the band comprising three blocks; it labels this identical single-block norm known. The real version follows directly from the real kernel and real equality witness. Standard row equality and coefficient estimates do not establish a new central invariant.

## value

FAIL

The invariant is well motivated and the proof is useful exposition, but the submitted research claim re-evaluates an already explicit exact norm of the same natural Fourier block. The residual observations supply neither a different invariant nor a new structural phenomenon: the norming inputs are the exact equality condition for one known finite convolution row, and the normalized asymptotic and error are direct from the same known generating function. No independently valuable new remainder is established in this record.

The dated certificate retains the supplied scientific assessment, sources and limitations.
