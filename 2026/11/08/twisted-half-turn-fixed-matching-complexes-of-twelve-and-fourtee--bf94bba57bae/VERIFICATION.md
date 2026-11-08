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

# Verification of the finite matching certificates

Run `python verify_twisted.py`. The standard-library script constructs the canonical edge sets; independently enumerates the original two-layer prism graph and its involution edge-orbits; checks equality of the fixed orbit-face model to the quotient Möbius matching-face model; generates every matching; applies each monotone edge-toggle stage; and explicitly checks *global* acyclicity by topological sorting the directed full Hasse diagram, including the empty simplex. It also computes all reduced mod-two homology ranks from boundary matrices and compares them with critical-cell predictions.

For the twelve-vertex Möbius ladder there are \(1102\) augmented faces, \(546\) matching pairs, ten critical three-simplices, \(4008\) Hasse incidences, and mod-two reduced Betti number ten in dimension three. For the fourteen-vertex Möbius ladder there are \(3546\) augmented faces, \(1765\) pairs, sixteen critical four-simplices, \(15057\) Hasse incidences, and mod-two reduced Betti number sixteen in dimension four. The full executable output is embedded as `verification_output.txt`.

The finite certificate is exhaustive only for those two sizes; generalization of their wedge multiplicities to further widths is not asserted. The PL orbit-model proof itself holds for every \(k\ge3\). Independent review has not been performed.
