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

Run `python verify.py` with Python 3, NumPy and SciPy. The script independently constructs the full unordered two-hard-core-boson hopping Hamiltonian and the full rate-one symmetric-exclusion generator, rather than populating the proof's reduced block matrix. For every integer \(3\le m\le8\), it directly exponentiates both full matrices at six observation times, checks conservation and compares against the derived formula: **36 quantum and 36 classical comparisons**, with maximum deviations \(9.44	imes10^{-15}\) and \(3.11	imes10^{-15}\), respectively, in the executed environment. It also compares the finite-size asymptotic upper and lower bounds through \(m=16384\) and verifies the classical limit numerically.

The proof for every \(m\ge3\) is the exact incidence matrix/singular-value calculation in RESULT.md. The finite direct-matrix replay is corroboration only. No mathematical independent audit was performed and the program does not certify historical originality or physical robustness.
