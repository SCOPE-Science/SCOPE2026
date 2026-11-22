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

Connected cuts with both induced sides connected classify all facets of a connected graphical zonotope; their Euclidean facet measures are sqrt(|S||T|) times the product of induced spanning-tree counts. The complete-split graph has exactly 2q peripheral-singleton directed facets and (2^p-2)2^q clique-splitting facets with the stated expressions. Matrix-tree gives τ(K_a∨I_b)=(a+b)^(a-1)a^(b-1), including a=1/b=0 boundary. Reweight the split-cut sum by T∼Bin(q,k/p), derive fixed-p expectation q^(p-1)(constant+O_p(q^-1)); divide by the 2q singleton area to obtain A_p q^-3/2+O_p(q^-5/2). For p→∞ express A_p/p^1.5 as two symmetric endpoint sums of binomial mass b_(p,k)/[k(1-k/p)]^1.5, dominate by O(k^-2) and use b_(p,k)→e^-k k^k/k!. This gives C*=∑ e^-j j^(j-3/2)/j!, not a simultaneous two-parameter limit.

## originality

PASS

Classical spanning-tree/connected-cut results supply the necessary finite formula framework. The directly related published K_(2,q) complete-bipartite area theorem establishes the same concentration exponent for a different graph with coefficient 2; it does not contain the complete-split clique area spectra A_p for p≥3 or the endpoint C*. Primary Padrol–Pilaud–Poullot covers combinatorial normal fans/deformation cones, while Dukes gives the tree count. No strong source directly covers the two-level asymptotic; unknown equivalent work remains possible.

## value

PASS

This computes the complete intrinsic facet-area spectrum for a natural two-parameter family of graphical zonotopes, not just a combinatorial face count. A vanishing exponentially small fraction of singleton facets captures almost all boundary area, with a sharp family-dependent q^-3/2 deficit and an explicit nontrivial endpoint-Poisson limit as clique size grows. These results illuminate the mathematically meaningful contrast between uniform facet sampling and surface-area sampling.

The dated certificate retains the supplied scientific assessment, sources and limitations.
