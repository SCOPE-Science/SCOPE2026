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
# Verification record

The finite checker `verify_sparse_angles.py` was run with Python 3. For every \(m=4,5,6,7,8\) and every \(2\le n\le\min(5,m-2)\), it generated all vertices as ordered placements of the largest positive labels, computed facet equality incidences afresh and compared the full resulting facet-pair set with the predicted ridges. For each ridge it built the two normal vectors directly and checked the normalized squared dot-product via exact integer identities, including the sign determining acute versus obtuse angles. All three class counts matched. Totals: 14 cases, 17,218 vertex occurrences, 6,789 ridge incidences. The script printed `SPARSE_RIDGE_ANGLE_PASS`.

The exact closed-form count ratios were evaluated at \(m\in\{256,1024,4096\}\) and offsets \(n-\log_2m\in\{-2,0,2\}\); the observed ratios approach \(1/8,1/2,2\), respectively. These numerical checks do not prove the asymptotic law. That law rests on the ratio-of-consecutive-terms domination and the binomial central limit theorem in the written proof.

No independent mathematical audit, independent priority certification or external validation has been performed. The scientific risk of unindexed stronger coverage remains open.
