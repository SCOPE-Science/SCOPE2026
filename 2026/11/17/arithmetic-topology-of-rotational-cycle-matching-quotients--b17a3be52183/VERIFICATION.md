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
# Verification of the quotient classification

The mathematical proof is contained in `RESULT.md`; the following are **finite exact corroborations** rather than infinite certificates. The two standalone scripts read no input files and do not rely on any unpublished data. Execute them with Python 3, and install SymPy for the second script.

`python verify_rotation.py`

The first checker exhaustively generates independent edge subsets, rotation-invariant edge orbits, and fixed-point Euler characteristics for \(8\le n\le18\). It verifies the Euler sums of the covering complexes, all generated stabilizer subgroups, the generator's signed chain Lefschetz number, and the predicted full quotient rational Euler characteristics.

`python verify_prime_quotients.py`

The second checker constructs the quotient cellular chain groups for \(p=5,7,11,13\), including signed face identifications under cyclic rotation. It verifies both boundary compositions and uses integer Smith normal forms (not floating-point linear algebra) to calculate all homology groups. For \(p=11\), quotient cell counts are \((1,4,7,5,1)\), free homology occurs in degrees zero and three, and the sole torsion is \(\mathbb Z/11\) in degree one. For \(p=13\), quotient cell counts are \((1,5,12,14,7,1)\) and the sole torsion is \(\mathbb Z/13\) in degree one. Widths five and seven have the homology of a circle.

`check_output.txt` records both actual successful executions. These scripts do not compute the cup products or prove the nonzero spectral-sequence transgression; those are deduced mathematically in the proof. They do not check infinitely many widths, higher composite-length integral homology, or independent publication priority.
