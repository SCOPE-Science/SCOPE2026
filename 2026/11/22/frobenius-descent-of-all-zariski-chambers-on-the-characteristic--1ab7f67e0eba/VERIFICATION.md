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

# Verification

Run `python3 verify_fano_chamber_descent.py` with Python 3.10 or later and no third-party packages. The program reconstructs all 168 invertible binary three-by-three maps and their fourteen-vertex actions, checks preservation of the entire geometric intersection form, and exhausts 16,384 negative-support candidates. It checks negative definiteness with exact rational \(LDL^t\) separately from the induced-degree-at-most-one criterion, then checks the five fixed-support polynomials using independent direct-mask and vertex-orbit-union enumerations. It partitions all 2,257 supports into exactly 54 collineation orbits and verifies Burnside's formula and both order-seven conjugacy classes. The successful output is `fano_chamber_verification_output.txt` and concludes with `FANO_FROBENIUS_ZARISKI_CHAMBER_DESCENT_OK`.

The algebraic geometry (exhaustive negative-curve classification, chamber-to-support correspondence, and ground-field descent via a Galois-stable effective support) is established in `RESULT.md` rather than inferred from finite computation. The statement does not claim an independent audit, a classification of all forms or universal historical priority.
