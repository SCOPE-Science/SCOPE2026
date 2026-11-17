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

Enumerating all balanced four-mers gives exactly 96, 52 reverse-complement orbits with 8 fixed and 44 admissible two-member orbits. A 44-vertex deletion-shadow conflict graph has 344 edges. Fourteen explicit conflict cliques from certificate.json cover each vertex at least twice (36 with multiplicity 2 and eight with 3); a deletion-compatible independent set therefore has size ≤7, and seven explicit pairs realize it, giving 14 DNA words. Independent increasing-index enumeration of all compatible seven-orbit subsets yields exactly 20, and a full 16-action group calculation gives orbit sizes 4,4,4,8. Every seven-set was independently checked maximal, so no eight-set exists; this is a complete finite certificate, not merely a solver result.

## originality

PASS

The prior unrestricted strand-closed quaternary length-four maximum 22 without fixed words does not determine the maximum or optimizer census after exact GC balance; prior constant-GC Hamming codes use a different error metric. The targeted 14-word/20-code optimum is a motivated intersection of established coding constraints and not a recomputation of an existing table found in relevant full texts.

## value

PASS

GC balance, reverse-complement closure, avoidance of self-complement strands, and single-deletion correction are natural simultaneous DNA storage constraints. Their exact feasible maximum and complete 20-solution equality classification constitute an independently checkable finite extremal coding fact not implied by unrestricted or Hamming models. No longer-length theorem is required for this precisely motivated finite optimum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
