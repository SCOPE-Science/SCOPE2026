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

# Computational verification and limitations

The supplied `verify.py` requires only Python 3's standard library. Run `python3 verify.py` from the extracted package directory. A successful execution ends with `CYCLE_DIHEDRAL_INTEGRAL_LATTICE_VERIFIED`.

It constructs independent-set complexes by direct enumeration. For each \(1\le k\le7\), it expands the three proposed integer chains using every one of their \(2^k\) terms, explicitly evaluates all signed simplicial boundaries, checks the two maximal-independent-face pairings, applies every generator of the dihedral action with orientation signs, confirms the matrices and exact group relations, and calculates both coinvariant orders from integral determinants and gcds of minors. For \(1\le k\le5\), a separate boundary-rank calculation checks reduced Betti rank two over characteristics two, three and five.

These finite checks neither establish an infinite theorem nor replace the algebraic proof in RESULT.md. The infinite argument uses an independently published nonequivariant sphere-wedge theorem, explicit cocycle duality with determinant one, integer orientation formulas and elementary Smith forms. No completed independent mathematical audit is represented by this file.
