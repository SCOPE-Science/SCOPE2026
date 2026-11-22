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

Run `python3 check_matrix.py` and `python3 check_jordan.py` from the directory containing both files. Both use only the Python standard library. `matrix_results.txt` and `jordan_results.txt` contain actual successful execution outputs.

The first checker explicitly constructs \(\mathrm{AG}(2,s)\) for \(s\in\{2,3,4,5\}\), including finite-field order four, forms the graph adjacency and reversible two-level transition as binary matrices, and calculates the nullity of \(T^t-I\) for every divisor of the claimed global order. This is compared with the displayed all-time formula. The second independently computes binary incidence rank and ranks of the first five powers of the adjacency matrix, checking the Jordan rank identities from the proof. Both report PASS. The same exact formulas have additional integer checks of Möbius inversion and sharp-order orbit positivity in these four examples.

The programs corroborate but do not certify all affine planes; the universal proof uses incidence axioms and exact linear algebra. No independent audit has been performed. No non-Desarguesian incidence database, additional prime characteristics, or stochastic variants are asserted to have been checked.
