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

For every canonical plane full binary tree with n>=3 internal nodes, the inorder Loday coordinates are v_i=L_iR_i; every pair of the n+1 leaves has a unique LCA, hence sum v_i=n(n+1)/2. At root with left/right leaf counts a,b, the polynomial identity a²b²+S(a-1)+S(b-1)-S(a+b-1)=ab(a-1)(b-1), S(k)=sum_{j=1}^k j², inductively proves sum v_i²=S(n)+sum_u L_uR_u(L_u-1)(R_u-1). Subtracting n(n+1)²/4 gives exact squared-radius baseline n(n²-1)/12 plus nonnegative local penalties. Each penalty is divisible by 4 because both L(L-1) and R(R-1) are even. Zero penalty iff every node has a leaf child, yielding 2^(n-1) combs. Least positive penalty 4 requires exactly one internal node with L=R=2 (two cherries) and all ancestors unilateral leaf attachments, giving 2^(n-3) trees. All other penalties at least8; n1,n2 exceptional single-shell boundaries explicitly excluded. Independent enumeration of ALL tree profiles for n1..9 reconstructed coordinates and penalties and matched every exact radius and both shell counts. Finite enumeration corroborates but induction proves arbitrary n; the center is the known Loday vertex barycenter, not asserted min enclosing ball.

## originality

PASS

Best-of-knowledge original exact metric TREE STATISTIC and first two Loday vertex-radius shells. Classical coordinate formula, known permutahedron barycenter and comb common vertices are acknowledged prior; earlier facet inradius and Euclidean edge spectrum concern different metrics. No dominating vertex-shell classification was identified, with tree-imbalance aliases remaining a concrete risk.

## value

PASS

The canonical Loday associahedron is a central Catalan polytope and the vertex barycenter provides a natural Euclidean reference. Its local nonnegative branching defect formula is a structural identity that quantizes ALL squared radii modulo4, immediately classifies nearest and second-nearest trees with sharp dimension-independent squared gap4, and counts both shells exactly (2^(n-1),2^(n-3)). Those tree-shape stability statements are usable at every dimension, not a numerical experiment or routine preexisting barycenter statement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
