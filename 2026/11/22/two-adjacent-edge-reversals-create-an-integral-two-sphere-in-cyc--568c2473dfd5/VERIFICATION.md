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

# Reproducibility and proof checks

Run `python3 verify.py` with Python 3 and no third-party dependencies. The supplied `verification_output.txt` is its recorded output, not a substituted certificate. For all odd orders from 5 through 15 and all allowed second-arc separations, the checker constructs all transitive faces directly from tournament orientation, compares them against the asserted cyclic-block complex with exactly the two new triangles (and one exceptional tetrahedron), and verifies every proposed free-face collapse pair. An independent boundary-rank calculation over \(\mathbb F_2\) confirms the nonextremal two-dimensional class and extremal acyclicity for orders at most 11.

The proof of the all-parameter statement is the exhaustive *symbolic* classification of new triangles, four-faces and higher faces, combined with the natural nerve equivalence of the primitive attaching loops. Finite computations alone do not prove the infinite claim and do not test integral torsion directly. The argument supplies the integral homotopy type independent of field computation. External independent auditing has not been performed.
