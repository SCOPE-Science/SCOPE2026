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

# Exact verification

The supplied `verify.py` uses the Python 3 standard library only. It independently enumerates all permitted placements (row/column injections with modular diagonal distinctness) and all cliques in the 49-square compatibility graph, asserting exact equality of the face sets and closure under taking faces. The program builds signed integral boundary matrices, carries out unimodular unit-pivot chain cancellations, checks every entry of the nonunit rank-one matrix against the primitive reference column, checks its Smith invariant is nine using exact integer greatest-common-divisor operations, and establishes the primitive surviving generator. A separate modular boundary-rank calculation on the originally rebuilt faces over characteristics two, three, and five corroborates the 3-primary discrepancy. Every recorded count and printed value must match the observed `verification_output.txt`; the script terminates in `ALL_CHECKS_PASS` only when all asserted checks succeed.

The computation is exhaustive for the defined 49-vertex complex, not an experiment extrapolated to an infinite family. It establishes integral homology, not full or equivariant homotopy type. An independent external audit has not been performed.
