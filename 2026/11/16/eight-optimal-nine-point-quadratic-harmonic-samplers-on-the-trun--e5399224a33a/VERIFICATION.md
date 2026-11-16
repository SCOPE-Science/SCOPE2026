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
# Reproduction and mathematical verification

The standalone file `verify_truncated_tetrahedron.py` needs Python 3 and SymPy and uses exact integer and rational arithmetic for all mathematical accept/reject comparisons. From the labeled tetrahedral vertex coordinates it reconstructs the harmonic addition-theorem kernel, the integer polynomial evaluation matrix, and the rank-three left-kernel certificate. It generates the complete permutation action on three deleted directed-edge labels, verifies the thirteen orbits contain every one of the 220 triples, and tests one representative of each orbit using exact arithmetic. Its determinant-inertia separation proves eight and only eight optimizer sets; its exact characteristic polynomial and isolated rational roots give the optimum. The output's PASS statements report assertions that actually ran successfully.

The finite search is exhaustive for this fixed twelve-point geometry, not a numerical search over all spherical placements. Rank and spectral comparisons are exact; decimal approximations shown in prose are for readability only. The checker does not establish historical novelty or any extension to different degrees, point sets, or sample weights.
