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

Every alternating circle has the same number of starts in each phase. For n=2r the two required counts are (ab)^r; for n=2r+1 they are a(ab)^r and b(ab)^r, giving both lower bounds directly, even with wrap or repeated windows. The overlap digraph is strongly connected: append the destination vertex after zero or one filler symbol to match the phase. When n is even the two degrees at a vertex are equal. When n is odd and a>b, the B-first vertices have incoming excess a-b, and the A-first vertices have the opposite deficit. Appending the first B letter rotates a B-first vertex bijectively onto an A-first vertex; duplicating precisely these edges a-b times balances every vertex without deleting any edge. The reverse roles and a=b follow identically or need no addition. An Euler circuit gives one circular host, not a disconnected cycle cover: successive edges share n-1 symbols, so reading their first symbols gives the edge label at each cyclic start. This also covers n=2 and singleton alphabets. Independent replay `python3 /workspace/reproduce_frozen.py 2` finds shortest closed covering walks by breadth-first search on vertex and covered-edge set for 11 small families. The frozen script was inspected, not executed; finite optima are corroboration, not the unbounded proof.

## originality

PASS

Credit the known exact-once balanced cases and their degree obstruction. The distinct supported claim is the imbalanced odd optimum for coverage of both phases and its explicit minimal repeated-factor multiset. The closest one-phase theorem has the same number at an appropriate choice of designated phase, but allows missing opposite-phase targets. No equivalent or dominating coverage for the imbalanced contribution was established in the bounded checks.

## value

PASS

The earlier feasibility obstruction leaves a natural optimization question once exact-once coverage fails. The exact surplus and feasible single-cycle multiset solve that question for all sizes and lengths; in particular they allow one to size and construct a schedule that covers both phases. The claim does not address the number of optimal hosts or linear covers.

The dated certificate retains the supplied scientific assessment, sources and limitations.
