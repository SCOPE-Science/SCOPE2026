---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

For the resolvent B=(μI+L(K_mn))^-1, block inversion gives within-left off-diagonal c·n/(μ+n), within-right c·m/(μ+m), across c=1/[μ(μ+m+n)]. Two-class Rademacher variance is 4c² times weighted same-color unordered pairs, so minimizing it is maximizing C(x,y)=αx(m−x)+βy(n−y)+nx+my−2xy. For interior grid points, C(x+1,y−1)+C(x−1,y+1)−2C=2(2−α−β)>0; all optima lie on boundary up to color reversal. Concave edge sequences give exact integer optimizers and the proper-coloring transition α(m−1)≤n and β(n−1)≤m; both inequalities cannot fail together. Direct exact enumeration of 147 small cases corroborated, including star (m,n,μ)=(10,1,1) variance 1/4 versus 5/16.

## originality

PASS

Frommer–Rinelli–Schweitzer supply the general stochastic-probing variance identity for fixed colors, but do not solve the global partition optimization for all shifted Laplacian inverses of K_mn in the materially read text. Distinct published hypercube and screened-cycle two-color results have different kernel weights. The sharp improper-coloring phase is a new mathematical comparison within bounded searches.

## value

PASS

The exact all-size classification changes a natural numerical linear algebra design choice: two fixed-cost stochastic trace probes may be better with an improper graph coloring; the sharp phase and star counterexample give an analytically useful criterion not reducible to a routine variance identity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
