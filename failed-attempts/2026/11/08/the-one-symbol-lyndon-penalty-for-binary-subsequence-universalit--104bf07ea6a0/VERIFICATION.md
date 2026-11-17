---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

Reconstructed binary greedy arch lemma, lower bound 2k, periodic non-Lyndon 2k candidate for k>=2, and at 2k+1 two cases (00 at start or unique 11) to force the claimed two Lyndon words. Boundary k=1 has unique 01. Independently enumerated all binary length-2k+1 Lyndon k-universal words for k=1..7, recovering predicted list; checked actual verifier source (k<=8). General statement rests on the written arch/rotation proof, not finite enumeration.

## originality

FAIL

A complete published classification of all shortest unbordered binary subsequence-universal words already includes the Lyndon family as a strict subclass; its explicit generator can be filtered by the standard rotation test. The identical optimum is previously proved; exact two Lyndon members do not create a new structurally independent result.

## value

FAIL

The already-published complete natural classification of every shortest unbordered k-universal word determines these Lyndon witnesses by the standard minimal-rotation predicate. The submitted result supplies a restricted list and proof, but no independently needed classification outside that complete earlier parametric census; the one-symbol optimum itself was already known for the stronger unbordered class.

The dated certificate retains the supplied scientific assessment, sources and limitations.
