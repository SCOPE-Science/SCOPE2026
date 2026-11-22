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
# Verification and limits

The proof is reconstructible from `RESULT.md`: (i) \(f_1,f_2\) are local regular parameters at the \(16m\) common coefficient zeros, (ii) the blow-up principalizes their ideal and makes the coefficient map to \(\mathcal O(-D)\) surjective, (iii) the two strict-transform charts are smooth and exceptional only over the original lines, (iv) the canonical determinants cancel, and (v) vector-bundle/point-blowup formulas determine topology and motive.

Run `python CHECK.py` with SymPy. The actual check passed exact cyclotomic common-root and squarefreeness tests for odd \(n=5,7,\ldots,21\), exact local blow-up chart identities, and symbolic motivic/Euler identities. The symbolic chart identities are universal; the finite root tests are not a proof for all \(m\). The independent audit is not performed.
