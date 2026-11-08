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

The included Python 3 script `check_half_integral.py` computes the two finite graph-sum formulas and separately enumerates the ten two-sample edge probability tables for each edge of five labelled test graphs. Only tables whose vertex marginals coincide are retained. The second test checks whether any complete assignment satisfies all supported edge pairs. The verified ordered pairs (no-disturbance, support-extendible) are \((40,36)\) for a triangle, \((136,128)\) for a four-cycle, \((116,116)\) for a four-vertex path, \((140,124)\) for a triangle with a pendant edge, and \((464,448)\) for a five-cycle. The expected script terminal message is `CHECK_OK`.

The proof in RESULT.md independently establishes that, in this special precision regime, support extendibility is equivalent to probabilistic noncontextuality, and that the no-signalling model has contextual fraction exactly zero or one. Exhaustive finite tests are not a proof for arbitrary graphs. The denominator-three example is verified symbolically from its tables and explicit convex decomposition. The software uses the Python standard library only. Independent audit is not performed.
