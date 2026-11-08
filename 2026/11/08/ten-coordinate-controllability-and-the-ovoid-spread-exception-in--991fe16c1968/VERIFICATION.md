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

Run `python3 verify.py` from the directory containing this file. The script requires only Python 3's standard library. It deterministically constructs the 30-vertex graph, performs all exact finite rank tests, and prints `PASS` after confirming the exact control-set census.

The analytic part of the proof is in `RESULT.md`. The numerical certificate is exhaustive in the following finite sense: all 3003 five-vertex choices of each type are tested, the admissible 1518 edge choices are partitioned into complete orbits under all 720 permutations of the six base labels, and every admissible 1518 matching choice is tested against one representative from each of the eight orbits. Group invariance makes this a complete classification of all 1518-squared candidate pairs, not a sample.

All crucial modular rank decisions are provably identical to rational rank decisions by the Hadamard determinant bounds of 243 for the incidence minor and 10,077,696 for the nine-column eigenspace minor, both below the chosen prime 1,000,000,007. The certificate independently checks direct 30-state reachability on a controllable placement and an exceptional one.

The verification proves the stated finite result for this exact unweighted incidence graph only. It does not prove a corresponding result for other generalized quadrangles or for perturbed edge weights. No independent external audit has been performed.
