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

The universal statements were verified by an algebraic proof using the block Gram matrix of the multiplication pairing and its kernel. Two standalone programs corroborated the rank formula on small quivers:

- `python frob_rank_checker.py` enumerates all linear functionals and computes the Gram-matrix rank by modular Gaussian elimination over \(\mathbb F_2\) and \(\mathbb F_3\). It tests 26 cases including loops, two parallel arrows, cycles, chains and forks. The output ends with `ALL_FROBENIUS_RANK_CHECKS_PASS 26`.
- `python frob_gf4_checker.py` uses arithmetic in \(\mathbb F_2[t]/(t^2+t+1)\) and computes direct matrix ranks independently. It checks five quivers and ends with `GF4_ALL_FROBENIUS_RANK_CHECKS_PASS`.

For both programs, predicted rank distributions are independently constructed from arrow-support and diagonal masks, not the matrix elimination routine. The expected total number of functionals is \(q^{n+m}\). The scripts use only the Python standard library and terminate without downloads.

Finite enumeration does not certify all quiver sizes or field orders, nor does it establish historical originality. No independent audit has been performed.
