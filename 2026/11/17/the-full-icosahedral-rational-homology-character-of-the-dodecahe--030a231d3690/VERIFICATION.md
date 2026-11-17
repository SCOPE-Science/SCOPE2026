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

The executable `verify_dodeca_symmetry.py` uses the Python 3 standard library only. Execute it from the package directory with `python3 verify_dodeca_symmetry.py`; compare stdout with `VERIFIER_OUTPUT.txt`. An actual execution on the embedded file returned `DODECAHEDRAL_PERFECT_MATCHING_CHARACTER_PASS`.

It enumerates all 36 perfect matchings, all 30,504 faces (including the empty face), 120 explicit graph automorphisms, and computes signed traces on every automorphism. Separately, it generates every invariant face from edge-orbit subsets and computes geometric fixed-space Euler characteristics. The two methods agree in all 120 cases. Class frequencies, central parity, irreducible rational characters and invariant dimension are checked exactly.

The previously published nonequivariant homology theorem (degree-two order-two torsion and 20 free degree-three generators) is an explicit input, not an independently reconstructed integral Morse proof. The new character calculation is exhaustive and exact for the stated finite graph; it does not provide an integral equivariant lattice classification or an independently certified global novelty result.
