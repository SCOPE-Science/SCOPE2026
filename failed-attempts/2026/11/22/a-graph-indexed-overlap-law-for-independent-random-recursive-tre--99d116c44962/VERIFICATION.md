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

At arrival k the equality moment for A counts k^{c(A)} choices out of k^q, including isolated vertices, giving the claimed rank expansion; different arrivals are independent. Forest rank is |A|, so all edge coordinates factor, not only their covariances. For a simple cycle the independent product differs in exactly the full square-free monomial; after dividing by the independent factors, its coefficient is unchanged when taking the log. Thus the exact cycle cumulant is the sum of k^{1−ℓ}−k^{−ℓ}, strictly positive from k=2 onward and summable for ℓ≥3. Restricting a larger graph to the cycle amounts to setting other marks to one. For n=2 every mark is deterministic, so the stated restriction n≥3 in the converse is necessary. The scalar PGF is the independent insertion PGF of permutation cycles (the Gamma quotient is understood by continuation at apparent poles). For any fixed real projection, the variance is (H_{n−1}−Σ_{k<n}k^{−2}) times the squared Euclidean coefficient norm, by pairwise independence; bounded summands satisfy Lindeberg at √log n and the zero projection is trivial. Near z=1, both factors have identical singleton terms and all higher terms are uniformly O(k^{−2}); shrink the complex polydisc for the first finitely many factors and sum analytic logarithms. Differentiation there is justified by local uniform convergence. Exact bounded replay: take three copies and n=3. At k=1 the parent is forced. At k=2 enumerate eight binary parent triples; on a triangle the overlap vector (2,2,2) and the three permutations of (2,1,1) each occur with probability 1/4; the mixed cumulant is 1/8. On the two-edge path the four pairs in {1,2}² occur with probability 1/4 each. This agrees with direct rational enumeration. The source verifier was inspected, not executed; that finite replay does not establish the general limits.

## originality

FAIL

The decisive prior mathematical object is the multivariate zero-field Potts partition function, not the superficially similar Cayley-tree law. The complete frozen joint law is the immediate independent product of the classical normalized Potts identity with color counts 1,...,n−1. The forest boundary and cyclic residue are the classical forest/cycle factorization defect read from that same identity, followed by independent summation at those color counts. The zeta difference and normalized infinite product are direct evaluations of this specialization, and the fixed-dimensional normal limit is the standard bounded-array consequence. The presentation is correct and useful for this application, but does not isolate a genuinely new claim beyond mechanically extracting these consequences. The mismatch is scientific prior coverage, not unavailability of literature.

## value

FAIL

Shared fixed-label parent edges are a natural agreement statistic, and separating exact, pairwise and limiting Gaussian independence is a meaningful question. The offered result nevertheless adds no independently developed structural claim beyond the direct product evaluation of known graph-coloring laws, the first cycle coefficient already implied there, and standard convergence arguments. It can be useful as an exposition or computational recipe, but the application alone does not clear the scientific-value bar for an independent finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
