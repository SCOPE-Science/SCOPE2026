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

# Verification and scope

Run `python3 verify.py` using a standard Python 3 interpreter. Expected output: `VERIFY_OK`.

The checker reconstructs exact integer matrices \(Q,B,D\), confirms their displayed powers and determinants, checks seven parity types for every nonzero binary starting vector, and verifies dyadic leading-term matrices. It exhaustively tests all primitive initial triples modulo \(2^k\) for \(1\le k\le5\), then performs nonexhaustive higher-precision tests on five distinct triples for \(6\le k\le12\). The checker is not an exhaustive verification beyond \(k=5\) and is not the proof of the infinite assertion. The proof in `RESULT.md` explains the all-precision valuations, isometric branches, and even-fiber pairing. Independent mathematical audit has not been performed.
