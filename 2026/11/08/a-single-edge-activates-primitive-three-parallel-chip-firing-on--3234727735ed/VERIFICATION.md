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

# Reproduction and scientific limits

Run the bundled `verify_direct.py` and `verify_phase.py` under Python 3 with no third-party dependencies. Their captured standard outputs are `direct_output.txt` and `phase_output.txt`. Direct iteration exhausts bounded labelled configurations for \(1\le n\le6\); the phase checker independently enumerates local firing-phase inequalities for \(1\le n\le8\). Each compares every mass coefficient in its tested range against the exact claimed expression, not just the totals. Both passed when executed in the final package preparation.

All primitive-three states lie inside the checked finite chip box for each tested graph, by the proved confinement lemma. The finite checks establish the test cases only. The universally quantified claims, sharp gap, population formula, single-edge contrast, and limiting distribution are proved symbolically in `RESULT.md`. Other periods, attraction basins, and unindexed historical literature have not been exhaustively resolved. Independent audit is not performed.
