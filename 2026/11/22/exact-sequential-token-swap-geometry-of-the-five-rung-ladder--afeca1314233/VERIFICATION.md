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

## Exhaustive finite verification

Run `python3 verification/check.py` from the package root. The script compiles both included C++17 implementations, explores the complete \(10!=3{,}628{,}800\)-permutation state graph, compares the distance distribution, four exact antipodes, transport-bound shortfall distribution and unique maximizer against `verification/expected.json`, and runs smaller-ladder calibration cases. The source-based program was executed from the packaged paths and reported `Independent exhaustive checks: PASS`.

The two implementations use distinct permutation representations (Lehmer-ranking arrays versus packed four-bit states and hash-based visitation). Each uses FIFO breadth-first search from the identity and generates all thirteen legal swaps. Completeness follows from visiting all \(10!\) distinct configurations with shortest-path labels.

The mathematical transfer from the identity-source census to every ordered source-target pair uses token-label transitivity, not exhaustive enumeration of every ordered pair. The displacement bound follows because each individual swap reduces the sum of destination distances by at most two.

## Scope and limitations

No claims are made for longer ladders, parallel swaps or asymptotics. Exactness is conditional on the included finite enumeration and its standard implementation assumptions. The source code is reviewable and reproducible, but its execution is not a substitute for independent external mathematical audit. Historical originality is limited to comparisons with accessible indexed sources and inspected primary literature; older unindexed computations may exist.
