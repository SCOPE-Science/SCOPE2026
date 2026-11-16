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

Run `python3 verify_exact_witnesses.py` beside `verify_mod101.cpp`. The check was executed successfully from these final artifact paths and printed `DODECAHEDRAL_ERASURES_EXACT_CHECK_OK`.

The C++ checker exhaustively evaluates \(125970\) eight-row subsets of the \(20\times9\) harmonic evaluation matrix reduced by \(\sqrt5\mapsto45\pmod{101}\), finding \(123030\) independent bases and \(40991\) distinct hyperplane closures, exactly twenty-five of size twelve and none of size thirteen. The Python checker constructs integer-pair coefficients in \(\mathbb Z[\sqrt5]\) and confirms exact nonzero polynomial witnesses with precisely each twelve-vertex zero set. It also compares the collected closures with the exact witnesses rather than assuming they are the same.

The proof relies on the exact reduction implication from characteristic zero to characteristic \(101\), followed by separate characteristic-zero witnesses; modular tests alone would not prove existence of null vectors over \(\mathbb C\). The verified claims are limited to the specified twenty vertices and the degree-at-most-two spherical harmonic space. No externally independent validation was performed.
