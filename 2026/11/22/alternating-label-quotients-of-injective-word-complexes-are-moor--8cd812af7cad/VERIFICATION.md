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

# Reproducible checks

The standalone `verify.py` builds genuine alternating-group word orbits for each integer \(3\le n\le8\), using three-cycle generators without presupposing parity-orbit formulas. It independently computes each cellular boundary matrix, checks the chain property, the intermediate maps, and exact Smith forms of the top maps. This execution returned `ALTERNATING_INJECTIVE_WORD_QUOTIENT_ORBITS_OK` with cell counts and Smith diagonals reported in the result. Reproduction: install Python 3 and SymPy, then run `python verify.py`.

The uniform classification instead depends on the explicit written parity formula for *every* \(n\ge3\), genuine CW cancellations, the sphere-wedge attaching-map classification in dimension at least two, and a separate fundamental-group presentation for \(n=3\). No finite sample is claimed to establish that universal derivation. There has been no independent external proof audit or external certification.
