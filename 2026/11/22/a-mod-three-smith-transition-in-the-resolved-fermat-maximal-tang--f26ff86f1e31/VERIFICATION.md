---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

For d>=3 over C the Hessian forces a maximally tangent point onto a coordinate axis, and each axis point gives contact d by restricting the Fermat equation to its line. The different-pencil crossings are ordinary and distinct: a three-pencil concurrence would require three cyclic coordinate ratios with product 1 but with all d-th powers -1. At the three coordinate centers the blowup separates the distinct tangent directions and contributes one node per pencil line. The connected dual graph therefore has 3d+3 rational components, 3d^2+3d nodes and genus 3d^2-2; each component has valency at least three. In the reduced Laplacian presentation, taking same-pencil differences gives m times each difference, and the primitive sum t_a is the only difference coordinate coupled to the remaining relations. This splits off 3(d-2) independent C_m factors integrally. The first two base-line relations eliminate their hubs with unit coefficients; substituting them in the hub relations leaves d^2(2y_1-y_2-y_3)-t_1-dt_2-dt_3 and its switched counterpart. The third base-line relation eliminates y_3 with coefficient m-2d=1 after passing to differences, leaving the stated 5-by-5 presentation. For p not dividing m the three t_a disappear and the last block has Smith factors d^2 and 3d^2. For p|m and p!=3 that block is invertible, leaving three m-primary factors. For p=3|m, write w=r_1-r_2: the first bottom relation eliminates r_2 with coefficient d^2, and the difference relation is 3[d^2 w+(d-1)(t_1-t_2)/3]=0. The bracket is a valid 3-adic generator since d is a unit and 3|(d-1). This adds a separate C_3 to the three m-primary factors. Reassembling in divisibility order yields both formulas, and the determinant gives the claimed order. The Néron interpretation is the conditional unit-thickness split semistable one, not a claim of existence of a family.

## originality

PASS

The Fermat tangent arrangement and its cross-pencil incidence are known. The component/node/ genus census is a direct consequence of those incidences and is not assessed as independent novelty. The new substance assessed is the integral Smith classification and the residue-three transition for the graph with all three exceptional hubs retained, not the Laplacian formalism or its Néron interpretation.

## value

PASS

The object is the entire natural maximal-contact tangent boundary of the Fermat family, not a chosen subarrangement. The full critical group, unlike just its order, distinguishes the mod-three behavior and gives the exact finite component group whenever the stated semistable model is realized. The bounded-size integral presentation and all-degree primary analysis are useful beyond recomputing a few examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
