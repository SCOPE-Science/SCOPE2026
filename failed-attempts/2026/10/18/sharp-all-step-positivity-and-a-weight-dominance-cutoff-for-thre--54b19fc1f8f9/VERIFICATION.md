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

FAIL

The positivity classification itself is correct. On the range of L the identity L²−2sL+3tI=0 reduces the denominator to AI+BL. Multiplying its inverse by L gives the stated edge numerator xA+tB, over the product of the two positive denominator values, including the repeated-eigenvalue and zero-edge cases. For h>0 the numerator has one positive root precisely when 3x>2s; two edges cannot meet that inequality. The diagonal follows from the strictly positive scalar Padé factor, and the two-vertex case from its single contrast eigenvector. The strong-edge asymptotic follows by substituting t=x(y+z)+O(1). However, RESULT.md line 27 explicitly asserts double stochasticity even at negative entries. With the standard definition, the valid universal statement is unit row and column sums, not double stochasticity. The record's own (5,1,1), h=10 example has T12=−950/290563 and disproves the ancillary assertion. This wording correction cannot rescue originality. Independent finite replay: python3 -B /workspace/branches/reproduce_frozen_checks.py 3 compared 560 rational matrices using Cramer's rule, including this exact entry; it is corroboration, not the universal proof. Uploaded code was inspected, not run.

## originality

FAIL

The distinct October 25 indexed theorem covers the full October 18 finding, also including the strong-edge asymptotic and two-state minimality. This is demonstrable coverage in the indexed corpus, not a determination that the later-dated entry had chronological priority or that either derives from the other. There is no supported distinct mathematical remainder to repair.

## value

FAIL

An exact positivity horizon in the minimum reversible dimension is a motivated design invariant, but the indexed theorem already supplies it, the asymptotic and the full entry law on the same class. The remainder is a numerical substitution and a terminology correction, not an independently valuable new finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
