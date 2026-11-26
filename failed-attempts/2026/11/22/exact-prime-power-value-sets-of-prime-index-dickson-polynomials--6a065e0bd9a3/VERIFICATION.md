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

The Laurent substitution X=z+a/z is injective on polynomials and gives Frobenius reduction. Differentiating the Laurent identity and squaring yields the normalized derivative identity; cancellation and monicity give D_p'/p congruent to (X^2-4a)^((p-1)/2). On ordinary discs the higher Taylor terms vanish after normalization and reduction modulo p, so uniquely lifting the unit linear map gives all outputs in the depth-two ball and the asserted fibers. For a square unit a=b^2, homogeneity reduces to parameter 1. With m=(p-1)/2, the geometric sum z^(-m)(z^p-1)/(z-1) proves the square factorization of D_p(Y,1)-2; that factor is p at Y=2 and has derivative divisible by p there since m>=2. Thus the normalized exceptional map is the identity modulo p as a polynomial, giving depth-three balls at the stated centers and p^2 fibers for k>=3. Reduction modulo p keeps branches disjoint, including the boundary precisions k=1 and k=2. For p=3 and a=1 the exceptional normalized map at +2 is u(1+u)^2, with two values modulo 3; the negative branch contributes two and the ordinary branch nine modulo 81, confirming the stated exclusion. Independent finite enumeration agreed in 11 cases; replay files: /workspace/branches/0cb9656a-330c-4e32-a1b0-7782732ae7f8/record4_independent_replay.py and record4_replay_smoke.txt, record4_low_levels.txt, record4_replay_extended.txt in that directory. The replay tests only those cases.

## originality

FAIL

The exact exceptional classification is materially covered by a distinct indexed finding. Its r=1 case supplies the parameter-one depth-two and depth-three branches and the exact fiber law; the unit domain and codomain scalings x=bY and output=b^p times output transport all of it to every square unit a=b^2. That includes both exceptional centers and all the low-precision cases. The same date does not establish priority. The nonsquare case is not stated by that counterpart and exact nonsquare coverage by the 1991 paper was not verified from the original statements. The failure is based on demonstrated duplication of the frozen claim's central exceptional increment, not on the unavailable paper.

## value

FAIL

The wild degree-p parabolic fibers are a well-motivated problem, but that substantive part is already present in the distinct indexed classification up to a unit change of coordinates. The nonsquare remainder has no exceptional branch: the standard Dickson identity directly gives a unit normalized derivative everywhere, and one uniform Taylor–Hensel step then gives every size and fiber. No independent nonroutine remainder or useful repaired claim is established by the frozen record.

The dated certificate retains the supplied scientific assessment, sources and limitations.
