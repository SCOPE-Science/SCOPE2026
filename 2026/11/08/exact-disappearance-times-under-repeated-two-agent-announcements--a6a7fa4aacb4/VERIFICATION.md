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

Ordinary world-deleting announcement that neither S5 agent knows p is exactly simultaneous deletion of oriented incidence edges meeting vertices with zero current indegree or outdegree. For an arc e:u->v, survival to t is equivalent to existence of directed walks of length at least t entering u and leaving v, giving the exact disappearance time min(h^-(u),h^+(v))+1 when finite; cyclic walks give infinity. In an acyclic digraph, predecessor+arc+successor is a directed path with at most N arcs, bounding strict rounds by ceil(N/2), attained by an alternating bipartite path. If there is a directed cycle, the 2-arc (multigraph) or 4-arc (proper frame) minimum persistent cycle leaves at most N-2 or N-4 deletable arcs, attained by an outward attached path. This proves both sharp maxima including N=1 and stable-core cases. Independently implemented direct S5 partition-color restrictions vs oriented-walk recurrence for all 2,16,200,3600 labeled partition-pair/valuation instances at N=1..4, obtaining maxima (1,1,2,2) with proper same; finite checks corroborate the general induction.

## originality

PASS

The eventual directed (1,1)-core and its random digraph deletion process are established in Pittel–Poole, while knowing-whether and repeated announcement semantics predate this theorem. The submitted exact per-world *synchronous* deletion-time formula and the two different all-N tight size laws for ordinary S5 world restriction were not established by Resultary or inspected accessible prior statements. Yamada's believed/arrow-deleting update framework is non-equivalent. Earlier fully general synchronous core peeling could imply this specialized law and remains a residual risk because its complete primary literature was not exhaustively read.

## value

PASS

The exact number of potentially informative communication rounds in a finite two-agent information model is a natural complexity invariant. The directed-walk normal form gives every world's disappearance stage and sharp proper-vs-multigraph world-count thresholds, going beyond a generic finite termination bound or anecdotal puzzle. The all-N extremizers supply motivated structural comparison.

The dated certificate retains the supplied scientific assessment, sources and limitations.
