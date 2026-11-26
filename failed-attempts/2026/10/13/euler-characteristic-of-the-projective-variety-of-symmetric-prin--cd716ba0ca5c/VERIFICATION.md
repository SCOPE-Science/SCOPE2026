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

In the affine chart of the empty minor the principal-minor coordinates are Δ_I(A). Scaling a symmetric matrix by A ↦ DAD, with D=diag(z^(2^(i−1))), induces the weight 2Σ_{i∈I}2^(i−1) on Δ_I. The action preserves the closure and the subset-sum weights are distinct, so the ambient projective fixed points are exactly the 2^n coordinate lines. The image of diagonal A is the dense affine chart of the Segre product of n projective lines: its coordinates are ∏_{i∈I}a_ii. Its closure therefore contains every coordinate line; equivalently, the stated homogeneous degeneration has the unique least exponent at the selected subset. Localization gives χ_top(Z_n)=2^n, and compactly supported additivity gives zero for the ambient complement. For the dimension, the first and second minors recover all diagonal entries and the squares of every off-diagonal entry, so the affine chart map has finite fibers and its image closure has dimension n(n+1)/2. No extra smoothness assumption is needed. The finite tests described in VERIFICATION.md were not rerun.

## originality

FAIL

A distinct indexed record, b13467fc6f51, explicitly states that the projective variety of principal minors of symmetric matrices also has Euler characteristic 2^n. This is the same object and invariant for the claimed range, not a parameter match inferred from its broader title. The complement formula follows by additivity and the dimension was already stated by Oeding. The distinct record calls the symmetric case previously known but does not identify its source in the decisive passage; the evidence establishes equivalent coverage, not which same-day record originated it.

## value

FAIL

The complex projective object and its Euler invariant are natural, but the exact invariant is already covered in a distinct indexed statement. The complement contributes no additional numerical information beyond that equality, and the dimension is known. The frozen claim does not leave a separate new, motivated invariant to validate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
