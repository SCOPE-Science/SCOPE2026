---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

Probability-normalized angular θ for first two coordinates is independent of s=x1²+x2²~Beta(1,(d−2)/2) and transverse direction. The displayed transverse harmonic degrees j=0..3 give exhaustive orthogonal cubic decomposition; dimensions sum exactly to d(d−1)(d+4)/6. h(θ)=sign(cos2θ) has Fourier coefficients 2/π at ±2, zero at ±4 and −2/(3π) at ±6; hence T=I/2+K/π in indicated finite blocks. Exact beta moment correlations η0²=(d−2)/(3(d+2)), η1²=d/(2(d+2)) produce K0 4×4 eigenvalues ±(R_d±1)/3, K1 three-level 0,±sqrt(d/(d+2)), K2 ±1, K3=0. Block dimensions give zero multiplicity m+dim H3(m)=binom(d,3), and 4 simple outer branches, plus ±1/π of multiplicity d(d−3)/2, plus ±sqrt(d/(d+2))/π of multiplicity d−2. R_d monotone increasing with d and <sqrt7 yields strict order and sharp condition number. Independently diagonalized K0 in d=4,5,9 with max error 4.44e−16, a finite consistency check only. Boundary d=3 excluded because already covered by earlier pure-cubic quarter-lune result.

## originality

PASS

Best-of-knowledge PASS for d>=4 higher-dimensional exact paired-lune spectrum. Read full published d=3 quarter-lune result: parity can double its spectrum for d=3, which is intentionally excluded. General spherical Slepian method of Simons et al. gives eigenvalue formulation and numerical cap calculations on S² rather than these exact nine all-d sector levels. Other published cubic cap and octant masks and quadratic lune bands are different region/degree data. No exact higher-dimensional paired-lune coverage was found; full literature inventory remains bounded.

## value

PASS

Natural exact Slepian concentration invariant: complete nine-level spectrum across all ambient dimensions gives sharp stable restriction to a half-area disconnected mask, shows a binomial(d,3) protected half-energy sector, and an explicit dimension-independent optimal conditioning law. The sector classification is more informative than a routine numerical eigenproblem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
