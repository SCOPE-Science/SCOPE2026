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

Execute `python3 verify_cycles.py` and `python3 verify_prism.py` using Python 3.10+ (standard library only). The first checks all 36 allowed 4-mers, constructs the 18 contracted directed edges from actual overlap paths, enumerates every fixed-edge Euler circuit, and verifies exactly 4,800 distinct rotation classes plus the stated witness. The second builds the prism graph independently from permutation transitions and checks the 75 spanning trees by enumerating all 126 candidate five-edge subsets, and independently applies BEST to obtain 4,800.

The complete proof also requires the graph-theoretic suppression argument, Kirchhoff's theorem and BEST's theorem as written in `RESULT.md`. Exhaustive tests of the finite graph do not replace these identifications. No external or independent mathematical audit has been performed.
