---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

PASS. The exact generator for a distinct pair of spins under unit per-vertex neighbor copying and rate-mu fair reset produces (1+mu)u=w for both same-part classes and [1/a+1/b]+(2-1/a-1/b)u=2(1+mu)w for a cross-part pair. Solving gives u=(1/a+1/b)/(1/a+1/b+2mu(2+mu)); w=(1+mu)u. Expanding M² across N diagonal spins and a(a-1)+b(b-1),2ab pairs gives submitted variance. Direct symbolic substitution independently confirms equality with the Oct 18 published variance under spontaneous flip rate eta=mu/2. Differentiating the rational expression in P=ab at fixed N is negative for N>=2; with H=ab/N comparable to min(a,b), bounded spins imply convergence in probability M→0 iff min(a,b)→infinity, while fixed m yields 1/[1+2mu(2+mu)m]. The full-state verifier's 48 small stationary laws are corroborative, not a proof of all sizes.

## originality

FAIL

Two earlier published mathematically equivalent or stronger theorems explicitly cover this exact finite model. Oct 18 2026 Resultary theorem for vertex-clock noisy copying on K_{a,b} with spontaneous spin flip eta gives SAME exact unweighted population variance and fixed-minority limit; fair resampling at rate mu is precisely spin flip at eta=mu/2. Independent SymPy simplification verifies the submitted variance minus earlier V_V formula is identically ZERO for symbolic a,b,mu. Nov 2 2026 Resultary theorem uses EXACT fair-reset theta=mu and explicitly displays the same u_same, w_cross pair correlations for all a,b>=2, plus stronger critical Beta–Gaussian law. Submitted monotone-in-ab and iff-minimum-branch-diverges criteria follow by direct differentiation and bounding from these exact earlier formulas, so unmentioned consequence wording cannot make it original.

## value

FAIL

The stationary noise scaling on imbalanced bipartite graphs is a natural quantity, but the submitted all-size formula, cross-versus-within correlation, and fixed-core positive limiting variance were published earlier; its balancing extremizers and if-and-only-if self-averaging criterion are immediate algebraic consequences of that identical expression. No independently motivated new invariant remains to support scientific value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
