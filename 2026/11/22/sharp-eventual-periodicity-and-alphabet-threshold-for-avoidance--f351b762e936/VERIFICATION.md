---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Independently enumerated binary words through length eight using base-4 encoded Parikh sums, verified the exact counts, 12 contexts, 10 length-six transitions and six length-eight phases, and checked the unique correct continuation of each length-eight phase. This is a finite certificate for all lengths because appending a bit can only create a forbidden suffix of length 4 or 6; the six distinct phases exhaust length eight and always have the periodic continuation. The two additional length-seven words make the onset sharp. Independently checked both distinct same-length returns for each of the three prescribed constraints (ternary joint and each binary single order), checking every factor in the seed plus each block and exact return of the maximal context. Any future crossing factor is then checked by the next return, so the choices concatenate freely and arbitrary remaining length is obtained by a prefix of one return. Counts are positive and submultiplicative by factoring a word at a fixed index, giving existence of entropy and the stated strict bounds. Replay: python3 /workspace/branches/reproduce_decisive.py; the frozen scripts and verification notes were inspected without execution.

## originality

PASS

The supported distinct result is the exact binary rigidity and onset under the two exact orders, joined to a constructive exponential-growth threshold and binary inclusion-minimality. Neither standard overlap graphs nor periodic examples are by themselves the originality basis.

## value

PASS

The first two nontrivial half-length restrictions constitute a minimal pair that forces binary words into just one periodic orbit after a sharp finite cutoff, while adding a third symbol or removing either restriction permits independent choices forever. This gives an exact rigidity benchmark for bounded Abelian-square avoidance and distinguishes zero capacity from genuine exponential growth; finite counts alone would not establish that distinction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
