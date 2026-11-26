---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

The cascade is stable and its controllability matrix is triangular with determinant product w_i^(n−i). At distinct poles the impulse-response coefficients form a triangular matrix with diagonal gamma_i divided by the preceding pole differences. In the Gramian this matrix multiplies a symmetric Cauchy matrix on both sides. Its squared determinant cancels the Cauchy Vandermonde; continuity extends the formula to repeated poles at μ>0. The closed simplex gives zero determinant only on its boundary, so maximizers are interior. A permutation that moves a higher rate earlier strictly improves the numerator with fixed denominator; exchanging an infinitesimal amount at equal rates has zero denominator derivative and positive numerator derivative in that direction. Under strong damping the denominator divided by (2μ)^(n²) tends uniformly to one, and the strict weighted-log maximizer gives the reported fractions. Under weak damping the descending poles bound the denominator below by 2^n times product λ_i^(2(n−i)+1). In particular μ^(n−1)det W is bounded above by 2^(−n)/(μ+w₁) times product μ/(μ+w_i) for 2≤i<n. For a trial w_i=μc_i, exact factorization gives μ^(n−1)det W= F_n(c)/(2(μ+w₁)) times product of [w₁/(2μ+w₁+w_j)]² over 2≤j≤n, with w_n=0. The positive trial limit forces bounded c_i at optimizers and w₁→S, and this same factorization excludes a zero limiting c_i. Uniform convergence on the resulting compact set and comparison to every fixed ordered trial vector identify all accumulation points. Sorting never decreases F_n, so comparison with ordered trials suffices. In log coordinates log F_n is strictly concave by its diagonal log(2+2 exp y_i) terms, and differentiating gives the displayed stationary equations. This proves the shared limit and coefficient for every optimizing family. At n=3 the equation is c²−2c−4=0, and F_3=c²/[4(1+c)(2+c)²] gives the stated constant. At fixed positive rates only the terminal diagonal factor 2μ vanishes. Proof replay: RESULT.md §§1–6. VERIFICATION.md and verify.py were inspected, not run; its exact recurrence checks the determinant, not weak-limit optimality. The result does not claim finite-μ optimizer uniqueness, and total mass is not conserved in the presence of leakage.

## originality

PASS

The accepted distinct statement is the all-dimension optimal weak-damping allocation and its limiting value on this directed cascade, not the general SISO determinant identity or the generic observation that optimal designs may approach disconnection. An unusually close same-day comparison has the same rescaled leading scalar objective in dimension three, but not the directed chain's general allocation theorem.

## value

PASS

The weak-leakage optimum is singular: it sacrifices all but the first rate on the original budget scale yet maintains controllability and achieves a larger determinant divergence power than every fixed positive design. The theorem identifies the unique downstream profile and coefficient in every dimension and contrasts it with the nonsingular strong-leakage profile. This is materially more than evaluating a known determinant or rescaling the three-node example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
