---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The beta integral on monomials gives a rising factorial in j divided by (n+2)^{overline k}. Its highest Bernstein coefficient is the falling factorial of n, so selfadjointness and polynomial filtration give the Legendre eigenvalues, with zero on the orthogonal tail. Writing m=n+1, the product gives −m log λ=h_k+2m Σ_{r≤k}(artanh(r/m)−r/m), strictly exceeding h_k on positive finite-rank degrees. At k=1 exponent n fails by n log(1+2/n)<2; lower exponents, including M_n^0=I, fail there too. For k≤m/2 the cubic remainder bound gives an error at most (2/9)m^(−2)h_k²e^(−h_k); for k>m/2 including k>n, m<2k≤2h_k gives the asserted constant-4 bound from e^(−h_k). The fixed-degree cubic term is h_k²/(6m²). The displayed diagonal summable majorant gives trace convergence and hence the operator norm conclusion (maximum at h=2). For a fixed c, the remaining exponent shift d=c−1 changes the eigenvalue power by first-order −d h_k e^(−h_k)/m. The power difference at k≤m/2 is dominated after scaling by C_d h_k e^(−h_k/2) using −log λ≤C h_k/m and m−|d|≥m/2; the tail k>m/2 obeys the same type of majorant using m<2k. Replacing scale m by n is asymptotically immaterial. The claimed trace and operator constants agree with independent decimal evaluation.

## originality

FAIL

The distinct indexed multivariate centered-clock theorem directly covers the main assertions by specializing d=1, θ=(1,1), t=1, and Schatten p=1. It gives one-sidedness, the explicit leading coefficient with a strictly stronger remainder, and the fixed-shift law. The one-dimensional exact integer minimality is expressly acknowledged in that record, and follows immediately from its spectral product and a degree-one check. The explicit coefficient 4 in the uniform Loewner envelope is not its headline, but is a coarse elementary bound from the same centered product and its low-mode/tail split. There is no remaining substantive independent claim in the frozen package. This conclusion is about demonstrable mathematical coverage; the multivariate record itself credits an earlier unweighted theorem, and no historical ordering or source of discovery is inferred from the shared date or that unlinked attribution.

## value

FAIL

A sharp diffusion clock and trace-ideal leading law are scientifically useful; both are covered by the more general exact centered expansion. The residual contributions are an elementary scalar confirmation of integer minimality already acknowledged there and an explicitly nonsharp constant from the same low-mode and tail estimates. Neither supplies a distinct useful quantitative or structural result beyond the established comparison.

The dated certificate retains the supplied scientific assessment, sources and limitations.
