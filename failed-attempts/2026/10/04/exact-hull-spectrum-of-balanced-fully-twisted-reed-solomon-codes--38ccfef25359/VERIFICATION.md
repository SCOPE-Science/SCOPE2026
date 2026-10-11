---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

The primary source's balanced-case proof explicitly permutes the stacked generator/parity-check coefficient matrix into independent \(2\times2\) blocks. The first block has determinant \(1+\eta_1^2\); for \(i\ge2\), the block has determinant \(-(\eta_i+\eta_{k+2-i})\). Every singular block has rank exactly one, so the total rank deficiency equals the stated hull dimension. Counting the involution orbits on \(\{2,\ldots,k\}\), including the even-\(k\) fixed point where \(2\eta_i\ne0\), gives the product enumerator and LCD constant term.

## originality

FAIL

The decisive block decomposition is already printed in the primary source's proof of Theorem 4.2(ii): it lists exactly the same \(2\times2\) blocks and their determinants. The submitted hull formula is the nullity obtained by allowing those published blocks to be singular, and the enumerator is then elementary independent counting across the displayed blocks. Under the rule that direct corollaries are covered without matching wording, the claim is not original.

## value

FAIL

The hull dimension and enumerator are natural invariants, but in this precise balanced family they are obtained mechanically from a block diagonalization and determinant conditions already printed in the source proof, followed by elementary orbit counting. That is a useful extraction, not an independently substantive mathematical advance under the common value standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
