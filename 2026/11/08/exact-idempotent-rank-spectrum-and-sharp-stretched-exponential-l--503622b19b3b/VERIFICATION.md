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

# Verification and boundaries

The finite verifier is `verify.py`, using only the Python standard library. Running `python3 verify.py` independently constructs all closed nearest-neighbor walks on each even cycle with 4, 6, 8, 10, 12, or 14 vertices, turns each into an actual graph endomorphism, tests equality of its square with the original map, and tabulates image sizes. A separate path-adjacency dynamic program predicts each rank multiplicity; all complete spectra match. The observed idempotent totals are 9, 25, 73, 221, 685 and 2157. It also compares exact counts for larger even dimensions 64, 128 and 256 with the claimed analytic scale as a non-proof sanity check; the script prints `VERIFY_OK` on success.

The proof of the general formula does not invoke computational enumeration: it uses image-path geometry and exact matrix-power walk counts. The asymptotic constant is derived from the two top path eigenmodes and a uniformly localized Laplace sum. The limiting Gaussian law follows from the same local expansion. These are infinite mathematical arguments; finite experiments cannot independently certify them.

Originality comparisons distinguish the previously known total graph-endomorphism count and general retraction principle from the proposed rank spectrum, and distinguish the unconstrained range-penalized walk asymptotics from the fixed opposite-endpoint walk count. The earlier Michels–Knauer paper and any broader unavailable count remain publication-priority risks. Independent audit has not been performed.
