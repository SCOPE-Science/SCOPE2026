---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

I verified the uniform result with a separate exact certificate: /workspace/prism_independent_replay.py encodes ordered vertex-state pairs, composes the rule twice on every five-column word, and obtains the 23 possible adjacent time-two pairs by exhausting every six-column input. It checks all 1,491 five-column walks in that pair relation, none of which can produce an excited center two steps later. Every actual time-two cone is among these walks, even for wrapped rings, so no site is excited at time four and time five is all-rest. Direct enumeration of the three small rings gives exact maximum four with respectively 24, 336, and 3,380 first hits at four. For the stated six- and seven-column witnesses, the check gives an excited upper vertex at column 3 at time three; for n>7 the central radius-three cone is unchanged. All results concern synchronous updates with distinct open-neighborhood neighbors. I did not run the uploaded verifier; its output is frozen recorded evidence.

## originality

FAIL

The sharp cyclic classification is covered as a direct consequence of a stronger published seven-rung local truth table, plus explicit two-step witnesses on the small rings. This is a coverage finding against the current catalogue, not a priority claim about a distinct November entry whose catalogue date follows the frozen October record. No nonmechanical remainder of the stated finding survives this comparison.

## value

FAIL

The sharp finite transient for an unbounded graph family is a meaningful question. The stated cyclic result, however, contributes no distinct extremal phenomenon or independently needed count beyond the stronger local predictor: every ring size follows from identifying slots in one trigger and checking elementary small witnesses. The certificate is a useful correctness check but is not itself the claimed new invariant or theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
