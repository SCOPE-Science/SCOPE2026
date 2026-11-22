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

# Reproducibility and boundaries

Execute `python3 verify.py` on Python 3. The checker is self-contained, requires no external dependencies, and prints `VERIFY_OK` only after all assertions pass.

It independently generates the explicit cyclic endpoint words and their parity prefix masks, checks the geometric crossing criterion on all pairs of gap choices through size \(22\), confirms every proposed run-type count at sizes \(7\) through \(36\), confirms the exact construction count at sizes \(5\) through \(36\), and enumerates all cyclic chord pairings through six chords. The direct pairing census contains \(11{,}464\) diagrams across sizes one to six.

The unrestricted upper bound is a theoretical consequence of two cyclic gaps determining the trace, with the empty trace supplied by a same-gap insertion. The unrestricted explicit lower-bound count follows from the exhaustive interval-run classification in `RESULT.md`. Computational enumeration is finite and is not a proof of statements at arbitrary size.

No proof of the exact global shatter function at every finite size is claimed, nor is an independent audit represented as performed.
