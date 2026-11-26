---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

The six distinct quadratic Walsh characters are orthonormal, so unit variance is the unit sphere. On the two values of the product of the three relative signs, opposite edge coefficients combine by a sum or difference. This is an orthogonal change of coordinates, and each parity class has the same absolute moments as a linear three-sign sum with coefficients from its own block, scaled by √2. A positive sign product on a four-cycle lets vertex sign changes clear its four edge signs. The two profiles reduce to (1,1,0)/√2 and (1,1,1)/√3 in an active block, with zero in the other, modulo vertex and overall sign symmetries. Direct expansion of the four absolute powers at the square gives normalized quadratic coefficients −p/2 and p(p−3)/8. At the complete profile the first variation vanishes by symmetry, the S₃-invariant Hessian is scalar on the tangent plane, and the coefficient along (1,−1,0) has sign 4p−5−3^(p−1). Inactive-block mass r costs a positive multiple of r² by homogeneity and adds only O(rᵖ), uniformly in its direction, giving strict maxima on the sphere where claimed and a saddle when the complete profile has positive active curvature. The moments obtained by evaluating the four absolute powers agree with the finding. Strict convexity and the signs at p=2, 5/2 and 3 give uniqueness and separation of the two nontrivial roots (for the crossing use t=p/2−1 and 3(3/2)^t+6^(−t)−4). Independent 50-digit interval evaluations bracket p_loc in (2.34182245474,2.34182245476) and p_cross in (2.73627732198,2.73627732202). The complete branch at p_loc is not classified; the square argument still applies there.

## originality

PASS

The nearest useful equivalence is to the two-sparse and diagonal profiles of the three-sign Khintchine moment, together with perturbations into the other parity block. General dimension-free inequalities and fixed-count diagonal stability for p≥3 are genuine background, but the inspected results do not establish the Hessian sign change, the distinct moment crossing below 3, or coexistence on the four-sign quadratic sphere. The bounded review supports that distinct local claim, not priority for Khintchine extremizers.

## value

PASS

The smallest quadratic Walsh space with these competing support patterns supplies a concrete instance where the onset of local stability and the change in moment ordering are separated. The orthogonal parity reduction and exact roots explain why a comparison of just the two moment values could not detect the onset of coexistence. This is useful finite variational information even without a global sharp norm.

The dated certificate retains the supplied scientific assessment, sources and limitations.
