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

# Finite verification details

Run `python check_bitmask.py` and `python check_sets.py` in a fresh Python 3 environment. Neither uses external libraries, network access or solver calls. Both enumerate every one of the \(2^{16}=65536\) vertex subsets in each graph. The first stores sixteen 16-bit open-neighborhood masks, applies the exact total-domination predicate, and computes induced perfect matchability by the standard recursive partner decomposition for a fixed selected vertex; it also independently checks all 256 entries in the neighborhood-incidence equivalence and the two exceptional claws per center. The second constructs graphs with coordinate-pair sets, enumerates by `itertools.combinations`, applies direct set-intersection predicates and an independently written recursive matching search.

Expected total-domination coefficients in degree order 0 through 16: `0,0,0,0,80,1056,4768,9520,12150,11280,7992,4368,1820,560,120,16,1` for both graphs. Expected paired-domination coefficient arrays: Shrikhande `0,0,0,0,48,0,4384,0,12054,0,7992,0,1820,0,120,0,1`; rook `0,0,0,0,80,0,4464,0,12150,0,7992,0,1820,0,120,0,1`. The two programs check these arrays or their differences and assert the key combinatorial identities.

The finite sample space is completely exhausted, so no larger-graph extrapolation is necessary or asserted. The calculations confirm exact integers for these graph definitions, but no external independent scholarly validation has been performed. The primary historical-priority risk is inaccessible or unindexed literature, not an unfinished computational search.
