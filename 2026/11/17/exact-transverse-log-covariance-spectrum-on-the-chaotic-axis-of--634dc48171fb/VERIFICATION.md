---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

PASS: For mu1,nu1>0 and 0<nu0<nu1 the y=0 Jacobian is upper triangular with normal QUOTIENT multiplier nu1*x-nu0; this is not a stable vertical eigenspace or nonlinear predator persistence statement. Doubling-angle parametrization of x_j=sin^2(2^j*pi*theta) is measure preserving and ergodic. The centered log observable is the sum of two L2 log-sines shifted by +/-phi; its cosine Fourier coefficients are -2cos(2*pi*k*phi)/k. Matching frequencies k=2^m*l under doubling and applying the Bernoulli B2 Fourier identity yields Gamma_m exactly for all m>=0. Stationary covariance summation proves Var(log|D_n|)=nGamma0+2sum(n-m)Gamma_m for every n>=1, and Birkhoff gives almost-everywhere exponent log(nu1/4), excluding zero-multiplier exceptional seeds. Rational B2 evaluations independently confirm eta=1/2 gives finite variance pi^2(2-2^{1-n})/12 and eta=3/4 gives pi^2(3n-4+2^{2-n})/9. Direct independent checks covered 62 rational covariance/variance identities. A finite test is not an infinite proof.

## originality

PASS

PASS best-of-knowledge: the published Anteneodo (2003) eqs (7)-(11) contain a general Fourier autocorrelation framework, and eqs (13)-(15) explicitly solve the logistic DERIVATIVE observable at its turning point, which exactly covers eta=1/2. Lee et al. (2023) introduce the same coupled map and study mean Lyapunov/bifurcations, but not the displaced normal log observable or its full Bernoulli parameter family. The new content is the complete displaced-zero covariance spectrum, in particular the positive fixed-point-zero lag covariance and linear variance growth, not the previously solved turning-point case. Classical arbitrary-observable Fourier machinery is strong antecedent and does not by itself state this model-specific parameterized evaluation; equivalence in unindexed literature remains possible.

## value

PASS

PASS: The transverse quotient of a natural published two-population map has a neutral band with identical almost-everywhere mean exponent but sharply different finite-horizon fluctuations depending on the intrinsic multiplier zero; the exact Bernoulli spectral profile and bounded-versus-linear variance distinction are substantive finite-time dynamical invariants and useful for interpreting numerical transverse stability, with explicit cautions against nonlinear population claims.

The dated certificate retains the supplied scientific assessment, sources and limitations.
