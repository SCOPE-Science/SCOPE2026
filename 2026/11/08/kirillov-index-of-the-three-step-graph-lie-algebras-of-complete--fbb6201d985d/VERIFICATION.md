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

The accompanying `checker.py` is standard-library Python. Execute `python checker.py`; the expected output is archived in `checker_output.txt`. It constructs the Lie brackets of the two-color complete graph using independent edge and length-two-path functional values, computes Kirillov ranks by finite-field elimination, and checks the explicit mixed-block determinant-one witness by integer Bareiss elimination.

The script checks 36 parameter/prime-field witness configurations and exhaustively enumerates functional values in three small cases: \(2^8=256\), \(3^8=6{,}561\), and \(2^{15}=32{,}768\). Recorded ranks agree with the claimed bound. These computations do not prove the theorem for all part sizes and fields. The unrestricted proof instead uses the explicit \(5\)-row base certificate, the vertex-extension induction, and the symbolic determinant obstruction for \(K_{2,2}\).

The source defines a Lie algebra also in characteristic two; signs are interpreted with alternating brackets. External independent mathematical auditing has not been performed.
