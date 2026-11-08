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

The self-contained analytical proof in `RESULT.md` applies to every finite proper fair binary tree. The Python checker is corroborative rather than an infinite proof.

Execute `python3 verify_adaptive_haar.py` in the same directory using standard Python 3; no external libraries or downloaded assets are required. It independently enumerates all ordered proper binary tree shapes with one through seven leaves, constructs the probability-weighted signed kernel rows directly from the Haar basis, and exhausts ancestral sign choices using `fractions.Fraction`. It compares each sharp row value against the claimed closed expression and checks the full height spectrum for each leaf count.

Observed run diagnostics:

```
EXHAUSTIVE_PLANE_FULL_BINARY_TREES_PASSED 197
INDEPENDENT_KERNEL_ROW_EXTREMA_PASSED 1275
LEAF_COUNT 1 EXACT_SPECTRUM [(0, '1')]
LEAF_COUNT 2 EXACT_SPECTRUM [(1, '1')]
LEAF_COUNT 3 EXACT_SPECTRUM [(2, '2')]
LEAF_COUNT 4 EXACT_SPECTRUM [(2, '2'), (3, '5/2')]
LEAF_COUNT 5 EXACT_SPECTRUM [(3, '5/2'), (4, '13/4')]
LEAF_COUNT 6 EXACT_SPECTRUM [(3, '5/2'), (4, '13/4'), (5, '31/8')]
LEAF_COUNT 7 EXACT_SPECTRUM [(3, '5/2'), (4, '13/4'), (5, '31/8'), (6, '73/16')]
ALL_ADAPTIVE_DYADIC_HAAR_CHECKS_PASSED
```

The exhaustive domain is explicitly limited to seven leaves. A finite checker cannot establish the all-size dimension spectrum or all-depth formula; those follow from the displayed Bellman induction and exact tree-construction argument. No independent audit has been conducted.
