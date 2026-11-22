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

# Finite reproducibility checks
Run `python3 verify.py` using Python 3; only the standard library is needed. The standalone program recomputes the Fibonacci state sequence modulo each tested power of five, evaluates the power-index subsequence over the complete universal index cycle, and verifies every predicted residue fiber for the tested exponent/depth pairs. It also checks claimed periods and detects shorter periods at smaller depths, and checks the exact companion matrix relations and slopes used in the proof. In the actual execution it reported 221548 exact assertions across 70 scenarios, with maximum tested period 12500. These finite tests do not prove the classification for infinitely many indices, exponents or depths; the mathematical argument in RESULT.md is needed. Independent audit: not performed.
