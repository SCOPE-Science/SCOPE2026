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

# Reproduction of finite checks

The standalone `CHECKER.py` builds all incidence vectors and integer Gram determinants for every unordered three-edge subset of every unlabeled tree on \(6\le n\le11\). It checks the individual determinants \(4,6,8\), recomputes both sides of the stated intrinsic-volume identity, counts matchings and four-vertex paths directly, and compares all trees with the prescribed unique extremizers. It separately verifies the two same-degree six-vertex spiders.

Run `python -m pip install -r requirements.txt` and then `python CHECKER.py`. One completed run using Python 3 and NetworkX 3.6.1 printed:

```
THIRD_INTRINSIC_TREE_ZONOTOPE_CHECKS_PASSED 428 40821 416
SPIDER_EXACT_DIFFERENCE 0.07055236082016547
```

The first line reports the 428 nonisomorphic tree cases, 40,821 triple determinant checks and 416 non-extremal cases with strict bounds. The exact symbolic spider difference and the general \(n\ge6\) theorem are established by the accompanying mathematical proof; numerical output only corroborates them. No independent mathematical audit has been performed.
