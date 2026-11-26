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

Using the forward shift E on the recurrence, E^3=I+E^2 and E^7=3I+2E+4E^2, so B=(E^7-I)/2=I+E+2E^2 and B+B^2 is E+E^2 modulo two. The values u_3,u_4,u_5,u_6=1,2,3,4 make both corresponding scalar parities odd at each of r=3,4, at the base seven-step and doubled scales. Squaring I+2^(h+1)D_h makes D_h mod 2 stable from h=1 onward, and shifting by 7j does not alter the state mod 2. Thus each increment by 2^h of the branch parameter has valuation h+1; an odd number of such increments preserves that valuation because each divided increment is odd. Negating the order of s,t does not change it. The progression maps are therefore bijections onto their parity cosets modulo 2^k. The matrix congruence supplies period 7*2^(k-1); any period is divisible by seven by the nonconstant mod-2 cycle of prime length, and the r=3 valuation forces the full power-of-two factor. Direct recurrence gives 2 mod 8 only at n=4 and 7 mod 8 only at n=24 within the length-28 block. The parity-chart bijections then count exactly one hit per such target within each full period, since 28 divides that period for k>=3. An independent recurrence checked first register return, both chart permutations and the claimed singleton fibers through 2^14; the quantifiers beyond that range follow from the algebra.

## originality

FAIL

Demonstrable coverage, not a conclusion about calendar priority: distinct same-day Resultary record 1d412e89dd2f proves the exact two difference laws and both residue transversals after the normalization shift a_n=u_(n+1); it even rules out the other five isometry classes. The least period is independently known. The singleton supplement does not appear as a printed statement in that record, but is a mechanical consequence of its bijections and one mod-8 recurrence block. It can also be recovered directly from the earlier explicit mod-28 interpolation with two scalar parity evaluations. Thus no independently original main finding or nonmechanical remainder is established here. This is not a finding of false mathematics or a priority attribution between same-day entries.

## value

FAIL

The exact parity transversals are natural structural information, but are already supplied by the matching result. Relative to that coverage, the proposed additional singleton cylinders are obtained by filtering one length-28 table against those transversals (or by two parity tests in an available explicit interpolation). Neither the fraction one quarter nor least fiber size one adds content beyond that immediate deduction. There is no separate useful unknown invariant established at the required threshold: the frozen result deliberately does not classify the remaining fibers. No substantive repaired claim is supported by the existing evidence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
