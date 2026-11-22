---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

The actual twelve-vertex icosahedral graph with 30 edges (two pentagonal belts plus two apices) and the four-state threshold-one simultaneous excitation rule were reconstructed. An independent C++ full functional-graph computation traversed all 4^12=16,777,216 labelled states, finding exactly one fixed point and 208,850 primitive period-four cycles, 835,400 rotating periodic states, fixed basin 3,620,436, 20 nonempty joint depth/period classes, maximum depth ten achieved by 240 states and no other periods; hence F^14=F^10. Independent local successor-coloring count matches 835,400. NetworkX complete graph-isomorphism enumeration gives full automorphism group size 120 and exactly two size-120 extremal orbits represented by base-four codes 75769 and 441799. The exhaustive finite-state proof is valid only for this specified graph; the connected-graph rotation lemma alone does not prove the ten-step bound.

## originality

PASS

Best-of-knowledge PASS: compared the exact mathematical claim and implications against same-object primary literature and published result records. Previously known model definitions, finite-face methods, cone inequalities, or alternate-parameter/loss theorems are credited. The cited prior statements do not imply the submitted exact additional invariant. This is not a certification of comprehensive historical priority.

## value

PASS

The icosahedron is a canonical symmetric five-regular graph and four-state Greenberg-Hastings excitation is a standard excitable automaton. The complete 16.8-million-state dynamical census, sharp ten-update transient, complete basin sizes and two full-symmetry extremal strata are mathematically meaningful exact dynamical invariants not supplied by three-color or complete multipartite results. The result deliberately does not extrapolate to unrelated graphs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
