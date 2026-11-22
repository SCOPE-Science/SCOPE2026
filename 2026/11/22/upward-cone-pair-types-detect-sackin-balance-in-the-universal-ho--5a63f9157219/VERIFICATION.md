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

## Reproducibility

Run `python3 verify.py` from the directory containing the provided files. The script uses only Python's standard library and prints the recorded deterministic output in `verification_output.txt`.

It enumerates all rooted binary tree shapes through eight old leaves, subdivides ancestral edges by two distinct new labelled nodes, and obtains complete finite \((<,C)\)-signatures directly from the resulting rooted witnesses. For each shape it checks that the counts of strict-upward, strict-downward, and incomparable channels match the claimed formulas. It separately checks the minimum and maximum leaf-depth sums for each number of leaves, without assuming that all trees have the same balance.

The finite check does not prove classification for unboundedly many leaves; the normal-form construction, homogeneity, and depth induction in `RESULT.md` are the mathematical proof. The classical Sackin extrema are attributed rather than independently re-established by the bounded checker. No external independent audit has been performed.
