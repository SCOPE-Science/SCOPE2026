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

# Reproducibility and verification

The accompanying standalone `verify.py` is runnable as `python3 verify.py` without dependencies beyond the Python 3 standard library. It uses the original \(n^3\) polynomial constraints for every matrix, independently reconstructs support-block normality, evaluates linear ranks and the three-variable strong identity, and checks \(R^2=0\). It also checks equality of the Stirling and inclusion–exclusion formulas and the square-zero counting specialization.

Cases exhaustively checked: \((q,n)=(2,2),(3,1),(3,2),(3,3),(5,2),(9,2)\). The extension field in the last case is represented by \(\mathbb F_3[t]/(t^2+1)\), with all arithmetic explicitly implemented. Successful terminal marker: `VERIFY_ANTI_RB_COORDINATE_PARTITIONS_OK`. For \(q=3,n=3\), the resulting rank multiplicities are \((1,56,60,8)\); for \(q=9,n=2\), they are \((1,96,64)\).

These finite experiments are exhaustive only at the specified parameter pairs. The general arbitrary-field classification and generating functions are proved symbolically in RESULT.md; neither external independent audit nor an infinite formal certificate is represented.
