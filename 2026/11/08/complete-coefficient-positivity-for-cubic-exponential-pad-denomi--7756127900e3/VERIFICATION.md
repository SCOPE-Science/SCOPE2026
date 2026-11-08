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

Run `python verify.py` with Python 3 and no third-party packages. It prints `VERIFY_OK` only after checking the Padé coefficient recurrence against exact rational calculations over a finite grid, evaluating the translated cubic, and checking the real-pole residue inequality over finite parameter samples. Its direct algebraic assertions use exact fractions where possible; the root/residue samples use IEEE double precision away from singular boundaries.

The universal theorem does not depend on this finite suite. It rests on the strictly positive symbolic factorization of \(s^2v^2-R^2d^2\) and the exact partial-fraction identity in RESULT.md. The script is a reproducibility aid and supplies no independent audit; historical-priority questions remain open.
