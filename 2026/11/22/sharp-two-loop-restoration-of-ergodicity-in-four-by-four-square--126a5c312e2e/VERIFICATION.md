---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Summing the local ice equations along a cut shows that the positive-edge counts a and b (equivalently signed fluxes up to an affine normalization) do not depend on the cut. Face reversals preserve both; a directed horizontal reversal changes only a by one and a vertical one only b. Uniform horizontal and vertical orientations independently realize different cuts' flux values, giving necessity. I reconstructed the labelled state space by transfers between rows: for each incoming four-bit vertical row and each horizontal four-bit row, the ice equations uniquely determine outgoing vertical bits; retain binary outputs, concatenate four transfers and enforce periodic closure. Every ice orientation gives exactly one such sequence. Independently tested legal directed traversals by matching the four edges against either traversal orientation, then used graph search (not either frozen checker's union-find) over each designated subset. The result is 2970 states, 8768 facial edges, 69 facial components, 19 for any single designated loop, 11 for any parallel pair and one for every transverse pair. Across the 256 subsets, the numbers of subsets with 1, 5, 7, 11, 19, 69 components were respectively 225, 2, 8, 12, 8, 1. There are 16 minimizing pairs; supersets of a connecting pair remain connected. Positive proposals along all allowed types give the stated equivalence for irreducibility and a self-loop suffices for aperiodicity in that case. Replay: python3 /workspace/reproductions/review_02_ice.py (standard library). Both frozen verifiers were inspected, not executed. This is exhaustive only for the labelled C4 × C4 model and these fixed length-four loops; it proves no mixing-time result.

## originality

PASS

Supports the minimal fixed-position transverse-loop criterion and the associated mixed-repertoire enumeration. The 2970 states and 69 face-only components are established prior overlap and specifically excluded from the distinct claim. Homological necessity and generic loop updates are not new here.

## value

PASS

Face updates on a periodic constrained model are known to be disconnected. The exact smallest fixed update library that removes this obstruction on the canonical labelled 16-site graph is a useful finite benchmark and is not given by topology alone. In particular the result distinguishes allowance of all winding moves from just one specified move of each direction and gives concrete component counts useful for validating simulations. No dynamical speedup or larger-size conclusion is needed for this value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
