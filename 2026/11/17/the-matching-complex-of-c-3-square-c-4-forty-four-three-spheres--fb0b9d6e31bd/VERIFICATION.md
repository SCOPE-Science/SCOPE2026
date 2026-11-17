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

Use Python 3.10 or newer, without additional packages. Run `python3 torus_match_verify.py` from the extracted directory. The expected terminal marker is `TOROIDAL_C3xC4_MATCHING_INTEGRAL_SYMMETRY_PASS`, following a full JSON record also saved in `torus_match_verification_output.txt`.

The program constructs the twelve-vertex graph and twenty-four edges from the Cartesian-product definition, enumerates all 2764 matchings including the empty matching, and checks the six nonempty face counts. A complete Hasse-DAG topological sort on 2763 faces and 10488 covering incidences checks the 1358 gradient pairs, yielding critical counts 1,45,1 in dimensions 0,3,4. Exact integer Morse recursion produces seven \(\pm1\) boundary entries, whose gcd is 1. A separate direct mod-two reduction on original simplicial chain groups checks the boundary ranks 23,181,567,538,50.

For every element of the natural order-48 symmetry group, two different exact evaluations agree: the signed fixed-simplex Lefschetz sum and the independence-polynomial recurrence on valid edge-orbit conflicts. The program prints the resulting 15 conjugacy-class traces, the character inner products for all fifteen rational irreducibles, the total dimension 44, and the subgroup-invariant dimensions 1 and 4. All coefficients and decisions are finite integer operations.

These checks prove the finite arithmetic when reproduced; they do not independently review the mathematical applicability of discrete Morse theory, the standard homotopy interpretation of a primitive attaching vector, or finite-group rational transfer. They make no assertion about other graph sizes or integral homology of quotient spaces.
