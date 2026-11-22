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

# Reproduction and limits

Run `python checks/verify.py` using Python 3.8 or later. The checker relies only on standard-library `fractions` and `math` and prints `PASS 244035 assertions` on the present tested environment. It exercises 2450 exact rational polynomial identities, the exact cubic optimizer and gain, parameter-boundary tests, and a finite grid of candidate-versus-alternative amplitudes across twenty exponents and ninety-nine means.

The complete proof in `RESULT.md` proves the universal-quantifier claim. Finite sampling does not prove optimizer uniqueness, cannot establish nonexistence of unseen extrema, and is not evidence for historical originality. The root of the interior-optimizer equation is found numerically by bisection for testing; its existence and uniqueness are mathematical conclusions derived separately. Floating-point endpoints within \(10^{-13}\) of zero are treated as zero to eliminate roundoff in fractional powers.

No experiment in a real organism was conducted, and physiological response outside the published curve's validated range remains uncertain. Independent audit has not been performed.
