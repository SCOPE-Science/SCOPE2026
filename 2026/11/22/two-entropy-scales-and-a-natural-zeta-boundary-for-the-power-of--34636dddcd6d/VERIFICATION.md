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
# Mathematical verification record

Run `python3 verify.py` using only Python standard libraries. The program checks the even-language Fibonacci count for lengths 0–14 and the complete list of cyclic ternary words of periods 1–10 against the marked-code logarithmic zeta formula. It uses exact rational comparisons to prove \(221/500<r<443/1000\) from a finite sum and a rigorously bounded remaining tail. The output is recorded verbatim in `verification_output.txt`.

The general periodic-orbit identity is proved by marker decomposition. The exact natural boundary is proved analytically from Binet's formula and dense non-polar singularities of \(\sum_{j\ge0}t^{2^j}\) at dyadic roots of unity; testing finitely many coefficients cannot verify an analytic natural boundary. The cited entropy identity was available in the previous literature, and is independently justified by a word-count upper bound plus periodic growth. The full historical-priority audit of abstract renewal-system zeta literature and independent validation remain unperformed.
