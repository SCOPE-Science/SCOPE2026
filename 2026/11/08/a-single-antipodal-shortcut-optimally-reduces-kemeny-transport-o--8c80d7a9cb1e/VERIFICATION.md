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

# Verification procedure and limits

The mathematical proof uses the stationary-weighted commute-time identity, the rank-one Laplacian resistance update, and an elementary rational sign analysis. No finite computation is offered as an infinite proof.

The standalone Python file `code/verify.py` provides an independent *exact rational* check using Gaussian inversion of the grounded graph Laplacian. It recomputes effective resistances from scratch, forms Kemeny's degree-weighted resistance sum, and checks the proposed closed formula on all 100 inequivalent chord distances for cycle orders 4 through 22. It then checks strict negativity and distance monotonicity for all admissible chords on orders 23 through 300. This code requires only the standard library.

To replay after extracting the embedded files, run `python3 code/verify.py`. Expected output:

```
EXACT_INDEPENDENT_LAPLACIAN_OK 100 chords n=4..22
FORMULA_ALL_CHORDS_OK n=23..300
```

The check explicitly covers only the stated finite instances; it does not verify the general algebraic identities for all integers independently of the written proof. Bibliographic searches do not establish publication priority conclusively. External independent scientific audit has not been performed.
