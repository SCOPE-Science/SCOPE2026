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

The equation with one central input makes the horizontal component of R(z) zero by nondegeneracy. With R(z)=cz, the defining identity is equivalent to (A-cI)^T J(A-cI)=c(c-lambda)J and imposes no condition on the central functional. This is reversible, including in characteristic two. At a zero multiplier, count ordered isotropic frames, divide by bases per image, and count surjections to the image. At a nonzero multiplier a symplectic-basis block dilation provides a representative and the multiplier fiber is a coset of Sp; counting symplectic bases gives the claimed order. The scalar polynomial has one or two distinct roots according as the weight is zero or not. These are shifted ranks, not ranks of R. Fresh enumeration of horizontal blocks in dimension five over F_2 against the unshifted identity checked, per singular c, ranks 0,1,2 with counts 1,225,3150 and the nonsingular block count 720, before the 16 choices of functional; totals are 65536 and 108032. Replay: python /tmp/opencode/frozen_review_reproduce.py heisenberg.

## originality

FAIL

The advertised all-rank nonsingular branch and the whole weight-zero census are already present in a distinct indexed statement. For nonzero weight the odd-prime census is exactly equivalent, at the level of the counted tuples, to another indexed theorem. Outside odd primes the remaining formula is a routine consequence of the already available all-field reduction and counts, not a distinct new census method or phenomenon. This is a statement-level comparison, not a claim about who proved it first.

## value

FAIL

The isotropic/similitude distinction is mathematically useful, but the assessed extension does not add a substantive remaining invariant or structural result after the exact matching censuses and the multiplier normalization. Applying an already counted zero/nonzero multiplier split to c(c-lambda) only changes the number of scalar copies; the residual characteristic-two and extension-field cases use this same elementary count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
