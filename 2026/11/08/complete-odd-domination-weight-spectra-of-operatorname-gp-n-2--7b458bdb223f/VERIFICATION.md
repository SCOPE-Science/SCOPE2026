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

# Verification of the full odd-domination weight enumerator

Run `python3 verify_odd_matrix.py` and `python3 verify_odd_periodic.py` in the directory containing the two scripts. They require the Python 3 standard library only.

The first program independently constructs all \(2n\) equations of \((I+A)\mathbf s=\mathbf1\) for the actual graph (rather than assuming the proof's recurrence), row-reduces over \(\mathbb F_2\), enumerates all binary solutions and checks each against every original equation. It compares every weight count for \(5\le n\le60\) and verifies the kernel dimension. On successful execution the last line is `DIRECT_GF2_MATRIX_PASS_n5_to60`.

The second program enumerates all 1,024 binary candidate ten-step words, filters by the derived recurrence and cyclic consistency, reconstructs the inner ring, checks every neighborhood, and compares weight histograms for \(5\le n\le100\). It checks that exactly 64 ten-step words obey the recurrence. Its successful final line is `PERIODIC_RECURRENCE_PASS_n5_to100`.

The two methods are computationally independent in their primary state construction. The complete mathematical justification for all \(n\ge5\), including sizes and 5/10-periodic classification, is in `RESULT.md`; these programs are finite cross-checks. Historical priority and independent audit are not certified by program execution.
