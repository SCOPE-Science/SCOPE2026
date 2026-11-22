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

# Reproducibility

The supplied `checker.py` requires the Python 3 standard library only. Run `python3 checker.py`; it enumerates all normalized induced permutations, every relevant affine group element, all four squarefree-divisor Möbius terms, and all support residues. It verifies 72 interpolation values with prime field sizes, twelve extra prime-field controls, and three separate direct-orbit calculations.

The infinite statement follows from Fan's published degree-at-most-five and twelve-period theorem plus equality of degree-five polynomials at six independent prime-field arguments per residue class. The finite checks alone do not prove an unbounded claim. Dirichlet's theorem guarantees all twelve residue classes contain infinitely many prime-field parameters. The decoded packaged files, not an external run log, supply the executable finite verification.
