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

PASS: Nonfixed ordered-letter pairs fall into 2r(r+f) two-element coordinatewise-involution orbits, bounding the number of distinct allowable cyclic digrams. The quotient edge graph has two P_i→P_j edges of bit-flip labels 0/1 for every ordered pair, and one P_i↔F_a in each direction; it is balanced/strongly connected. A fixed symbol resets lift parity and makes an Eulerian cycle of all orbits lift to a word. If f=0, the xor of edge labels around a lifted word must vanish, but xor of all 2r² orbit edges is r² mod2, so odd r forces at least one omitted orbit; deleting one label-one self-loop preserves balance and connectivity and achieves 2r²−1. For even r all orbits lift. Direct independent constructions passed 64 small (f,r) cases, not used as an infinite argument.

## originality

FAIL

Exact prior Resultary October 18 theorem supplies full arbitrary-symbol-involution result, not just arithmetic-negation f=1,2, so claim is covered word-for-word in mathematical meaning.

## value

FAIL

FAIL: An earlier October 18 full theorem gives precisely the arbitrary-involution cycle length and constructive parity deficiency for every (f,r). The new quotient-graph/Euler-tour proof is mathematically natural but does not yield a previously unknown invariant, stronger enumeration, additional cutoff, or useful boundary beyond the older exact classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
