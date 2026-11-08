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

# Reproducible integer checks

With Python 3 and no external packages, run `python3 code/check_transfer.py` and `python3 code/check_direct.py` from the directory containing these files. Their exact captured standard output appears in `verification/transfer_stdout.txt` and `verification/direct_stdout.txt`.

The transfer checker constructs all \(9\) signed-edge states, verifies the \(5\)-state even block and the quartic matrix identity over the integers, enumerates the triangle-core boundary table within proved bounds, checks \(Z=3\), compares exact counts for \(2\le k\le12\), and checks the \(-8\) residual for every \(2\le k\le8\). The independent direct-state checker enumerates all integer labels within the derived degree-sum edge-gap cutoffs for \(2\le k\le5\), applies the diffusion update twice, and reports the exact number of initially two-periodic configurations. Its 1,458,000 combined candidate states provide bounded exhaustive examples but do not themselves prove the all-core theorem.

The all-core statement is established by the separate proof of edge reversal, tail-gap factorization, and the even transfer decomposition. The use of a program to verify an explicit small integer matrix identity is a reproducible finite certificate, not external formal certification or independent audit.
