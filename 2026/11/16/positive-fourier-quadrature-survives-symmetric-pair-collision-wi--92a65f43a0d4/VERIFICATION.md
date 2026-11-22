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

For every odd N=2m+1 and symmetric inward pair x0=αh,x1=(1−α)h, 0≤α≤1/2, the D_m Fourier kernel gives explicit real quadrature weights. Fourier inversion proves all N moment equations and Vandermonde uniqueness before collision. An alternating cosecant ratio and circular-distance inequality prove strict positivity of all indexed weights, including the two coincident endpoint labels (whose aggregate is the unique weight). At collision normalized Fourier matrix rank is exactly N−1 with simple left and right null vector (e0−e1)/sqrt(2); first-order singular-value perturbation yields 2π cos(π/(2N))/(N² sin²(π/(2N))) times (1/2−α), tending to 8/π. The proof is for all odd N; independent numerical moment solutions for N=3,5,9,15,31 and α=0,1/4,.499,1/2 verify positivity, exactness and sharp slope near α=.5, but finite checks are not an infinite proof.

## originality

PASS

No examined accessible primary theorem, exact table, or prior published mathematical result implies the complete specific final claim. This is best-of-knowledge originality, with the separately recorded plausible historical risks.

## value

PASS

The natural collision boundary of Fourier interpolation distinguishes two different numerical tasks sharply: positive exact quadrature remains optimally noise-stable in ℓ∞ even as Fourier coefficient recovery becomes linearly singular. An exact all-odd-order positive weight law and sharp N-dependent instability slope give a motivated structural benchmark beyond routine finite sampling.

The dated certificate retains the supplied scientific assessment, sources and limitations.
