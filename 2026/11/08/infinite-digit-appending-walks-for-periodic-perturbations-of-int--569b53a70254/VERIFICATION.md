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

# Verification report

Execute `python3 verify.py` using Python 3 and its standard library. Exact integer checks were run with the script extracted from the finalized package.

The test enumerates \(32{,}256\) candidate steps across eight dependent-base parameter configurations and finds \(230\) admissible steps, all resonant and satisfying the offset floor criterion. A finite-state graph check validates the nonterminal termination bound in sampled periodic patterns. For every \(0\le L\le11\), the explicit power-of-two offset construction realizes exactly \(L\) consecutive one-digit appends, attaining the proved bound. The output begins `VERIFY_OK` and includes `exact_integer=yes`.

Finite tests do not certify universal statements; the unrestricted proof is given in `RESULT.md`. The independent-root case is cited from arXiv:2610.18919v1 rather than independently established here.
