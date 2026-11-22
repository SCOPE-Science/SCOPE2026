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

The first program constructs the edge-adjacency graph of the binary three-cube, checks there are 24 edges, exhaustively branches on orientation bits with degree pruning, and applies the full integer Walsh transform. Its result reports 600 balanced orientations, 9,500,672 zeros, minimum nonzero multiplier 4, minimum even vanishing weight 4, and projection norm 29471/2048.

The independent Python implementation first solves the mod-two incidence constraints by spanning-tree leaf elimination and then enforces outdegree two. It checks 600 states among all 8,192 parity-admissible vectors, performs a second integer Walsh transform and obtains 4,639 reduced zeros and 3,553 reduced surviving frequencies. It asserts Parseval's identity, exactly zero vanishing two-edge characters, exactly 864 vanishing four-edge characters, minimum absolute nonzero value 4 and the same projection norm. A separate symmetry checker generates all 48 cubical automorphisms, checks group images of the quartic zeros, and certifies 21 orbits, of sizes 48 (15 orbits) and 24 (6 orbits).

The calculations are exhaustive only for the specified finite graph. Full external validation and literature-priority certification have not been performed. The included code and output data permit reruns but must not be mistaken for independent institutional certification.
