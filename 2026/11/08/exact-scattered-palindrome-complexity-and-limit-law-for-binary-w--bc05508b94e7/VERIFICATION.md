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

# Verification steps and limits

Run `python3 verify.py` using Python 3. The script uses no external packages. Its first algorithm enumerates distinct subsequences by a set recurrence and then tests palindrome identity; it does not use the mathematical gap formula to generate its expected count. This check traverses all 3,876 words with exactly three ones and length 3–18, including zero-length boundary gaps. Output: `GAP_FORMULA_OK 3876`.

The second check independently evaluates finite rational combinations of elementary exponential-integral identities, including the two-domain integral for \(\mathbb E[e^{-B}C\min(B,C)]\). Output: `RATIONAL_MOMENTS_OK 7/80 2299/1209600`. The source proof supplies the four zero/one-count cases, the Dirichlet convergence argument and the mixed moment integration.

The finite enumeration is not exhaustive over all lengths. Rational-arithmetic checks alone cannot establish the probability limit; that relies on the stated exact formula, uniform lattice composition convergence, and independence of normalized exponential coordinates from their sum.
