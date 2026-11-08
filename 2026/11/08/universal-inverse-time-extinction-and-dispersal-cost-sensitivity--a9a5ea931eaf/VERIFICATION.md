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

The exact theorem is reconstructed in `RESULT.md` using a strict Perron-weighted Lyapunov decrement, contraction of non-Perron modes, and scalar reciprocal asymptotics. The standalone source `verify.py` uses only the Python standard library.

From the folder containing this package, run `python3 verify.py`; a successful run ends in `VERIFY_OK`. It checks the two-patch critical linear matrix, the exact coefficients \(\alpha=1/2\) and \(\alpha=5/4\), and the exact amplitude ratio \(2/5\). It also confirms a heterogeneous three-patch rational Perron calculation with a strictly positive cost derivative and compares the rational nonlinear map with the second-order expansion on 1,755 components over two-, three- and four-patch systems, and checks illustrative 180,000-step trajectories against their predicted amplitudes.

These calculations are finite corroboration. They do not prove the universal limit, do not certify convergence bounds for arbitrary parameters, and do not replace the analytical argument. Independent external assessment has not been performed.
