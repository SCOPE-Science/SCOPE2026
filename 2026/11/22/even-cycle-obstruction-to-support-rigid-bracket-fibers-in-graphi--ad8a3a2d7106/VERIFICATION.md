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

A self-contained Python checker, `verify_graph_bracket_fibers.py`, enumerates horizontal input pairs and all central targets in eleven small configurations. It uses a second path for the proposed formula: enumeration of matchings in each edge-support subgraph, followed by the character-sum expression. This confirms the full fiber tables without using Fourier inversion to generate the direct counts.

The checker also verifies contrasting four-cycle target fibers over fields of sizes three and four. The output is captured in `CHECK_OUTPUT.txt`. Run `python3 verify_graph_bracket_fibers.py` from the containing directory with Python 3 and its standard library.

The general proof uses: the additive-character orthogonality identity; the nonsingular-principal-Pfaffian criterion for alternating rank; uniqueness of perfect matchings in induced subgraphs without even cycles; and the two-monomial Pfaffian of an even cycle. No exhaustive test of all graphs or fields is claimed. Historical originality is assessed from the named accessible literature, not certified independently.
