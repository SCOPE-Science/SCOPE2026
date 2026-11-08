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

The proof in `RESULT.md` is symbolic for every integer \(r\geq1\); it derives both the lower bound on the necessary finite model dimension and an explicit construction attaining equality.

`check.py` is a supplementary Python standard-library diagnostic. Running `python3 check.py` verifies, for ranks \(1\) through \(13\), the prescribed rank of the perturbation, an explicit nullspace basis, the independent backward-shift images, and direct-sum complementarity in dimension \(4r+2\). Each test uses integer matrix entries and exact modular Gaussian elimination, not floating-point rank thresholds. The output ends in `FINITE_DIAGNOSTICS_PASS` when all checks succeed.

The diagnostic is not an infinite-rank certificate or independent review. The published general defect upper bound is cited as background rather than re-proved. No assertions are made about infinite-degree, multiband, or uniqueness cases.
