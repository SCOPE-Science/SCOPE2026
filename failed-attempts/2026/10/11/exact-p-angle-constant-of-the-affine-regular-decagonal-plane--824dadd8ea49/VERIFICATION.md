---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

In the stated real 2D norm N(s,t)=max(|s+t|,|rs+t|,r|s|,r|t|,|s+rt|) with r=(sqrt(5)-1)/2, I independently intersected all 45 pairs of signed facet lines and found precisely the ten declared primal vertices, and verified ten signed dual supports. For unit x,y let A=N(x+y), B=N(x-y). Choose norming facets f,g. Then A+rB=(f+rg)(x)+(f-rg)(y) <= ||f+rg||_*+||f-rg||_*. Exact Q(sqrt5) arithmetic over 100 ordered facet pairs attains the maximal value 3-r; flipping y gives rA+B<=3-r. Together with 0<=A,B<=2 these constrain (A,B) to the six-vertex polygon explicitly calculated independently. The strictly convex quadratic Q=A^2+B^2-(r/2)AB has maximal value 4 at polygon vertices (central vertex strictly below 4), yielding (A^2+B^2-4)/(2AB)<=r/4 for x != +/-y. The unit vertices x=(1,0), y=(0,1) have (A,B)=(2,r) and attain r/4=(sqrt5-1)/8. All universal steps follow from duality and convexity, not numerical sampling.

## originality

FAIL

A separate published theorem on classical smoothness moduli of EVERY centered regular even-gonal Banach plane determines rho_{X_5}(t) at all t, including rho_{X_5}(r)=r^2/2 for r=(sqrt5-1)/2. The polar of a centered regular decagon is a rotation and uniform scaling of it, so X_5* is linearly isometric to X_5. By independent support-function exchange, M_r(X)=sup_{x,y in S_X}(||x+y||+r||x-y||)=sup_{f,g in S_{X*}}(||f+rg||_*+||f-rg||_*)=2(1+rho_{X*}(r))=2+r^2=3-r. Changing y to -y yields the symmetric weighted inequality. Thus the supposedly sharper structural result is an immediate exact corollary of the earlier full all-scale theorem. Standard convex optimization on the resulting six-vertex chord envelope and the adjacent-vertex witness then gives precisely the claimed S_P=(sqrt5-1)/8. This is complete mathematical implication, independent of whether the covering paper uses S_P terminology. The covering source was imported at 2026-10-11T13:11:02Z, versus the assigned result at 13:12:27Z; their Resultary public synchronization was the same 13:59:41Z, so public simultaneity versus original discovery priority remains a chronology qualification, not a reason to ignore the dominating published statement.

## value

FAIL

The Yang--Li P-angle is a mathematically natural invariant and an exact decagonal benchmark could be of reference value. However this particular contribution is a narrow isolated constant whose asserted key structural chord inequality is exactly a single specialization of the already published all-regular-polygon classical smoothness modulus via elementary duality. After this specialization, the only further step is a standard convex quadratic check on six vertices and the obvious adjacent-vertex equality witness, not a new structural lemma, classification, or distinct motivated unknown. Its exact answer is already mechanically implied by stronger known mathematics, so it does not fill a genuinely independent mathematical gap under the stipulated value standard; educational convenience is not a separate research contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
