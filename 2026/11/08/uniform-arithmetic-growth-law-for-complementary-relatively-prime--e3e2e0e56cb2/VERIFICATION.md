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
Execute `python3 verify.py`. The verifier uses exact integer arithmetic, an independent direct enumeration of nonempty subsets through size \(13\), and a Möbius-sieve computation for sizes up to \(400\). It checks both complement decompositions, the uniform two-sided inequality and the parity of the parameters. The calculations are illustrative, not an infinite proof. The bound for every larger integer follows from the combinatorial inequalities in `RESULT.md`.

Scientific limitations include the factor \(2(n+1)\) in the sandwich; no unit leading constant is asserted. Independent audit: not performed.
