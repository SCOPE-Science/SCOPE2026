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

# Computational corroboration
Run `python3 verify_unicyclic.py` using Python 3 with no third-party packages. The program independently backtracks over proper assignments of three named colours, checks that each non-isolated vertex has a singleton colour in its open neighborhood, and compares that count with an independent implementation of the cyclic signed formula. It additionally checks the positive/zero count against the gap criterion, and directly checks four-colour existence for small graphs when the three-colour count vanishes.

Completed output:
```
RANDOM_GRAPH_CYCLE_AND_DIRECT_THREE_COLOUR_CENSUS_PASS 276 total_vertices 1815
CYCLE_WITH_ALL_LEAF_SUBSET_PATTERNS_PASS 504
FIVE_CYCLE_ATTACHMENT_PHASE_TRANSITION_AND_BOUNDARY_PASS
VERIFY_OK
```

The first test set samples finite connected simple unicyclic graphs on three through nine vertices (including long and branched attachments). The second enumerates all 504 choices of attaching zero or one pendant leaf at each vertex of cycles of length three through eight. For small enough resulting graphs it performs complete direct colour enumeration; for larger instances it compares the signed formula against the independently encoded modular criterion. Random generation uses a fixed seed, and the script is standalone and reproducible.

The finite checks cannot establish the claim at unbounded order. The full proof in `RESULT.md` supplies the all-order local-factor bijection, residue closure reduction, and explicit four-colour constructions. No external audit or computationally exhaustive proof for all graph orders is asserted.
