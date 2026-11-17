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

Reproduction command from the package root: `python3 code/verify_wheel_quotient.py`.
The program requires Python 3 and SymPy; it was executed with Python 3.13.5 and SymPy 1.14.0. The actual complete output is embedded as `verification/output.txt`.

The enumeration includes all nonempty matchings, all increasing chains of such matchings, all twenty dihedral edge permutations and every orbit of chains. Burnside flag counts are independently checked, integer boundary compositions vanish exactly, and each integer Smith normal form has only unit nonzero factors. Matrix digests allow detection of inadvertent changes to boundary construction or ordering. The proof's van Kampen and Armstrong arguments are mathematical arguments; they are not claimed to be verified by code.

The final conclusion is a homotopy equivalence, not a homeomorphism. A failed execution or dependency error is not evidence of either correctness or incorrectness and should be resolved before reusing the numerical certificate. Independent audit has not been performed.
