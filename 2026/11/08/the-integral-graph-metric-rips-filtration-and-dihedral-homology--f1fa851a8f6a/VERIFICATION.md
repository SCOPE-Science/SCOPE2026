---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproduction
Run `python3 verify_bidiakis_rips.py` using Python 3.9+ standard library. Compare standard output byte-for-byte to `bidiakis_rips_verification.txt`. The program proves that the directed Hasse diagram of the specified matching has no cycle by a complete topological sort, reconstructs the cell counts, checks the full eight-element automorphism census, derives the rational homology characters by signed simplicial traces, and checks integer persistence endpoints from the complete homotopy results.

# Observed checks
The executable passed on the delivered sources: 166 radius-two nonempty faces, 82 matching pairs, one critical vertex and one two-cell, 460 acyclic directed incidences; radius-one 30 nonempty faces, 11 pairs, one vertex and seven critical edges, 36 incidences; radius-two mod-two boundary ranks 11, 35, 32, 4; exactly eight automorphisms; all eight signed character values per positive-degree stage; rational multiplicity decomposition. The final success marker is `BIDIAKIS_RIPS_EQUIVARIANT_CERTIFICATE_PASS`.

# Scope limits
The computation addresses exactly the graph encoded by the chord formula, not every cubic graph; homotopy conclusions use the discrete Morse theorem. The homology characters do not themselves certify a \(D_4\)-equivariant sphere homotopy model. Literature overlap is checked only relative to identified records and read primary sources. Independent audit is not performed.
