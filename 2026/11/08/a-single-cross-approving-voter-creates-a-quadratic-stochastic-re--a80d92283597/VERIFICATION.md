---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

Reconstructed from Phillips et al. Definitions 2.2, 3.5 and Teh Definitions 2.1–2.2. Every group with nonempty intersection either has an always-satisfied cross-approver or is contained in a pure bloc. Mixed exclusive groups alone have empty intersection even in the EJR+ single-round test. A pure bloc's full-horizon quota is maximal and if it fails, the opposite candidate must have won somewhere, witnessing failure of both EJR+ disjuncts. This proves both directions, including zero quotas. Independent enumeration of all nonempty groups for a,b=1..3, c=0..2, L=1..7 and T=0..L checked 945 profile/horizon/count cases: compute the intersection, union, largest single-option support and maximum voter satisfaction directly; static approval permits taking the largest cohesion demand. All three Boolean outcomes equal the interval test. Term-by-term differentiation cancels interior terms, leaving the two displayed masses. Their ratio decreases strictly from infinity to zero, proving the unique optimum when both quotas are positive; the endpoint cases follow by binomial tail monotonicity. Without overlap, floor/ceiling leaves 1–2 accepted counts so the maximal atom bound and Stirling at p=a/n match. With positive overlap, Chernoff tails and the adjacent failure atoms give the two KL exponents; these bounds also apply uniformly near the interior limit p_* (the atom prefactors are subexponential). Strict monotonicity of the two rate functions in opposite directions gives the unique balanced optimum and Stirling in the finite odds gives p_L→p_*. For a=b and c=1, L>=3 guarantees two positive symmetric quotas and a unique fair-coin optimum. The standardized half-width is sqrt(L)/n+O(1/sqrt(L)); CLT inside (0,infinity), maximal atom times number of accepted counts at 0, and Chebyshev at infinity establish all endpoints. As a finite diagnostic, summing exact integer binomial coefficients at L=n^2 for n=11,21,41,81 gives probabilities 0.724747,0.705194,0.694350,0.688627 against limit 0.682689. The packaged checker was inspected, not executed.

## originality

PASS

Best of knowledge: static EJR/EJR+ equivalence, temporal proportionality axioms and their deterministic achievement pre-exist. The independent stationary lottery classification and optimizing crossover add a different probability question, not a new axiom or binomial limit theorem.

## value

PASS

Quantifies when a stationary independent decision stream can meet established exact collective quotas without coordination: the exact finite bias and failure rate are operationally interpretable, and a change of one approval ballot turns an atom-scale probability into a nontrivial quadratic horizon crossover. This distinguishes independent scheduling from rules guaranteeing quotas through dependence. It is not a new CLT, general voting mechanism, or claim of scope beyond this profile family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
