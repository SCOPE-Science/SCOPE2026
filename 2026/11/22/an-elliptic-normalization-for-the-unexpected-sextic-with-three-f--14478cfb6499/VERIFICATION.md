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

`verify.py` is a standalone exact-arithmetic checker using SymPy. It reconstructs the interpolation from the thirteen printed base points and \(Q_0=(-31:-9:15)\), checks rank 27, builds the unique sextic, verifies the projective singular support and squarefree initial forms, and excludes every potential line factor. The calculation is finite and proves only this special fiber; the general-parameter extension comes from the explicit openness argument in `RESULT.md`.

The output observed was:

```
PASS: unique sextic, four singular support points, three ordinary nodes,
ordinary quadruple point, no linear factor; geometric genus one.
Degree 6, singular delta 3*1+6=9, genus 10-9=1, dual degree 30-6-12=12.
```

No independent mathematical audit or external formal proof certificate has been performed. Exceptional specializations of the moving point are not checked.
