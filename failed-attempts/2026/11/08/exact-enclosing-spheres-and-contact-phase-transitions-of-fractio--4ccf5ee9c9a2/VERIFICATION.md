---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-19.md",
      "INDEPENDENT_AUDIT_2026-11-19.json"
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

For n>=3 and real 0<tau<=n, the frozen result proves all vertices are 0/1 vectors of weights <=q, plus q-ones/one-s vertices for s>0. The max squared distance to a center c is ||c||² plus a max of affine functions of c, strictly convex and coercive, ensuring a unique center; permutation symmetry makes it diagonal. An origin bound and the cube midpoint constrain 0<=a<=1/2. The two farthest squared-distance profiles Dq=na²+q(1-2a) and DF=Dq+s(s-2a) cross at a=s/2, with stationary centers q/n and (q+s)/n. Their convex-envelope minimizer is precisely the median clipped to [0,1/2]. Strict increase in Boolean weight for a<1/2, the exact branch difference and strict convexity on segments classify all contacts (including transitions); a=1/2 contacts all admitted Boolean ranks, never fractional vertices. At integer s=0 and tau=n the formulas have correct limiting boundaries. For q=1,n>=5 the crossings s=2/n and 2/(n-2) and R²=(n-1)/n plateau follow algebraically. Fresh separate Fraction code tested 311 rational parameter instances, all 57,543 enumerated vertices and 35,554 exact contacts, plus 5<=n<=30 phase thresholds; computed 7-blob Git tree matches assigned SHA. This is supporting finite evidence, not the proof for arbitrary n,real tau.

## originality

FAIL

A previously published full theorem on precisely the same K_{n,t} supplies all formulas, quantifiers and contacts. The November 1 Resultary record gives median center and squared radius (Eq. 1), full Boolean/fractional contact classification, all three transition branches and plateau (Eq. 2), and proves them for n>=2,0<=t<=n. With m=q,delta=s,t=tau, the present theorem for n>=3,0<tau<=n is an immediate restriction; its highlighted n=5,tau=8/5 example and 1+s three-phase family follow directly. No surviving independent new statement is present in RESULT.md. This is not just matching a title or parameter; it is exact theorem-level implication from the inspected prior primary text.

## value

FAIL

The geometry is mathematically natural: the minimum enclosing sphere of a symmetrically truncated unit cube, with exact real-cap center, radius, contact orbits and sharp plateau. But in the final submitted claim every such exact fact, including the entire boundary phase classification and illustrative numerical instance, is a previously published consequence of the 2026-11-01 same-body theorem. Reworking a known complete classification without any new domain, invariant, proof technique or unentailed boundary information does not constitute an independently useful new mathematical finding. This is a known-result recomputation, not a rejection because the claim is elementary or because its computations are finite.

The dated certificate retains the supplied scientific assessment, sources and limitations.
