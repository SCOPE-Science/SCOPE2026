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

# Reproduction and scope
Run `python3 verify.py` from the directory containing this document. Python 3 standard library only; exact nonnegative integer combinatorics, arbitrary-precision integers, and integer comparisons are used. The program terminates after complete bounded loops in all parameter pairs \(p,q\ge1\) with \(p+q\le17\), plus \(p=14\), \(q=2,3,4,5\). The exact Eulerian recurrence, binomial-basis conversion, and direct lattice-slice count are implemented separately.

The verified execution printed four `PASS` lines for 120 positive cases through dimension 17, two and only two exceptions in dimension 18, reentrance for the fixed cube, and 1,982 coefficient signs with 2,122 independent direct-count equalities. Rational witnesses are asserted via exact factorial cross-multiplication. No floating-point operations or random tests are used.

This is a complete computation for the finite range in the theorem, not a proof of any unbounded sign assertion. Source coverage is provisional because the directly motivating 2026 article was available only as an abstract. No independent audit or human verification was performed.
