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

# Finite computational verification

Run `python3 proof/verify_k34.py`. Expected standard output is exactly the complete `proof/verify_k34.out` file. The code is standalone Python 3 and imports only the standard library.

For three unordered particles, the sufficiently subdivided graph has 19 vertices and 24 edges. Enumeration finds 969, 3264, 3510, 1192 cells in dimensions 0 through 3. All 4,702 cells of dimensions two and three pass their integral boundary-square tests. The exact modular ranks for differentials one through three are (968, 2289, 1192) over characteristic two and (968, 2290, 1192) over each of characteristics three, five, and 1,000,000,007. The rational ranks follow from the independent mathematical upper bounds in RESULT.md, specifically the six-dimensional cycle-lifting quotient of first homology; modular ranks alone are not claimed to establish them.

All 144 automorphisms are enumerated. Cubical boundary equivariance is checked on representatives of all fifteen conjugacy classes and follows for every member by group conjugacy. Signed cubical trace characters are computed for every group element. The complete character table is checked against rational irreducible characters, with exact integer multiplicities, and both invariant-subspace dimensions vanish. The last output line is `K34_THREE_UNORDERED_CHARACTER_PASS`.

The method does not determine the integral second-homology torsion, integral equivariant lattices, or a homotopy decomposition. No external independent audit is represented by these computations.
