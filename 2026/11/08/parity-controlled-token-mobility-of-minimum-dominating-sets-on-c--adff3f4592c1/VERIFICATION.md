---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Reproducibility

The program `verification/verify_prism_direct.py` uses explicit vertex subsets, closed-neighborhood bitmasks, and every possible swap. Its finite exhaustive checks of minimum sets and moves include $n=5,9$; the recorded outputs in `verification/direct_output.txt` also include other residue classes for comparison, not as new claims.

The separate program `verification/verify_prism_language.py` constructs the singleton-gap word families and checks the original domination condition, all pairwise one-token differences and host-graph adjacency. In particular, it checks each $n\equiv1\pmod4$ from 5 through 129. This finite check analyzes the generated words, not all possible size-minimal subsets. Its output is `verification/language_output.txt`.

Both programs use only the Python 3 standard library. From the package root run `python3 verification/verify_prism_direct.py` and `python3 verification/verify_prism_language.py`. The all-size proof for the claimed residue is in `RESULT.md`.
