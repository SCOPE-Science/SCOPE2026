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

# Reproducibility and verification

Run `python3 verify_archimedean.py` with SymPy available. The successful observed execution ended in `ARCHIMEDEAN_QUADRATIC_UNIQUENESS_CHECKS_PASS`.

The script uses exact arithmetic to (i) construct the twelve regular-truncated-tetrahedron vertices and confirm quadratic evaluation rank nine and sphere-equation kernel, (ii) check sample proper-octahedral orbits and the exceptional cube/octahedron ranks, (iii) verify weighted character orthogonality for the octahedral and icosahedral rotation groups and (iv) check quadratic interpolation rank nine on the exact regular icosahedron over the quadratic field with \(\sqrt5\).

The universal proof does not rely on brute-force testing all nonzero vectors, which is impossible. It uses decomposition into inequivalent irreducible representations, direct nonvanishing criteria for each summand, and an exact four-sign calculation for the truncated tetrahedron. The character checks corroborate the displayed computations; the standard classification of the thirteen Archimedean solids by proper rotation group is used as a geometric input.

No numerical experiments establish global uniqueness, and no independent audit has been carried out.
