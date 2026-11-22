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

# Reproducible checks

Run `python3 check_direct.py` to evaluate the actual sets of all distinct one-deletion outputs of every binary word at all weights and lengths from two through ten. The completed run compared 124,453 unordered pairs, checked the modular coloring on each edge, verified every displayed clique construction, and checked the ten pair intersections of the induced five-cycle.

Run `python3 check_intervals.py` to use a separately written alternating-interval generator and independently check every fixed-weight edge and clique through length fourteen. The completed run evaluated 247,598 directed edges and tested the induced five-cycle under all valid zero/one padding regimes through length sixteen.

Both programs use only Python 3 standard-library modules and print an explicit `PASS` line on completion. An assertion failure raises an exception. Finite tests are not proofs at untested lengths; the general proof is in `RESULT.md` and explicitly invokes the published Type-A characterization. The all-length claim does not assert a maximum independent-set size or that a global proper coloring proves graph perfection.
