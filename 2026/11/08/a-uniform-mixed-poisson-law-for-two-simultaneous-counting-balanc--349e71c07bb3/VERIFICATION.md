---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

In the loopless directed p=1/2 independent-arc graph with independent fair four unary labels, let each color difference d_w=(1_p-1_q,1_r-1_s). The global M_n/√n tends to N_2(0,(1/2)I). Conditional on colors, each row v independently sums arc indicators times d_w; mean (M_n-d_v)/2 and covariance (1/4)sum_{w≠v}d_w d_w^T≈(n/8)I. Positive linear counts of color types (1,0),(0,1) ensure full lattice span, allowing uniform Fourier local CLT with Q_{n,v}=(4/(πn))exp(-||M_n||²/n)+o_P(1/n). Directed row independence (including root A_ov) makes root Z_n conditionally Poisson-binomial, parameter ≈(2/π)exp(-||M_n||²/n). Le Cam plus CLT gives a mixed Poisson; for G~N_2(0,I/2), ||G||²~Exp(1), so exp(-||G||²)~Uniform[0,1]. Good-color row bounds O(1/n) and exponentially rare bad labels yield convergence of every fixed factorial moment. Source checker independently enumerates n=2,3,4 and n=3 direct all directed arc assignments, independently checks the mean through K~Binomial(n-1,1/2), and is not used to prove the limit.

## originality

PASS

Ghosh and Schwarzentruber (2026) supply the counting-modal semantics, derive small-model counts and tree asymptotics, and flag random general graphs as a future question. The present fixed depth-two formula on dense directed independent arcs has shared global color fluctuations causing a genuinely nondegenerate uniform random Poisson intensity, absent in independently branching tree models. First-order colored random digraph and mean-aggregation GNN convergence theorems do not address exact unnormalized count equalities. Resultary semantic search surfaced related counting-modal random frame limits but not this precise two-balance law other than the submitted record. The claim is specific and modest; best-of-knowledge priority is qualified.

## value

PASS

An exact natural depth-two counting-modal probability supplies a concrete nontrivial answer in a random-graph setting where the earlier motivating work studied trees. The uniform mixed-Poisson intensity is a mathematically informative counterexample to naive deterministic-Poisson/zero-one heuristics driven by shared global labels. It gives all fixed factorial moments and a closed logical truth probability, without needing a general theory of every counting formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
