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

The proof reduces the periodic knight convolution to a diagonal Fourier multiplier, factors that multiplier exactly, counts its first factor by cyclic-group homomorphisms, and uses the two-term Conway–Jones trigonometric classification to exhaust its second factor.

The included pure-Python script `verify_knight.py` was run directly. It passed 400 exact finite-field evaluations on every rectangular dimension from 5 through 24 and seven selected boundary checks. The checker evaluates the unfactored eight-shift multiplier, and the proof, rather than the finite experiment, establishes the formula for every integer pair at least five. The method does not give bounds away from the zero spectrum. No independent mathematical audit has been performed.
