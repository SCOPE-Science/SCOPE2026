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

Run `python3 verify_dihedral_pq.py` with Python 3 and no third-party dependencies. The script independently constructs the generated subgroup of each candidate finite subset using gcd congruences; it enumerates all one-, two-, and three-element faces, verifies the predicted face decomposition and the absence of four-element faces, then reduces the simplicial boundary matrix over the field with two elements. Output is recorded in `verification_output.txt`. Exact tested pairs are \((2,3)\), \((2,5)\), \((3,5)\), and \((3,7)\). This is corroboration only: the integral homotopy classification for arbitrary distinct primes uses the complete symbolic subgroup and spanning-tree proof in RESULT.md. No independent mathematical audit has been performed.
