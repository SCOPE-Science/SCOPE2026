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

# Verification record

The exact finite verification program `fixed_max_jump_check.py` uses only the Python standard library. Running `python3 fixed_max_jump_check.py` from the extracted directory enumerates all finite primitive jump sets with maximum at most twelve, groups the resulting numerical semigroups by minimal generating set and verifies that the predicted Boolean family equals the complete observed family for each target. It also directly evaluates the claimed cutoff and exact fiber size on the ordinary families through conductor thirteen and maximum twenty-nine.

Expected output ends with:

```
FIXED_MAX_JUMP_FIBERS_OK 365 distinct observed target pairs; ordinary c=1..13,m=1..29
```

Proof limits: the finite computation is not an infinite proof. The universal part follows algebraically from the irreducibility of minimal generators and the gcd identity; the ordinary threshold follows from reflection of all minimal generators. Spectral indistinguishability is **eventual** and uses the stated published dimension formulas, without asserting equality at every filtration weight or of the spectral moment values themselves.

The source for the defect-semigroup construction and spectral laws is https://arxiv.org/html/2611.14316v1. An earlier universal existence result at variable maximum is expressly excluded from the originality claim: https://the-omega-institute.github.io/trureturing-mdbook/Blueprint/D5/S3/Arith/Additive/NumericalSemigroupRealizability.html.
