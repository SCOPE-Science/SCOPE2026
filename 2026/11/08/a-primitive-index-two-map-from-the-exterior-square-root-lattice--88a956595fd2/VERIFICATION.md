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
# Finite exact checks and their limits

The executable `verification/verify_petersen_lattice.py` reconstructs the ten vertices and fifteen edges of the Petersen graph from disjoint two-subsets of five labels and uses a signed boundary matrix for the ordinary integral graph homology. It constructs an integer basis of its six-dimensional kernel, then builds the standard \(A_4\) action and its exterior square.

The program checks \(A(g)U=UW(g)\) for each of the 120 permutations, verifies determinant \(-2\) and Smith invariants \((1,1,1,1,1,2)\), and computes rank 35 modulo 101 for the 72-by-36 intertwiner system from two generating permutations. Existence of \(U\) gives the complementary rational upper rank bound; no probabilistic argument or finite-experiment-to-infinite inference is used. Its exact output is stored alongside the code.

The geometric identification with the Picard torus uses the normalization exact sequence for nodal curves and the ten-line incidence result; it is supplied in the proof rather than deferred to code. Galois descent follows functorially from the verified full \(S_5\)-equivariance. The calculations do not certify literature priority or independent validation.
