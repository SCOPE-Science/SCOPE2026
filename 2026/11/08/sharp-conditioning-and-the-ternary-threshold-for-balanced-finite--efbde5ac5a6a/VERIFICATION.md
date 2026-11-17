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

Use the cited Johnson intersection-matrix harmonic eigenvalue formula λ_j=(ζ-1)^j Σ_{l=0}^{k-j} C(k-j,l)^2 ζ^l with multiplicity C(2k,j)-C(2k,j-1); Legendre identity transforms the absolute values to (2sin(π/M))^k U_{k-j}(cot(π/M)). The displayed three-term recurrence has positive U_m for c>0, proving invertibility. For M≥4, c≥1 and positive recurrence make U_m nondecreasing, with M=4 tie at m=0,1; for M=3, T_m=3^{m/2}U_m(1/√3) obeys central-trinomial recurrence and r_m>√3 for m≥2, yielding minimum m=1 and maximum m=k with k=1,2 exceptions. Standard Laplace and generating-function singularity analysis gives the two sharp k-asymptotics at fixed M. Independent complex singular-value decomposition of the original balanced binary-slice matrices in all 15 cases k=1,2,3 and M=3,4,5,6,8 matches predicted full multiplicities to <6e-15. The finite SVD does not prove all k or reproduce the inaccessible original general eigenvalue theorem; reliance on the cited established intersection-scheme identity is explicit.

## originality

PASS

Ghareghani–Ghorbani–Mohammad-Noori (2009/2012) provide the broad Johnson intersection-matrix eigenvalues, Filmus the harmonic representation and Sun the generalized central-trinomial sequence. Those established parts are NOT claimed new. Resultary searches did not reveal an earlier exact minimizer-sector change at M=3, complete condition-number formula for this primitive-phase family, or its two sharp exponential asymptotics. The classical eigenvalue theorem and Legendre identity make the calculation possible but do not give the nonmonotone ternary order without the additional ratio induction. Priority is qualified because the complete Ghareghani text and other potentially relevant literature could not be independently retrieved.

## value

PASS

The inverse stability of a natural balanced constant-weight Fourier minor depends on the minimum positive harmonic singular value, not merely knowing an unordered Johnson spectrum. The discrete ternary switch from m=0 to m=1 and exact exponential stability rate is a motivated spectral classification that is not merely a tiny-example table. The result is narrow in modulus and balanced slices but precise and reproducible.

The dated certificate retains the supplied scientific assessment, sources and limitations.
