---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

A coloured clique vertex has w+q white neighbours, and either exceptional vertex w. Hence no forces while w>=2, and quotient state (w,x,y,ownership flags,mover) with 72 non-w combinations suffices. Full certificate TSV has 72 identical F3/F5 pairs; read verifier recurrence and its labelled-vertex independent cross-check. A deterministic w-independent transfer Phi for w>=2 extends F3=F5 to all w by induction, yielding root force sets {(1,1)} for even n and {(1,0),(1,1)} for odd n. Converting force counts using ceil/floor n/2 turns gives the specified seed sets, including the exceptional P3 boundary. Bounded finite certificate is a genuine base lemma, not improperly extrapolated.

## originality

PASS

PASS best of knowledge: published primary paper supplies rules, K5-e example, K4-e scalar and census up to nine vertices, but not the unbounded ordered outcome classification or 72-state two-periodic transfer argument. No stronger covering theorem found in searched records; inaccessible/unindexed work remains a residual priority risk.

## value

PASS

PASS: a nontrivial all-order classification of every optimal tie outcome for a competitive game, with distinct seed totals at every odd n; quotient periodicity is a reusable structural method beyond known small graph census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
