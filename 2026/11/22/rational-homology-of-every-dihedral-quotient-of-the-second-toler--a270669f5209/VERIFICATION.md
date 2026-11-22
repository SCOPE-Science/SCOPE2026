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
# Reproducibility and scope

Run `python3 check.py` from this package. It uses only the Python standard library. The first section enumerates signed dihedral orbits and checks the exact formula for the inclusive interval \(4\le n\le30\). The second, separately constructed section computes barycentrically subdivided geometric quotient chain matrices, reduces them modulo \(1009\) and \(2\), and compares Betti ranks for \(4\le n\le13\). The infinite-family proof is in `RESULT.md`; the finite tests are not substitutes for it.

No assertion is made here about integral torsion in the quotient, an integral quotient homotopy classification, or an independent mathematical audit.
