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

## Reproducibility

Run `python verify.py` with SymPy available. The script checks the two key polynomial increment identities as exact symbolic equalities and verifies a cancellation identity used in the proof. It applies the sufficient finite-time decision inequalities using rational arithmetic and computes a numerical transition bracket. All loops have finite stopping limits and are not certificates of the existence or uniqueness of an infinite critical orbit. Those facts follow from the monotonicity, comparison and ratio arguments in `RESULT.md`.

## Scientific bounds

The proof addresses a deterministic, symmetric two-voter system, not general graphs or the rate for asymmetric stubbornness. The critical threshold is not given in elementary closed form. The first public circulation day of the 2022 predecessor is not known exactly, although a day-stamped public catalogue entry exists for 2023-01-19 and a full-text author's archive URL indicates a November 2022 directory. Independent external validation has not been performed.
