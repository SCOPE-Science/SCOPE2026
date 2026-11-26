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

A generic vertical shift exposes exactly one integer-height section, at an independent uniform original height h. In the horizontal lattice the variables are k_i≥0 and their sum is bounded by 1+ch−sum(1−u_i). Decompose 1+ch=K+T: integrality of c makes K discrete uniform independent of T and of the horizontal phases. With W=sum(1−u_i)+(1−T), taking the floor of the bound gives K−floor(W) off a null set. Ordinary Eulerian cube slabs give the weights for floor(W), and weak compositions give B_r. The mass bounds follow by K=m+J and by counting K<J. At m=0 there is a positive contribution from K=J=1, at c from J=0, and at N=0 from K=1,J=2, so no listed support points are spurious; the plateau range includes the entire Eulerian row. Tiling by integer translates gives the mean as the integral of section volume (1+cz)^r/r!. For example r=2,c=1 gives masses 1/6, 2/3, 1/6 at 0,1,3 and mean 7/6. The LLN and K/r's uniform limit give the macroscopic threshold, including the equality case because the limiting uniform has no atom at 1/2. In the critical window the clipped positive part differs from the unclipped one only at J=0 by one. The centered floor-of-uniform-sum variable has CLT variance 1/12 on scale √r and uniformly bounded second moments; uniform integrability and r/c→2 give the stated Gaussian positive-part moment. At fixed r the scaled count differs from (K/c)^r/r! by a uniformly vanishing term, which gives moment convergence and the stated coefficient of variation. Smoothness also follows directly: at either horizontal level the active primitive facet normals are a horizontal signed coordinate basis (at the origin), or that basis with one row replaced by the sloping-facet normal (at a nonzero vertex), together with the level normal; the determinant is ±1. The supplied verification notes and verify_eulerian.py were inspected, not rerun; the finite checks are supplementary. The cube-slab attribution is correct in substance, but the cited Schmidt–Simion section for ordinary slabs is §3 rather than §2.

## originality

PASS

The frustum, its smoothness and its integer-dilation enumerator are prior work, as are cube-slab weights and general translation-count averaging. Distinct claims supported here are the explicit all-atom law for translations of this frustum and its dimension–shear occupancy limits, including the vanishing critical probability with an exact r^−1/2 prefactor. The nearest catalogue and primary sources inspected do not provide these claims for this family; this is not a certification of historical priority.

## value

PASS

A standard smooth family of growing dimension provides an exact example where the complete translate-count law and the probability of finding any lattice point carry information beyond the volume or the Ehrhart polynomial. The closed atom probabilities and plateau enable direct comparisons, and the rare critical-window probability has a useful explicit scaling function distinct from a usual occupancy CDF. These are substantive exact features of the motivated random-translate problem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
