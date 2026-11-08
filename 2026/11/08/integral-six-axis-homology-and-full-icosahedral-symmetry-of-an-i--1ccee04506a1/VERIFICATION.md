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

The theorem is verified by a structural proof in RESULT.md and the standalone executable `check.py`. Run `python check.py` with Python 3.10+, NetworkX and SymPy; no network access or external datasets are required. All twelve adjacency lists are in the script and in RESULT.md.

The program reconstructs the icosahedral graph and the entire ordinary independence complex; checks all simplices and vertex links, each pair's graph distance, the six antipodal edges, connectivity and Euler characteristic of the canonical spherical subcomplex; constructs the exact integer differentials and their Smith normal form; enumerates all 120 graph automorphisms; and calculates both signed-axis and signed-chain Lefschetz characters for each. The two character methods agree elementwise. The complete recorded output is `verification_output.txt`, ending in `CHECK_ALL_120_AUTOMORPHISMS_PASS`.

Reproducibility confirms the enumerated finite premises. The use of the closed-surface classification, the equivariant homology long exact sequence, and standard icosahedral character theory are explained mathematically in RESULT.md. Numerical computations alone are not used to infer a general theorem. The statement does not determine an equivariant homotopy type and has not been independently audited.
