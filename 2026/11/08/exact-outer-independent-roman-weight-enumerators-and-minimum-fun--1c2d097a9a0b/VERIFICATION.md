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

# Reproducibility and verification

The included standalone script `verification/verify_rook_outer_independent_roman.py` independently evaluates labels from the graph definitions, without using the derived inclusion–exclusion formula as its test oracle. It computes the symbolic formula separately and compares exact integer coefficient dictionaries.

Direct profiles: \((m,n)=(2,2),(2,3),(2,4),(3,3),(3,4)\). Exactly **558,495** ternary labelings examined; exact total valid counts respectively **46, 310, 1,900, 5,048, 73,864**. Their respective lowest-weight pairs (weight, number of minimizers) are **(3,4), (5,12), (7,24), (8,108), (11,504)**. Tests directly evaluated ordinary and total labeling conditions and confirmed the \(2\times2\) correction.

For 44 further ordered parameter profiles \(2\le m\le9\), \(m\le n\le10\), the independently derived minimum-coefficient formula was checked against the full symbolic polynomial. Additionally, 60,000 deterministic random labelings were tested on \((4,4)\) and \((4,5)\), including the total-condition equivalence.

Expected final line:

```
VERIFY_OK direct_profiles 5 direct_labelings 558495 symbolic_profiles 44 random_labelings 60000 OIRDF_weight_polynomial=PASS OITRDF_equivalence_and_boundary=PASS minimum_multiplicities=PASS
```

All finite checks passed when the script was run. These are evidence for debugging and reproducibility; the infinite-domain statements require the combinatorial proof. No independent audit was performed.
