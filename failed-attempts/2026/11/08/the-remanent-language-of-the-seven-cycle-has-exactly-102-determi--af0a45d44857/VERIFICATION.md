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

The seven-cycle orientation NFA starts at all seven vertices for each of 128 orientation masks. Signed-walk subset updates in the 128-fold product are exhaustive, with irrevocably empty components merged into a rejecting sink. Independent bitset BFS over all possible reachable tuples finds exactly 230 reachable states, 229 accepting, and Moore refinement stabilizes after partition sizes 2,4,7,9,11,13,15,17,24,34,38,42,46,50,58,68,74,78,80,82,84,86,88,94,102. Stable right-congruence plus distinguishing suffix induction proves exact minimality. Source checker also cross-checks independent pair distinguishability; no infinite extrapolation.

## originality

FAIL

The complete October 18, 2026 Resultary theorem already includes exactly the seven-cycle 230-state determinization and 102-state minimal complete DFA, with identical language definitions and sink conventions.

## value

PASS

An exact Myhill–Nerode complexity classification for the natural orientation-intersection language of a fundamental finite graph is a useful structural computational invariant requiring exhaustive minimization; historical coverage, not intrinsic mathematical valuelessness, is the rejection reason.

The dated certificate retains the supplied scientific assessment, sources and limitations.
