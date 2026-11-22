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
# Verification

Run `python3 verify.py` with Python 3.9 or newer. The program has no third-party dependencies. It regenerates all tournament faces and explicitly validates every free-face pair for the three base cases. The seven-vertex residual two-complex is checked through a presentation of its fundamental group using integer words and elementary Tietze eliminations. It compares all four stated link adjacency formulas and domination schedules against direct tournament orientation checks over integers \(3\le m\le33\), plus full simplicial collapses for \(2\le m\le7\).

These finite checks corroborate, but do not constitute, the proof for all integer parameters. The universal step follows instead from the two transitive link classes, their explicit modular-interval cross edges, and graph folding by closed-neighborhood inclusions. The certificate is a computational reproduction of stated checks, not an independent external audit.
