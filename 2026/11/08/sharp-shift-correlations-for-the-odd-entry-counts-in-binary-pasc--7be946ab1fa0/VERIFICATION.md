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

Lucas theorem gives F(n)=2^{s_2(n)} with exact dyadic means 3^L/2^L and second moments 5^L/2^L, so variance positive even at L=1. Carry-state enumeration for cyclic +h produces T0=[[5,0],[2,2]], T1=[[2,2],[0,5]], initial e=(1,0), final (1,1)^T. The trailing zero transfer normalized by 5^k converges exactly to v=(1,2/3)^T, and dividing the cyclic cross-sum by 5^L and subtracting (9/10)^L yields rational limiting Pearson rho(h)=5^{-ell} e product_{low-to-high digits}T_d v, with rho(0)=1. T0v=5v and T1v=(10/3,10/3)^T <=5v strictly in first coordinate, with all carry products preserving positive row first coordinate: every additional 1-bit beyond the highest required one strictly lowers rho, so the unique maximal positive lags are powers of 2, rho=2/3. Along alternating shift h_m=(4^m-1)/3, T1T0 has trace 24 determinant 100; Cayley–Hamilton gives r_m=(24/25)r_{m-1}-(4/25)r_{m-2} and positive roots (12±2sqrt11)/25<1, implying unattained infimum zero. Direct independent exhaustive finite equality of weighted cross-sums to transfer matrices for all lags through L=8 and 511 positive lags only corroborates universal algebra.

## originality

PASS

The classical Glaisher/Fine/Lucas row count is not new. Shifted digit-sum-difference distributions of Spiegelhofer and Emme et al. are closely related but are not directly the growing positively weighted product joint moment divided by variance nor the global all-lag extremizer theorem. Best-of-knowledge the sharp rational Pearson profile is original, with open risk from general unlocated q-multiplicative weighted autocorrelations.

## value

PASS

The number of odd coefficients in each Pascal row is a classical natural arithmetic observable, but its autocorrelation across row index is a genuinely different invariant. Classifying every positive shift, all extremizers and the rate of decay along structured binary lags reveals the carry-dependence structure of a canonical sequence rather than an arbitrary slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
