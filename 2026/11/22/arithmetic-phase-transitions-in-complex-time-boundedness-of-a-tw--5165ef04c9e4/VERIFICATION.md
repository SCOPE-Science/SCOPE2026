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

## Analytic verification
The Hermite polynomial core is dense in the stated \(L^p\) space. Necessity and sufficiency of the operator-domain condition follow separately from one-dimensional Epperson boundedness and product factorization. The uniform-distribution argument requires irrationality of the ratio, not merely distinct rates. The small-time rational formula requires the explicit zero-separation inequality stated in the proof. The exact cross-section transition holds only for irrational ratios in the form asserted. The proof does not claim a uniform discrepancy bound over finite imaginary-time windows.

## Finite diagnostics
`check_geometry.py` independently sampled the two simultaneous sine constraints at three positive horizontal coordinates with rates \(1,\sqrt2\), using \(1{,}200{,}000\) midpoint samples on \([0,10000]\). It compared observed fractions with the stated product-Haar formula. For commensurate pairs \((m,n)=(2,3),(1,1),(3,5)\), it sampled one period at two small horizontal coordinates using \(500{,}000\) midpoint samples and checked the exact common-zero formula. Executed output ended in `GEOMETRY_DIAGNOSTICS_OK`. These are numerical finite tests of the formulas; neither they nor their tolerances prove equidistribution or exhaustive correctness.

## Scope of certification
Self-review: passed. Independent audit: not yet performed. The work has no externally supplied proof certificate.
