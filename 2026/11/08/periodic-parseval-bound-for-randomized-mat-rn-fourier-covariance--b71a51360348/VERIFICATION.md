---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

Poisson summation gives e=A_h−T_hm. The tail T is 1/h periodic; cover [-1,1]^d by 2^d unit cubes (h≤1), each contained in one full period after shifting, and apply Parseval: ∫|T|²≤2^d h^d sum_{j∉[-m,m]^d}|khat(hj)|². The difference density v=ρ*ρ̌ is supported in [-1,1]^d and bounded by R. The Matérn spectral envelope and BGR half-space lattice bound at power 4ν+2d yield RMS tail C_(d,ν)sqrt R ell^(-2ν)(hm)^(-2ν-d/2). Include uniform alias a_h by L² triangle inequality. N diagonal entries carry deterministic e(0), the offdiagonals have q², giving exact Frobenius second moment; bounded differences 2M²/N for U-statistic give exp(−Ns²/(2M⁴)), and Borel–Cantelli gives fixed-parameter a.s. convergence. Independently checked spectral normalization/envelopes on 72 scalar cases and finite Parseval examples; analytic proof gives arbitrary d.

## originality

PASS

Barnett–Greengard–Rachh explicitly pose essentially the iid bounded-density Matérn covariance RMS extra d/2 exponent as Conjecture 9, proving only uniform kernel error and lattice-tail lemma. The submission gives the missing localized-Parseval proof and explicit constants. A November 2 periodic Matérn theorem has different torus/Haar hypotheses and no nonperiodic aliasing or arbitrary bounded density; its diagonal Frobenius identity is duly credited.

## value

PASS

Resolving a specifically formulated bounded-density stochastic Fourier Matérn conjecture with explicit constants and finite-N concentration is an independently useful numerical-analysis theorem. The extra d/2 exponent improves the RMS truncation guarantee over the uniform rate and matters for random kernel Gram matrices.

The dated certificate retains the supplied scientific assessment, sources and limitations.
