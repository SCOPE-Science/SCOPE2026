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

Run `python CHECK.py` using Python 3.8 or newer. The program constructs each order-six group table and all incidences, confirms the size, degrees and full block Gram identity, calculates the rank of the line-point incidence modulo three, and computes the reduced Laplacian's 2-adic and 3-adic Smith exponents via actual invertible elimination modulo high prime powers. It repeats the calculation for two different roots (a line vertex and a marked-point vertex), reassembles divisor-ordered invariant factors, checks their products against the independent symbolic Matrix-Tree count, and checks both complete decompositions.

For the cyclic table, the respective 2-adic and 3-adic exponent multiplicity vectors (for exponents 0,1,2,3) are (38,1,12,2) and (30,11,11,1). For the dihedral table they are (38,1,12,2) and (32,7,13,1). The program prints `NET6_CYCLIC_DIHEDRAL_NERON_GROUPS_OK` if all checks pass. The verifier uses no numerical approximations or external libraries.

The existence of the two geometric nets and the standard Néron component-group interpretation are cited from the primary literature; the checker verifies the integral graph calculations, not all facts in those papers. No claim of independent audit is made.
