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

Reconstructed the k≤4 fixed-tag survival hazard: P(A⊂S_s)≤C_k(s/N)^k. On surviving e, exact one-step feasible-edge ratio is [binom(s−2,2)−h]/[binom(s,2)−1−d−h], differing from q_s=(s−3)/(s+1) by [L d−2(s−2)h]/[D0(D0−d−h)]. Tag-triple/quadruple bounds yield |a_(s−2)−q_s a_s|≤B s/N³; q_s telescopes to 3/((N−1)(N+1)) and error sums to O(logN/N³). Δ(H)≤2 rules out stopping at size ≥4, so failure iff the terminal pair is forbidden. Independently implemented exact rational residual-pair DP for N=8 with one missing edge, a deleted perfect matching and a deleted path, finding 1/21 for a fixed missing edge in the single-edge case and 8/65 for deleted matching; finite enumeration is only corroboration.

## originality

PASS

Best of knowledge: unique contribution is shape-uniform per-forbidden-edge rare failure and conditional location across ALL degree-two H; the 3/2 constant for the perfect-matching deletion is already known.

## value

PASS

Shape universality for random greedy maximal matchings of almost-complete nonbipartite graphs is a motivated rare-event reliability theorem; per-edge conditional location and uniform error are not obtained from approximation ratios or a single symmetric example. The hypothesis allows arbitrary path/cycle components, hence removes nontrivial symmetry.

The dated certificate retains the supplied scientific assessment, sources and limitations.
