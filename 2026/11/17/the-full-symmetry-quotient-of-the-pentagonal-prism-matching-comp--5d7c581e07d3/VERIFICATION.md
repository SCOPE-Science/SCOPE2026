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

# Exact reproduction

Run `python3 verify_prism_quotient.py` from the directory containing the embedded standalone file. No third-party packages, network services, or external files are needed.

The program generates all 341 nonempty matching faces of the ten-vertex pentagonal prism, all barycentric flags, 20 group automorphisms, and 928 geometric quotient cells. It checks every cellular boundary squared, six finite-field Betti calculations, and the 463 unimodular integer cancellations yielding exactly one zero-cell and one three-cell. It separately constructs a spanning tree and eliminates all 61 fundamental-group generators with triangle relations. The all-rung simplex has a group-fixed barycenter, so the simply connected quotient conclusion follows by the published orbit-space fundamental-group theorem.

These are exhaustive finite computations for this particular graph. No claim about other prism widths is made; this is a self-review, not an independent audit.
