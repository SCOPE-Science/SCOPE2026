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

# Reproducibility and evidence

The proof is in `RESULT.md` and does not rely on numerical extrapolation. The standalone `code/verify_aging_phase.py` compares an exact age-chain propagation with the analytically derived renewal decomposition, checks age-law and waiting-time mass normalizations, and compares large-but-finite no-renewal probabilities with the incomplete Beta limit. On a recent Python installation containing NumPy and SciPy, execute `python -B code/verify_aging_phase.py` from the package root. Its observed result is a JSON object with status `passed` and `finite_assertions` equal to `1147`.

The experiment at \(\gamma=1/2\), \(t=k=4000\) gives persistence \(0.5000397862490525\), versus limiting value \(1/2\). This is only a finite-horizon diagnostic. It does not verify limits for arbitrary \(t\), phases or clocks; the complete proof covers the stated parameter quantifiers. No external independent scientific audit is claimed.
