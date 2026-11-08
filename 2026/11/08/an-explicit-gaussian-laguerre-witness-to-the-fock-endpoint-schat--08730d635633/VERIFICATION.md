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

Run `python3 CHECK.py` from the directory holding the packaged files. With the Python standard library this prints `GAUSSIAN_LAGUERRE_MOMENTS_EXACT_OK 3160`.

The assertions use exact fractions, factorials and binomial coefficients for the explicit Laguerre gamma moments at integer ranks \(2\le N\le16\). They check the first \(N+10\) diagonal entries for each rank block, the heat value at zero, the parity prefix, and the rational trace-error and heat-peak inequalities. These checks corroborate formula transcription and small cases; the proof in `RESULT.md` supplies the all-ranks estimates and convergence arguments.

The infinite symbol is specified by a closed formula with \(N_j=2^{j^2}\), \(t_j=N_j^{-4}\), \(b_j=j/N_j\), and \(w_j=2^{N_j^3}\). Its huge separation is theoretical rather than a numerically practical plot prescription. The trace-class exclusion uses the published endpoint estimate, whereas the \(p>1\) membership is established directly by a summable series of Schatten-norm bounds.

Scientific publication priority and independent mathematical audit remain unverified.
