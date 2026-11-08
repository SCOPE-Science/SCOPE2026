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

Run `python3 VERIFY.py` (Python standard library only). It returns:

```
CLASSIFICATION_OK 10626
FINITE_REDUCTION_OK 3432 AFFINE_EQUAL_BASES 2
VERIFY_OK
```

The complete factor-set implementation is independent of the rectangle classifier and checks every binary word with three ones through length \(23\). The finite-reduction certificate enumerates all ordered triples of nonmaximum gaps with sum at most \(10\), all four positions for the maximum and the three values \(m=M,M+1,M+2\). This is a complete finite base only because the proof in `RESULT.md` establishes a uniform bound and the eventual affine dependence on the maximum gap. The program does not by itself prove infinitely many lengths.

The program constructs candidate MAWs directly from rectangle memberships without invoking literature data, checks their actual strings against independently enumerated factor sets, and compares integer counts in all residual cases. No external executable, private dataset, mathematical proof assistant, or independent certification is required or claimed.
