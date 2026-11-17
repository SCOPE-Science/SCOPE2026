---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

Connected bipartite Hall description yields affine space ∑A x=∑B y and all box inequalities plus the one nonredundant Hall x(A0)≤y(B1). Orthogonal projection of ambient normals to this (2n−1)-space gives ell_n=√((2n−1)/(2n)) for a coordinate and sqrt(n/2) for Hall. Hence upper bounds r≤1/(2ell), r≤(n−s)/(n ell+sqrt(n/2)). Centers 1/2 in the box regime, or r ell on A0∪B0 and 1−r ell on A1∪B1 in Hall regime, achieve equality; saturated bounds plus affine equality force uniqueness. Equality of radii would require n−2s=n/√(2n−1), impossible for integers by irrationality/divisibility. Facet classification uses Mori Prop.3.4; independently LP-checked all n=2..4,s=1..n−1 using true projected normal lengths. Finite tests are not the all-n proof.

## originality

PASS

PASS best knowledge for an intrinsic Chebyshev-radius and active-facet transition of a vertex-incidence matching-induced polytope. Balas–Pulleyblank/Mori supply Hall/facet premises, while split-matroid and edge-matching polytope results have different metric objects or combinatorial invariants.

## value

PASS

Sharp, explicit Hall-deficit geometric phase change for a natural one-forbidden-biclique matching family, with unique optimal centers and a discrete facet-orbit switch; metric parameter sensitivity not supplied by general Hall feasibility.

The dated certificate retains the supplied scientific assessment, sources and limitations.
