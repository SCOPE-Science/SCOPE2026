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

# Exact verification

The standalone `verify_frames.py` has no third-party dependencies and runs with Python 3. Execute `python3 verify_frames.py`. It regenerates the complete candidate sets without preloaded frames, enumerates the exact dual LP basic feasible distributions using `fractions.Fraction`, applies only integer support inequalities to all six ordered tetrahedra, checks the determinant histogram and computes the complete signed-coordinate symmetry partition. The accompanying `orbit_classes.csv` is derived from the same complete frame list. The algorithm's finite domain follows from the proven integral pairwise-distance bound; neither a floating-point solver nor random sampling is needed.

Expected output includes: 24 nonzero vectors at norm at most two; no frame below radius \(3/2\); 62 nonzero vectors at norm at most three; 1264 subset-sum candidates; optimum counts 512, 408 and 8 at indices 1, 2 and 4 respectively; exactly 23 signed-coordinate orbits. The checker gives the exact complete list of orbit representatives and ends with `PASS`.

The underlying Chebyshev dual extreme-point classification is derived from four affine constraints and all 162 nonempty subsets of the eight signs having size at most four. The finite case analyses are exhaustive rather than approximations to a continuous optimization. This code does not establish publication priority or constitute an independent mathematical audit.
