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

The written proof is uniform for all integers \(p\ge3\) and does not rely on computational extrapolation. It gives a deletion-link homotopy cofiber, two integral rank-one homology modules, and exact generator actions. The chain-level Lefschetz argument evaluates the pole swap without a chosen non-equivariant wedge splitting.

Run `python3 check.py`. The script enumerates all independent faces for \(3\le p\le7\), all signed simplicial fixed-face traces for all automorphisms when \(3\le p\le6\) (and selected generators/composites for \(p=7\)), and full mod-two simplicial boundary ranks for \(p=3,4,5\). It checks the predicted trace formula \(1-(-1)^e+(-1)^{p-1}\operatorname{sgn}(\sigma)(-1)^{pe}\) exactly and compares ordinary mod-two Betti profiles with \(H_0=\mathbb F_2\), \(H_1=\mathbb F_2\), and \(H_{p-1}=\mathbb F_2\).

`verification_output.txt` records an actual execution from the package source path before packaging. No finite computation is asserted to verify the theorem for all \(p\), and no independent mathematical audit or external certification has been performed.
