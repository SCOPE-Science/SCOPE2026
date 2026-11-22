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
# Reproduction and limits

The theorem reduces the exact induced norm to the total variation of the cardinal single-jump response. This is an infinite-domain proof, based on the \(\ell^1\)-summability of the jump coefficients and an \(L^1\)-convergent derivative expansion. The three cell formulas and derivative turning-point identities are explicit in `RESULT.md`.

The self-contained `verify.py` checker uses only Python's standard library. Execute `python verify.py` to reproduce 18 exact step comparisons to floating tolerance, 2,160 randomized finite-signal upper-bound checks, the exact rational constants at \(\lambda=1/2\) and \(\lambda=3\), and stationary-point identities on both outer parameter regimes. The interpreter used for these tests was Python 3, and all checks completed successfully.

The finite tests do not prove the all-parameter theorem or historical originality. No independently executed audit or external certification is represented.
