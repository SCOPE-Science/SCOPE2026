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

With Python 3 and SymPy installed, execute `python check.py` in the same directory as this file. The observed output was:

```
VERIFY_OK jacobian=1 concavity=1 fold_parameter=2 area_cases=2 area_transition_C4_not_C5=1 exact_double_preimage=2 exact_areas=2
```

The checks reconstruct the exact Jacobian and fiber concavity, the critical curve, both area integrals, their fifth-derivative jump at \(\gamma=A/2\), the area fraction \(2/17\), and two distinct interior predecessor states yielding the exact target \((1/4,2/3)\) at \(r=1/2\), \(\gamma=1/3\). An additional exact area is checked at \((A,\gamma)=(1/2,1/5)\).

The symbolic checks establish identities over the rational-function field under the stated nonzero denominators; the proof's positivity, all-parameter quantifiers, uniqueness and boundary inclusion rely on the analytical inequalities in `RESULT.md`. No independent audit or external proof certification has been performed.
