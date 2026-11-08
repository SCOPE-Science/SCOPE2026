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

# Reproducibility and limits

The proof in `RESULT.md` establishes the all-seed and almost-everywhere infinite statements directly. `verify.py` is an independently runnable exact-rational implementation of finite indexing, endpoint identities, backward-branch upper bounds, extremal-orbit partial sums, and one explicit cycle. Run `python3 verify.py` with a standard Python 3 installation (no third-party packages). The expected terminal message is:

`VERIFY_OK exact_checks=27453 k_range=2..7 grid=17 inverse_depth=8`

The code does not exhaust uncountably many initial points or infinitely many times. Ergodicity of the full-branch tent map, backward-history realization, and the sharp limit interval are established mathematically, not inferred from numerical tests. There has been no independent scientific audit.
