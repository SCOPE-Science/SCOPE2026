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

# Verification instructions and scope

Run `python3 verify_hex_quotient.py` using Python 3.10 or newer from this directory. The program imports only Python's standard library and reconstructs all graph vertices, horizontal edges, vertical rungs, independence faces, row-exchange permutations, invariant simplex supports, and quotient barycentric orbit cells. It does not read or trust any other package result.

For every length from one through six, the code checks equality between the set of all invariant independent faces and the set of unions of even-column row pairs, with exactly \(2^n\) invariant faces including the empty face. It independently evaluates Euler characteristics and checks the quotient Euler characteristic by Burnside's formula. For lengths one and two, it constructs every flag of nonempty independent faces, uses full orbits of flags under the involution to form a cellular quotient model, calculates boundary ranks over \(\mathbb F_2\) using exact bitwise Gaussian elimination, and checks that the resulting Betti numbers match a single sphere in the expected dimension. At length one, an explicit greedy free-face elimination removes all six two-cells and six one-cells, leaving a connected nine-vertex, nine-edge graph.

The expected final line of `verification_output.txt` is `ALL_VERIFY_OK`. The finite calculations do not establish an infinite-parameter theorem by themselves and do not test integral torsion at all lengths; that conclusion instead follows from the explicit relative group-ring argument in `RESULT.md`. The geometric quotient is distinct from a homotopy quotient, and the result does not address end reflections or wider hexagonal strips.
