---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Orthogonal bimedian decomposition yields the four sign-pattern vertices (±a,±b,±c) with even minus parity. A central Haar plane generically separates vertices 1+3 or 2+2; spherical sign correlation E(sgn(u·v_i)sgn(u·v_j))=1-2θ_ij/π yields q=3-(4/π)Σarcsin√p_i. Fix t=max p_i and split p2+p3=1-t under p2,p3≤t. Strict concavity of f(x)=arcsin√x for x<1/2 makes the minimum q occur at p2=p3=(1-t)/2 and the maximal q at (t,1-2t) for t<1/2, else approach p3→0 giving q→1. The inverse intervals and t=1/2 geometry follow. Independently simulated 240,000 Haar normals over three shapes and checked 1,200 random conditional triples; analytic proof, not sampling, establishes the continuum theorem.

## originality

FAIL

The earlier November 2 complete SCOPE theorem on the SAME nondegenerate equifacial tetrahedra and Haar CENTRAL planes already gives exactly q(p)=3-(4/π)Σarcsin√p_i and proves global STRICT SCHUR-CONVEXITY of q on the three-part simplex. At fixed t=max p_i, the vector (t,(1-t)/2,(1-t)/2) is majorized by every feasible p, while for t<1/2 the vector (t,t,1-2t) majorizes every feasible p; for t≥1/2 the boundary vector (t,1-t,0) is the majorization maximal closure point. Evaluating the old q formula on these majorization extremes gives precisely Q_-, Q_+, the t=1/2 transition, the nonattained supremum and inverse intervals. This is direct known Schur-ordering coverage under the identical geometry and probability measure, even though the earlier paper did not print Q_±.

## value

FAIL

The fixed-maximum parameter t is natural and the exact interval is correct, but after the prior complete Schur-ordering theorem the optimization is an immediate one-dimensional majorization corollary with no new structural lemma, unknown exact invariant or nontrivial classification. The t=1/2 switch is the endpoint of the obvious p2≤t constraint; it supplies no independent mathematical advance. Finite Monte Carlo checks and a different restatement of inverse bounds do not rescue it.

The dated certificate retains the supplied scientific assessment, sources and limitations.
