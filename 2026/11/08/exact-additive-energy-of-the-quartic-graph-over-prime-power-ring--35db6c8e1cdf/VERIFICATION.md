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

Run `python3 verify.py` using Python 3.8 or later; no third-party dependencies. Its expected line is
`VERIFY_OK prime_power_cases=10 squarefree_cases=4 primitive_strata=6 max_prime_power=125`.

The script directly counts solutions of the quartic collision polynomial modulo \(p^k\), compares independent graph-pair multiplicities for smaller moduli, tests Chinese-remainder multiplicativity on four squarefree moduli, and directly checks primitive single/double-intersection strata. This verifies finitely many instances only. The general recurrence rests on the proof in `RESULT.md`; independent audit has not been performed.
