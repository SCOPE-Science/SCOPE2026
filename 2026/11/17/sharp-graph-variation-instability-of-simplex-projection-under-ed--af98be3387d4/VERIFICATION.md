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

The Euclidean simplex KKT threshold (x_i-tau)_+ gives full-dimensional active-support cells and Jacobian J_A h=h_A-average_A(h), zero off A, all A nonempty. Since this map annihilates constant directions, a discrete layer-cake representation and graph coarea give an exact linear operator seminorm maximum over all nontrivial cut indicators S. For k=|A|, a=|A∩S|, b=k-a, and cut c=|∂S|, cut edges contribute <=c and internal edges <=ab(n-k)/k. Hence L(G)<=1+max_k floor(k²/4)(n-k)/(k lambda); exact integer parity optimization yields F_n=(n²-1)/16 for odd, n²/16 for n divisible by 4, (n²-4)/16 for n=2 mod 4. For n>=4q choose balanced even maximizing k, split the n-k inactive vertices between two cliques and bridge exactly q matched active vertices: each clique has >=q+1 vertices, and every cut splitting one clique has >=q internal edges, while the clique-separating cut has q. The chosen A,S achieve all edge terms with equality. Perturb x_i=r/k on A, -1 off A by epsilon 1_S in the same active cell, giving exact pairs. The n=2,3 q=1 edge cases use a bridge witness. Independent exact rational n=8,q=2 construction yielded quotient 3 matching 1+(64/16)/2; F_n integer expression independently checked through n=16. A single-input graph TV decrease follows scalar 1-Lipschitz clipping after the fixed threshold.

## originality

PASS

Best-of-knowledge PASS: Duchi/Condat/Martins-Astudillo establish KKT and active Jacobians, but no arbitrary-graph TV operator modulus. The earlier published precise cycle graph formula and complete graph Gini formula concern single graph families. The exact all-G active-cut theorem and edge-connectivity sharp extremal family are not consequences of cycle-only or Euclidean norm conclusions.

## value

PASS

The sharp n²/(16q) edge-connectivity envelope exposes quadratic growth of two-input instability despite contraction of each individual graph signal; it relates a natural nonlinear projection problem to graph min-cuts and yields sharp graph constructions for every feasible n>=4q. That is a meaningful stability classification and geometry of extremizers, not merely a new integer table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
