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

Summing independent leaves gives alpha/(1+beta)=1/2 and Bernoulli(r) leaves. The transfer matrix for fugacity 1/2 gives stated finite-cycle mean p_n and Fourier eigenvalues, with constant mode s_n strictly least (even-cycle bound and odd-cycle sign checked). Total covariance yields a Fourier 2x2 block [[a,-ra],[-ra,r²a+c r(1-r)]]. Positive rank-one order in a pins the least mode to s_n. Schur-complement Q_t(r) is strictly concave and tangency H(t) crosses once, proving unique maximin r_n<1/2 and strict suboptimality of r=1/2. Independent enumeration n=3..10 reproduced rim Fourier spectra and optimum; infinite proof rests on exact transfer and tangency, not grid search.

## originality

PASS

A calibrated fixed-marginal Bernoulli pendant observation design and its all-n unique E-optimum are not supplied by the published proper-colouring pendant transfer, hard-core spectral-independence mixing, or corona enumeration that were searched. Best-of-knowledge only; general stochastic E-optimal design may have an equivalent block theorem.

## value

PASS

The least singular-value design of dependent occupancy coordinates is a natural robust sampling invariant. The theorem supplies a nontrivial unique tuning and complete 2n-dimensional spectrum uniformly in n, with a surprising strict failure of uniform-sunlet sampling; not merely relabelled independent-set counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
