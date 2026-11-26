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

For n strict ascents the first n digits must be weakly increasing. Equal adjacent digits defer the comparison to the next suffix; at the last digit v, the first different digit in the independent tail must exceed v. Apart from a null set this is also sufficient. The prefix count is binom(n+v-1,n-1) and the tail factor is (b-1-v)/(b-1); summing by two hockey-stick identities gives the frozen formula and its fixed-b asymptotic. At b=2 the same comparison gives A_j=1-D_j almost surely, jointly in j. At b≥3 all-one histories have positive probability and their continuation ratio 1/b+(b-2)/(b(n+2)) strictly varies even beyond any proposed memory order. Independent interval intersections for n=2 give 1/4 and 2/9 at bases 2 and 3; these are spot checks, not the proof. The supplied checker was inspected, not executed. No Lean or expert attestation is inferred.

## originality

PASS

Pass the all-integer-base ascent law and sharp binary memory classification, not the previously known tripling specialization. The strongest inspected related sources concern the exact b=3 case, realizable ordinal patterns rather than their probabilities, generic entropy growth, or a different probability model. No equivalent all-base evaluation or classification was established in the bounded comparison.

## value

PASS

There is a sharp qualitative distinction between the iid base-two ordinal observations and infinite memory at every higher integer base, despite iid generating digits in all cases. The exact run law supplies a quantitative memory diagnostic and its base-dependent polynomial prefactor, not just another parameter example of the known tripling calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
