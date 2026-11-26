---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

At h=1 the second-coordinate reset forces any positive primitive pair to be (p,q²),(q,p²) with p≠q. The sum and divided difference of the first-coordinate equations give u=1+(v+2)/a and P_a(v)=v²−Bv+a+2=0, where u=p+q, v=pq and B=a²−a−3. Conversely these two symmetric identities recover both cycle equations when u²−4v>0 and v>0. For positive a≤(√5−1)/2 the real roots are negative; after that the discriminant is negative through the interval up to a_Δ=(3+√13)/2. At a_Δ the double root has u²−4v=3(1−√13)/2<0. For a>a_Δ both roots are positive. With w=a+v+2, the remainder of a²(u²−4v)=w²−4a²v modulo P_a is (a+2)(a+1)+(−3a²+a+1)v, so the discriminant at v_- is strictly larger than at v_+. Their product after scaling each by a² is −a²(a+2)(3a³−10a²−8a−4). By continuity and this sign change at the unique positive cubic root a_*, both are negative below a_*, only the larger reaches zero there, and only the larger is positive above. At the zero p=q is not primitive. On the surviving branch det K=4v_-²; implicit differentiation gives v_- strictly decreasing to zero and crossing 1/2 at a_d=(3+√39)/2>a_*. Thus det K>1 already excludes attraction below a_d. For a≥a_d, using the orbit equations in the trace gives H=a²v(1+tr K+det K), a polynomial whose product at the two v-roots is −a²(a+2)Q(a). I reproduced this product and verified all coefficients of Q(t+9/2) are positive. The branch has no zero of H there and its sign is negative as seen at a=5, where det(I+K)=(39269−7347√29)/50<0. The characteristic polynomial at −1 is therefore negative, giving a real multiplier below −1 including at a_d. These arguments establish the positive primitive census and linear nonattraction for h=1 only, not global basins, longer periods or other steps.

## originality

PASS

The map, positive fixed point and local flip analysis are prior; the cubic at h=1 follows from the fixed-point multiplier condition and is not itself a new local threshold mechanism. The supported distinct result is a complete positive primitive period-two census along the reset slice and the global-in-parameter exclusion of attracting two-cycles on that slice. The primary prior text gives local conditional results and selected examples, not this full census or all-parameter Floquet inequality.

## value

PASS

The slice is mathematically natural: the reset of the second coordinate exposes exactly solvable exchange constraints absent at a generic Euler step. The local flip location alone does not settle whether other positive pairs exist or whether a sink appears farther from the collision. The full census plus exclusion of attraction on the whole surviving branch answers both questions for an established map, including the harder region where the determinant test ceases to decide. It gives no claim about continuous-time periodic orbits or other step sizes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
