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

# Verification

The standalone `verify.py` constructs the literal adjacency graph, simulates parallel rounds of the ordinary zero-forcing rule, and tests every initial subset for path lengths \(4\le m\le14\). It checks the exact structural zero-forcing criterion, enumerates all inclusion-minimal forcing sets via single-element deletions, and compares these families with a separately generated explicit classification. It also checks \(1000\) deterministic pseudorandom seeds per path length at \(m=20,35,60,100\).

Run `python3 verify.py`. Expected terminal output includes `EXHAUSTIVE_ALL_SUBSETS_AND_MINIMAL_CLASSIFICATION_PASS` for each tested small length, `LARGE_RANDOM_FORCING_CRITERION_PASS` for each larger length, and final `VERIFY_OK`. The unrestricted result rests on the written proof, not on these finite tests. An independent mathematical audit has not been performed.
