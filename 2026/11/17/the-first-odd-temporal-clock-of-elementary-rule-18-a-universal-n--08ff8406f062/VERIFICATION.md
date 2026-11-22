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

For cyclic binary Rule 18 on every n>=3, the local formula (1-m_i)(l_i xor r_i) gives a bijection between F_n^t-fixed states and length-n closed walks on the 4^t temporal-column graph. The explicit generator considers all l,m and every allowed r, and tests all edges. Independently checked the graph by brute-force temporal triple constraints and a different directed-core elimination: t=1,3,5,7,9 respectively had (active,edges,remaining cycle-core)=(3,2,1),(48,56,1),(583,992,1),(6583,16256,1),(72048,261632,1), with only the all-zero vertex in the core. A separate direct Python evolution of all 2^n configurations for n=3..11 found no nontrivial odd cycles for n<11 and exactly two primitive 11-orbits at n=11 (minimum state representatives 75 and 105; 22 states). Thus this precise threshold theorem is supported by an exhaustive finite *time-height* certificate coupled to an all-circumference transfer lemma; it neither proves absence of all longer odd periods nor classifies larger rings.

## originality

PASS

The Rule 18 fixed-time-column obstruction and sharp n=11 onset are distinct from the prior temporal-two, image-fiber, and statistical/domain analyses. Search found no previous theorem implying these exact all-ring short-odd exclusions and first occurrence. This is a qualified assessment, not proof of priority against historical finite-CA period catalogues.

## value

PASS

The least odd primitive clock and least circumference are natural exact dynamical invariants of one elementary cellular automaton; a uniform finite transfer certificate for all ring sizes and sharp witnesses is a nonroutine and reusable structural boundary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
