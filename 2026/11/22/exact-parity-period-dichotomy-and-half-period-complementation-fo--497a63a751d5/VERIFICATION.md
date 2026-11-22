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

The claim is proved over the entire infinite set of orders \(k\ge2\) by a reduced generating denominator and exact squarefree-factor decomposition. The code verifies, but does not replace, the algebraic derivation.

Use `python3 check_parity.py`. The exact modular polynomial-gcd test covers all \(2\le k\le500\); exhaustive binary state cycles cover \(2\le k\le18\), checking minimal return to the impulse state and every half-period bit flip when required. No probabilistic sampling is used in these finite tests. Beyond these finite ranges the proof, not enumeration, supplies the quantified conclusion.

The theorem gives no explicit formula for the odd factor of the binary least period and does not cover moduli larger than two. Independent scientific audit has not been conducted.
