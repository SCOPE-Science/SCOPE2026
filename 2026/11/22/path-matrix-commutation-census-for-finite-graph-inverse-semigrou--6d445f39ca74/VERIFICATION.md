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

The standalone `verify.py` reconstructs semigroup products from the unique path-pair normal form and checks every element-centralizer cardinality and total ordered commuting-pair count against the closed formulas.

Executed as `python3 verify.py` with no dependencies beyond the Python standard library. Result: PASS on 1099 acyclic simple graphs with one through five vertices, 681 acyclic multigraphs with two through four vertices (parallel-edge multiplicities zero through two, at most eight edges), and four explicit numerical examples. The examples are order/pair totals (6,22), (15,125), (35,817), (11,71).

Finite checks do not constitute proof for infinitely many graphs. The general proof is the prefix-normal-form and aggregation argument in RESULT.md. No independent scientific audit has been performed.
