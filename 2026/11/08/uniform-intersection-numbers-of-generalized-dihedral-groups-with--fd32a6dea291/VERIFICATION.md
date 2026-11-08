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
The standalone `verify.py` program uses standard Python 3 and does not require packages. It constructs all additive subgroups of each tested finite abelian kernel by iterative closure, identifies every maximal proper additive subgroup, forms their generalized-dihedral maximal-subgroup candidates via all reflection cosets, and enumerates all subsets of the resulting collection. Every intersection is represented by an exact integer bitset over the entire semidirect product. It checks the size of the Frattini subgroup and equality of the observed minimal and uniform intersection numbers with the symbolic formulas.

Run `python3 verify.py` and compare its entire standard output with `verification_output.txt`. The cases are \(A=C_3^2\), \(A=C_9\times C_3\), \(A=C_3\times C_5\), and \(A=C_3^2\times C_5\), with 279,040 examined subsets of maximal subgroups in total. The last case explicitly tests simultaneous independent Sylow-rank constraints.

These finite computations do not prove the formula for arbitrary odd abelian groups. The critical unbounded step is supplied by the full proof's maximal-subgroup and hyperplane-count arguments; the Python checker is a reproducibility and error-detection aid. No independent mathematical audit or external certificate has been performed.
