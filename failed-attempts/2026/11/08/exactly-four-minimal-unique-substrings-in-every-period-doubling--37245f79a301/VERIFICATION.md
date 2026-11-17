---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

PASS: D_k=A B A A with A=D_(k-2), B=C C and A=C C*; primitive cyclic shifts separate A/B classes. Every length m factor repeats; exactly four length m+1 extensions are unique, and companion-prefix divergence prevents longer MUSs. Independent direct enumeration of all substring frequencies for k=3..8 agrees with all four starts. Proof treats boundary occurrences, not circular strings.

## originality

FAIL

FAIL: 2026-11-02 complete prior mathematical theorem gives exactly the same four zero-based intervals, length 2^(k-2)+1, all k>=3 and same period-doubling substitution.

## value

FAIL

FAIL as a new research contribution: the full exact MUS inventory and length are established in the earlier mathematical theorem; the alternate proof and finite verifier do not supply a distinct new invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
