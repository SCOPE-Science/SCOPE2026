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
# Computational verification

Run `python3 verify.py` (Python standard library only).

The program constructs each cycle-power graph directly from cyclic distances, tests compatibility on all four cross-endpoint pairs, enumerates all possible selected edge-subsets up to the proved upper bound, and tests maximality by checking every possible addition. It separately evaluates the coefficient formula by integer convolution and tests the predicted contiguous support and extremal multiplicities for larger parameters.

Observed successful execution:

`VERIFY_OK graph_instances=44 edge_subset_candidates=116874 induced_matchings=5627 maximal_induced_matchings=3230 arithmetic_parameter_pairs=888`

Full graph-level coefficient comparisons: \(1\le r\le4\), \(2r+1\le n\le16\). The enumeration covers every cardinality which could support an induced matching, by the proved \(n/(r+2)\) upper bound. Exact coefficient and support checks: \(1\le r\le8\), \(2r+1\le n\le120\). The finite tests cannot certify an infinite theorem; the cyclic gap proof is the justification for unrestricted parameters. No external audit or independent certification has occurred.
