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

Independent exhaustion reduced to one pencil. For any smooth pencil of symmetric forms Q,R, Q is invertible and A=Q^{-1}R has irreducible cubic characteristic polynomial, since a rational eigenvalue would give a singular pencil member. Identify the space with K=F125; self-adjointness for Q makes Q and R the trace pairings with coefficients c and cα, where α generates K. PGL2(F5) is regular on the 120 degree-three elements (a stabilizing fractional-linear map gives a relation of degree at most two); multiplying input by K* adjusts c up to F5*, because squaring is bijective in K*/F5* of order 31. Thus all smooth pencils are conjugate. A pencil stabilizer normalizes K: a pencil basis change replaces A by a fractional-linear function generating the same field. Such a stabilizer is semilinear, and for each of the three Frobenius powers there is exactly one projective multiplier carrying the resulting coefficient plane back to itself: K*/F5* acts regularly on the 31 coefficient planes, as a nonrational multiplier cannot preserve a proper nonzero subspace. Hence the pencil orbit has 372000/3=124000 elements. The independent exact replay /workspace/record1_pencil_certificate.py verifies all six forms in the common displayed pencil, tests the 156 quotient lines with 25 new members each, and finds exactly the two printed nets. It also recomputes their geometric rank-one ideals on the remaining charts and the two permutations of 31 rational points. The ideal for type A on u=1 is (v+w²−w+1,w³−w²+w+1); the cubic is irreducible and separable. Type B and both infinity charts are empty. Transitivity on pencils now gives one extension of each type everywhere, and counting 31 pencils per net gives 4000 nets in each orbit and stabilizer 93. This verifies the complete claim without rerunning the frozen full-size sweep.

## originality

FAIL

The central two-orbit classification is covered in an equivalent formulation: the known strong-isotopy classes of commutative presemifields of order 5³. The geometric distinction, rational permutation, counts and opposite-type extensions follow from the two known normal forms and elementary invariant or orbit counts. This is a positive coverage finding, not a negative inference from missing sources.

## value

FAIL

The census is an accurate explicit illustration of the known complete classification, but its proposed contribution is not a separately substantial finite invariant: the rank-one and permutation facts are immediate in the known normal forms, and the precise extension count follows from the transitive pencil orbit and order-31 multiplier action. No independently motivated, nonmechanical remainder is established for this frozen claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
