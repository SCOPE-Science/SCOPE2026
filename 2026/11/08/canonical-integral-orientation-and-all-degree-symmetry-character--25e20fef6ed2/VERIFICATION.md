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

Run `python3 verify_flex.py` in this directory. The standard-library-only program enumerates all orientation states and all cubical cells for 48 connected graphs: all connected labeled graphs on 2–4 vertices and five representative five-vertex graphs. It verifies every square boundary against the source/sink cellular cocycle, checks exact preservation by each enumerated graph automorphism, and tests the cubical Euler characteristic against the point/circle alternatives. For all four-vertex-or-smaller circular components it independently locates a positive length-\(n\) sink-flip core cycle.

The recorded result in `verification_output.txt` is:

`ALL_VERIFY_OK graphs=48 orientations=1798 cells=3158 squares=201 automorphisms=326 core_cycles=85 components=964 circular_components=122 fixed_circular_character_sum=396`

This is an exact finite sanity check, **not** a proof of the universal assertion. The infinite argument is the cellular cochain calculation, Kozlov's published universal core-cycle theorem, integral Künneth naturality, exterior signs and rational transfer, all explained in RESULT.md. No independent audit or external certificate is claimed.
