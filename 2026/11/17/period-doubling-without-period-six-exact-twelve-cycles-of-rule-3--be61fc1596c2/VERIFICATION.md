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

## Finite-state replication

The complete finite proof has two independently organized C++17 implementations, `transfer_certificate.cpp` and `direct_crosscheck.cpp`. Compile with `g++ -O2 -std=c++17` and compare their output to `transfer_output.txt` and `direct_output.txt`.

The first checks all \(4{,}096\) and \(16{,}777{,}216\) ordered temporal-column pairs for heights six and twelve using incoming-degree elimination. The second explores all the same pairs using path marks rather than indegrees, reconstructs every periodic ring, tests its least spatial period, directly applies Rule 30 for each time slice, and determines the least temporal period from the evolving ring. Agreement covers every cyclic component, not merely selected witnesses.

`make_witnesses.py` generates the four explicit strings printed in `witnesses.txt`; the independently implemented Rule 30 update confirms least periods six and twelve as appropriate. The separate finite graph exhaustions support the nonexistence claims for every circumference via the column-transfer bijection proved in `RESULT.md`.

## Limits

The graph certificate is exact but has not been independently externally assessed. It does not enumerate attraction basins, general temporal periods, or nonperiodic infinite configurations. Originality relies on the listed primary-source comparisons and is not a guarantee against unpublished or unindexed results.
