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

# Reproducible checks and precise limits

Execute `python verify_transfer.py`, `python verify_dynamics.py`, and `python verify_symbolic.py` in a directory containing these standalone programs. Python 3.10+ is sufficient for the first two; the symbolic program needs SymPy 1.12+.

`verify_symbolic.py` constructs the exact three \(3\times3\) integer transfer matrices and \(9\times9\) exclusion matrix directly from signed color increments; exact rational inversion verifies both all-size generating functions. `verify_transfer.py` independently counts labelled colorings for rung lengths 2–6 and uses integer transfer up to length 30. `verify_dynamics.py` independently evolves the actual synchronous CCA and GHM maps to their recurrent cycles and measures every vertex's rate for all initial colorings through length 5. Captured outputs accompanying these scripts are from runs of the included versions.

Tests do not prove the external arbitrary-graph activity theorem, which is explicitly invoked as [1, Theorem 3] in `RESULT.md`. They also do not constitute independent expert validation or resolve historical priority. No claimed classification of entry times, primitive cycle counts or general random initial conditions beyond the uniform-product case is made.
