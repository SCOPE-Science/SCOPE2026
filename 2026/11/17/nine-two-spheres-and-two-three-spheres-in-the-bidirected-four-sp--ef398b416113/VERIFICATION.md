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
# Reproduction and limits

Run `python3 verify_fan4.py` from this directory using a standard Python 3 installation; no third-party dependencies, network access, or external files are needed. The output `verify_fan4.out` was obtained by executing this exact program.

The implementation independently constructs the 14-arc digraph and enumerates all possible 14-bit arc subsets. It verifies the path condition and subface closure; reconstructs every pair of the fixed 74-pair Morse matching; checks all 402 incidences for a directed cycle; applies exact signed integer elimination to every critical three-cell; computes full mod-two boundary ranks 13, 43 and 18; constructs a rational basis of the kernel of the top simplicial boundary using `fractions.Fraction`; and computes the signed chain action of the path-reversal involution.

The finite certificate establishes the claim for this explicitly specified five-vertex fan; it does not imply any general formula for larger cones. Homotopy conclusions rely on standard discrete Morse theory and the Hurewicz identification of the attaching classes of three-cells over a simply connected wedge of two-spheres. This is a self-review, not independent audit or formal mechanized proof.
