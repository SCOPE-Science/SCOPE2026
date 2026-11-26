---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Partition the defining interval of B_1 into m equal translates of its scaled interval and convolve n times. This gives B_n(t/m)=m^(1-n) times the sum of B_n(t+n(m-1)/2-j_1-...-j_n) over 0≤j_a<m, a pointwise identity by continuity at these orders. In the normalized Zak sum, k'=k-K+sum(j_a) gives precisely m^(1/2-n) z^K D_m(z)^n Z_1 B_n(x+r,ν) with the stated sign. The prior unit-scale theorem uses the same centered convention and gives exactly the congruence class (1/2,1/2). The mask's simple unit-circle zeros are all the nonidentity m-th roots. Odd m gives r=0 and a disjoint center zero; for even m the only unit-scale zero falls on the line at ν=1/2, at x=1/2 for even n and x=0 for odd n. Finite Laurent-polynomial dependence on frequency implies exact order n at every other line point and at least n+1 at the exceptional point. The root at z=1 is removable in the quotient for D_m, not a zero. Independently, exact rational Cox–de Boor recursion checked 4100 Laurent coefficients and 100 unit-scale fibers at z=-1 for n=3..6 and m=2..6. The all-size proof does not follow from this finite test.

## originality

FAIL

In the same centered normalization, Hasannasab–Lemvig already display a general all-frequency Poisson formula and the sinc-power Fourier transform at the start of the proof of Lemma 2.2, as well as all-order unit-scale uniqueness on p. 1. Before imposing resonance in that proof, take b=m an integer. At u=ℓ+ν the quotient sin(πmu)/sin(πu) is (-1)^((m-1)ℓ) times sin(πmν)/sin(πν). Thus each Fourier coefficient is multiplied by m^(1/2-n) times the nth power of the latter quotient, and the ℓ-dependent sign is exactly exp(2πirℓ). Collecting it shifts x to x+r and contributes exp(-2πirν). The elementary geometric series rewrites the remaining factor as z^K D_m(z)^n, including ν=0 by continuity. This direct specialization of the displayed earlier formulas gives the boxed factorization, not merely the previously printed inclusion of horizontal lines. Simple mask zeros and the stated unit-scale uniqueness then give all the listed zeros and frequency orders, without a new analytic estimate or classification lemma. Identical factorization in an additional indexed record gives further overlap (there restricted in its finding to m≥3); its catalogue date is not used to infer priority.

## value

FAIL

The integer-resonance subfamily is mathematically motivated, and collecting its zero set is useful exposition. Under this standard the frozen exact result does not fill an independent scientific gap: substituting an integer in the available Fourier–Zak coefficients extracts a single geometric factor, after which the published unit-scale result gives the complete claimed set and line orders. No nonreciprocal scale, additional exceptional multiplicity computation, or genuinely unprovided fact is established here.

The dated certificate retains the supplied scientific assessment, sources and limitations.
