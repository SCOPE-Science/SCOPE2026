---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

Tilting the killed symmetric kernel of rate d/2 in each direction gives the factor exp(-lambda t)rho^(j-i); reflection subtracts the kernel from the reflected start. The initial rho^i cancels exactly. In the sine integral, v=u/sqrt(t) and j<=L log(t) permit replacement of sin(jv)/(jv) by one uniformly on bounded u, with Gaussian domination. For diffusive i, evaluation of the remaining Gaussian sine integral gives A_d y exp(-y^2/(2d)), y=i/sqrt(t), in tB_t/j; for i<=t^(1/2-delta), replacing the other sine ratio yields A_d in t^(3/2)B_t/(ij). Bounding both sines linearly also gives the global ij t^(-3/2) bound. Telescoping the Bessel difference for i>=2j uses j indices comparable to i, and shifting the unrestricted Fourier integral by an imaginary h=min(k/(2dt),1) gives the stated t^(-1/2) times exp[-c min(k^2/t,k)] bound. These estimates control the large-i tail; the global bound makes the small-diffusive-i remainder O(epsilon^(2-beta)) below beta=2. The weighted diffusive Riemann sum then gives the normalized gamma transformation in the finding. At beta=2 the harmonic sum up to t^u contributes u log(t) for 0<u<1/2, the total contributes (1/2)log(t), and the mass above sqrt(t) is lower order. At beta>2 the global bound is summable against i^(-beta)rho^j; counting-measure dominated convergence gives total variation after normalization. The terminal tail j>L log(t) is negligible by the geometric majorant, and in each regime the joint restricted weights factor with j rho^j. The terminal normalization is rho/(1-rho)^2. In the QSD recurrence a pi_(j+1)+b pi_(j-1)=(a+b-theta)pi_j with pi_0=0, theta=lambda gives the positive double-root solution j rho^j; larger theta cannot give positive weights, and smaller theta gives a larger law by an increasing likelihood ratio relative to j rho^j. Thus the identification as the minimal QSD is correct. The two frozen scripts and recorded results were inspected, not executed; no finite probe substitutes for the uniform limits.

## originality

PASS

Credit classical killed kernels, QSD selection, and the materially overlapping same-day terminal/survival asymptotics. The distinct supported result is the joint posterior law of the initial and terminal sites, particularly the critical uniform law on normalized logarithmic scales and the independence statement across the three regimes. No accessible statement gives that joint result or the uniform-in-start information that would imply it. This is a limited statement comparison, not a priority guarantee.

## value

PASS

The result identifies which starting states account for survival even when the terminal law is unchanged. It distinguishes diffusive, logarithmically spread and lattice-localized entrances with exact limits and shows they decouple from the terminal site. In particular the log-uniform threshold law contains information absent from the logarithmic survival prefactor alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
