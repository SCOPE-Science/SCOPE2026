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

For the actual RESULT.md equations (1)–(6), invertibility makes the basis squares span and strong connectivity propagates one square in a nonzero ideal to all the others. A proper closed vertex set gives the converse ideal; singular matrices have a proper square ideal or zero multiplication. Counting block-triangular invertible matrices gives the stated cut probability, in particular (q−1)/(q^n−1) for each elementary event. Two distinct elementary events require at least 2n−3 distinct zeros. Second Bonferroni and a middle-cut union bound, conditioning from independent entries by dividing by φ_n(q), establish the explicit error even when the middle sum is empty. The k=2,n−2 terms are O(n²q^(−2n+4)); all remaining terms are bounded by 2^n q^(−3n+9)≤q^(−2n+9). The same exceptional-event bound divided by the leading failure probability gives the conditional one-cut estimate, with its orientation split by transpose. Finally φ_n−φ_∞=O_q(q^(−n)) is lower order than the failure probability, so the stated first-order deficit has the correct sign and constant. These asymptotics are for fixed q; the exact bound and counting argument apply to all prime powers. The supplied finite checker was inspected, not executed, and covers only small prime fields.

## originality

FAIL

A distinct indexed record in the identical labelled invertible-matrix model gives the same sharp simplicity law under stronger uniform control, with the same elementary-cut argument and conditional structure. This is demonstrable coverage in the available record set, not an inference about publication priority from catalog dates. The remaining explicit bound and all-matrix normalization give no nonmechanical independent remainder.

## value

FAIL

A sharp law and structural explanation for the dense simplicity question would be valuable if distinct. The package reproduces the covered mechanism and rate; the displayed unsummed elementary cut bound and the immediate product-tail normalization add no substantive surviving scientific claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
