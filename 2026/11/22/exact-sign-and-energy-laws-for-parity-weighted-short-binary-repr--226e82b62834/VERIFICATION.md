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

The exact signed recurrence follows from a terminating digit decomposition of short representations. The complete eight-state transition table and its rational generating-function equations prove the sign count, and two telescoping recurrences prove the exact first and second moments. The separate checker `verify.py` enumerates signed strings independently for the small cases, exhaustively compares actual signs against the state machine on complete dyadic ranges, and verifies both moments on the stated finite intervals. These computations are corroborative and not an infinite certificate.

Novelty is assessed against the 2023 representation theorem, the 2008 signed recurrence, the 2021 fixed-length polynomial study, and the published 2026 Fibonacci zero-set theorem. The zero-set theorem itself is prior knowledge, not a new assertion. Unindexed stronger results remain a risk. No independent scientific audit has been performed.
