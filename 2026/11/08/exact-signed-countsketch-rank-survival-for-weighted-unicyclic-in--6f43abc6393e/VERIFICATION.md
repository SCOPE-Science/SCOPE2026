---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

For connected simple unicyclic n-edge graph with deleted incidence column, weighted matrix B has rank n-1 and 1D left null c_e=z_e/a_e on its unique cycle and zero on attached trees. Signed CountSketch S has kernel dimension n-u (u occupied buckets). Full rank on c-perp is possible only for u>=n-1: no collisions always passes; precisely one doubleton collision passes iff sigma_f c_e != sigma_e c_f. Tree/tree pairs never pass, cycle/tree always pass, different-scale cycle pairs always pass, equal-scale cycle pairs pass with probability 1/2. Counting disjoint hash cases gives [F_n(s)+(ell(n-ell)+binom(ell,2)-T/2)F_(n-1)(s)]/s^n for every integer s>=1 (zero when s<n-1). Equal-scale K is concave in ell with real optimum (4n-1)/6 and distinct-scale discrete increment n-1-ell gives maxima ell=n-1,n (n>=4). Weyl perturbation shows the algebraic rank jump need not produce numerical conditioning. Independently enumerated exact ranks for n=3/4, s=2/3 and weight patterns, matching probabilities 3/8, 8/9, 1/3, 4/9.

## originality

PASS

Best-of-knowledge PASS: rank-preservation bounds and generic sparse subspace embeddings do not give the exact unicyclic cycle-circulation collision coefficient K or equality-pattern dependence on positive edge weights; correlated two-block SparseStack results concern a different input and hash structure. Resultary queries for weighted unicyclic incidence/CountSketch found this candidate and related sketch work, not the exact theorem. Residual priority risk remains for specialized matroid/hashed-incidence literature.

## value

PASS

PASS: Exact rank survival for the natural unicyclic graph-incidence family, optimizers over cycle length and a discontinuity between rank and conditioning give a useful benchmark and a structurally motivated boundary case for random sparse sketch reliability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
