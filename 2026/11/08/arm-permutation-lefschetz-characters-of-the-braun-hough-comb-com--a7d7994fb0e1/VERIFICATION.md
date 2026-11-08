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

Run `python verify_comb_euler.py` using the Python 3 standard library only. Its expected exact output is embedded as `verification_output.txt`.

The verifier constructs all graph edges directly from the definition, recursively enumerates every independent face, applies each arm-label permutation to oriented simplices, computes its sign by the inversion parity of the image of the ordered face, includes the augmented empty face, and sums signed traces. It checks all permutations for each of 18 parameter pairs, totaling 498 permutation checks, 20,996 individually enumerated independent faces across the graph cases, and a separate four-state signed matching-transfer check for the even-parity Euler sequence through degree 28.

The independent checks cover finite cases, not arbitrary graph sizes. The uniform proof is the orbit-bijection/Lefschetz-sign argument combined with a published recurrence and a known homotopy sphere fact; no computational extrapolation is asserted as proof. No independent external audit has been performed.
