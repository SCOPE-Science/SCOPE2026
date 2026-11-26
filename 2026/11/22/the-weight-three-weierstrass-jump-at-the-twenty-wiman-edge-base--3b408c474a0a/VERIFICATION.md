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

Adjunction for C∼−2K_S gives K_C=(−K_S)|_C; restriction of sections is an isomorphism by H^0(K_S)=H^1(K_S)=0 on the rational surface. The six displayed bidegree-(2,2) sections vanish at the three blown-up centers (use the corresponding homogeneous coordinates for the two infinite-chart points) and their distinct nonconstant monomials give independence. Thus their local coefficients give the full canonical series. In independent exact polynomial-ring code I checked F(1,u)=0, ∂_y(2F)(1,u)=4−2u with inverse (1+u)/6, constructed the t=x−1 solution through degree seven, and substituted it back into 2F to verify every coefficient through t^7 vanishes. I recomputed the jet determinant by subset DP in Q[p,u]/(u²−u+1); it is (4p²−105)(4p²+3)^3/62208. On 4p²=105, all five-row minors through order 4 and all six-column minors through order 6 vanish. The reported minors for orders 0..3, (0,1,2,3,5), and (0,1,2,3,5,7) were reproduced; the norms of the first two are 3(4p²−6p+219) and 729(4p²+27)/4, nonzero at both parameters, and the last minor is −486p. Thus the truncated ranks through successive orders 0..7 are 1,2,3,4,4,5,5,6, yielding the claimed orders, gaps and weight. The parameter normalization and excluded singular fibers agree with the inspected primary model; neither exceptional parameter is singular. Transitivity of A_5 on the twenty-point orbit transports the calculation. The simultaneous inversion of x,y preserves G and negates H after multiplying by x^4y^4, permutes the blowup centers and identifies the two fibers. Total canonical weight is 210 for g=6, and this orbit contributes 60 at each of the two signs. Replay: python3 /workspace/branches/recheck_3.py (SymPy); the submitted verifier was inspected, not run. Only smooth complex fibers and the marked orbit are classified.

## originality

PASS

The positive judgment is for the exact canonical orders and jump locus on the distinguished twenty-point orbit, not for the pencil, equations, orbit, singular-fiber list, sign symmetry or general theory of canonical jets. The strongest accessible same-pencil sources establish structural facts but the inspected decisive passages do not imply this exceptional ramification calculation. The most relevant inaccessible historical comparison is Edge 1981, noted explicitly below; its unavailability does not establish historical priority or block a binary verdict.

## value

PASS

The marked points persist intrinsically throughout a natural genus-six family; their being ordinary is not forced by symmetry. Detecting and classifying the precise two smooth parameters where all twenty jump to weight three simultaneously determines a substantial and exact part of the canonical ramification divisor, and distinguishes those parameters in the marked family. The complete local vanishing sequence is more informative than detecting that a Wronskian vanishes. No novelty or value is claimed here for a full ramification-divisor classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
