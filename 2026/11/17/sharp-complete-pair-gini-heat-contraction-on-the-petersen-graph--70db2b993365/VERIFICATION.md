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

The Petersen graph on ten 2-subsets of five points with disjointness edges satisfies A^2=2I-A+J, giving eigenvalues 3,1,-2 and nonconstant heat rates 2 and 5. The exact spectral identity 3(H_t x)_i-3(H_t x)_j = e^-2t[(A+2I)x]_ij + e^-5t[(I-A)x]_ij reduces G(H_t 1_S) to G(y+r z), r=e^-3t. Independent enumeration of all 1022 nontrivial ten-bit subsets found max G(y)/(|S|(10-|S|)) by size 11/3,7/2,67/21,37/12,3,... symmetric, strictly below 11/3 except singleton/complement. Convexity G((1-r)y+3r x)<= (1-r)G(y)+3rG(x) proves the all-t bound; singleton coordinates have stable ordering 2+r,1-r,0 and attain equality. Dobrushin half-L1 row distances give delta=(4e^-2t-e^-5t)/3, with the stated positive gap. This proves a continuous-time formula from exhaustive finite graph lemma plus analytic interpolation, not time sampling.

## originality

PASS

The relevant Gaubert–Qu theorem is for Hopf oscillation and dual total-variation contraction, a different Banach seminorm. For the same Petersen kernel the computed oscillation coefficient delta(t) exceeds the exact complete-pair Gini coefficient gamma(t) for all t>0, proving non-equivalence of the two numerical claims. Published Petersen heat-positivity and maximal-operator findings concern different operators/metrics; no inspected source gives the target full t-dependent Gini norm or strict singleton-cut finite lemma. This is bounded priority, not a claim of absolute exhaustiveness.

## value

PASS

PASS: An exact all-time Gini norm on the Petersen heat semigroup is a natural finite graph diffusion benchmark that distinguishes complete-pair dispersion from Hopf/Dobrushin oscillation. The full continuous parameter dependence, strict optimal cut classes and explicit quantitative gap are not a mere textbook restatement of the graph's known spectrum; the exhaustive finite combinatorial lemma has a motivated role and the result does not claim a general graph theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
