---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

For each output edge, harmonic-measure difference nu is a zero-mass leaf signed measure; telescoping along root-to-leaf paths gives its exact dual edge-Lipschitz norm as sum over cuts |nu(C_e)|. The sign of each cut is realizable by a tree potential (acyclicity), hence not merely an upper bound. For non-path trees, leaf-distance witness g=d(a,.) gives Lg=2-deg<=0; w=H(g|leaves)-g solves Lw=deg-2>=0 with positive source at a branch and zero on boundary, so strict maximum principle yields w>0 inside, forcing an edge slope >1. On paths affine interpolation is norm one. On spiders, center is conductance-weighted by inverse arm lengths; directly bound output slope by 1+(m-2)/(L_i sum 1/L_j), exact with distance-from-shortest-leaf boundary data; simultaneous triangle-equality saturation gives all norming data. Shortening a minimum arm to one reduces denominator, and reciprocal convexity balances others for fixed n,m. AM/HM lower bound and balanced witnesses give (1/2+o(1))sqrt(n) and strict 1+sqrt(n-2)/2 upper bound. Exact rational verification source read and bounded independent reasoning; previous code tests are finite only.

## originality

PASS

IMPORTANT partial prior coverage: the October 26 2026 weighted-metric-star theorem explicitly gives ||E_w||=max_i sum_{j≠i}w_j(L_i+L_j)/L_i; substituting physical unweighted-tree effective conductances w_i=(1/L_i)/sum_h(1/L_h) already implies the standalone spider norm formula. That formula alone is NOT credited as original. What survives includes general finite-tree cut/hitting-measure identity, iff-path nonexpansivity, complete norming leaf-boundary extremizers, fixed-vertex and leaf-count balanced-arm optimization, and sharp worst-spider sqrt(n)/2 growth. Naor-Sheffield proves existence of nonlinear infinity-harmonic nonexpansive extension rather than stability of the particular mean-value harmonic linear operator. Abodayeh-Anandam gives tree Green identities and Dirichlet solutions, not sharp Lipschitz operator norms. Best-of-knowledge PASS based on surviving compound theorem.

## value

PASS

Determining when a canonical energy-minimizing extension is Lipschitz nonexpansive and how badly it can expand on trees is a natural metric-potential problem. The general tree computable cut norm, path-only obstruction, extremizer geometry and worst-spider sqrt(n) growth remain useful even with the fixed-star norm antecedent.

The dated certificate retains the supplied scientific assessment, sources and limitations.
