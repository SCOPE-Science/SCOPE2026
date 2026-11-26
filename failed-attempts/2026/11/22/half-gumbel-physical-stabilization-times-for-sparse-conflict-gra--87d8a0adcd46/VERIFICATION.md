---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Under the stated atomic free-color guard, a recoloring never creates a conflict, and the first activation of either endpoint removes each initially conflicting edge. Thus T is the maximum of the endpoint minima of the independent first activation times, with T=0 for no conflicts. At t>=0 the untouched vertices are iid Bernoulli(e^-t), giving the independent-set CDF and the equality with the zero-edge event. The line graph is a valid dependency graph, including independence of each indicator from the entire family outside its dependency neighborhood. Including self-pairs gives b1=(m+D2)q^4; the ordered distinct adjacent pairs give b2=D2 q^3, since they share ONE vertex and their union has three vertices. The frozen proof's 'share exactly three endpoints' is a wording error, not an error in the formula. The external-dependence term is zero. At t=(log m+x)/2 the mean is e^-x, the q^4 error is O_x(m^-1+D2/m^2), and the q^3 error is O_x(D2/m^(3/2)); all vanish under the stated hypothesis. D2<=2m Delta gives the degree corollary. A star survives iff its center and at least one leaf are untouched, and a clique completes iff at most one vertex remains untouched, giving both advertised boundary laws. The hypothesis is sufficient only. The frozen checker was inspected, not run; its exact finite cases concern the scheduling reduction, retained-set sums and pair counts, not the Poisson limit.

## originality

FAIL

The exact clock representation is covered by the cited stabilization paper. Combined with the established local-dependence Poisson theorem, the proposed bound and scaling are direct specializations: the usual two error sums reduce to self-pairs and ordered adjacent pairs without an additional probabilistic argument. The independent-set formula and the two exceptional laws follow immediately from the same representation. This assessment is about prior implication, not an assertion that an inspected paper prints the exact D2 statement verbatim.

## value

FAIL

Physical completion is a motivated observable and the resulting formulas are useful expository examples. But the record adds only a routine application of a standard bound to a known clock representation, with an elementary sufficient degree condition and immediate extreme-order-statistic examples. It does not establish a nontrivial boundary, characterize when convergence holds, or handle graphs beyond the generic error bound. No distinct valuable remainder is established as a repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
