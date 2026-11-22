---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

For a full type-B_n Coxeter normal fan in standard Euclidean Rⁿ, each facet ray is a nonzero signed-support vector. Simplicial fan two-cones correspond to nested nonempty signed-support pairs with compatible signs. For 1≤k<ℓ≤n, their number is 2^ℓ C(n,ℓ) C(ℓ,k); the paired outward normals have dot product k and norms √k,√ℓ, yielding interior angle θ_{k,ℓ}=π−acos√(k/ℓ). Treat each coordinate as belonging to a signed smaller support (2 choices), signed larger-only support (2), or outside (1); requiring both signed support classes gives R_n=5ⁿ−2·3ⁿ+1. Thus uniformly chosen ridge corresponds to Mult(n;2/5,2/5,1/5) conditional on A,B≥1, with θ=π/2+atan√(A/B). A↔B symmetry pairs θ+θ′=3π/2, so mean exactly 3π/4. Difference A−B has variance 4n/5 and delta-method derivative (5/8,−5/8) at densities (2/5,2/5), yielding asymptotic normal variance 5/16. Exponentially rare boundaries plus fourth moments of A−B justify UI and n Var→5/16. The fixed metric, full fan, unweighted ridge counting, and n=2 polygon convention are essential. Independent exact combinatorial checks confirmed ridge totals and exact mean n=2..10. No claim of area-weighted or affine invariance.

## originality

PASS

Prior type-B Coxeter-fan results give signed-support facet chains and ordinary face enumeration, so the ridge count itself is not new. The complete Euclidean angle-by-multiplicity law across every realization with this fan, exact 3π/4 mean, and Gaussian 5/16 variance are metric/probabilistic statements, absent from the inspected earlier primary fan-combinatorics. A contemporary type-D theorem quotes the type-B mean and derives a different fork-deficit; it is a same-day related result, not an earlier general theorem covering the B angle CLT. Mathematical relationship is documented rather than silently treating incidence as new.

## value

PASS

Ridge-angle distributions are natural metric statistics of a classical high-symmetry polytope family. The result shows fan-level invariance despite arbitrary support offsets, gives the entire exact spectrum, a dimension-independent mean and the precise 1/√n fluctuation scale. This is beyond repackaging the classical ridge-count formula and can be used to benchmark Coxeter geometries and metric deformation questions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
