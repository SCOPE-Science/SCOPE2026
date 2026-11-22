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

# Verification of local translated-cusp congruence counts

The standalone standard-library program `check_counts.py` checks the claimed prime-power counts by substituting candidate residues into **both original polynomials**. It covers 71 prime-power cases, including powers of two through \(2^{16}\), three through \(3^{11}\), and multiple odd primes through their stated ranges. A second direct all-pairs loop independently checks 29 small prime-power cases and 19 composite CRT cases, all passed.

The code uses no symbolic results from the proof other than the prediction function. Complete enumeration validates only the finite listed cases; it does not prove the uniform formula. The proof's nonstandard cases are the double-root count, the ternary \(3\)-adic splitting at valuation two, and the binary parity split. Each is reconstructed in the proof, including all low-power boundaries.

The limiting-distribution theorem is an application of an existing published theorem [1], not independently reproved. The original polynomials are coprime over \(\mathbb Q[x,y]\) because their difference is linear in \(x\) but the substituted first polynomial remains a nonzero quartic. The limiting GCD's first-level prime factors are summable, so the Euler product is positive; the local moment threshold is \(3/2\), while the global moment threshold is \(1\). No claim about convergence of finite-box expectations is made.

References: [1] https://arxiv.org/html/2311.05369v1, Theorem 3.1. [2] https://arxiv.org/html/2105.13883v3, Sections 1 and 6.
