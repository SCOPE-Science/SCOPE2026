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

The proof in RESULT.md covers all finite connected simple base graphs of order at least two and all complete attachment sizes at least two. Independently coded computational comparisons are illustrative finite checks, not general mathematical certification.

Run `python3 verify_a.py` and `python3 verify_b.py` with Python 3 and no dependencies. The recorded outputs are `verify_a_output.txt` and `verify_b_output.txt`. The first checker exhausts each model's minimum sets, token-jump transitions, edges and components for several small base graphs. The second checker uses a different data representation and verifies equality of actual and predicted minimum-set families for every connected labelled base graph of orders two through four with attachment size two, and order three with attachment size three. Both checks passed.

Independent scholarly audit has not been performed. No external formal verification, certificate of worldwide novelty, or source priority guarantee is asserted.
