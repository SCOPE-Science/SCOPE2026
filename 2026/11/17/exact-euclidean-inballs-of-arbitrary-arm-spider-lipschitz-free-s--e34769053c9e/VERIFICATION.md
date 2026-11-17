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

# Reproduction and limits

The analytical proof in `RESULT.md` establishes the formula for every integer number \(q\ge3\) of arms and every collection of positive integer arm lengths. The inequalities are exact (not floating-point computations): the key necessary replacement is strictly positive whenever an arm has mixed signs, since the tree has at least one vertex beyond that arm. The finite checker is corroboration only.

Extract `check_spider.py` alongside the other accompanying files and run `python3 check_spider.py` with Python 3. It uses `fractions.Fraction`, `itertools`, and standard-library-only exact rational elimination. It checks (1) all 1,022 signed paths through length nine for the arm-variance inequality; (2) 86 spider length profiles by brute-force enumeration of 68,904 polar vertex sign configurations, comparing exact radius, contact count and affine dimension of all centers; and (3) 1,113 profiles for the signed triangular-weight partition dynamic program.

Expected output from an observed local replay:

```text
ARM_PATH_VARIANCE_INTEGER_IDENTITY_PASS 1022
SPIDER_ALL_SIGNED_EDGE_POTENTIALS_PASS profiles=86 potentials=68904
TRIANGULAR_PARTITION_COUNTS_PASS profiles=1113
ARBITRARY_ARM_SPIDER_THEOREM_FINITE_CHECKS_PASS
```

No finite numerical enumeration certifies the result for unbounded arm lengths; its proof is the strict universal variance comparison, cube-facet characterization, signed-partition identity, and linear-algebraic normal-rank argument. No independent audit, formal verification, or expert certification has been performed. The result concerns unweighted trees and the exact zero-sum Euclidean embedding only. Other terminology may conceal an equivalent published formula.
