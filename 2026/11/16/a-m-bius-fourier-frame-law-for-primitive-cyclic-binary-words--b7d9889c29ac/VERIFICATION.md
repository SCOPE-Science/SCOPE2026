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

Pointwise period Mobius identity 1_primitive=sum_{q|n}mu(q)1_period_divides(n/q) gives exact N_n and coordinate covariance: for period dividing n/q, coordinate product sums 2^(n/q) if positions coincide mod n/q, otherwise zero. This circulant matrix diagonalizes in spatial DFT: B_{n/q} acts with scalar q iff q|k. Global sign-flip kills all constant-to-coordinate correlations. To show extrema, F_n(S)-F_n(S union {p})=p H(T,m), T=n/p, m=prod primes S, and H(T,m) equals (1/T) sum over words excluding periods T/r (r|m) of the square of their coordinate sum. It is nonnegative, strictly positive when T>=3 by one-negative-coordinate primitive witness, positive T=1, and for T=2 is zero only at m=2. This yields unique equality when n=2p odd prime, S={2}, adding p. For n>=3 the one-negative word gives H_n>0; trace n of normalized coordinate Gram and maximum 2^n/N_n>1 place constant eigenvalue 1 between coordinate extremes. n=2p Mobius cancellation gives exact closed form. Bound 2^n-H_n<=n^2 2^(n/2) implies exponential tightness. Direct independent enumeration at composite n=4,6,8,9,10 confirmed exact Mobius Gram and spatial DFT eigenvalues; source checker directly enumerates through n13 and exact subset inequalities through n200, but all-n proof uses squared-sum identity.

## originality

PASS

Primitive-cycle covariance differs from one-color-binary surjective words for composite n: the latter only exclude constant words and have full position-permutation symmetry, while true primitive words exclude every proper-period pattern and possess only cyclic symmetry. Exact composite Fourier bands and twice-odd-prime degeneracy are not supplied by the compared surjective-word theorem.

## value

PASS

Complete eigenvalues of a natural signal-restriction frame on indexed primitive necklaces, a sharp conditioning formula and a non-obvious arithmetic equality mechanism n=2p are useful structural invariants. Not a mere Mobius necklace count: the position-dependent Gram spectrum is an additional new operator fact.

The dated certificate retains the supplied scientific assessment, sources and limitations.
