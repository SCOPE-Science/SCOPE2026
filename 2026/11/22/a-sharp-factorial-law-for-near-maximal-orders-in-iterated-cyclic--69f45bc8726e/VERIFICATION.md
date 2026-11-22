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

The mathematical argument is self-contained after the standard permutational-wreath definition. The proof uses exact event conditioning, an exact recursion for \(F_h(j)\), the complement recursion, and a summable remainder induction. It does not infer an infinite theorem from finite tests.

Reproducibility: Run `python3 checker.py` in the same directory as the extracted files. The program enumerates full permutations from the iterated wreath construction and computes element orders from cycles; it compares the full exact order distribution against an independently evaluated rational recurrence. The captured `checker_output.txt` is supplied. The included tests cover groups up to 32768 elements; the proof covers all prime orders and wreath depths.

The near-maximal fixed-defect asymptotic does not apply when defect or prime varies with depth. Existing cycle-index results already imply all exact finite-depth distributions; priority of the new asymptotic prefactor has not undergone independent historical certification.
