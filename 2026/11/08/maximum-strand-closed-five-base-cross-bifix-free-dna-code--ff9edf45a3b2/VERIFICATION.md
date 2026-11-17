---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

For a nonempty reverse-complement-closed 5-mer code, the first-letter set P is disjoint from its Watson--Crick complement. A complement-preserving letter permutation moves P into {A,C}; all words then lie in {A,C}Σ^3{G,T} (256 candidates). Its odd-length reverse-complement orbits all have size two. Independence from all proper cross-prefix/suffix overlaps leaves 56 admissible orbits and a simple incompatibility graph with 412 edges. The 18 listed cliques partition all 56 orbit vertices, so an independent set has at most 18 pairs, i.e. 36 codewords. The listed 18 orbit indices form an independent set, proving the bound attainable. This is a complete finite certificate, not an unverified solver bound. Independently reimplemented DNA reverse complement, raw orbits, admissibility, all ordered overlap conflicts, graph, partition and 18-pair witness in JavaScript: 128 raw orbits, 56 admissible, 412 conflicts, 18 genuine disjoint cliques, zero missing edges, 18 pairwise compatible witness orbits and no errors. Both Python verifier implementations were inspected from the assigned tree. The exact finite count proves the fixed-length theorem; it claims nothing for longer lengths.

## originality

PASS

The exact max cardinality 36 is for simultaneous length-five reverse-complement closure and mutual uncorrelatedness, with no GC-content constraint. The earlier published 24 optimum has an additional requirement of two or three GC letters, and so cannot upper-bound the larger family; its orbit graph has 120 vertices rather than these 56 unrestricted-under-GC canonical orbits. Unrestricted quaternary length-five non-overlap optimum 81 does not imply an optimal strand-closed subcode of cardinality 36. The length-four strand-closed optimum 17 is a distinct length. Stanovnik--Moškon--Mraz describe unrestricted short-code structures/tables but do not impose Watson--Crick closure in the inspected full article. Historical coding-table priority is qualified.

## value

PASS

This is the exact feasible maximum for a natural, physically motivated orientation-invariant DNA synchronization constraint, at the first odd nontrivial five-symbol length beyond three. A rigorous sharp clique partition plus explicit witness is a useful exact constrained code-size fact even without a general length-n capacity theorem; the 81 unrestricted or 24 GC-restricted optima are not interchangeable.

The dated certificate retains the supplied scientific assessment, sources and limitations.
