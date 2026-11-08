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

The standalone `verify.py` recomputes the full spectrum by enumerating all characteristic sequences of degrees \(3q\) for \(q\in\{7,13,19,31,37\}\), evaluating exact conductors, and comparing with the symbolic classification. The separate Apéry-shortest-path implementation checks every enumerated sequence at the first two degrees and a deterministic subsample at the third; it does not rely on the characteristic-sequence conductor identity for those comparison values. The actual stdout is embedded in `verification_output.txt`.

This is finite cross-validation, not a replacement for the all-primes proof in `RESULT.md`. The cited primary literature establishes the characteristic-sequence characterization and conductor identity, while the uniform gcd-chain reduction, congruence obstruction and interval overlap are proved explicitly in the result. The test \(q=5\) shows why the modulus-six hypothesis is substantive. No independent scientific audit has been performed.
