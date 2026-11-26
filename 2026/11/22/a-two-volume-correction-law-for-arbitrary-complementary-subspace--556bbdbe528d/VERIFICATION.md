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

Reconstructed the visible-facet and Dirichlet normalization and checked the result by a separate radial argument. For a visible supporting hyperplane of the joined polytope the support is negative. If it meets only factors in I, the dimension of its exposed face is at most sum_{i in I} d_i-1, so a facet must meet all factors; equality forces an individual facet in each. The common nonzero support levels put the affine difference spaces in independent blocks and add r-1 join directions. Conversely the normals of visible individual facets rescale to common support -1. The cone volumes then factor with the claimed factorial ratio. Independently, in each direction meeting K_i at positive radius let its ray interval be [a_i,b_i]. For block radii rho_i>0 the point belongs to the joined hull iff there are convex coefficients lambda_i in [rho_i/b_i,rho_i/a_i] summing to one (upper bound infinite when a_i=0). The origin-adjoined hull only requires sum rho_i/b_i<=1. The missing region on these rays is therefore the simplex sum rho_i/a_i<1, contained in the first simplex; it is empty when an a_i=0. Integrating the radial densities rho_i^(d_i-1) yields the same factorial ratio times the product of far-radius volumes minus the product of near-radius volumes. Their factor integrals are c_i and c_i-v_i respectively; zero blocks and rays with no positive radius do not contribute. This also handles lower-dimensional factors. Empty factors give zero ambient D-volume immediately because a positive-dimensional block is missing; no approximation to an empty body is needed. Independence factors the finite expectations. The regular-polygon formulas follow by the cyclic retained-edge probabilities, with negative shoelace terms removed by adjoining the origin (diameters have zero term); their square–pentagon substitution gives 155/3072 and 35/1536 as stated. Replay: RESULT.md lines 39–78; VERIFICATION.md and verify.py read without executing the frozen script. Scope is orthogonal complements under the stated Euclidean normalization.

## originality

PASS

The supported distinct component is the exact product correction for arbitrary origin-exterior factors and any number of orthogonal blocks, not the centered free-sum identity or the centered square–pentagon configuration. The inspected comparators establish the centered product, a special join type, or a general cone-volume ingredient. None of the inspected statements supplies the joint near-radius simplex or the visible-facet product correction.

## value

PASS

The identity removes the origin-containment obstacle that makes the standard product unusable for arbitrary convex joins. It compresses full-dimensional volume to two scalars per factor even in the presence of degenerate or exterior layers, and gives a nontrivial expectation calculation under independent deletion without enumerating cross-layer hulls. The value is in the correction and its generality, not the familiar centered special case or a single numerical example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
