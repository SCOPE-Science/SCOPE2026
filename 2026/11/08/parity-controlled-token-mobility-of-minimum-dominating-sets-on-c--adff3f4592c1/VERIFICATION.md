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
# Reproducibility

The program `verification/verify_prism_direct.py` uses explicit vertex subsets, closed-neighborhood bitmasks, and every possible swap. Its check covers all lengths \(3\le n\le12\) except \(n\equiv2\pmod4\); the exact outputs appear in `verification/direct_output.txt`. This is exhaustive for each checked finite length.

The separate program `verification/verify_prism_language.py` constructs the singleton-gap words from the theorem and independently checks the original domination condition, all pairwise one-token differences and host-graph adjacency through \(n=129\), omitting the nonclaimed lengths. Its output is `verification/language_output.txt`. The language test does not enumerate all possible size-minimal subsets; the direct checker does so in its stated range.

Both programs use only Python 3 standard library, are deterministic and terminate without external data. Execute from the extracted bundle root using `python3 verification/verify_prism_direct.py` and `python3 verification/verify_prism_language.py`. Their tests verify exact finite instances and state-to-state adjacency; the all-length correctness claim rests on the proof in `RESULT.md`. Independent human/third-party validation has not been performed.
