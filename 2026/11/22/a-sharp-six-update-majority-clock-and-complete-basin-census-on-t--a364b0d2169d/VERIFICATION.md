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

# Reproduction notes

The two Python 3 scripts use the standard library and have no external dependencies. Run `python3 check_majority_a.py` and `python3 check_majority_b.py` from the package directory. Both independently traverse all \(4096\) states of strict majority on the labelled Bidiakis cube. Their graph constructions, state representations and orbit algorithms are independent.

The first script enumerates 20 fixed points, 103 primitive two-cycles, the complete first-entry and individual basin spectra and graph automorphism orbit classes. The second builds edges explicitly and independently reproduces all recurrence, entry-depth, basin and witness checks. Both assert that all periods are one or two. The witness initial integer configuration 59 first reaches the cycle (33,66) at time six.

This proves the finite enumerated claim subject to execution of the supplied transparent code. It is not a claim of independent human or external validation or of historical-priority proof.
