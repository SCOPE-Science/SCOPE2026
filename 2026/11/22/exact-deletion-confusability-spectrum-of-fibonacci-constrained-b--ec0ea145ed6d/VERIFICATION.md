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

The exact finite-state proof certificate is `artifacts/transfer_certificate.json`. Run `python3 artifacts/verify_transfer.py`; it builds the underlying six-state nondeterministic common-deletion alignment and independent `11`-avoidance memories, determinizes to seventeen reachable states, refines twelve counted-equivalence classes and retains nine productive classes. It verifies the complete integer polynomial identity \((I-zM)p(z)=d(z)b\) with \(d(z)=(1-z)(1-z-z^2)^3\) and checks the claimed generating function.

The independent direct-enumeration checker `artifacts/verify_bruteforce.py` builds every admissible binary word, its distinct one-deletion descendants, and the resulting undirected edge set through length fifteen. It checks both the total edge generating function and the Hamming-edge refinement. Neither finite enumeration nor extrapolation is used for the all-length argument.

Both programs were executed successfully and are fully included in the package. The proof assumes literal linear indexed words, arbitrary single-symbol deletions, and no restriction on the receiver words. An independent scientific audit has not been performed.
