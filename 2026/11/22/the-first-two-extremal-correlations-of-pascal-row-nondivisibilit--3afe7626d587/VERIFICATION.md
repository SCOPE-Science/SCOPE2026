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

# Verification and scientific limits

The proof in `RESULT.md` derives the universal assertion from the digit identity and an exact two-case base-\(p\) carry convolution. The crucial symbolic identities have integer-polynomial numerators whose signs are proved for all primes \(p\ge3\). In particular, the single-digit comparison polynomial \(E_p(a)\) decreases as \(a\) increases and satisfies \(E_p(p-1)=p-2>0\), and a nonzero digit above the units place gives a strict correlation gap below the second tier.

Run `python check.py` with the Python 3 standard library. The checker independently builds Pascal rows modulo each of \(p=3,5,7,11\), checks the Lucas/Fine digit count, computes exact cyclic mixed moments by direct finite summation and by the carry recursion, and checks rational shift rankings. Its successful comparison covers 2,000 one-row checks, 444 cyclic-moment shift checks, and 2,296 shift-bound checks. These are finite consistency tests; the universal theorem rests on the proof, not empirical extrapolation.

The conclusion is about fixed shifts under cyclic sampling modulo \(p^L\). It does not imply a finite-\(L\) extremal statement, an error estimate uniform in a growing displacement, or independence of row counts. Literature originality is conditional on the inspected texts; external independent review is not performed.
