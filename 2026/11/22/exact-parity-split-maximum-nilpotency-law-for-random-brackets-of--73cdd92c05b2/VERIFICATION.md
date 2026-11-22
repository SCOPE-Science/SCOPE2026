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

## Checks performed

The standalone `checker.py` was executed under Python 3. Exact-rational exhaustive low-superdiagonal checks passed for \((n,q)=(3,2),(4,2),(4,3),(5,2),(6,2),(7,2)\). A separate algorithm in the same checker performed full strictly-upper matrix multiplications and powers, on every ordered matrix pair for \((n,q)=(4,2)\) (4096 ordered pairs) and \((4,3)\) (531441 pairs). All tests agree with the theorem; see `checker_output.txt`.

The proof independently establishes all dimensions and all finite fields; no finite experiment is used to extrapolate an infinite theorem. The finite checker uses prime-field modular arithmetic, and hence does not directly test extension-field implementations; the proof uses only field axioms and size. Historical priority is not independently certified. This is not a proof of complete Jordan-type distributions or all possible bracket fibers.
