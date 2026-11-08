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

# Reproducibility and limits

Run these three standalone Python 3 scripts, each without third-party dependencies:

```
python verify.py
python verify_direct.py
python verify_dualities.py
```

`verify.py` constructs the quadratic finite fields of orders four and nine, enumerates normalized anti-involution scalars and fixed-radical twists for complete height-two bipartite posets of sizes \(1+1\) and \(2+2\), checks algebra basis anti-multiplicativity and involutivity, and verifies uniqueness/counts. It prints per-duality counts of 6, 12, 432, and 10368. `verify_direct.py` enumerates all semilinear anti-automorphisms of the two-element chain over each field independently of the normalization equations and identifies the involutions. `verify_dualities.py` exhaustively enumerates order-reversing poset involutions and conjugacy orbit profiles of crowns on six, eight, and ten vertices.

All scripts were run successfully and reported `VERIFY_OK`. Their finite test cases are exact enumerations of the specified small objects but do **not** prove the theorem for arbitrary posets or arbitrary prime powers. The universal proof rests on the idempotent-lifting normal form, square-zero multiplication, finite-field norm and trace surjectivity, and edge-scaling conjugation. Independent audit has not been performed.
