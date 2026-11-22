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

# Reproducible verification

Run `python3 verify.py` with any current standard-library Python 3 installation. The program directly builds output sets for 181 parameters between -90 and 90 for each \(1\le k\le8\), computes the proposed counts from independently coded recurrences, and compares them. In nonunit cases it compares the entire residue set against the specified cylinder decomposition. It also checks eight selected nonunit parameters through \(k=10\).

Observed result: `PASS: 1464 direct prime-power counts and 488 full-set identities`.

The proof of the complete infinitely many parameter and precision cases is in `RESULT.md`, based on Hensel lifting and exact rescaling identities; finite enumeration by itself cannot establish it. The historical full-text priority comparison noted in `REVIEW.md` remains incomplete. This package has not been independently audited.
