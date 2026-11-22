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

# Verification and limitations

The all-parameter theorem is proved by a graph-incidence minor bound and a strict finite union bound, not by computational extrapolation. The quantitative steps requiring checking are: every integer minor of a \(k\)-cell row matrix, with at most one appended label-difference row, has absolute value at most \(2^k\); \(\binom{3k}{2}<4^k\) for every integer \(k\ge1\); a primitive element of a free \(\mathbb Z/p^2\)-module is killed by a random linear form with probability \(p^{-2}\); and the same probability holds for two independent forms over \(\mathbb F_p\).

A standalone C++17 checker (`cayley_sparse_check.cpp`) exhaustively enumerates the set partitions of \(3k\) equation-label slots for \(k=1,2,3\). It tests relation and pair-difference augmented ranks at small relevant primes against a modulus \(17\) reference, and verifies addition-chain constructions for selected primes. There are exactly \(5,203,21147\) equality patterns for the respective values of \(k\). This is a finite sanity check, not the general proof.

Compile and run:

```sh
g++ -O2 -std=c++17 cayley_sparse_check.cpp -o cayley_check
./cayley_check
```

Expected terminal marker: `SPARSE_CAYLEY_PRIME_SQUARE_CHECKS_OK`. This was observed in the package-source trial. The paper's original public sequence is limited to orders at most \(23\), and the present theorem does not claim exact \(m(p^2)\) for every prime. There is no independent mathematical audit.
