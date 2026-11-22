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

# Reproduction and limits

Run `python3 verify.py` using a Python 3 standard library installation. The verifier constructs all vertices of each tested strong path product and checks every three-element subset directly using the maximum of coordinatewise absolute differences. It recomputes both formulas independently of the case derivation and asserts equality of the maximum perimeter and the number of achieving triples.

The comparison covers twelve mixed-side instances, plus uniform powers with side orders from two through five and dimensions from two through four when the vertex count is at most 150. Some instances are deliberately tested twice via the two independent loop selections. The checker reports `UNORDERED_TRIPLES_CHECKED 676739` and `VERIFY_OK`.

The finite enumeration does not prove the formulas at unbounded size or establish the limit distribution. Those are proved using the coordinate argument, inclusion-exclusion and elementary probability in `RESULT.md`. No independent audit has been performed.
