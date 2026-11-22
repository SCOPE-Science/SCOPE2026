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

The exact calculation uses all \(2^{12}=4096\) exterior monomials in a twelve-generator Chevalley–Eilenberg complex. `character_exact.py` computes exact rational cohomology traces by independent multidegree blocks; `invariant_exact.py` separately checks every differential square and all twelve equivariance identities, then calculates the full-dihedral invariant complex; `subgroup_exact.py` supplies further subgroup calculations, including the identity-group full cohomology. `crosscheck.py` reconstructs all six conjugacy-class traces from the subgroup invariant ranks without consulting the character algorithm's intermediate elimination bases.

All code is standalone Python with no third-party dependencies, internet calls, numerical tolerances, or saved cross-run dependencies. Included output files record concrete successful checks, including the final `crosscheck.py` PASS. These are exhaustive finite-dimensional computations over \(\mathbb Q\); they rely on the established Nomizu identification for the topological interpretation and do not test any claimed general result beyond this twelve-dimensional complex.

No independent mathematical audit has been performed. An exact finite computation does not, by itself, certify publication priority or establish integral torsion and multiplicative cohomology.
