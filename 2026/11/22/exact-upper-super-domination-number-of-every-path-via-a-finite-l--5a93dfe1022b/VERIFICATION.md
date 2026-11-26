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

Complementation exchanges inclusion-minimal super domination with maximal open irredundance, which is hereditary and hence maximal iff all one-vertex additions fail. A flip affects only witness statuses within distance two, all decided in the radius-four window, with nonexistent neighbors excluded. The padded suffix transitions accept exactly those words; the restriction to n>=2 is necessary. I independently built the window truth table from induced graph neighbor intersections and verified exact shortest-distance inequalities for 233 states including the sink, 403 edges including 58 finalizations, and sink distance zero. Along any accepted word those inequalities give 7|T|-2n>=0. The seven explicit tails give the rounded bound exactly. For three or more blocks, an interior nine-window is one of seven phases, and any window touching a boundary or tail is determined by at most eight nearby periodic symbols and that fixed end. Thus the verified finite factor list exhausts the infinite construction. P1 has only the full super dominating set. Replay: `python /workspace/audit-replay.py 4`; the supplementary literal graph check covers n=2..11, not the infinite quantifier.

## originality

PASS

The supported contribution is the exact path extremal value for every order, not the invariant, complement duality, or the nine-symbol recognizer. The same-day unweighted path census already contains essentially that recognizer; the cardinality optimization, its weighted all-order bound and the explicit sharp boundary words are distinct. No ordering is inferred from the shared date.

## value

PASS

Resolves the remaining exact-value ambiguity for a natural graph invariant on all paths. The all-order weighted certificate and endpoint-corrected sharp words give a usable result beyond finite tables or the unweighted census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
