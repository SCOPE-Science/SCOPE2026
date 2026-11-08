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

# Reproducibility

Run `python verify.py` with Python 3 and SymPy installed. The script constructs each weighted sunlet Laplacian directly from its cycle and pendant edges, removes two chosen leader rows/columns, and inverts the resulting rational grounded matrix. It independently compares that inverse trace against the three closed formulas and checks every predicted optimizer and its count for integers \(3\le n\le8\), including each exact critical conductance and multiple off-critical values. It also checks, by exact symbolic simplification, the two final pairwise differences used in the proof.

Observed local replay: `PASS: two symbolic comparison identities, with positive coefficients for n>=3`; `PASS: 1797 independently inverted rational grounded matrices and 29 exhaustive optimizer classifications`.

These finite checks are not infinite certification. Universal correctness is supported by the exact Green-kernel identities, Schur complements and sign arguments in RESULT.md. Independent audit is not performed.
