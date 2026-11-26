---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification

In this directory, run `python verify_chebyshev_dual.py` with SymPy installed. The exact polynomial calculations check the 73 coprime pairs with \(2\le a\le12\), \(a<b\le18\). They verify derivative coprimality, Wronskian degree and squarefreeness, the derivative ODE identity, endpoint values, and the degree and corrected leading coefficient of the first Gauss coordinate. They also check the degree differences that give the two local orders in the Gauss chart at infinity.

```
Exact Chebyshev Gauss–Wronskian checks passed for 73 pairs.
```

This finite regression does not prove the universal claims. The general proof in `RESULT.md` uses the Chebyshev ODE and the coprime derivative root separation, together with the base-point-free Gauss map, characteristic-zero biduality, and local vanishing orders.
