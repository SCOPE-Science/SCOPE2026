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

Proof reconstructs periodic points of the compact closure (the dyadic cycles and all-zero configuration), since escaping periods contribute only singleton or zero nonperiodic limits. Distinct words with two or more 1s determine their dyadic gap; N-period singleton placements cover exactly N-r positions, while the other 2r singletons first enter at 2N. The all-zero and period-one all-one blocks give h(1)=2 even at n=1. Summation gives exactly 2n words and first/second moment geometric identities; summably weighted dyadic atoms yield the phase family and differentiation of m(t)=2/t-4/(3t²) gives endpoints 2/3, maximum 3/4 at t=4/3. All n>=1 including n a power of two are covered, and the normalized variance q(t)-m(t)^2 is explicitly justified.

## originality

PASS

Best-of-knowledge original as an exact statement/implication after direct comparison of primary material and relevant published mathematical results; significant inaccessible or indirect antecedents are retained below rather than equated to novelty proof.

## value

PASS

A natural countable zero-topological-entropy but densely periodic subshift separates mere periodic-density and linear word complexity from quantitative least-period penetration; its exact all-n histogram and nonconvergent normalized weak profile give an accessible counterexample and precise benchmark for symbolic dynamical recurrence questions, not an arbitrary finite slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
