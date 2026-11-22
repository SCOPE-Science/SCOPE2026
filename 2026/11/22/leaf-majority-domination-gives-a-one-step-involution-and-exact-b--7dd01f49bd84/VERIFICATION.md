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

# Verification notes

The exact all-core proof consists of the leaf-copy identity, strict domination of a unanimous pendant block over all core neighbours, the resulting block-swap involution and a product of binomial first-step fibre counts. It covers all finite simple core graphs and all multiplicities strictly greater than local core degree.

Run `python3 verify_exhaustive.py` and `python3 verify_orbits.py` in a directory containing the included files. The scripts use only the Python standard library. The first program exhaustively checks the full neighbourhood map and the independent binomial basin product on 78 graph/mantle cases, totaling 1,363,612 initial states. The second independently constructs named-vertex graphs and tuple-state trajectories, checks 37,956 initial states on six graphs, and exposes a boundary failure with fewer leaves. The actual recorded console outputs are included. The computational cases are finite and are not a proof for arbitrary core size.

Historical priority is not independently certified. No third-party validation has been performed.
