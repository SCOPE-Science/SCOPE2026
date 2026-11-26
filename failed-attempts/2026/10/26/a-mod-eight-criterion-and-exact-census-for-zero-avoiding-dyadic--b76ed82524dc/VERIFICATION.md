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

Reduction by the common power of two is injective on its depth stratum and preserves periods and zero events. The primitive mod-two three-cycle forces any return index to be a multiple of three. Writing that index as 3·2^r times an odd integer, the displacement matrix divided by 2^{r+1} is invertible mod two: the base cases are M³−I=2M and M⁶−I=4M³, and further squaring preserves invertibility. Thus the primitive period is 3·2^{h−1}. The coefficient of M in M⁶ is 8; in each subsequent square its valuation rises by one since the scalar coefficient remains odd. Odd powers preserve that coefficient valuation, and mod eight the Fibonacci zeros occur precisely at multiples of six. Therefore the projective zero-bearing orbit has length 3·2^{h−2} for h≥3, and for h=1,2 its length is the full projective cardinality. At h=3 the norm is odd, changes sign under T and is unchanged by odd scaling; the six projective directions with norm ±1 are exactly the six on the zero-bearing orbit. At larger h, every zero-bearing direction reduces to this orbit, and equality of orbit size with the number of its lifts gives the exact iff. Each safe direction has 2^{h−1} representatives, giving 3·2^{2h−3} safe states and 2^{h−2} cycles at that depth, and summing gives the stated k≥3 counts. The zero pair and k=1,2 are excluded appropriately. Independent cycle enumeration at k=3 and k=8 corroborated 24 and 32760 safe states and 2 and 126 cycles, with the criterion and every safe period tested.

## originality

FAIL

The dyadic census is already implied by a preceding stronger Resultary first-hit theorem, and the exact aggregate object is recorded in OEIS. The prior theorem not only counts hits but lists the actual primitive hit set at every modulus. The remaining mod-eight recognition rule is a concise reformulation of that set: reduction and equality of cardinalities identify the hit set with a full pullback, and the sign-changing determinant evaluates the fixed twelve projective directions. The cycle counts add the usual primitive period to the already implied state counts. This is a direct deduction, not a rejection based on inaccessible papers or a claim that the norm-test wording previously appeared verbatim.

## value

FAIL

Fast membership recognition for arbitrary dyadic seeds is a naturally motivated exact question, and the local norm rule is convenient. However, the prior theorem already enumerates the same set comprehensively; the uniform localization is a direct pullback/cardinality deduction and its norm label is a twelve-direction calculation. The aggregate is already recorded and the cycle count is obtained by dividing by the standard primitive period. The frozen record therefore does not supply an independently needed new exact invariant beyond a compact implementation of already implied information.

The dated certificate retains the supplied scientific assessment, sources and limitations.
