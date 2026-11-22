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

For every nonconstant real vector x, sorting or nested layer-cake cuts gives sharp (n−1)D(x)≤G(x)≤floor(n²/4)D(x), with singleton and balanced binary cuts saturating. Both induced operator inequalities immediately follow for row-stochastic P on the constant quotient. The Dobrushin row-L1/2 formula holds by optimizing over [0,1]^n. Rank-one P=J+(4n)^{-1}uv^T with zero-sum u,v is strictly positive bistochastic, and its exact δ and γ factor into primal/dual cut seminorms; two explicit choices independently attain c_n and 1/c_n for all n≥2. Independent exact rational binary-cut tests for n=2..8 confirm both families; n4 symmetric positive-semidefinite Laplacian perturbations give γ(B+)=10/3 vs δ(B+)=3 and γ(B−)=7/2 vs δ(B−)=4, yielding both strict orderings, while c_n=1 for n2,3. Finite tests corroborate the all-n proof rather than extrapolate it.

## originality

PASS

Bounded PASS for the dimension-sharp two-sided comparison and constructive saturation under positive doubly stochastic matrices, with opposite rankings within symmetric positive-semidefinite four-state kernels. Dobrushin identity and elementary seminorm equivalence are old; no newness attributed to those premises.

## value

PASS

Sharp equivalence between two natural finite-state Markov contraction metrics matters because Gini measures all-pair signal disagreement while Dobrushin measures worst-pair spread. The sharp loss grows linearly with states despite strictly positive bistochastic mixing, and even reversible PSD Markov chains reverse which coefficient is larger at the first possible size. This structural difference and extremal witnesses provide meaningful dimension-dependent insight beyond copying a textbook seminorm inequality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
