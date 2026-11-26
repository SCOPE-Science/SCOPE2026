---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Fix A and U=im A. For uniform B the map B|_U is uniform in Hom(U,V), and postcomposing with the surjection A produces a uniform endomorphism of U. Since AB lands in U, nilpotency is equivalent to nilpotency of its restriction (at most one extra iterate is needed). The Fine–Herstein count then gives conditional probability q^(−rank A), including rank zero. This equals Pr(Aw=0|A) for an independent uniform vector w. Apply it to the product T of the first k−1 factors (T=I for k=1). The probability that Tw is nonzero is (1−q^(−n))^k: w must start nonzero, and each independent uniform factor encountered from right to left maps a given nonzero vector to a uniform vector. A nilpotent radical preserves and reflects nilpotency on passage to the quotient, since x^m in J and J^s=0 imply x^(ms)=0. Equal fibers give independent uniform quotient inputs; the direct-product block probabilities multiply. The zero ring has probability one. Frozen verify.py was inspected, not executed. Its 21 comparisons are exact finite convolutions for the selected matrix rings over prime fields and three additional rings, not verification of the all-rings or all-length quantifiers.

## originality

FAIL

The same arbitrary-length law for all nonzero finite unital rings is stated in a distinct indexed complete-profile result that also classifies identical probability sequences. The zero ring convention adds no substantive remainder. A separate exact semisimple result and a more general cyclic rectangular result also cover the main matrix identity. These findings establish current exact coverage, not priority or a provenance relationship; the matching indexed records carry later dates. One- and two-factor prior results and the elementary implication of the classical nilpotent count further limit the scope of any distinct contribution. No narrow repair survives.

## value

PASS

The all-length profile is a meaningful structural ring statistic: it ignores the radical and conflates a full matrix block with the corresponding extension field. Correctness and this structural usefulness do not make the result distinct from the exact indexed coverage; the scalar, two-factor, and zero-ring slices would not rescue it.

The dated certificate retains the supplied scientific assessment, sources and limitations.
