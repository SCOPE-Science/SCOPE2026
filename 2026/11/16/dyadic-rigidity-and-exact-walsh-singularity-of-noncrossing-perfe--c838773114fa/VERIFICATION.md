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

The Catalan number C_n has v2(C_n)=s2(n+1)-1 by Legendre. Expand each independently signed matching weight as product(1-2I_negative_edge). Prescribing r disjoint noncrossing chords splits residual matchings into Catalan products over r+1 complementary regions; the binary digit-sum inequality shows each term (-2)^r*product C_m is divisible by 2^(s2(n+1)-1). At the all-positive signing the exact 2-adic valuation is attained; an odd prime cannot divide all Walsh coefficients, since Walsh inversion over F_p would make the nonzero indicator identically zero. If C_n is odd every signed sum is odd. Otherwise the anti-reflection choice of root-chord signs pairs and cancels terms for even n, and for odd n uses a recursively zero-signed pair of central half-polygons, because (n+1)/2 remains non-dyadic. Vertex switching yields orbits of size 2^(2n-1), since the eligible chord graph is connected K_{n,n}. An independent polygon dynamic program exhaustively checked all frequencies for n<=4 (zero counts n2=8, n4=15104) and reflection witnesses to n=79, distinct from the pinned full checker. Finite checks support, but do not replace, the all-n reflection and valuation proofs.

## originality

PASS

Known Catalan 2-adic valuations and height-dependent weighted Dyck path theorems are credited; the assessed new statement uses all independent polygon chord signings and obtains both exact all-frequency gcd and an if-and-only-if zero classification, which is not a direct corollary of those height-dependent theorems.

## value

PASS

It resolves a natural dichotomy for the entire family of Catalan noncrossing perfect matching codes: when the full Walsh convolution is invertible, when it has a kernel, and a uniform exponential lower bound on that kernel when singular. Exact dyadic gcd and reflection witnesses connect Catalan arithmetic, geometry and Fourier inversion, beyond restating a Catalan parity fact.

The dated certificate retains the supplied scientific assessment, sources and limitations.
