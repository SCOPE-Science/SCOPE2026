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

# Exact verification and limits

Run `python verify.py` with Python 3 and SymPy. The script builds each cycle's independent sets, constructs its positive-literal union-compatibility matrix directly, and computes the Smith normal form with SymPy's integer-domain implementation. It separately evaluates all link weights by direct supersets and by path factors, reconstructs the integer zeta congruence, and checks the cubic rank recurrence. All checks use exact integers, not floating-point approximations.

Observed full replay:

```
C4: types=7, rational_rank=3, torsion2=0, equality_and_SNF=OK
C5: types=11, rational_rank=11, torsion2=0, equality_and_SNF=OK
C6: types=18, rational_rank=12, torsion2=1, equality_and_SNF=OK
C7: types=29, rational_rank=15, torsion2=0, equality_and_SNF=OK
C8: types=47, rational_rank=35, torsion2=0, equality_and_SNF=OK
C9: types=76, rational_rank=40, torsion2=1, equality_and_SNF=OK
C10: types=123, rational_rank=63, torsion2=0, equality_and_SNF=OK
VERIFICATION_OK: 7 exact integer-matrix SNFs; 24449 feasibility entries; rank/link checks through C19
```

In addition, link-weight counts were checked for cycles of lengths 11 through 19. The finite replay does not certify infinitely many lengths; the incidence factorization, path recursion, transfer matrix, and formal-power-series coefficient argument in `RESULT.md` prove the general case.

No Lean proof, external expert assessment, or independent audit has been performed.
