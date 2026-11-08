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

## Reproduction
Run `python3 check_neighborhoods.py` and `python3 check_gaps.py` in the directory containing those two embedded standalone scripts. They use only the Python standard library. Compare output with `neighborhood_check.txt` and `gap_check.txt`.

The first script explicitly constructs the wheel graph, tests the global locating-dominating property against both graphs for **all** subsets until the minimum size is reached, then obtains the exact token-slide graph, its edge count, and components for every wheel of order 4 through 14. It uses the full definitions rather than the rim-gap lemma.

The second script separately enumerates all cyclic distance words meeting the proved necessary-and-sufficient conditions for three or more selected rim vertices, reconstructs their translated configurations, and forms their slide graphs for orders 7 through 14. At order 14 it independently checks the full dihedral orbit, the two rotation orbits, and that every code has degree one.

These two programs provide finite exhaustive verification, not a proof for larger wheels. The only claim beyond the finite cutoff is the general gap-characterization lemma, which is proved in `RESULT.md` under its stated hypotheses. No independent audit or external formal verification has been performed.
