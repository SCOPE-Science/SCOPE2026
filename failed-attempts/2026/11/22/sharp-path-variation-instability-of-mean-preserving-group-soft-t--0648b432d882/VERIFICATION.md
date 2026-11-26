---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Pass for the frozen theorem. On the centered space, for r>λ the derivative is (1−λ/r)I+(λ/r)uuᵀ, with u the unit centered radial direction; for r<λ it is zero. A nonconstant centered line intersects the sphere in at most two points, so piecewise integration and directional quotients as r decreases to λ identify the sharp coefficient with the maximal rank-one norm. In path differences, the norm of uuᵀ is V(u) max_j |uᵀb_j|, where b_j is a centered cut step. Writing V(u) as the maximum of (Dᵀσ)ᵀu, the rank-two Rayleigh calculation gives (||Dᵀσ||₂||b_j||₂+|(Dᵀσ)ᵀb_j|)/2. The inner product has magnitude one; alternating signs maximize the first squared norm at 4n−6 and a middle cut gives the second at floor(n²/4)/n. Their simultaneous maximizer gives the stated coefficient and a norming direction. For n≥3 every differentiable point of a nonconstant centered segment has derivative norm strictly below the coefficient; integration is strict for each finite positive-denominator pair, while perturbations by the cut step just outside the sphere approach equality. A same-sign exterior ray attains one in n=2 and at λ=0 the map is the identity. Centering and radial scaling give the one-input bound; Euclidean nonexpansivity follows from the stated convex proximal representation. Expanding the root gives n/2+1/8+O(1/n). Independent replay in branches/0941b798-12a2-427e-a36c-93ad058cfe5f/independent_finite_check.py enumerated signs and cuts through n=9 and reproduced near-sphere witnesses; those checks support the arithmetic, not the general proof.

## originality

FAIL

A distinct indexed record, 1111820a6506, states the identical operator and seminorm, sharp formula for the same n and threshold ranges, limiting direction and nonattainment, boundary cases, asymptotics, and one-input and Euclidean bounds. The explicit proof already uses the same rank-one reduction and alternating-sign middle-cut optimization. This is demonstrable statement-level equivalence; it does not rely on inferring creation order from path dates or on lack of access to any other paper.

## value

FAIL

The known theorem itself is useful: it distinguishes one-input diminution from two-input amplification and gives a nonattained sharp constant. The frozen record supplies no independently new mathematical fact or stronger outcome beyond the already available coefficient, witnesses, and proof, so it does not add a valuable surviving contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
