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

Under the UNCONDITIONED independent-arc digraph with p=λ/n, source, sink and isolate indicator means are a=q^(n−1), a and b=q^(2n−2); distinct same-type indicators use disjoint arc sets. Source-sink overlaps contain one forbidden arc and isolate-isolate overlaps two. The exact nine moment identities yield the stated 3×3 Sigma with s=e^(−λ). A separate symbolic determinant check gave s⁴(1−s)²[1+(λ−1)s][1−(λ+1)s], positive for 0<λ<1. For the CLT, rth joint cumulants of fixed grouped labels correspond to connected overlap graphs; with d labels require d−1 O(n^−1) edges and sum to O(n); normalized cumulants of order r>=3 vanish, with bounded fourth moments. Directed simple cycles length l>=2 have Poisson limits with means λ^l/l; fixed forcing of t cycle arcs changes at most t local indicator coordinates, O(t/sqrt(n)) in normalized totals, yielding asymptotic independence. Tail expectation sum_{l>L}λ^l/l→0 and positive limiting acyclicity probability (1−λ)e^λ permit transfer to the conditioned law and second moments via uniform integrability. No λ>=1 claim. Independent exact algebra checks confirmed covariance symmetry, determinant and selected finite moments.

## originality

PASS

The full 1995/1996 Gessel paper provides a multivariate finite generating function, so finite distribution is not new. The 2022 Ralaivaosaona paper proves individual marginal normal laws. Neither inspected theorem gives this explicit 3-way conditional Gaussian and its nonzero cross-covariances, and a Resultary ordered-DAG source-sink law uses a different DAG model.

## value

PASS

An explicit nondegenerate joint covariance matrix for three tightly related but non-independent local random-graph counts under global acyclicity, plus a proof of invariance under conditioning and independent rare directed-cycle counts, goes beyond previously published separate marginal CLTs. This is a natural fluctuation classification with meaningful simultaneous observables, not an arbitrary parameter slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
