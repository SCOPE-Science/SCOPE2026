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

Run the bundled checker with `python3 verify.py` using only the Python standard library. It independently constructs shortest representatives in every residue class modulo \(P_n\), computes genus and Frobenius from those Apéry representatives, and tests symmetry at all indices \(1\le n\le12\). The exact output obtained was:

```
VERIFY_OK indices=12 through=12 exact_aperies=yes Pell_identity=yes rank_gcds=yes symmetry_iff_1_2_4_or_3_divides=yes
```

The checker does not prove the theorem for all \(n\). The written proof uses the Pell strong-divisibility theorem, identity \(5P_{n+4}=P_n+12P_{n+3}\), and the standard characterization of symmetric three-generated numerical semigroups. Index hypotheses and exceptional cases are explicitly handled in the proof. There is no external independent audit.
