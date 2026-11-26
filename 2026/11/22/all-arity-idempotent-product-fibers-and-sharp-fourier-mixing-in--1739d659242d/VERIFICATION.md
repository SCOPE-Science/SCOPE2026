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

Squaring determines the idempotents. By multiplicativity of b, the normalized product exponent is the product of b(λ_t−λ_(t+1),i_(t+1)−i_1) over t=1,…,k−1. Indeed the original exponent multiplies consecutive cross-terms and inverse self-terms, and the extra i_1 terms telescope to the normalization. For fixed (i_1,λ_k), the differences reconstruct all λ_t backwards and the shifted indices reconstruct the i_t directly, so the k−1 increments are independent under uniform sampling. Perfection and orthogonality give multiplier |A[j]|/n for χ_j. A character of order r has ker(j)=A[m/r]. Fourier inversion yields the fiber formula with the factor n^(2(k−1)) for the internal choices, as required. The C4 ⊕ C2 example gives 16(64+16c_2(v)+c_4(v)), reproducing all four fibers. A has an element a of order m; by perfection b(a,−) then has order m as a homomorphism to C_m and is surjective. This proves width two (one for idempotents themselves). For r with p-adic valuations α_p, the eigenvalue is the reciprocal of the product of p raised to sum_j max(0,a_pj−a_p+α_p). Each α_p>0 incurs a cost of at least p^(r_p), strictly greater if α_p≥2; using multiple primes also raises the cost. Thus the stated dominant characters and smaller remainder are exact. The endpoints are uniformly distributed and, conditional on each, the same normalized Fourier law holds, so TV equals the cyclic TV. The absolute-value error bound is uniform over the finite state space and the leading coefficient is positive. In fact the minimum p^(r_p) is attained at a unique prime, since nontrivial prime powers of distinct primes cannot tie; the displayed sum is valid and then its coefficient is (p−1)/p.

## originality

PASS

Credit the exact all-arity normalized Rees fibers and sharp total-variation rate in the perfect character-table family, not general Rees theory, the use of character orthogonality or Ramanujan sums, or qualitative semigroup convergence. The inspected rank and matrix-idempotent sources do not displace that claim. The closest general probability paper was available only in abstract, so this is a bounded comparison, not an assertion about everything in its full text.

## value

PASS

The normalization and independent-increment bijection are useful because fixed endpoint products ostensibly share intermediate indices. The exact decomposition makes the entire finite-length product distribution and its rate accessible from torsion data in a natural family, rather than just proving support or asymptotic uniformity. The rate distinguishes even groups of the same order and exponent: C4 ⊕ C4 gives 1/4 while C4 ⊕ C2 ⊕ C2 gives 1/2. This is a concrete use of the sharp invariant beyond the routine invocation of Fourier inversion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
