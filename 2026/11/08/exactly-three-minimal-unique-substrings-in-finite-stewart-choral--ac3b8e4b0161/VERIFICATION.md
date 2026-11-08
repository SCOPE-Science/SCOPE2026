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

# Reproducibility and scientific limits

Run `python3 verify.py` from a directory containing the standalone verifier. It requires only the Python 3 standard library. The script constructs \(W_k=\varphi^k(0)\) for \(k=2,3,\ldots,9\), independently computes all minimal unique substring positions by suffix-array longest-common-prefix calculations, and checks the exact three predicted pairs. It additionally checks all four repeated-factor blocks, the central single-bit flip, the two occurrences of the distinguishing prefix, and the two trimmed-image recurrences. For \(k\le4\) it compares against a separate direct occurrence-counting enumeration.

The expected final line is `STEWART_CHORAL_MUS_VERIFY_OK`. The largest checked input has length 19683. The universal theorem is proved symbolically in RESULT.md; no finite test can certify untested iterates on its own. No independent audit or external certification is claimed.
