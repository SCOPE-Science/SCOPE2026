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

# Reproducibility

Run `python3 verify_templates.py` and `python3 verify_windows.py` from the directory containing the accompanying standalone programs. The saved outputs `verify_templates.out` and `verify_windows.out` contain the actual successful checks.

`verify_templates.py` uses all possible starts modulo a power of the prime greater than the factor length. The one position divisible by that power, if present, can carry any of the \(q\) symbols. It compares these exactly enumerated factors against the recurrence in RESULT.md across 525 prime/alphabet/length choices.

`verify_windows.py` does not use a finite prefix. It enumerates every compatible starting residue modulo that same prime power subject to the prescribed phase modulo the window length, with a freely variable high-valuation symbol when appropriate. Chinese remainder compatibility shows this enumeration is exact, including rare high-valuation events, for each sampled \((p,q,n,r)\). It checks 13,542 phase cases. Its finite enumerations confirm examples but do not replace the stated universal proof.

The implementation is ordinary Python 3 with no third-party dependencies. A full infinite-parameter computer certification and third-party mathematical audit have not been performed.
