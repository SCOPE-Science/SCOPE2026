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

# Verification and limits

The standalone `verify_random_simple.py` script is pure Python and reproduces the exact small-instance enumeration by running `python verify_random_simple.py` from the directory containing the package files. The accompanying `verification_output.txt` contains the actual output. Five prime-field/dimension cases were enumerated. The program uses independent algorithms for invertibility, strong connectivity, and monomial-action orbits; it verifies the orbit–stabilizer relation, Burnside consistency, and invariance of simplicity under natural-basis changes.

The general asymptotic rests on the symbolic cut union bound, coordinate-orbit dimension bound, loop obstruction to diagonal automorphisms, and Burnside's formula. The finite checker does not prove these claims for arbitrarily large dimensions or for arbitrary nonprime finite fields. The proof handles all prime powers because it uses only field arithmetic and counting, not a prime-subfield restriction.

The scientific comparison distinguishes existing general Burnside formulas and the previously solved two-element-field case. Other equivalent derivations may exist; independent literature and mathematical review have not been performed.
