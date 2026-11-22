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
# Reproducibility and limits

Run `python3 verify_heawood.py` (Python 3 standard library). The input graph is built from the seven lines \(L_j=\{j,j+1,j+3\}\pmod7\). The code verifies the Fano incidence Gram identity, independently calculates ranks over exact rational numbers and modulo \(101\), exhausts the \(3,003\) six-absorber placements, checks the geometric characterization of all \(21\) rank-five sets, and enumerates the seven-, eight-, and nine-detector thresholds. The universal threshold additionally has a separate all-real-vector support proof in `RESULT.md`; enumeration of finite configurations is used only for the exact finite counts. Positive but otherwise arbitrary detector rates are handled analytically by the dissipative eigenvector characterization, not by sampling rates. Historical-priority certification and independent audit have not been performed.
