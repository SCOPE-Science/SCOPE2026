---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

On ℤ, the ordinary heat-kernel difference d_j(u)=p₁(u,j)−p₁(u,j+1) solves a positive irreducible tridiagonal system; off-diagonal positive paths imply d_j(u)>0. For 0<s<1, Bochner positive-stable subordination integrates these strictly decreasing kernels at positive times, giving symmetric strictly unimodal p_s∈ℓ¹. Therefore the ∞→∞ forward-difference norm telescopes to 2p_s(t,0), with the same sign-step extremizer. For 0<a<b≤1, the CDF difference g(y)=F(U^a;y)−F(U^b;y) has the strict sign − on 0<y<1 and + on 1<y<4^b. Integrating by parts yields Δp=t∫e^(−ty)g(y)dy. H=e^tΔp/t has H′=−∫(y−1)e^(−t(y−1))g(y)dy<0; H(0)=m(b)−m(a)>0 from strict convexity of m(s)=E(U^s), m′(0)=E log U=0; H→−∞ from the strictly negative y<1 interval. There is one simple positive zero and the stated reversal. Beta identity and Laplace saddle rescaling give displayed short- and long-time coefficients. Analytic positivity and derivative signs establish all times/orders; finite evaluations do not.

## originality

PASS

Sharp ordinary lattice heat kernel and fractional diffusion estimates precede this record, but none of the inspected statements gives the common ∞→∞ step extremizer together with an all-pairs unique reversal of the norm ordering across fractional orders. Both operator-norm direction and different-order quantifiers matter. Existing fixed-order decay estimates do not imply the global one-crossing Laplace comparison.

## value

PASS

Identifies the exact worst-case rough-input smoothing norm for every order with one extremizer, and proves a surprising global reversal: no fractional power dominates another in sharp gradient smoothing at every time. This is not a routine rate estimate; the strict one-crossing classification removes ambiguity among a continuum of diffusion orders on a natural lattice model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
