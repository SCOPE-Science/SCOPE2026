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

For every n>=3, support function of all roots e_i−e_j maximizes upper minus lower coordinate, so a facet must have exactly two functional levels corresponding to a nonempty proper subset S; each facet is the orthogonal product of simplices Delta_S−Delta_Sc. Simplex Gram determinant s gives Euclidean a_n,s=sqrt[s(n-s)]/((s−1)!(n−s−1)!). Multiplying by binomial(n,s) yields tilted hypergeometric area law with h=(1−4(X−n/2)^2/n²)^{3/2}; 1-Eh<=3/[2(2n−1)] gives dTV<=3/(4n−5). Hypergeometric CLT yields variance n/8 vs binomial-facet n/4. Facet distance rho_s=sqrt(n/[s(n−s)]); cone decomposition plus Vandermonde yields exact volume sqrt(n)/(n−1)! binomial(2n−2,n−1). Taylor expansion using hypergeometric variance n²/[4(2n−1)] and fourth moment O(n²) gives surface 1−3/(4n), area/volume 1−5/(4n); parity r_n=2/sqrt(n)(1+O(n^-2)) yields 1−1/(4n) tangency deficit. Independent n=3,4,5,30,100 tilt and volume-cone checks, while original checker separately uses Qhull n=3–6; finite checks corroborate, not prove all n.

## originality

PASS

Facet *classification* and known volume are previously established background, but actual intrinsic Euclidean facet areas, their global area-weighted hypergeometric tilt and explicit TV rate, Gaussian variance-halving relative to counting facets, and first-order inball tangency deficit were not implied by the inspected primary and published results. The standard Euclidean embedding and physical surface measure are essential and not lattice/Ehrhart substitutes.

## value

PASS

Intrinsic surface measure of the maximally symmetric complete type-A root polytope is a natural geometric invariant, distinct from normalized volume and face counting. The exact all-n distribution, explicit total-variation rate to a natural hypergeometric law, halved asymptotic facet-size variance, and quantified asymptotic inball tangency answer concrete surface-geometry questions that researchers could use. The previously known facet labels and volume are credited, not presented as new standalones.

The dated certificate retains the supplied scientific assessment, sources and limitations.
