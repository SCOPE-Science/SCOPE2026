---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The bracket forces a derivation's central block to be R(C), where C is its V-block, and leaves the shear B free. Locality on the center implies that T(u wedge v) lies in u wedge V + v wedge V. On basis wedges this rules out disjoint-index terms. Testing (e_i+e_r) wedge e_j modulo its tangent space identifies the off-diagonal coefficient from j to k for any two choices i,r distinct from j,k. Subtract their exterior Lie action. For the resulting diagonal map, wedging its value at (e_i+e_k) wedge (e_j+e_l) with that bivector gives the opposite-pair sum relations on every distinct quadruple. These force the diagonal coefficients to be s_i+s_j: solve on a fixed triple using 2 inverse, extend from the first index, and use the paired sums for all other edges. This proof works over the stated finite as well as infinite fields. Uniqueness follows by recovering the off-diagonal entries and using s_i+s_j=0 on all pairs to get s=0. At a noncentral v+z the shear can absorb any discrepancy from R(C)z by prescribing its value at v; at a central point use C=A. Thus the independent blocks, equality criterion, vector-space quotient dimension and finite-field counts all follow.

## originality

FAIL

The complete theorem as submitted is covered by a distinct verified Resultary finding: the normal form, ordinary-derivation criterion and dimensions match in the same characteristic over every field, with a strictly larger rank range n>=3. The finite-field cardinalities are direct powers of the dimensions already stated there. This is a finding of substantive existing coverage, not a finding that the distinct record appeared first or that either is derived from the other; its displayed UTC date is later.

## value

PASS

The full normal form is a natural structural classification that explains exactly how pointwise derivations can disagree with ordinary ones, uniformly over nonclosed and finite fields as well. The substantial content is the central tangent-space rigidity and the independence of the two blocks, not the routine conversion of dimensions to counts. The useful type of result is distinct from this submission's failure to establish additional content beyond the matched record.

The dated certificate retains the supplied scientific assessment, sources and limitations.
