---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

## Reproducible checks

Run `python3 verify.py` using Python 3 and its standard library. The script gives three independent families of finite checks:

- Directly enumerate every self-map on sets of one through six vertices, construct the cyclic set from the functional digraph, aggregate counts by exact mask, and compare every Walsh multiplier with the independent rooted-forest/Krawtchouk formula.
- Verify exact valuations and the explicit normalized modulus identities for each of 46 odd-prime-power dimensions up to 169, considering every possible Hamming weight.
- Independently construct and eliminate the complete convolution matrices modulo the relevant prime for dimensions three, five, and seven; the observed ranks are respectively \(6\), \(30\), and \(126\).

The supplied run passed **7,435 exact assertions**. Integer arithmetic is used throughout; no stochastic approximations, unverified numeric sign decisions or floating-point certificates are used. The finite cutoff is a reproducibility bound, not an infinite theorem. The all-size justification is the arithmetic proof in `RESULT.md`, including the local Walsh diagonalization argument.

## Scope and limits

These checks do not determine Smith factors at primes other than the prime underlying the vertex-count power. Independent mathematical audit has not been performed.
