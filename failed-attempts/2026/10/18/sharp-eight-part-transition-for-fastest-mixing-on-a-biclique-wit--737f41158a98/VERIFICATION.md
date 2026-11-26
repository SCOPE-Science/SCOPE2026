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

Convex averaging preserves feasibility and takes the full symmetric stochastic problem to the two edge orbits; it does not imply unrestricted uniqueness. The even mode is 1-my, the ordinary differences have eigenvalue z=1-(m-1)x-y (absent at m=2), and the odd block is E in RESULT.md. Its first column gives a squared lower bound 1/m+m(m-1)(y-1/m)^2. Equality at 1/m forces y=1/m and tr E=0 because the off-diagonal is nonzero and the first column is a maximal singular direction. The remaining z=(m-2)/(2m) is compatible precisely through integer m=7. For the high branch set r=m-1, v=tr(E)/2, s=sqrt(m^2-8m+8), D=2r+s and t=(m-2)/D. Then z=v+(m-2)y/2 and ||E||=|v|+rho with rho=sqrt((1-ry-v)^2+r y^2). At v=0, y=2/D the candidate is feasible, z=rho=t and |1-my|<t. The supporting plane of rho has slopes -s/(m-2) in v and -L with L=r(s-2)/(m-2)>0 in y. Any pair with objective <=t thus has Delta y>=0 and v<=0; for v<0 the two bounds require L Delta y>=(1+s/(m-2))(-v) and Delta y<=2(-v)/(m-2). These are incompatible because (m-2)(1+s/(m-2))/2-L=m(m-s)/(2(m-2))>0. Therefore v=0 and Delta y=0, certifying optimality and invariant uniqueness. The intact all-edge-symmetric walk minimizes max(|1-2p|,|1-p|) at p=2/3, and rationalizing the difference gives the exact penalty and limit 4/9. Independent full-matrix diagonalization at m=2,3,4,7,8,9,12,20,60 agreed to 1e-15; numerical certificate checks at m=8..200 had residual <=4.3e-14. Frozen checker and requirements inspected, not executed.

## originality

FAIL

A distinct indexed Resultary record dated 2026-10-25 supplies demonstrably equivalent coverage of the substantive m>=3 optimum, weights, 7/8 transition and leading penalty, with the same objective and admissible class. This is a finding about coverage in the inspected corpus, not an inference of who obtained the result first or from whom. The m=2 endpoint is the known P4 theorem. The exact penalty identity and invariant uniqueness are immediate consequences of the matched formula and equality conditions; there is no distinct substantive remainder to pass.

## value

PASS

The underlying mathematical fact is worthwhile: removing one cross edge activates a different spectral constraint at a sharp part size, and the exact quadratic-order loss quantifies the robustness of fastest mixing to the first edge failure. A fixed-size SDP or the intact graph optimum does not supply that uniform classification. This scientific value does not make the separate equivalent coverage original.

The dated certificate retains the supplied scientific assessment, sources and limitations.
