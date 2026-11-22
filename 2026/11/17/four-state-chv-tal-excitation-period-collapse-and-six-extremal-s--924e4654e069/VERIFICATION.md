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

The pinned 24-edge four-regular Chvatal graph and 0->1 only upon excited-neighbor, 1->2->3->0 rule were reconstructed directly from the package and its two independent C++ implementations. Independent C++ functional-graph enumeration built every successor over all 4^12=16,777,216 labelled states (no sampling), removed zero-indegree vertices, traversed every residual cycle and back-propagated depths. It obtained one fixed state, 29,602 primitive four-cycles (118,408 rotating states), period-1 basin 3,791,756, exactly 21 joint depth/period cells, maximum first entry 12 and 48 maximizers; hence F^16=F^12. Independently evaluating the local successor-supported four-color predicate gives 118,408. Full NetworkX graph automorphism enumeration found eight automorphisms, six orbits of eight extremal states with exactly the six stated representatives. This proves a finite fixed-graph census, not arbitrary graphs; only period-dividing-four recurrence is characterized structurally, while the exhaustive functional graph excludes other periods.

## originality

PASS

Best-of-knowledge PASS: compared the exact mathematical claim and implications against same-object primary literature and published result records. Previously known model definitions, finite-face methods, cone inequalities, or alternate-parameter/loss theorems are credited. The cited prior statements do not imply the submitted exact additional invariant. This is not a certification of comprehensive historical priority.

## value

PASS

The Chvatal graph is the canonical smallest 4-regular triangle-free 4-chromatic graph, making its finite deterministic four-state excitation dynamics a motivated exact model rather than an arbitrary small sample. The complete 16.8-million-state classification, 12-step sharp cutoff and six extremal automorphism orbits identify meaningful dynamics and symmetry that qualitative graph theory does not predict. It is a finite exact invariant of a natural graph, not an asserted universal graph theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
