---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-08.md",
      "INDEPENDENT_AUDIT_2026-11-08.json"
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

PASS. The directed face condition independently fixes a partial vertex-successor map with distinct incoming/outgoing arcs and no directed directed cycle. Exhaustion of 2^12 masks gives 279 faces including empty and f=(12,54,104,84,24). Inspected and independently replayed the 134-pair acyclic matching on all 278 nonempty faces/876 cover incidences; the exact signed integral unit-pivot algebraic Morse reduction leaves one critical 0, one 2, four 3, four 4 cells with all integer differentials zero. Therefore H0=Z, H2=Z, H3=Z^4, H4=Z^4, no torsion. A CW model with no 1-cells gives pi1 trivial. Zero cellular boundaries do not establish all higher attaching maps null, and no wedge is claimed. Independent replay: /mnt/data/scope03_independent_check_20261108.py, generated from inspected source, passed the entire finite enumeration and integer reduction.

## originality

PASS

PASS best-of-knowledge. Deshpande–Sawant 2026 establishes directed-linear-forest framework and poses cyclic examples; Caputi–Collari–Di Trani–Smith 2022 treats paths/polygons/other orientations, not this cyclic complete-tripartite six-vertex blow-up. Undirected octahedral Morse or matching complexes in Resultary are different functors and do not imply these integral homology groups. No exact 1,4,4 degree-2/3/4 table of this orientation was found; priority risk from unindexed finite examples remains.

## value

PASS

PASS. The cyclically oriented complete K_{2,2,2} is a canonical small strongly connected cyclic blow-up precisely where acyclic directed-linear-forest exclusions become meaningful. Its three adjacent positive homology degrees differ sharply from the in/out-degree-only matching-join S^2, giving a concrete exact integral base case for the cyclic multipath problem posed in recent literature. The finite scope is intrinsic, not an arbitrary unmotivated slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
