---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

An idempotent strict graph endomorphism retracts C_n onto its image, which if proper must be a path of k consecutive cycle vertices. The complement maps to a length n-k+1 nearest-neighbor walk between fixed path endpoints; n placements give e_{n,k}=n(A_k^{n-k+1})_{1,k}. For even n, the two extremal eigenmodes of path adjacency have combined amplitude 4 sin²(pi/(k+1))/(k+1), giving a saddle exponent a j + pi² n/(2j²) at j=(pi²/log2)^{1/3} n^{1/3}. A localized discrete Gaussian Laplace sum yields 16 sqrt(2 pi a s/3)*2^n*n^{1/6} exp(-(3/2)a s n^{1/3}) and centered n^{1/6} rank CLT. Independent exhaustive enumeration of ALL strict endomorphisms via closed +/-1 cycle walks for n=4,6,8,10,12,14,16 exactly matched every rank count and totals 9,25,73,221,685,2157,6881. Odd n gives only automorphism idempotent identity.

## originality

PASS

The finite strict-CYCLE idempotent rank formula and its sharp two-ENDPOINT prefactor were not determined by the inspected prior strict-PATH free-tail convolution or WEAK-cycle lazy walks. Although their cubic-root location and normal scale resemble published path and range-penalized-walk laws, neither exact cycle rank counts nor the sharp prefactor and rarity constant are implied by those other boundary conditions. Best-of-knowledge originality remains provisional due inaccessible 2023 cycle-monoid primary full text.

## value

PASS

Strict cycle graph endomorphisms form a natural finite transformation monoid. Their exact idempotent image-rank enumerator, sharp stretched-exponential total and explicit centered CLT give genuinely useful algebraic and probabilistic invariants (including rare-retraction counts and typical image geometry); unlike an arbitrary small computation, they solve all even n and provide a specific boundary-conditioned prefactor not supplied by the compared path or weak-cycle results.

The dated certificate retains the supplied scientific assessment, sources and limitations.
