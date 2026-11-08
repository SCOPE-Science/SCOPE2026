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

# Reproducible finite checks

Run `python3 verify_conic_torus.py` with the Python 3 standard library. This constructs the exact prime-field conic, builds the restricted additive Fourier matrix in binomial-coefficient form, and independently computes ranks of its action on truncated polynomial modules over \(\mathbb F_p\). For the test primes \(3,5,7,11,13,17\), the observed ranks agree with the Smith-exponent predictions at every checked truncation length through \(\min(p-1,m+1)\). The last line is `CONIC_TORUS_LOCAL_SMITH_PASS`.

The truncated characteristic-\(p\) model agrees with the cyclotomic \(\pi\)-adic quotient only at lengths at most \(p-1\), which is why the checker does not use higher lengths. In particular, for \(p=3\), these modular tests alone do not independently determine the final exponent \(2\). The checker also evaluates the full four-by-four cyclotomic determinant exactly as \(\det F_3=9\), consistent with total \(\pi\)-valuation four and the predicted last exponent. Infinite-prime validity still follows from the symbolic character proof in `RESULT.md`, not extrapolation. No computation attempts to prove nonvanishing for infinitely many primes or check unrelated Fourier minors.

The proof's pivotal steps can be checked directly: the dot product equals the real part of a quotient in the norm-one group; the character basis is invertible because the group order is prime to \(p\); the first nonzero binomial residue occurs at degree \(\min(r,N-r)\); every earlier coefficient has sufficient \(p\)-adic divisibility to preclude cancellation. Together they establish the entire local Smith list. Independent validation has not been performed.
