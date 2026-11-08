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

# Reproduction and limits

Run `python3 verify.py` with a standard Python 3 interpreter; no external packages or internet are required. The program reports `VERIFY_OK_MODULAR_QUANDLE` on success. Its finite checks are logically separate from the proof.

The program builds the linear operator \(\sigma_{-1}+\sigma_2-I\) in the augmentation-ideal basis over each of eleven odd prime fields, computing its kernel by exact row reduction; checks explicit eigenvectors by direct quandle multiplication; enumerates all \(289\) nonzero predicted idempotents for \(p=17\); verifies the existence of \(272\) nonbasis solutions and sampled core-quandle products; and exhaustively evaluates every quandle-algebra coefficient tuple over \(\mathbb F_3[R_3]\), \(\mathbb F_9[R_3]\), and \(\mathbb F_5[R_5]\). These total idempotent counts are \(4,10,6\), respectively.

The finite computations do not constitute an exhaustive search for all primes or all extension fields, do not certify a published-priority claim, and do not replace the symbolic logarithm and eigenvector proof. Independent audit has not been performed.
