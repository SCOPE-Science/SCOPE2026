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

For n>=3 the unsigned K_n edge-incidence B has full row rank over characteristic 3. A=B^T B+I and BB^T=(n-2)I+J with J^2=nJ. Rank C^r=rank(BB^T)^{r-1} gives exact length-one/two Jordan blocks in all three n mod3 classes, including n=3. A block J_s(2) or J_s(1) lifts under (u,v)->(Au-v,u) to J_{2s}(1) or J_{2s}(-1), while adjacency eigenvalue 0 yields an order-four two-dimensional block. Frobenius gives fixed dimensions min(2s,3^{nu3(t)}), restricted to divisible-by-2 time for eigenvalue -1; order-four blocks contribute two if 4|t. This proves the all-time displayed E_n(t), global orders 9/18/36, and period populations by Mobius inversion. An independently written exact mod3 matrix implementation checked ALL 1<=t<=L_n and n=3..8 with predicted nullities.

## originality

PASS

The generic reversible previous-state construction and Johnson graph definition are standard. Nearest related published exact wave clocks concern complete bipartite/Hamming/crown graphs or strongly regular graphs in characteristic two. Their adjacency modules cannot be specialized to the signed unsigned-edge incidence Jordan structure over F3 of J(n,2), and no listed stronger result entails the given 9/18/36 n mod3 clock or E_n(t). Claim remains best-of-knowledge versus unindexed modular association-scheme sources.

## value

PASS

The triangular Johnson graphs are a basic natural algebraic graph family. The exact characteristic-three Jordan resonance and its consequences for all-time reversible dynamics supply a structural family classification and precise primitive periods/orbit populations, including a sharp n mod3 phase boundary. The result is not just a routine restatement of finite reversibility or real adjacency eigenvalues, since modular nilpotent chains control the clock.

The dated certificate retains the supplied scientific assessment, sources and limitations.
