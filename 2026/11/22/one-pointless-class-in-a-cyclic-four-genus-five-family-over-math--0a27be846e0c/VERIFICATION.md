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

# Verification record

The package includes `verify_cyclic4_F17.py`, which uses only Python 3 standard-library operations. Run `python3 verify_cyclic4_F17.py` to exhaustively enumerate the \(16\cdot17\cdot16=4352\) coefficient triples and verify the discriminant, nonsquare and orbit conditions. Expected output: `CYCLIC4_POINTLESS_F17_VERIFIED smooth=4096 pointless=32 normalized=4 diagonal_orbits=1`.

The complete mathematical proof, including the exact pointlessness criterion, eight-row classification table, square-scaling normalization and diagonal orbit argument, is contained in `RESULT.md`. The finite sweep is exhaustive over the specified family; no conclusion about other hyperelliptic families is drawn. Independent audit has not been performed.
