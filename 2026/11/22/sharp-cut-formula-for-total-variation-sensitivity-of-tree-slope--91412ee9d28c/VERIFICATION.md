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

# Reproduction and evidentiary limits

Run the standalone standard-library Python program `check.py` in the same directory. It checks exact rational component averaging against the cut formula for every active edge mask and every graph edge on all 145 labeled trees with two through five vertices. It separately checks heterogeneous masses on paths and three-leaf stars, the sharp unweighted four-leaf-star value, the exact six-node nonlocal example, and the degree-three caterpillar construction at multiple lengths.

The checker also constructs a strictly complementary feasible face for the star with center mass \(1\) and one leaf mass \(10\), verifies exact KKT multipliers under a small finite perturbation, and confirms the attained gain \(20/11\) without solving a floating-point optimization problem. The observed terminal success marker is `ALL_TREE_EDGE_BAND_VARIATION_CERTIFICATES_PASS`.

The infinite family of trees and all positive masses/box widths are established in the analytical proof, using the local-active-face characterization, tree cut basis, and exact boundary accounting. The finite tests are consistency checks, not exhaustive proof. The scientific originality comparison was conducted against the named primary literature and published related mathematical results, with residual historical priority uncertainty. No independent mathematical audit or external certification has been carried out.
