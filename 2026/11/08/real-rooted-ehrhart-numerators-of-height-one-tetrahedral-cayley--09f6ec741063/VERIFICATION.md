---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

The height-one Cayley polytope conv((aΔ3,0),(bΔ3,1)) has integral slices at t=j of kP of size binomial(a(k-j)+bj+3,3). The exact k+1 term sum and fourth-order finite difference derive the asserted h1,h2,h3 coefficients and h4=0 by width-one interior-point obstruction. With X=a-1,Y=b-1, the h_i are explicit positive polynomials (except degree-drop h3). For X+Y=0, h*=1+3z; for X+Y=1, h*=1+9z+5z² with positive discriminant 61. Otherwise the cubic discriminant satisfies an exact identity 432D=Σ c_ij X^iY^j with 90 strictly positive nonzero coefficients, including linear coefficients 7776 each, hence D>0 on integer X+Y>=2; all three roots are distinct real and negative because coefficients are positive. Independent SymPy computation from the h_i formulas reproduces exactly 90 positive coefficients, c_10=c_01=7776 and constant zero. Six facets, primitive edge-direction determinants ±1 at each vertex and integral height coordinate show smoothness and lattice width one.

## originality

PASS

The closest 2026 Liu–Tang–Tao–Zhang result classifies smooth few-facet geometry and proves ordinary Ehrhart polynomial coefficient positivity, not a statement about all zeros of the *numerator* h* for this non-product tetrahedral frustum. A different 2026 published Cayley family R_{2,c} is seven-facet and has 2-simplex×segment fibers, so its one-parameter cubic-discriminant root statement does not cover the present two-parameter six-facet tetrahedral bundles. Ferroni supplies counterexamples to h* unimodality for other Cayley polytopes, and Nill large-width real-rootedness cannot apply to exact width one. The strongest plausible original Liu paper remained inaccessible in full, which is recorded as a real priority risk rather than automatic O failure.

## value

PASS

The lattice width-one all-two-scale tetrahedral bundle is a natural smooth four-polytope family at the exact structural boundary where generic real-rootedness is not guaranteed. A complete two-parameter real-simple-negative numerator-root theorem with a fully checked sign-positive discriminant identity is a meaningful exact classification, beyond merely proving Ehrhart coefficient positivity or testing sample frusta. The result does not claim all smooth six-facet polytope numerators.

The dated certificate retains the supplied scientific assessment, sources and limitations.
