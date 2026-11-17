---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-08.md",
      "INDEPENDENT_AUDIT_2026-11-08.json"
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

For x∈c0 with sup norm M and t scalar, ||T(x,t)||_p^p<= (2^p+1)M^p <=(2^p+1)||(x,t)||_p^p. Finite vectors +1 on indices 0..N and -1 at N+1 give ||Dx||∞=2 and Σa_nx_n→1, proving exact norm; bidual acts with identical coordinate formulas on ℓ∞⊕_p R. Equality forces t=0, ||Dx||∞=2 and |Σa_n x_n|=1. Positivity makes all positive-weight coordinates equal a common sign of modulus 1. For full support bounded x is constant on every index, so cannot have ||Dx||∞=2; if a_k=0, flip x_k in ℓ∞ to realize bidual norm. If support is infinite, no c0 vector can have |Σa_n x_n|=1; if finite, a finite sign-reversal beyond support realizes both. Endpoint p=∞ is max{2,1}=2 and X∞ isometric c0; distortion 2^(1/p)→1. Independent direct equality reasoning covers p=1 and arbitrary infinite support; code is finite diagnostic only.

## originality

PASS

PASS best-of-knowledge for exact all-support trichotomy and explicit counterexample with renorming distortion arbitrarily close to one. Prior primary Theorems 3.3 and 5.1 give respectively the isometric c0 endpoint and existence of some renorming failure but do not imply the quantitative near-isometric boundary and exact operator classification. Other published support-pattern examples for different norms/operators do not alone imply this claim.

## value

PASS

The phenomenon sharply tests stability of second-adjoint norm attainment: any nonzero finite distortion from c0 can destroy a property universal at the exact c0 norm, and the support trichotomy separates original/bidual outcomes. Although elementary in technique, these are motivated structural boundary cases and exact formulas for a natural scalar-extension operator, not arbitrary finite computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
