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

The accompanying `verify.py` uses exact symbolic polynomial arithmetic to check the normalized sextic, the doubled infinity-section equation, normal derivatives on the coordinate infinity lines, the normal quadratic discriminant, the representative affine singular-line identities, and both decisive local Taylor jets. It prints `exact symbolic checks: PASS` if successful. The analytic local normal forms follow from the holomorphic splitting lemma and divisibility by the squares of the two singular-axis parameters; symbolic computation alone is not a proof of that lemma or a complete classification. Exceptional parameter values 0 and ±1 are excluded. Independent validation has not been performed.
