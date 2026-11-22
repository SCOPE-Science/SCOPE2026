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

# Reproducible verification

Run from the extracted package root (Python 3, standard library only):

```sh
python verification/check_fano.py
python verification/check_pg3.py
```

The first program constructs the fourteen-vertex Fano incidence graph and computes its distance matrix; exhaustively enumerates all independent sets of size six or seven; finds the 70 feasible colour-1/colour-2 class pairs; assigns every one of the 720 permutations of the higher named colours; checks 50,400 resulting colourings; and tests every potentially valid one-vertex recolouring into colours 1 and 2 in the eight-name palette. Moves into a different higher colour are excluded a priori, since all higher colours are occupied and the graph has diameter three. It verifies 40,320 edges, 10,080 degree-four centres and 40,320 degree-one leaves.

The second constructs the 26-vertex order-three projective-plane incidence graph by homogeneous coordinates modulo three, exhaustively enumerates its near-maximum independent sets and all 260 feasible reduced low-colour configurations, then tests both directions of every possible 1-to-2 or 2-to-1 move. It verifies 26 degree-nine centres, 234 degree-one leaves and 234 edges. Its reduced state space ignores permutations of higher singleton colour names, and the general proof justifies that reduction.

These finite tests reproduce the stated small-order checks but do not constitute an independent all-parameter proof. The infinite-family assertion depends on the exact incidence argument in RESULT.md. The inspection of accessible literature is not an absolute guarantee of novelty.
