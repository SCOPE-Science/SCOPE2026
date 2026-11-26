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

On the active 2×2 block J, the eigenvalues of JᵀJ give largest singular value (t+√(t²+4ρ²))/2, strictly less than one exactly when t+ρ²<1. The error matrix for U is S² since S annihilates e₁. For Vθ the complementary projector is zzᵀ with z=(0,−sinθ,cosθ), and the rank-one product (Sz)(zᵀS) has characteristic polynomial λ²(λ−zᵀS²z). Its spectral radius is ρ|ρ−q| for q=t sin(2θ), compared with ρ². The comparison is strict deterioration iff q>2ρ, improvement iff 0<q<2ρ, equality at q=0 or 2ρ. The maximum attainable q=t gives exactly the stated existence criterion. At θ=π/4 the ratio |1−t/ρ| diverges at fixed 0<t<1 even as both radii tend to zero. The enriched norm there is the product of the two rank-one vector norms, (ρ²+(t−ρ)²)/2; the original norm follows from the singular value of the block with diagonal ρ² and shear 2ρt. Dimension three is necessary for strict nesting of nonzero proper subspaces. An independent exact matrix/characteristic check including the stated numerical witness passed; replay with python3 /workspace/audit_checks.py 1.

## originality

PASS

The supported distinct claim is the exact orthogonal-nesting threshold and unbounded relative spectral penalty for the specified contractive same-smoother two-grid family. General nonnormal spectral pathologies and the Galerkin error-map formalism are not new. The closest located literature counterexample uses nonorthogonal projectors and a norm, not this spectral comparison with orthogonal corrections.

## value

PASS

It tests whether increasing a Galerkin space helps asymptotic convergence when even the unpaired smoother is a strict contraction and all corrections are orthogonal. The minimal-dimensional counterexample separates same-smoother from adjoint-paired schemes and gives a finite threshold identifying exactly when monotonicity fails, plus an unbounded relative effect. Neither a generic nonnormal transient warning nor a counterexample with oblique projection answers that question.

The dated certificate retains the supplied scientific assessment, sources and limitations.
