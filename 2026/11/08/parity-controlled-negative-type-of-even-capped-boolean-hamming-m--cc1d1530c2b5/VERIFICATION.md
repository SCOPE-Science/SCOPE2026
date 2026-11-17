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

PASS: For Boolean Hamming distance clipped at fixed even r, nonconstant Walsh eigenvalues equal -Q(s), with Q=1+sum_{t=2}^r[t^p-(t-1)^p]K_{t-1}^{(n-1)}(s-1). Thus negative type iff all Q>=0. For r=4,n>=8, cubic Krawtchouk form subtracts parity mode as (z+m)R(z), with R>0 on full real z domain for 0<p<=1 and m=n-1>=7; derivative comparison makes parity Q strictly decreasing and gives unique root 0<beta<1. Exactly one parity layer null, so embedding dimension drops by one. Uniform Krawtchouk magnitude bounds prove n^(r-1)beta -> (r-1)!/ln(r/(r-1)) for every fixed even r; finite test n8..11 independently checked all frequency modes and roots on both sides, not infinite proof.

## originality

PASS

PASS with credit limits: Classical Schoenberg/Sánchez supplies negative-type and finite-metric threshold machinery. The published nonbinary four-cap fixed-alphabet asymptotic recovers the binary cap4 leading constant, so the value 6/log(4/3) is not independently original. The exact for-every-n>=8 cap4 threshold, unique null character and sharp embedding dimension, plus hierarchy for all fixed even r>=6, survive the inspected prior comparisons; older metric-transform primary literature remains an access risk.

## value

PASS

PASS: Sharp supremal Hilbert snowflake/conditionally negative definite exponent with a unique Fourier nullspace and endpoint embedding dimension is a natural spectral metric invariant. Determining all fixed even-cap decay orders and a finite-dimensional cap-four exact threshold is motivated by kernel admissibility, not an arbitrary small instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
