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

The attached `checker.py` constructs each undirected labelled simple graph independently from its edge mask, computes the parity of every open neighborhood, then computes the parity of neighbors whose first-step value is odd. It checks every labelled pair \((d,t)\) against the exact fiber count for \(2\le n\le6\), including zero-probability pairs, and prints `ALL_TWO_LAYER_EXHAUSTIVE_CHECKS_PASS` on success.

The analytic proof is the alternating-extension lemma, whose matrix congruence creates a bijective parametrization of every possible graph fiber, followed by a count of hyperplane intersections. The exhaustive program is an independent finite cross-check and does not itself prove all sizes.

The motivating 2026 result addresses satisfiability rather than probability, and its discussion explicitly describes modular quantifiers as an extension beyond its presented syntax. Prior random graph matrix methods (including the already-known uniform degree-parity distribution) and an earlier symmetric-equation theorem were compared by their actual assumptions and conclusions. No independent external mathematical audit is asserted.
