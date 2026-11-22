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

# Verification record

The standalone `verify.py` computes Franel numbers from the integer recurrence and checks the first \(58\) against direct exact binomial-cube sums. It reproduces the complete base-\(29\) digit residue table, the three mod-\(841\) constants and derivative residues, and every claimed valuation class for \(0\le n<2600\). It also counts the complete \(0\le n<841\) sample, yielding \(676\) valuation-zero, \(154\) valuation-one, and \(11\) higher-valuation cases.

These computations check only a finite range. The all-index theorem rests on the cited Gessel–Lucas congruence for Franel numbers and on the proof's exhaustive finite base table. The known Gessel–Lucas theorem is a published mathematical premise, not independently recertified by these calculations. Higher valuation layers are not asserted.

