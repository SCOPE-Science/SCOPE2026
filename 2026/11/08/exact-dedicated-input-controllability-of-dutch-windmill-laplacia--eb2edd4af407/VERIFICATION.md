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
Run `python verify.py` with Python 3.9 or later. The script is self-contained and uses standard-library integer arithmetic. It builds the stated graph Laplacian, tests the exact full-column rank of finite-field Kalman/Krylov matrices at two primes, checks that the neighbor placements stall zero forcing, and checks a hub-plus-one-per-petal forcing placement. It exhaustively rejects zero-forcing initial sets of at most \(m\) vertices for seven finite examples. Successful output begins `VERIFY_OK`.

Sampled ranges: \(2\le m\le5\), \(3\le\ell\le11\); \(36\) graph orders and \(72\) prime-field tests, plus \(776\) exhaustive forcing trials. These computations do not prove an infinite family. The paper's analytic PBH proof supplies that part, including the all-parameters spectral-gap lemma and the hub-resonance comparison. The verifier tests the packaged claim only and makes no independence claim.
