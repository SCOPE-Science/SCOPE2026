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
# Reproducible verification

Execute `python3 verify.py` using Python 3 and the standard library. At the time of preparation, it printed `SIGNED_PERMUTAHEDRON_EXACT_OK` and exact counts \(1,3,15,105,945,10395\) for ranks \(1\) through \(6\). It checks each rank's cancellation-free base-three direction, all signed permutations, the central-binomial identity, three independent rank-four generic direction families, and a complete balanced rank-three illumination incidence matrix (each of 48 vertices receives 15 of 48 directions).

The all-rank theorem is not an extrapolation from these checks. Its proof rests on the normal-cone identification, the finite exchangeable and sign-invariant Sparre Andersen theorem, openness of strict illumination, and the signed-permutation orbit averaging argument.

No independent mathematical audit has been performed. No claim is made about ordinary illumination or nongeneric coordinate generators. The referenced 2023 fluctuation theorem and 2023 normal-fan theorem are imported mathematical results and are separately identified in RESULT.md.
