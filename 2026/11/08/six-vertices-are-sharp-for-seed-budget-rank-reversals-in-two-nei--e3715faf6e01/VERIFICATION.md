---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

Absolute deterministic threshold-two closure is characterized by two-neighbor forts: a seed set fails iff its complement contains a nonempty subset each of whose vertices has ≤1 neighbor outside. Explicit minimal forts of theta(2,2,3) and bridge-connected two triangles give full contagious-set vectors (0,0,0,10,14,6,1) and (0,0,0,12,13,6,1). Uniform k=3 ranking 10/20<12/20, k=4 ranking14/15>13/15. Independent complete bitmask enumeration visits all connected labeled graphs on n≤6 (1,1,4,38,728,26704), all 2^n seeds, all degree-sequence matched profile pairs; the sole reversing pair at n=6 is those profiles, occurring in 180 and 90 labeled graphs, equal to permutation orbit counts 6!/4 and 6!/8. Exact binomial summation yields independent-seed difference p³(1-p)²(3p−2), so the single interior crossover is 2/3. A six-vertex connected pair has seven edges, making two-seed full activation impossible via edge-count 2(6−2)=8.

## originality

PASS

Published fixed-budget two-seed contagion and complex-contagion path-length literature do not compare full-activation probabilities at multiple seed budgets for degree-matched graph pairs nor classify the unique smallest reversal. The earlier six-vertex clustering example uses expected cascade size at k=2, whereas the present theorem has c_A(2)=c_B(2)=0 and reverses full activation between k=3 and k=4. No direct implication or exact matching table found.

## value

PASS

Same-degree networks can reverse their chances of full adoption solely because the seed budget moves from three to four, and six is the uniquely sharp first order. This exact, fully classified structural counterexample shows degree statistics alone do not order a natural nonlinear diffusion success probability; the complete seed profiles and Bernoulli crossover at 2/3 are useful benchmarks for small network contagion design and analytic fort arguments.

The dated certificate retains the supplied scientific assessment, sources and limitations.
