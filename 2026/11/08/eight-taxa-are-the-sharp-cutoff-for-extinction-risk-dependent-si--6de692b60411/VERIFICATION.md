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

# Verification instructions and boundaries

The package contains `verify.py` and `SHAPE_CERTIFICATE.tsv`. Execute `python3 verify.py` with Python 3 and no third-party modules. It regenerates all \(24\) anonymous rooted binary shapes of 2–7 leaves from a complete unordered-root decomposition, checks the table's dominant profiles, and separately constructs all \(11,465\) labeled binary trees of 1–7 leaves. For the eight-tip witness it verifies both rational probability examples, all candidate gains, and the exact expected phylogenetic diversity via all \(128\) survivor configurations for each protected leaf.

The polynomial factorization and the strict increase of \(q^2+q-1\) on \((0,1)\) are the **infinite-parameter proof**, rather than a finite numerical experiment. Exhaustiveness applies to small rooted *full-binary* unit-edge trees, not other tree classes. All outputs are reproducible exact integers and rationals; an independent external audit has not been performed.
