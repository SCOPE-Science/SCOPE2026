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
Run `python3 verify_nxm8.py` (Python standard library, no dependencies). The checker starts from unordered polygon pairs, constructs all eligible noncrossing partial matchings, enumerates their strict face chains and cyclic/dihedral orbits, and checks the unique surviving coface condition and absence of higher cofaces for every elementary collapse. It rebuilds exact signed attaching words after contracting a spanning tree and replays generator eliminations only when a generator occurs once in a chosen two-cell word. The final assertion is a degree-two attaching word plus an empty word for the cyclic quotient and a single vertex for the full dihedral quotient.

The code was executed against the package source and printed `VERIFY_OK`. The n=5,6,7 cross-checks verify that earlier small examples collapse to graphs and give torsion-free first homology. None of these finite checks is extrapolated to untested polygon sizes. Independent validation has not been performed.
