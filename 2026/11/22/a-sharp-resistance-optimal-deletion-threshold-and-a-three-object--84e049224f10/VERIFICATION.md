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

# Reproduction and scope

Run `OPENBLAS_NUM_THREADS=1 python verify.py` with Python 3, NumPy, and SymPy available in the directory containing this document. A successful run prints `PASS: 908 parameter sets; exact inversions, Laplacian spectra, KKT and threshold checks.`

The program reconstructs unnormalized Laplacians directly from every individual edge weight, verifies the full Laplacian eigenvalues and inverse trace, checks budget saturation and the nonlinear KKT conditions (including one-sided deleted-edge conditions), and compares admissible nearby allocations at 810 pairs of network order and price/budget parameters. It also performs exact rational inversions and characteristic-polynomial checks at small network orders and exact rational comparisons of the three previously published thresholds for 96 orders.

The universal theorem is proved algebraically in `RESULT.md`; this script's finite cases are not an exhaustive enumeration of infinitely many orders or real price values. The cross-objective comparison uses separate previously published D- and E-threshold theorems rather than attempting to re-prove those theorems.
