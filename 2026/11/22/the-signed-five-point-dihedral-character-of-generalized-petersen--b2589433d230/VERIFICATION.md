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

# Verification scope
The independent exact-arithmetic program `check_gp_dihedral.py` reproduces all rotation and reflection trace identities for the four indices \(n=5,10,15,20\), totaling 100 action traces. Run it from the extracted package directory with `python check_gp_dihedral.py`; its standard-library recursion enumerates independent subsets through the deletion formula at \(-1\). The finite output is a consistency check, not an exhaustive proof of the family. The complete argument in RESULT.md establishes the all-integer claim by a general orbit-graph Lefschetz formula, Kim's nonequivariant classification, parity reductions, and rational character theory. The integral representation, quotient torsion, and nonstandard full automorphism groups are not checked. No independent mathematical audit has been performed.
