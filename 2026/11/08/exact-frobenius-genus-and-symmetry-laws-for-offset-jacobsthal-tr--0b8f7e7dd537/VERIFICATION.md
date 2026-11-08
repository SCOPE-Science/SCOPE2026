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

# Verification and limits

The included `checker.py` is a standalone Python 3 script with no nonstandard dependencies. Running `python3 checker.py` computes exact Apéry residue minima by shortest paths in the finite residue graph for every \(3\le n\le16\), then compares the resulting Frobenius and genus invariants with all case formulas. It also checks the three-candidate minimizer transitions for all residue classes at every \(3\nmid n\) in this range, and verifies the symmetry-defect classification. The saved authentic output is included as `verification_output.txt`.

The unbounded statement is established instead by the proof in `RESULT.md`: a recurrence identity, two-generator gluing at multiples of three, an unrestricted three-candidate Apéry reduction elsewhere, strict minimizer comparisons, and exact symbolic summations. Checking finitely many \(n\) alone would not prove the unbounded result. The 2024 broad-recurrence source was compared at the level of its abstract and stated index scope rather than its entire article; independent external review of priority and proof has not occurred.
