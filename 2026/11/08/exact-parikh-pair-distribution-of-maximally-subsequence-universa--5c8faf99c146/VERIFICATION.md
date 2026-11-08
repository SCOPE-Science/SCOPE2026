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

# Verification

The exact formula follows from the unique greedy arch factorization of words with exactly \(k\) letters \(b\) and index \(k\), and from counting scattered \(ab\) pairs in each arch. Check first the arch criterion and the forced one-\(b\)-per-arch classification. For the \(i\)-th arch, the independent choices are \(ba\) or \(a^{u+1}b\) with \(u\ge0\). Verify that an extra \(a\) in the latter contributes \(k-i+1\) pairs; extract the coefficient of \(z^r\). The reciprocal symmetry follows by reversing words and the \(a\)/\(b\) multiplicities are preserved. The claimed low-degree coefficients can be recomputed directly from the first terms of \(\prod_{j=1}^k(1+q/(1-zq^j))\).

Run `python3 checker.py` in the directory containing the supplied standalone script and the other extracted files. This uses no external dependencies. It directly enumerates words with the stated content, independently tests every target subsequence, and compares the histogram to the formal-product calculation. One successful replay printed:

```
PASS: 25 independent parameter cases, 6441 enumerated binary words, 25 unweighted totals, 250 reciprocal coefficients, 80 edge coefficients
PASS: k=4, r=1, C=6..14: [1, 4, 7, 8, 8, 8, 7, 4, 1]
```

Finite enumeration does not establish the theorem for all \(k,r\); the finite tests are checks of the derived proof. The theorem does not cover both letter multiplicities strictly greater than \(k\), does not prove bit-complexity for large binary-encoded parameters, and does not establish historical priority. No independent mathematical review was performed.
