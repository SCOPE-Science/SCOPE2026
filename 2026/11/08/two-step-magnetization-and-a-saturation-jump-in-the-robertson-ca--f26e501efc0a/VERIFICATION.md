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

Run `python3 verify.py`. Standard Python 3 is sufficient; the implementation does not require Sage, Mathematica, network access, or external packages. The script checks graph parameters and all 20 microcanonical sector maxima and counts with two independent exhaustive algorithms. It verifies the exact lower envelope by rational comparisons on every field interval, and all degeneracies at zero and critical fields. The printed terminal result `VERIFIED` means only that those in-package finite and algebraic assertions succeeded, not that publication priority or independent validation has been established.

The proof is finite and exact for the stated graph; it is not a finite simulation used to assert an infinite statement. In particular, the independent-set count 1,950 is a known value used as a consistency cross-check (Cambie and Jooken, 2023), not an independently novel finding.
