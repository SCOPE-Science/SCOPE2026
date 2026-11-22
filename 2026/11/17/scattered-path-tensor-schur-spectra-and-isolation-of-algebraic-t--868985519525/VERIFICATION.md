---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

The Schur norm formula for the main/upper diagonal mask is Levene 2014 Theorem 4.2, namely sigma_k=2/(k+1)cot(pi/[2(k+1)]) increasing to c=4/pi by Corollary 4.6. Exact multiplicativity under Kronecker products and supremum for Hilbert block-diagonal sums make the finite block norms a multiplicative monoid P, and bounded countable sums yield exactly bounded suprema of P. Let F={sigma_k:k>=2} union {c}; sigma_2=2/sqrt(3)>1 bounds the number of factors in any bounded product sequence, so compactness of F proves closure P equals all finite F-products and also equals union_m c^m P. For an accumulation point of this set, a sequence of distinct products with bounded factor number must have at least one factor tending to the only nonisolated element c, so S prime equals c S; conversely sigma_k p -> c p with distinct values. Repeated positive rescaling gives S^(m)=c^m S, and S^(omega) empty because each element of c^m S is at least c^m -> infinity. Each sigma_k is algebraic (cyclotomic cotangent) while c transcendental; c^m p cannot coincide with c^n q when m!=n and p,q positive algebraic, giving exact rank m, and no algebraic accumulation points, including at 2. This derivation is exhaustive and does not rely on a finite near-2 experiment.

## originality

PASS

Levene 2014 supplies sigma_k and 4/pi, Levene 2026 supplies tensor/supremum closure for the full uncountable Schur spectrum and notes near-2 products. The audited narrower family generated solely by finite path masks has a countable closed scattered spectrum, exact Cantor--Bendixson ranks and isolated algebraic thresholds, which are not implications stated in the inspected papers without the additional bounded-factor compactness/derived-set argument. An abstract general theorem about products of isolated convergent sequences could subsume the topological portion, a residual priority risk.

## value

PASS

The restricted path-generated norm family is mathematically natural because these are the explicit calculable nontrivial Schur idempotents and tensor/direct-sum are canonical operator constructions. A complete topological spectrum classification and algebraic isolation contrast with an unresolved accumulation question in the much larger full spectrum; the exact Cantor--Bendixson rank of every point is a useful structural invariant, not a mere near-numeric example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
