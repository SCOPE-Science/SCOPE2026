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

# Exact reproducibility

Execute `python3 verification/check_petersen.py` from the package directory (or by absolute script path). Only Python's standard library is used. Expected marker: `PETERSEN_TREE_WALSH_PASS trees=2000 signings=32768 orbits=396 rank=18856 gcd=16 projection=36651/1024`.

The script builds the 10 vertices as 2-subsets of five elements, the 15 disjointness edges, and the 2000 spanning trees by union–find over all 5005 nine-edge candidates. It evaluates the complete 32768-character unnormalized Walsh transform using exact integer butterflies; verifies **every** one independently against a 9-by-9 signed weighted Laplacian determinant computed by integer Bareiss; reconstructs 396 symmetry orbits from all 120 permutations of the five base elements; verifies the supplied orbit and magnitude certificates; checks multiplier and projector Parseval identities and minimum positive multiplier; and evaluates the exact endpoint projection numerator 1172832. No random seed, external packages, online data, or floating-point rounding are needed.

The exact finite census is exhaustive for the Petersen graph, but is not a general graph-family statement or external mathematical review. No claim of originality follows solely from the computation.
