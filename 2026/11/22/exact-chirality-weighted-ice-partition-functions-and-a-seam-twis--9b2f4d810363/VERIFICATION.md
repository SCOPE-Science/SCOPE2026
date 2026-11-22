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

# Verification of chiral-weighted ice seam polynomials

The standalone `verify_ice.py` reconstructs cubic prism and twisted Möbius base graphs directly, builds all line-graph edges from common endpoints, and enumerates every arrow assignment satisfying two incoming arrows at every line-graph vertex. It independently records each designated triangle's local indegrees to obtain the full chirality polynomial. It compares every coefficient with recurrence-polynomial predictions at each width three through seven for both boundary conditions. It also checks the exact polynomial seam difference for every length from three through one hundred, using integer polynomial arithmetic. The successful observed output ends with `ICE_SEAM_POLYNOMIAL_IDENTITY_OK n=3..100`.

The infinite-family proof is the symbolic nine-state transfer matrix computation supplied in RESULT.md. The finite verifier supplies corroboration, not the logical basis for all positive lengths or continuous fugacities. No numerical conditioning, random sampling, or inaccessible external library is required.
