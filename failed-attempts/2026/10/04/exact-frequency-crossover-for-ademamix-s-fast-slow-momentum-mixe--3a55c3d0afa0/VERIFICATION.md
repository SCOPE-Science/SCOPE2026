---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The source recurrences are scalar first-order stable EMAs. Substituting a harmonic input gives the standard transfer function \(H_\beta(\omega)=(1-\beta)/(1-\beta e^{-i\omega})\). Squaring the slow/fast ratio yields a quotient affine in \(\cos\omega\); differentiation gives \(2(\beta_3-\beta_1)(1-\beta_1\beta_3)/(1+\beta_3^2-2\beta_3\cos\omega)^2>0\) with respect to \(\cos\omega\), hence strict decrease in \(\omega\). The endpoint values and crossover formula follow algebraically. For constant or alternating gradients of fixed magnitude, bias correction makes the second moment exactly \(G^2\), so it cancels in the gain ratio. The actual verifier replays the recurrences and source-parameter periods; independent calculations reproduced the four quoted crossover periods and Nyquist gains.

## originality

FAIL

The mathematical claim is an implication-level corollary of two already-public ingredients: the AdEMAMix paper states the exact fast and slow EMA recurrences and their linear mixture, while the transfer function and frequency response of a scalar exponential moving-average filter are standard signal-processing facts. Taking the quotient of two first-order EMA magnitude responses, differentiating a fractional-linear function of \(\cos\omega\), and evaluating DC/Nyquist are routine algebra. The source paper need not print the crossover formula verbatim for the result to be covered under the audit rule.

## value

FAIL

The frequency-domain interpretation is useful for understanding the optimizer, but the mathematical content is a routine textbook analysis of two first-order EMA filters followed by direct substitution of published hyperparameters. It does not introduce a nonstandard structural lemma, natural unresolved exact invariant, or difficult boundary beyond what the recurrences already encode. Under the shared value standard, this is explanatory analysis rather than a separate worthwhile mathematical result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
