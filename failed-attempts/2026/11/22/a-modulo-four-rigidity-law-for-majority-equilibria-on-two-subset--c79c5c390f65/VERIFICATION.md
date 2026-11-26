---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

For n=0,1 modulo four with n>=5, D=(n-2)(n-3)/2 is odd, so open-neighbor strict majority is unambiguous and commutes with bitwise complement. Regard the active pairs as the edges of an ordinary labelled graph with T edges and degrees d_i. Inclusion-exclusion on the active pairs incident to i or j gives N_ij=T-d_i-d_j+[ij active]. Put k=(D-1)/2=(n-1)(n-4)/4. At an active fixed pair one must have d_i+d_j<=T-k. Summing over active pairs gives sum d_i^2<=T(T-k); since sum d_i=2T, Cauchy–Schwarz and T>0,n>4 give T>=n(n-1)/4=m/2. For a nonunanimous state its complement is nonempty and also fixed, so the opposite bound is identical and there is equality. Equality in Cauchy–Schwarz forces d_i=(n-1)/2 for every i. This excludes even n and, for n=1 modulo 4, every simple graph of the requisite degree gives N_ij=(D-1)/2+[ij active], proving the converse and strict local majorities on both colors. Distances 1 through (n-1)/4 in a cycliclabelling construct such a graph at every admissible odd n; expansion of the labelled edge product counts the regular graphs without dividing by automorphisms. At n=5 the only 2-regular simple graphs are five-cycles, numbering 4!/2=12. A separate direct disjointness-mask replay (python3 /workspace/branches/3e0fb83d-c3b3-40b9-95fe-84cfa80e1f12/enumerate_fixed_numpy.py) exhausts 1,024 states at n=5 and 268,435,456 at n=8, with fixed-state active-count distributions 0:1,5:12,10:1 and 0:1,28:1 respectively. The deposited code is exhaustive only at n=5, with 7,500 direct-vs-degree random tests over five sizes and explicit circulants at n=5,9,13. Nothing about primitive two-cycles or even Kneser degrees follows from these tests or the theorem.

## originality

FAIL

The complete classification is a direct equality-case specialization of the published spectral bound for defensive k-alliances, not a known claim merely at Petersen size. Theorem 8 and its inequalities (7), (9) in Rodríguez-Velázquez–Yero–Sigarreta, applied to both colors with k=1 and Laplacian connectivity D-1, force equal sizes and identical minimum crossing degree pointwise. Substitution of the ordinary edge incidence identity makes the regular-graph correspondence and modulo-four split immediate. The source does not itself phrase the corollary in Kneser majority language. The frozen proof is a correct elementary alternative to this spectral derivation.

## value

FAIL

The family is natural, and the active-degree proof is a neat self-contained exposition. However, the exact cutoff and labelled structural classification both follow by substitution and saturated equality in a published broader cut bound; the ordinary edge-product coefficient and circulant example do not give an additional exact invariant. The distinct finite replay at n=8 is corroboration of the same corollary, not a surviving new phenomenon. No scientific novelty or new value is established by recasting the result as a dynamics theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
