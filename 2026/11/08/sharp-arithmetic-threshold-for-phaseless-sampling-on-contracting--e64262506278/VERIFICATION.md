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

Use Python 3 with SymPy, in the same directory as `verify_spiral.py`, then run `python verify_spiral.py`. A successful run prints `GEOMETRIC_SPIRAL_PHASE_VERIFY_PASS distinct=12 collision=3 resonance=57 exact_vandermonde=9`.

The checker verifies distinct geometric bases for a nonresonant algebraic contraction across degree bounds zero through four, the first collision at rational angular denominators one, two, and four, 57 exact ambiguous-pair equality calculations, and an exact nine-dimensional lifted Vandermonde inversion for a quadratic. The proof of the all-degree and all-holomorphic results is analytical, based on a determinant identity and a dense-rotation argument; the finite checks do not validate those claims by enumeration. The checks are same-model corroboration only and do not constitute independent audit or certification.
