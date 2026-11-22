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

# Verification of the exact NOR orbit census

The claim applies to simple circular ladders with \(n\ge3\), binary states, simultaneous open-neighborhood NOR, and **no** self inputs. The proof is in `RESULT.md`; its critical nonstandard step is the odd-rung graph-cover isomorphism, given by a two-modulus coordinate map and independently checked by the direct cover enumerator in `check_transfer.py`.

Run `python3 check_dynamics.py` and `python3 check_transfer.py` from the extracted file directory. The first reconstructs graph adjacencies independently and examines all \(87{,}360\) states over sizes three through eight, including the one-update recurrence identity. The second constructs the ordered-pair transfer, optionally verifies its nine-by-nine characteristic polynomial with SymPy, matches closed trace formulas for \(n=3,\ldots,30\), enumerates cyclic words through \(n=9\), enumerates prism maximal independent sets through \(n=8\), and enumerates cover maximal independent sets through \(n=5\). The programs were executed successfully before package creation.

Expected printed rows for \(n=3,4,5,6,7,8\) are, respectively, `prism 3 6 20 7 64`, `prism 4 6 36 15 256`, `prism 5 10 122 56 1024`, `prism 6 20 400 190 4096`, `prism 7 28 842 407 16384`, and `prism 8 46 2116 1035 65536`.

The determinant identity, cover isomorphism, and polarity argument are finite algebraic/combinatorial reasoning, not inferences from numerical data. Unverified matters include a definitive historical novelty search and independent external audit. Computational checks are bounded to the stated finite sizes, not exhaustive over all \(n\).
