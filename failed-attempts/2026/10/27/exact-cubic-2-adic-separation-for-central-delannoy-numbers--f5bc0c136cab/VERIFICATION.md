---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The interpolation F(z)=sum 2^k binom(z,k)^2 converges uniformly on Z_2 by integrality of each binomial. For z=2u, u odd, reduction mod 8 leaves 4 binom(z,2)^2≡4 in F(z)−1. On z=4w each k-term has Gauss valuation at least B(k), by subtracting twice the sum of max(nu2(j)−2,0) over j<k. The bound tends to infinity; the independent exact calculation finds min B(k)=10 for 9<=k<=31, and k/2+9/2−2 log2(k) is increasing and at least 10.5 for k>=32. Thus the series is restricted analytic on the scaled ball and the tail vanishes coefficientwise mod 128. The separate exact rational polynomial replay for k=1..8 gave residual coefficient valuations for degrees 0..16 of (infinity,infinity,12,7,7,10,9,11,10,18,16,20,19,28,24,27,26) after subtracting 64w³. The quadratic coefficient is exactly zero, not merely 0 mod 128: formal differentiation proves Li2(t)+Li2(t/(t−1))=−log(1−t)^2/2, with valid restricted-series substitution on t in 2Z_2. At t=2 both arguments are 2 and log(−1)=0. Together with vanishing of the linear term this yields F(4w)−1=64w³ times a unit series congruent to 1 mod 2, proving the exact order on 4Z_2 away from zero. Euler's rational hypergeometric transformation can be evaluated at t=2, giving F(−m−1)=−F(m); continuity extends it to every 2-adic index. This transfers each even residue ball to the corresponding odd one and preserves the valuation. The cases cover n>=1; n=0 is outside the assertion. The finite replay verifies arithmetic, not the infinite identities or bounds, and did not execute the frozen script.

## originality

FAIL

Lengyel explicitly conjectures each cubic branch and proves both small-valuation branches, so the cubic proof would be a meaningful resolution if outstanding. But distinct indexed mathematical records actually state and prove the cubic branches, and the dyadic-fibers result also gives the same critical analytic factorization with coefficientwise odd-unit control and the same reflection. Taken with Lengyel's lemmas they cover the entire frozen claim. This is a determination of mathematical coverage at review, not historical priority, which cannot be inferred from the catalogue dates.

## value

FAIL

Proving Lengyel's two exact conjectured valuations is mathematically motivated and the cubic orders matter to dyadic interpolation. But the checked catalogue already gives these orders and the stronger controlled cubic structure needed for exact fibers. The frozen proof's different finite expansion of eight terms is a useful cross-check, not a distinct exact fact or a new method materially beyond the same dilogarithm cancellation, interpolation, and reflection. No valuable distinct remainder in the frozen theorem was identified for repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
