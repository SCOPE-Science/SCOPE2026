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

Run the standalone, standard-library program `verify.py` with `python3 verify.py`. It constructs each hypergraph from scratch, checks each vertex subset against the original edge-at-most-one condition, and checks maximality by testing every possible addition. It then compares the actual maximal sets with the separately generated decorated-independent-set family. This cross-check includes all labelled simple base graphs of orders at most four for uniformities \(r=3,4\), plus loose cycles with \(n=4,5,6\), also checking their exact coefficients.

Observed command output:

`VERIFY_OK instances=156 vertex_subsets=567300 maximal_sets=2498 full_families=PASS loose_cycle_coefficients=PASS`

The finite enumerations do not verify the theorem for all graphs, all orders, or all uniformities. The unrestricted proof is by necessary-and-sufficient classification. The no-isolate premise is used in proving that each omitted original vertex cannot be added; the checker independently handles isolated vertices by requiring them in every maximal set. The counting-hardness reduction is a mathematical reduction, not an experimental extrapolation. Publication priority remains provisional because a closely related recent independent-domination article is not available in full text. Independent mathematical audit has not been performed.
