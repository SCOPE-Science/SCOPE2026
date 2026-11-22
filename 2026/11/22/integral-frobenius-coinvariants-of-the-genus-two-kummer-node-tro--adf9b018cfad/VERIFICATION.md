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

The standalone `verify_kummer_coinvariants.py` constructs the node–trope incidence matrix from the six-label description and checks the equal-incidence and degree identities exactly. It tests all \(720\) permutations for incidence compatibility, computes the Smith diagonal of the base matrix, and computes Smith normal forms for one conjugacy representative per partition. Separately, Hermite normal forms of the augmented integer presentation matrices give exact residue indices at moduli \(2\), \(3\), and \(4\). These are enough to reconstruct every elementary divisor because the universal incidence identity kills the quotient by twelve.

Execution command: `python verify_kummer_coinvariants.py` with Python 3 and SymPy installed. Successful execution ends with `PASSED: 11 classes, 720 permutations, 16x16 incidence, exact integral Smith forms`.

The proof applies to finite fields of odd characteristic, not to nonreduced two-torsion in characteristic two. The calculated group is a formal integer-incidence cokernel, not an arithmetic Picard or Brauer group. The calculation does not settle whether an equivalent equivariant table was computed in unindexed historical design literature.
