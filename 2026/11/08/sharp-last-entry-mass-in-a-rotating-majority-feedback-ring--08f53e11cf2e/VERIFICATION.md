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

The following standard-library programs were executed from their accompanying paths and their output captured as ordinary text: `python3 check_dynamics.py` and `python3 check_transfer.py`.

`check_dynamics.py` enumerates every one of the \(32{,}760\) initial binary words for \(3\le n\le14\) under the original feedback map, checks the first time the orbit enters the no-singleton set, compares the count at clock \(n\) against the theorem, checks no trajectory requires more than \(n\), and independently traverses the periodic rotational classes. `check_transfer.py` computes the actual four-state transfer traces and the Möbius periodic-orbit counts for \(1\le n\le100\), and counts rightmost-equal-pair patterns for \(3\le n\le16\). The captured outputs are included as `check_dynamics.out` and `check_transfer.out`.

The proof for unbounded \(n\) is the monotone cyclic-disagreement argument and the rightmost-pair enumeration in `RESULT.md`, not the enumeration logs. The programs have no external dependencies. No unproved converse, unresolved numerical certificate, independent audit, or extrapolation from finite samples is claimed.
