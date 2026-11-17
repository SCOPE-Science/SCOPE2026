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

Run `python3 verify_icosa_antipodal.py`; no packages beyond the Python standard library are required. It builds the icosahedral graph, derives its central antipodal involution from unique graph-distance-three partners, enumerates all 5,887 nonempty matchings, and reconstructs every signed simplicial boundary. It checks both antipodal eigenspace chain complexes over the primes three and five against exact rank tables. A logically separate unsplit boundary-matrix construction recovers the sum of the two eigenspace ranks in every degree at both primes.

The executed program's complete recorded output is embedded as `icosa_antipodal_output.txt`. Successful replay ends in `ICOSAHEDRAL_ANTIPODAL_TORSION_SIGN_PASS`. The argument from the finite mod-three rank table to integral antipodal torsion uses the natural universal coefficient sequence and the fact that order-two invariants are exact after localizing away from two. The code proves its enumerations via finite exhaustive operations; it does not establish unrelated claims about higher-dimensional graph families or the two-primary homology of the quotient.
