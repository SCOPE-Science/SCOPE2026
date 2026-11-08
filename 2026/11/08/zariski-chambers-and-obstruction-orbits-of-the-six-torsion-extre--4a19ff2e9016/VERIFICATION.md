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

# Reproducibility and limits

Run `python3 verify_chambers.py` with the Python 3 standard library. Expected last line: `EXACT_PRINCIPAL_MINORS_AND_ORBIT_AVOIDANCE_AGREE`. The test enumerates all \(131072\) subsets of the \(17\) negative curves; it uses exact integer Bareiss determinants, no floating-point arithmetic, and an independently coded forbidden-hypergraph avoidance pass. Its recorded output is `verify_chambers.out`. The polynomial coefficients are asserted exactly; three singleton, one size-three, and eleven size-six translation orbits cover the \(72\) minimal forbidden supports.

The mathematical input is the intersection form established in `RESULT.md` using adjunction, fibre combinatorics and the known Mordell--Weil classification and height formulas. The script does not certify the cited published classification or prove the abstract theory of Zariski decompositions. It computes the *entire finite combinatorial classification* once that input is fixed, rather than extrapolating from samples. No external independent audit has been performed.
