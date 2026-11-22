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

The exact-identity and exhaustive-finite-enumeration certificate is `CHECK.py`. Run it with `python3 CHECK.py`; no nonstandard packages, network, downloaded files, or floating-point arithmetic are required.

For each of the two four-symbol group tables, the checker verifies the entire twenty-vertex adjacency matrix, its degree sequence and sixty-four edges; the exact characteristic polynomials of the adjacency and weighted intersection matrices via independent integer power traces; the total of 576 order-four Latin squares from the full enumeration of four permutation rows; the seven classes of the coloring table; and the 5400 versus 8568 labeled four-colorings. A second, direct graph-coloring search independently reproduces these two totals. Color relabeling then gives 225 versus 357 unlabeled four-class partitions.

The mathematical proof requires only the row/column and symbol-partition structure supplied by the geometric classification. It does not infer surface realizability, algebraic independence of divisor classes, or any theorem from finite samples. Numerical geometry beyond the proposed graph intersection pairing is outside scope.
