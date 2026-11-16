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

# Checks and mathematical limits

Run `python CHECK.py` in the directory containing the script with Python 3 and SymPy from `requirements.txt`. The checker computes all sixteen complex Gaussian moments, sixteen entries of the normalized Parseval Gram matrix, and twelve radial consistency identities using symbolic exact arithmetic. It prints `EXACT_FOCK_CUBIC_SIX_NODE_CHECKS_PASS 44` on success, without floating-point tolerance. It is an exact construction check, not an exhaustive enumeration of all possible planar nodes.

For universal minimality, the full proof uses real-quadratic annihilation of at most five sites, moment orthogonality, perpendicular-line geometry, and a positivity/Vandermonde argument. Central-symmetry uniqueness uses distinct-radii and further moment interpolation. Historical priority and independent audit remain unverified.
