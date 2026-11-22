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

The delivered standalone `verify.py` computes the element order of each affine-group element by direct multiplication in six independent finite arithmetic models and checks exact coefficient-by-coefficient agreement. It includes split rings in characteristic three and five, and nonsplit radical-square-zero mixed-characteristic quotients of orders \(27\) and \(125\). Each coefficient of the theorem's order enumerator was checked without relying on symbolic group-order arguments. Run `python3 verify.py` to obtain `VERIFY_OK`. These tests do not prove the unbounded theorem; the multiplier decomposition and exact power formula in `RESULT.md` give that proof. The published class/character-degree comparison is an independently established input, not verified by this checker.
