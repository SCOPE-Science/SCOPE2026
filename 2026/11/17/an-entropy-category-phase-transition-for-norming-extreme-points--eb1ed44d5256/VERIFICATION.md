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

Let I_n be disjoint successive blocks of size m_n=max(1,ceil(c log_2(n+1))) and lambda_n=n/(n+1). Row sums lambda_n<1 prove non-attainment of T on c0; the disjoint ℓ1 action has norm ∑lambda_n|y_n|<∥y∥_1 for every nonzero y, so the first adjoint does not attain. T**1 has norm one. For iid signs with favored probability q=max(p,1−p), each row is a binomial m_n mean, independent across n. Binomial Chernoff upper bounds and one-binomial-mass lower bounds give n^(−c D_2(r∥q)) up to logarithmic factors; independent Borel–Cantelli proves limsup |row mean|=2R(c,q)−1, R=1 at/below c_*=1/(-log_2q), otherwise D_2(R∥q)=1/c. Multiplying by lambda_n does not change the limsup, and dist(z,c0)=limsup|z_n|. If this is less than one, finitely many initial rows also have modulus <1, giving nonattainment for typical signs. Norming-sign set is the intersection of open dense late-block events, and a zero-density forced sequence of constant blocks gives a full-dimension Cantor subset. At c=c_* the all-favored-block probabilities have divergent sum, so equality case is included. These prove the exact fixed-operator category/measure distinction for every c>0 and p∈(0,1); finite diagnostics alone do not prove any almost-sure claim.

## originality

PASS

A best-of-knowledge new simultaneous product-measure, Baire-category, Hausdorff-dimension and quotient-norm phase diagram for a fixed explicit real c0 block averaging operator. The broad existence of second-adjoint norm attainment and the large-deviation ingredients are prior results, not claimed new.

## value

PASS

The mismatch between Baire genericity/full Hausdorff dimension and Bernoulli almost-sure norming is a concrete natural boundary in the geometry of norm attaining second adjoints. The logarithmic block sizes are exactly the Erdős–Rényi rare-event scale, not an arbitrary finite slice; the relative-entropy rate gives the exact bias-dependent transition and quotient norm, information absent from a bare universal existence result. This exact invariant is independently useful when comparing topological and probabilistic notions of typical norming extreme points.

The dated certificate retains the supplied scientific assessment, sources and limitations.
