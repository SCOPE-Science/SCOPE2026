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

A point is missed by the three closed translates exactly when the three relevant characters are all -1. The sum of the product of their three factors (1-chi) expands to 22-T, using the three vanishing single sums and the three pair sums of -1. Each missed point contributes 8; each center with both differences nonsquare contributes 4. Thus 22-T=8M+4R. Hasse bounds |T| by 10, so coverage is equivalent to R=3 and T=10. Normalizing the triple gives T=chi(t)T_lambda, and R=3 forces t nonsquare. The independently recovered cubic-sum table has T_lambda=-10 only at 13 and 18, the two roots of lambda^2-lambda+1; both lambda and lambda-1 are squares there. A direct independent test of all 2,300 subsets found exactly the asserted 100 covers, all 600 ordered parametrizations mapping six-to-one onto those covers, and the same orbit of the given representative under the 300 affine-square maps. Inversion swaps the two roots, so swapping the second and third points converts one root to the other without changing the nonsquare condition on t. The stabilizer order follows, and the pair intersection sizes 6 and 7 exclude any two-center cover.

## originality

FAIL

The classification is correct but is a direct specialization of two earlier results. Brouwer–Martin's proposition 0.1 proof applied in the complementary Paley graph forces a zero common-neighbor triple at q=25 to attain the elliptic Hasse endpoint, with R=3. Their proposition 0.3 proof explicitly relates the endpoints to supersingular Legendre parameters and nonsquare dilation. Auer–Top give both the Deuring polynomial criterion and the point count of the supersingular Legendre curves over the prime-square field. At p=5 the polynomial is exactly 1+4 lambda+lambda^2, and the supersingular Legendre point count is 16, i.e. T_lambda=-10. Conversely 16 points give trace 10 divisible by 5, hence supersingularity, as also used for the endpoint in Brouwer–Martin. Thus the two parameters are forced without a new enumeration, the nonsquare twist changes the trace sign, and the count and single orbit follow from ordered triples and the reciprocal pair of roots. This is a mathematical coverage finding, not an inference from an uncited later remark or a bare matching parameter.

## value

FAIL

The order-25 boundary is naturally motivated and the finite result can be useful as a check. But its purported contribution—the precise parameters and count of the covering triples and their affine-square orbit—is mechanically implied by the prior endpoint reduction and Deuring criterion. The remaining 23-entry trace calculation is an auxiliary small-field recomputation, not a separately motivated surviving claim in this record.

The dated certificate retains the supplied scientific assessment, sources and limitations.
