---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

The finite chain ring valuation criterion xy=0 iff nu(x)+nu(y)>=ell gives low independent L and high clique H with block A=[[0,B],[B^T,J-I]]. Ideal cardinalities yield B*1_H=-1_L, BB^T=-J_L and |H|=-1 modulo prime p. Solving kernel equations for (z,y): y=B^T z + T1, low forces s+T=0, high-coordinate sum 2T=-s; hence T=s=0 in every characteristic, including p=2. Kernel=(z,B^T z) with sum z=0, so rowspace=(t1_L-By,y), rank |H|+1. Each low valuation layer has cardinality divisible by p, so restricted code dot product is y.y', yielding one-dimensional hull. Constant B-columns occur at the socle and (if ell even) the middle layer; they and only they give singleton codewords and d(C)=1. Equal-valuation low differences prove d(C-dual)=2. Independent direct ring example F3[u]/(u^4) has n=26 rank=9, as asserted; finite equal-characteristic tests do not replace the chain-ring proof.

## originality

PASS

The 2026 Sarkar–Hansda–Maji paper studies the specific F_p[x]/(x^4) graph for odd prime p, obtaining dimension p^2 and hull 1, which are explicitly preexisting special cases. Its claimed adjacency-code minimum distance two conflicts with an explicit socle-column unit word in the same simple adjacency model; the present uniform result instead gives minimum distance one, prime-field rowspace and dual in all nilpotency lengths ell>=3 and all finite commutative chain rings (including mixed characteristic). The graph valuation description is standard; the new content is exact modular code structure and weight-one classification. Potential prior general modular split-graph code theory is a residual risk.

## value

PASS

The adjacency code of a graph is a canonical linear code, and a whole structural class of finite chain rings is intrinsically motivated. Exact rowspace and dual, hull dimension, both distances and first weight-enumerator coefficient for every ring provide useful algebraic invariants and expose a critical coding-theoretic error-correction limitation. This corrects the claimed positive minimum distance of the closest prior special case and extends to residue prime powers and mixed characteristic; it is more than a small exact instance or a restatement of known graph structure.

The dated certificate retains the supplied scientific assessment, sources and limitations.
