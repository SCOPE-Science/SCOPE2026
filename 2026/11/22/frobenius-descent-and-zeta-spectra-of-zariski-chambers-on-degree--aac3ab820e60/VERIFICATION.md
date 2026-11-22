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

# Reproducible checks and their limits

Invoke `python3 verify_chamber_spectrum.py` in a directory containing this document and the script. The script is self-contained and depends only on the Python standard library. The observed terminal marker was `DEGREE5_CHAMBER_FROBENIUS_ALL_120_OK`.

The calculation constructs all ten exceptional classes in the integral intersection lattice, independently identifies their Petersen adjacency, enumerates all candidate supports via geometric intersection testing and via a separate complete edge-star/triangle classification, and checks identity of the two 76-element sets. It then applies all 120 five-label permutations and checks all seven stated orbit profiles and their fixed support-size coefficients. Exact combinatorial formulas check each fixed-point number and the first two full periods of extension-field counts.

The code does not enumerate degree-five del Pezzo surfaces over finite fields. The universal surface statement instead uses the known classification of their geometric exceptional curves and Frobenius action, the negative-definite-support criterion, and the explicit arithmetic rational-divisor construction written in the proof. The all-degree zeta identities follow algebraically from complete cycle decompositions, not a bounded numerical search. No independent mathematical audit or formal proof-assistant certification is asserted.
