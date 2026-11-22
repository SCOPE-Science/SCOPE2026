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

Run `python verify_degree_wheel.py` from the extracted directory. The script uses the Python standard library only. It checks all 924 candidate edge subsets, 320 genuine spanning trees, the 128-point unnormalized Walsh transform, 128 independent signed six-by-six Laplacian determinants, 13 exact dihedral orbits, the complete signed spectrum, 38 zero modes, and the inverse Walsh transform of the recoverable-frequency indicator. Exact integer arithmetic confirms the projection numerator absolute sum 420 and denominator 128. No random sampling or numerical tolerance is used.

The finite certificate is exhaustive only for the stated six-rim wheel. The code does not prove a general-wheel formula or independently certify historical priority.
