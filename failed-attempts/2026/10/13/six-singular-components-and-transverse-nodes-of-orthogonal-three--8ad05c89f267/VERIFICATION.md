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

The complete-intersection premise applies over C in the stated range. It can also be checked dimensionally: over anisotropic v1 the first two orthogonalities restrict v2,v3 to v1-perp, and the last is their nondegenerate pairing, giving one irreducible dense locus of dimension 3M−3 (over v2≠0 it is a vector bundle; v2=0 lies in its closure). The nonzero isotropic-v1 locus has dimension at most (M−1)+2(M−1)−1=3M−4, and v1=0 gives 2M−1. Codimension three gives the complete intersection, and generic Jacobian rank three and unmixedness give integrality. A singular point has V H=0 for a nonzero hollow symmetric H. Three nonzero edge coefficients give invertible H and V=0; one coefficient forces two columns to vanish; two force their common column to vanish and the others to be proportional in an isotropic direction. These cases are also sufficient. This yields the six distinct, incomparable M-dimensional components. Each rank-one cone has Segre degree 2(M−1), as the top hyperplane product has one factor from P¹ and M−2 from its degree-two quadric. Adding the three linear degrees gives 6M−3 and the codimension is 2M−3. At generic B, eliminate the two projections onto the nonisotropic column and trivialize its nondegenerate orthogonal complement locally; the equation is the pairing of two copies of that complement. At generic A, use the frozen Witt chart u=xw+yz+s, v=aw+βz+q, r=cw+δz+t, with a near 1 and λ nonzero, eliminating y and δ. For a direct analytic check, change to β'=β+⟨q,q⟩/(2a), t'=t−cq/a, s'=s−xq/a. Then the eliminated last equation is exactly ⟨s',t'⟩−2(λ+c/a)xβ'=0. Absorb the unit −2(λ+c/a) into x. The M parameters a,q,c are smooth and the remaining 2M−2 coordinates form a nondegenerate quadratic hypersurface. These checks establish the actual analytic product, not only its tangent cone, for both strata and hence all six components by symmetry.

## originality

FAIL

The distinct indexed record c10306725487 proves the same reduced singular components, dimensions, Segre and total degrees and generic ordinary quadratic transverse types for the same symmetric-bilinear zero fiber over C, in the stronger range M≥3. The displayed conclusion there is for completions, but its proof gives the same holomorphic normal forms by standard analytic implicit-function and Morse lemmas (or the direct pairing argument below). The equivalence and implication are demonstrable irrespective of the unresolved relationship of the records and their path dates. The older sources checked directly also supply the prerequisite and partial smoothness results; they are not substituted for the decisive indexed comparison.

## value

FAIL

A complete reduced singular locus and generic transverse-type calculation for a natural zero fiber would be useful if distinct. Here the indexed result already covers the locus, degree and local normal forms for a larger dimension range, and the holomorphic reformulation is immediate from that proof. There is no remaining new invariant, non-generic stratum analysis or stronger claim of scientific value in this submission.

The dated certificate retains the supplied scientific assessment, sources and limitations.
