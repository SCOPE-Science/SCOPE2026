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

Reconstructed the derivative operator by adjoining the hinge w=(x-h)_+ to the affine subspace. With b=1-h, its affine projection is b²/2+β(x-1/2), β=b²(1+2h); the residual v has squared L² norm h³b³/3. If F(t)=∫_t^1 v and A(t)=6t(1-t), the derivative kernels on the left and right cells are A−βF/‖v‖² and A+(1−β)F/‖v‖². This gives the piecewise kernels in RESULT.md:34–43 by integration. For the left row the negative part on the long side beyond (1+2h)/3 has integral 2b²/(9h); the right row is its reflection with h and b swapped. Both have integral one, so taking the larger absolute integral and its kernel-sign derivative gives exactly the attained L∞ result. The squared L² norm is the top eigenvalue of the weighted row Gram matrix; integrating the polynomial pieces gives cross inner product −3(1−2h)²/(20hb), trace 3(1+4hb)/(10hb), and discriminant 9(1−4hb)(1−3hb)/(100h²b²). The adjoint applied to a top eigenvector supplies an admissible extremizing derivative. Both formulas decrease strictly as the mesh approaches balance: for L², write u=hb and observe that 1/u and sqrt((1−4u)(1−3u))/u decrease on (0,1/4]. Substitution verifies both minima and the leading graded constants. The one-cell affine projector has kernel A and fixed seminorm gains (1 and sqrt(6/5)), so it has no grading divergence. In RESULT.md:45 the prefactor for a slope kernel is a difference of coordinate vectors, not scalar hat values; the explicit kernels and proof calculation use that interpretation. Read checker.py and VERIFICATION.md; no uploaded code was executed and no formal verification is claimed.

## originality

PASS

The supported distinction is the exact pair of attained, fixed two-cell derivative-to-derivative norms, with their balanced minima and precise singular-grading behavior. The reviewed indexed statements concern L¹ variation or bounded-input projector/slope norms; broad stability estimates and qualitative instability do not establish these sharp numbers. This is a bounded best-of-knowledge decision, not a priority certification.

## value

PASS

This is the smallest mesh that can isolate grading-dependent instability of the ordinary L² projection. Exact best factors make the comparison quantitative: the Lipschitz seminorm grows as the inverse short-cell length while the Hilbert seminorm grows as its inverse square root. The formulas also give concrete worst inputs and the unique optimal knot. These are useful sharp benchmarks for mesh-dependent stability, not just repetitions of an upper estimate or numerical examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
