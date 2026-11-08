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
# Reproducible checks and limits

The proof in `RESULT.md` applies to all integer \(n\ge2\), and the cubic result to \(n\ge3\). No external or independent verification has been performed.

From the directory containing the seven files, execute `python CHECK.py` using Python 3 standard library only. On the packaged reviewed program the actual outcome was `CHECK_OK assertions=70325`.

The program independently enumerates all pairs of shells and performs exact rational moment checks for every dimension \(2\le n\le100\). For dimensions \(2\le n\le10\), it constructs every vector in each shell and computes every entry of every two-shell Gram matrix directly; third-order coefficients are checked where relevant. It also checks the critical paired-ratio polynomial identity for divisors up to dimension 600. All calculations use exact integers/Fractions. The unbounded mathematical conclusion rests on the written ratio argument and not on the finite test range. No computation of a numerical eigenvalue is needed for the analytic spectrum.
