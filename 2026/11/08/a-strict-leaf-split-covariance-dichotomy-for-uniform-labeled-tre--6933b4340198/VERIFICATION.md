---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

For fixed S of size k, exactly one crossing edge has probability k^{k-1}(n-k)^{n-k-1}/n^{n-2} by two Cayley trees and a uniform joining edge. The two internal trees and join endpoints become independent uniform conditional on S; each component contributes g(m)=m(1-1/m)^{m-1} surviving leaves (g(1)=1). Summing split indicators (dividing equal-size splits by 2) yields Cov(L,B_{n,k})=b_{n,k}[g(k)+g(n-k)-ell_n]. When k=1, B=L and Var(L)>0 for n>=4. For k,n-k>=2 the proof bounds g(m)<(m+3/4)/e and ell_n>(n+3/2)/e using convergent log series and concavity, so covariance<0. Expanding gives conditional deficit -1/(2e) for both sides growing. Fresh independent Prüfer enumeration computed all mixed moments n=4..6 using exact fractions and checked formulas/signs. Algebra establishes all n>=4, not enumeration.

## originality

PASS

The key joint finite-n vertex-split/leaf statistic is not the marginal leaf fringe variance or deterministic phylogenetic leaf-set split balance. Inspected Janson and Fischer–Liebscher relevant primary sections do not state the all-size sign dichotomy. Meir–Moon (1970) related cutting model full text was not accessed: named residual priority risk. Resultary returned other correlations with different pair statistics.

## value

PASS

A natural local-vs-global structural covariance phenomenon in a classical uniform labeled random tree is completely classified at all admissible n and cut sizes, including universal macroscopic conditional loss; not a tiny unmotivated instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
