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

The provided `verify_cube_graph.py` builds the entire integral weight-three reduced Świątkowski complex from the three-coordinate cube, with canonical ordered halfedge-difference bases. It checks the chain identities in both adjacent degrees, and records exact unit-pivot counts 879 for degree two and 448 for degree three, with zero remaining matrices; `verification_output.txt` is the recorded stdout. The integer cancellations prove saturation of the corresponding images. Together with connectedness of the configuration space, they imply \(H_0=\mathbb Z\), \(H_1=\mathbb Z^6\), \(H_2=\mathbb Z^{17}\), and zero higher homology. The computation is exhaustive only for this finite weight-three complex; it is not an independent audit or a general theorem for more particles.
