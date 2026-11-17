---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

Every section is f(u)+v g(u), deg f<=2, deg g<=1, over q>=5, t=q-1>=4. A full u=a fiber imposes f(a)=g(a)=0 and W subset V_a=(u-a)<1,u,v>, dimension3. Two full fibers leave at most one-dimensional section, so dimension r>=2 has at most one full fiber. Rank 1 max zeros 2t from quadratic two roots; rank 2 max t+1, with unique W=(u-a)<u-b,v-c> indexed by a != b and b,c nonzero giving t^2(t-1) optimizers. Rank3 either W=V_a with t zeros or has at most one point per fiber: if all t fibers have a common zero, degree<=3 minors f_i g_j-f_j g_i vanish identically; proportional polynomial pairs force dim W<=2, contradiction. Rank4 evaluation at two torus points independent; rank5 constant 1. Therefore all maxima (2t,t+1,t,1,0) and N_r=(t(t-1)/2,t^2(t-1),t,t^2,1), with d_r=t^2-z_r. Independently enumerated all 42,175 subspaces of F5^5 (r totals 781,20306,20306,781,1); all maxima and optimizer counts matched. This finite enumeration supports but does not prove all prime powers.

## originality

PASS

Umaña and Velasco (arXiv:1404.4063 Theorem 3.4) give length/dimension/minimum distance of degree-one toric codes including Lawrence prism, not all optimizer multiplicities or their geometries. González Sarabia et al (arXiv:1611.06405 Theorem 18, Example 19) compute second weights for complete degree-bounded projective torus codes, not this proper sparse five-dimensional cubic scroll evaluation space or its optimizer counts. Resultary earlier cubic scroll Hamming spectrum is rank-one only and quartic S(1,3) hierarchy is another code. Uniform r=2,3 optimizing-section classifications and multiplicities survive; priority still qualified against specialized unindexed toric subcodes.

## value

PASS

The cubic scroll S(1,2) is a canonical degree-one toric variety and the generalized weight hierarchy governs multiword support. Counting all maximizing 2- and 3-dimensional spaces identifies projective linear sections of maximum point incidence; the exact uniform optimizer multiplicities are a natural nontrivial higher-support invariant, useful independently even if single-word weights are known.

The dated certificate retains the supplied scientific assessment, sources and limitations.
