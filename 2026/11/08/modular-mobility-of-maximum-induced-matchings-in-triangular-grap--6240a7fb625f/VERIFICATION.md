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

The all-order claim is proved symbolically in `RESULT.md`. Two stand-alone Python 3 checks use different encodings and have no external library dependencies.

`python direct.py` constructs the triangular graph from its vertex-intersection definition, enumerates every candidate subset of the known maximum size, tests the induced matching condition directly, and enumerates all one-edge jump and slide transitions for \(3\le n\le8\). It verifies the exact state count, both degree formulas, and the component-size multiset.

`python abstract.py` instead enumerates partitions into disjoint marked triples and unused labels, independently produces legal neighboring states, checks symmetry of every transition, and verifies counts, degrees, and component-size distributions for \(3\le n\le9\).

The captured standard outputs are `direct_output.txt` and `abstract_output.txt`. Both programs ran without errors and reported PASS for every tested input. Neither finite census establishes the all-order theorem by itself; the proof of the support bijection, local move characterization and spare-label connectivity is necessary for the infinite extension.

Review status: Self-review: passed. Independent audit: not yet performed.
