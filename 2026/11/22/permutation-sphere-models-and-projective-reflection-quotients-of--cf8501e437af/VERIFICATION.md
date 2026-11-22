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

# Reproducibility and boundaries

Run `python3 checks/verify_spider.py` at the extracted package root. This uses only the Python standard library and prints `VERIFY_OK; direct subgroup-orbit complexes: 32 ; odd path widths: 58`. The script enumerates exact independent-set face polynomials, subgroup arm-orbit models and Euler characteristics for the specified finite examples, compares the literal PL fixed-orbit simplicial model, and tests the predicted top orientation signs by the reduced Lefschetz formula. The odd-path range checks the ordinary quotient Euler characteristic using the geometric fixed-space Burnside formula.

These checks do not compute integral Smith normal forms for arbitrary quotients, do not certify equivariant Whitehead equivalence by finite enumeration, and do not replace the unrestricted topological proof. The integral projective-space torsion follows from the explicit representation-sphere quotient model in `RESULT.md` and the standard integral cellular homology of projective space.

The exact reference basis and checked source types are stated in `RESULT.md` and `AUDIT.json`. No independent mathematical audit is represented here.
