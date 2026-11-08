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

The theorem for every integer \(m\ge2\) is established by exact congruence and parity arguments in RESULT.md. The bundled `verify.py` independently implements the defining floor/ceiling operations, checks both endpoint skew tent identities for every state, checks the two-step reflections, tests the fourth iterate, enumerates the complete primitive cycle partition, and validates fixed-point counts of powers one through twelve at both endpoint controls for every \(m\in\{2,\ldots,14\}\).

Reproduction: from the same directory as this document, run `python verify.py` with standard Python. No extra software, data, numerical tolerance, or network access is required.

Observed successful output:

`VERIFY_OK m=2..14 endpoint_controls=26 checked_states=65528 cycle_counts_and_fixed_point_spectra=exact`

The test covers \(65{,}528\) ordered endpoint/state pairs. Finite enumeration checks consistency but is not an independent proof for unbounded \(m\); the all-size result depends only on the exact integer algebra given in RESULT.md. This document records no independent scientific audit or external certification.
