---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

Perfect measurement resets exactly the observed coordinate error. The symmetric two-state Markov sensor has stationary consecutive run K with P(K=k)=eps r^(k-1), and the other coordinate error has conditional normal variance C(B^k-1), independent of K. This yields exact covariance tail, moments, mean q/(1-rB), and a Gaussian scale mixture for |E|. Rescaling z²/C=B^(N+theta), geometric upper-j tail and super-Gaussian lower-j tail justify uniform phase-dependent convergence; Mellin transform gives Fourier coefficients proportional 2^s Γ(s+1/2)/s, nonzero for all harmonics. Strict convexity yields the stated unique switching-price optimum in the symmetric Markov family. Independently evaluated 9 phase-tail asymptotic cases, first complex Fourier harmonic and switching-cost grid.

## originality

PASS

Classical packet-loss Kalman studies establish power exponents/moment thresholds and mention difficult arithmetic-case coefficient calculations. The complete inspected 2019 primary article does not specify this period-one Gaussian-error amplitude with every nonzero complex Fourier coefficient, nor the exact Markov sensor-switching price optimum. Existing related Resultary papers treat different packet-loss staging/sensor problems; no dominating theorem found.

## value

PASS

It isolates the exact Gaussian rather than covariance tail in a natural two-sensor scheduling model, proves the genuinely nonconstant lattice modulation at every harmonic, identifies sharp moment bounds and gives an explicit price-dependent sensor switching policy within a well-stated class. The precise arithmetic amplitude resolves a coefficient question left open/difficult in the relevant general theory and is a useful tail-quantile diagnostic.

The dated certificate retains the supplied scientific assessment, sources and limitations.
