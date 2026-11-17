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
The all-parameter proof uses an explicit description of the Alexander dual, a uniform elementary-collapse argument, equivariant Alexander duality, and signed Lefschetz trace identities. The finite verifier `VERIFY.py` is a separate check, not a substitute for those arguments.

On the packaged files, running `python3 VERIFY.py` reproduces `VERIFIER_OUTPUT.txt` and finishes with `VERIFY_OK`. It verifies 1,200 elementary unique-coface removals for sixteen values of the ladder width, 800 signed dual-complex character calculations, and 72 independent direct checks of the ordinary cut complex at three smaller widths. It also verifies connectedness and the correct edge count for the collapsed graph in every tested case.

The nontrivial all-parameter ingredients are the classification of dual faces, the freeness of the square-by-square elementary collapses despite shared antipodal graph edges, and the orientation-sign relation in equivariant Alexander duality. These are proved in `RESULT.md`. Computations do not address uncatalogued literature or identify an integral equivariant module structure. No independent external validation has been performed.
