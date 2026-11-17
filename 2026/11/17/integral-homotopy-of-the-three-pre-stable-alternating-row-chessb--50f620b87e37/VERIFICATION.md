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

# Verification record

`verify.py` constructs two independently specified complete orbit cellular chain complexes for every width in the theorem. The first enumerates the actual \(A_4\)-orbits of all allowed row injections; the second uses the explicit parity convention and signed face formula. It verifies the two chain identities and the full exact integral Smith normal forms of all three boundaries using `sympy==1.14.0` with no floating-point arithmetic.

Run `python verify.py` in this directory after installing `requirements.txt`. The observed results, reproduced from this package, are stored verbatim in `verification_output.txt`. Both constructors check all column subsets and all legal ordered row injections, not a selected sample. These calculations are finite; the wedge-of-spheres/Moore conclusion additionally uses the topological argument in RESULT.md and does not follow from logs alone.

An independent mathematical audit has not been performed.
