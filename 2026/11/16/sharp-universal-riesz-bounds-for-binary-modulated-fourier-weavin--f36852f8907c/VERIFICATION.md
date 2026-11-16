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

# Verification and reproducibility

For the main assertion, examine the four analytical steps of `RESULT.md`: the exact Gram operator and its norm bound, the accretive invertibility argument, the shifted Hilbert matrix lower bound with the precise \(\pi\)-normalization, and the two distinct phase-boundary obstructions.

Run `python CHECK.py` with Python 3, NumPy and SciPy. A successful run reports 250 finite checks, including random finite binary partitions, Hilbert-corner finite sections, a direct boundary Hardy identity and critical regularized vectors. The tests were executed successfully for this record; they are consistency checks, not proof of infinite-dimensional statements.

The critical proof uses the explicit branch of \((1-z)^{-lpha}\) and the independent inequality \(lpha<1/2\) to establish square-integrability. At equality its regularizations have diverging squared norm but uniformly bounded analysis energy. The higher-phase failure is incompleteness, not merely poor conditioning. The quantitative positive-regime bounds are simultaneous for all \(J\subseteq\mathbb Z\), with sharpness in an infimum/supremum sense.

No formal proof assistant or independent verification was used. The available literature comparison leaves an older exact-stability-constant overlap risk and does not claim a complete priority certificate.
