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

The included `verify_waveform.py` runs with Python 3 standard library only. From the package directory run `python3 verify_waveform.py`; the recorded output is `verification_output.txt`.

The integer recurrence reproduces the first ten values of the published power-scale Abelian complexity. A separate brute-force oracle enumerates all windows of length \(4^m\) inside the nine ordered pairs of \(m\)-substitution blocks for every \(0\le m\le5\), which covers all factors at these lengths because all nine pairs occur. This verifies 54 individual block-pair contexts and their combined extrema.

For the third centered moment, the script uses 16,384 deterministic midpoint phases, a 24-term \(\sqrt7\)-geometric waveform, 60-decimal arithmetic, Machin's arctangent identity for \(\pi\), an alternating arctangent series for \(\theta\), and a 20-term Taylor polynomial for cosine after reducing angles. The analytic Lipschitz quadrature and uniform-tail errors together are under \(1.0499\cdot10^{-5}\); a conservatively allowed additional numerical error of \(10^{-15}\) is included. The resulting interval is entirely negative. The infinite empirical convergence and exact moment series are proved in RESULT.md and not inferred from finite samples.

No independent scientific audit has been performed.
