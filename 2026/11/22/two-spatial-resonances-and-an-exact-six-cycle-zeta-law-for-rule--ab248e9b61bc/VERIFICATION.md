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

An anchored length-n closed walk on pairs of p-bit time histories enforces the exactly-one rule at every site and time. It determines a unique initial row fixed by F_n^p and conversely is determined by that row. Anchor and orientation are retained, so the trace counts labelled configurations, not rotation/reflection classes. A fresh bitwise reconstruction and Kosaraju decomposition gave the stated cyclic SCCs. The only branching block has 60 vertices, with 12 vertices of outdegree two within the block; all paths to the next such vertex have length five. The nonbranching vertices induce an acyclic graph, so eliminating them by the Schur complement reduces det(I−zA) on that block to the determinant of I minus the weighted branch adjacency with weights z^5 per path. Enumerating all 324 collections of disjoint directed branch cycles (including the empty collection), with sign minus per cycle, gives 1−6z^10+9z^20−4z^30=(1−z^10)^2(1−4z^10). All other cyclic components are simple cycles of lengths [1,2] at heights 1 and 3, [1,2,4] at height 2 and [1,2,4,8,8,8] at height 6. This independently gives both determinant identities, also reconfirmed via exact Newton identities in a separate reconstruction. The formal log derivative extracts all trace differences; fixed-by-1 is contained in fixed-by-3 and the trace equality makes them equal. Thus only fixed-by-2 must be subtracted from fixed-by-6 to count exact period six. The coefficients are 24 on multiples of eight, and 10(4^(n/10)+2) on multiples of ten, with addition on multiples of forty. Dividing by six counts temporal orbits and the table agrees. Replay: node /workspace/rule22-replay.js. The two supplied scripts were read, not executed; their bounded direct enumeration alone is not the all-length proof.

## originality

PASS

Credit the historical finite tables, the known period-six patterns, and the extended de Bruijn method. The distinct claim is the complete labelled, oriented, all-circumference period-six census and its exact determinant factorization for Rule 22; the independent check also proves the all-length absence of primitive period three, which was reported in the historical finite-table context. No priority claim is made for the existence of the smallest examples or for the general method.

## value

PASS

Gives a complete exact temporal orbit census at a natural return time for a standard cellular automaton. It distinguishes a bounded population from an exponential one, accounts for their coexistence, and proves the omission of all other circumferences rather than extrapolating a finite cycle table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
