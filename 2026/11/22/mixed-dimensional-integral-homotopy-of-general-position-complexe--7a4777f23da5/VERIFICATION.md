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
Run `python3 verify_double_spider.py` with Python 3 standard library. The program independently builds each tree, computes all geodesic distances, enumerates all simplicial faces using forbidden triples, and checks exact agreement with the proved arm/hub face description. Separate mod-two boundary reduction checks all reduced Betti ranks against the formula. The attached output is from an actual replay on the embedded script: 147 parameter sets, 28,556 nonempty faces, all passing. The check is finite and mod two; it cannot independently certify the infinite statement or its integral homotopy type, which are established in the proof. Independent audit has not been performed.
