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

Write the translation index as mℓ+j and apply Parseval on the unit Zak square for the integer translation/modulation indices (ℓ,n) at each residue j. This gives the multiplier sum_j |Zg(x+j/m,ω)|² with no prefactor; the change from minus to plus shifts is reindexing modulo spatial quasiperiodicity. This sum is 1/m-periodic in x. The geometric tails combine as (H+Jz)/((1−q/z)(1−rz)), with z=e^(2 pi i ω), q=e^(−a), r=e^(−b), H=e^(−ay)−qr e^(by), J=r(e^(by)−e^(−ay)). Both numerator coefficients are nonnegative on [0,1] and not both zero. The modulus-squared numerator is nonnegative and nondecreasing in cos(2 pi ω), and its positive denominator strictly decreases; if the numerator vanishes at the lower endpoint it is positive at every larger cosine. This forces the two extremal frequencies. At ω=0 each positive exponential sum squared is strictly convex in x; equal boundary values give only the endpoint maximum modulo 1/m. At ω=1/2 the derivative has the sign of bVt²+(a−b)Ct−aU for t=e^((a+b)x); precisely one positive root and equal boundary values imply by Rolle that the minimum is unique and strictly interior. The two coefficient vectors are not proportional for m≥2, so the lower bound is positive. Continuity gives equality between pointwise and essential extrema, and frequency monotonicity gives A<B. All arguments include a=b and require no numerical limits. The inspected numerical script compares closed complex Zak tails and a bounded scalar minimizer only at finite parameter choices.

## originality

FAIL

The distinct Resultary entries 400c3e36998f and 76de6cc216c1 already give the same sharp bounds and Zak extremizers at redundancy two and at every higher integer redundancy, respectively, after unitary dilation. The proof of the latter has no step requiring unequal rates, so the symmetric higher-redundancy fiber claim is included by immediate specialization of that argument; the symmetric bounds are independently explicit in Faulhuber–Shafkulovska Eq. (9.1). Combining the covered regimes leaves no substantive distinct claim. Later catalogue dates document coverage, not priority or direction of dependence.

## value

PASS

The mathematical result gives exact stability constants and identifies the spectral locations for a natural continuous asymmetric window family at all integer redundancies, turning a two-dimensional extremization into a single explicit root. This is useful information not supplied by frame existence alone. It is nevertheless covered for originality purposes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
