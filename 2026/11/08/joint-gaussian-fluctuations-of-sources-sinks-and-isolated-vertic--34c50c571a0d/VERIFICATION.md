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

# Verification and its limits

The mathematical proof is in `RESULT.md`, including the exact forbidden-arc moment identities, connected-cumulant bound, short-cycle factorial-moment argument, coupling under finitely many forced arcs, acyclicity tail bound, and positive definiteness calculation.

Run `python3 verify.py` in the extracted directory. The stand-alone Python standard-library checker returned `VERIFY_OK 116 exact/algebraic and limit checks`. Specifically, for graphs on 2, 3 and 4 vertices it enumerates every directed-arc subset at three rational probabilities and compares all nine mean/variance/covariance entries as exact fractions. It additionally checks determinant positivity for five parameter values and the finite-size covariance approach to the limiting formula at size 100000. This numerical calculation is corroboration only; it does not validate the joint central limit theorem or independence from rare cycles. Those assertions rely on the written proof.

No independent audit, historical-priority certification, formal proof assistant, or externally validated infinite proof is claimed. The theorem excludes the critical and supercritical regimes.
