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

The complete analytic proof is in `RESULT.md`; it establishes all quantifiers and equality cases. `checker.py` is a standalone, standard-library-only Python 3 supplement. Run `python3 checker.py` after extracting it and `RESULT.md` into the same directory.

The checker independently evaluates the symmetric cost formula and the explicit classification, verifying 7,000 seeded random parameter sets and 455,000 comparison-grid points against the claimed global optimizers. It tests the exact two-threshold example \(\alpha=1\), \(\beta=3\), \(q=1/5\), with \(T_{\mathrm c}=\log(9/5)\) and \(T_{\mathrm e}=\log(6/(\sqrt{33}-3))\). The paired times at \(T=0.7\) are approximately \(0.055825985792\) and \(0.644174014208\). Additional comparisons check the square-root splitting coefficient and the finite-lag long-horizon limit. An illustrative log-hazard check uses \(h_0=3\), \(P=1\), and \(q=1/5\).

The numerical search is not an exhaustive proof of the continuous global minimum; that follows from the analytic strict increase of the hyperbolic-sine ratio. The tests do not validate the phenomenological memory law in real coral populations or establish historical mathematical priority. No independent audit was performed.
