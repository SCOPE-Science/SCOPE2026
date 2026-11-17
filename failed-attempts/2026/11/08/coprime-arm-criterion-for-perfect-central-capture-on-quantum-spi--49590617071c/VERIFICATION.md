---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-14.md",
      "INDEPENDENT_AUDIT_2026-11-14.json"
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

The finite-dimensional non-Hermitian generator has purely surviving modes precisely in the Hermitian adjacency eigenspaces with zero hub amplitude; the invariant complement is strictly dissipative. Each open Dirichlet path arm has sine eigenmodes at 2J cos(πk/L_i). Equal energies mean equal reduced fractions a/b; each b divides exactly m_b arm lengths, and the hub junction constraint removes a single weighted coefficient direction. Consequently multiplicity per primitive fraction is (m_b−1)_+, giving the totient sum, gcd criterion and rank-one-complement projector with diagonal sine² sitewise survival. The source verify_arithmetic.py derives exact integer Krylov ranks, and verify_projector.py reconstructs eigenspace projectors for 145 graphs; an independent new exact Krylov check on augmented lengths (2,3,5), (2,3,6), (2,2,2) yielded dark dimensions 0,3,2, respectively. Finite numerics are corroboration only; the all-length theorem is analytic.

## originality

FAIL

DECISIVE PRIOR COVERAGE: an already published October 13 Resultary/SCOPE finding states the identical all-spider totient dark dimension, pairwise-coprime complete-capture condition, arbitrary-state survival and exactly equivalent sitewise Ramanujan-sum formula. Original arm notation counts edges ℓ_i and uses n_i=ℓ_i+1; current L_i is this same n_i. The original absorber K=JA−iγΠ and current JA+εI−iγΠ/2 differ only by harmless γ rescaling and common phase. Two sin² sum equals φ(b)−c_b(h), making site laws algebraically identical. Later October 18 and November 2 publications additionally cover or strengthen site-selective absorption. The final claim cannot pass originality, and disclaimers/certificates are not repairs.

## value

FAIL

FAIL as a new contribution: although the spectral/coprimality theorem is a natural and useful mathematical-physics fact, the complete dimension, capture classification and site probability are already published at equal generality. The package adds no motivated uncaptured invariant, stronger result or other scientifically useful distinction; repeating a known exact theorem and rewriting Ramanujan sums is not a new valuable result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
