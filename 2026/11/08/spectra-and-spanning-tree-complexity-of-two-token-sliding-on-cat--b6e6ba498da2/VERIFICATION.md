---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Any independent cell pair shares a row or column; a third independent cell must lie in that same line. For k >= 3 the unmoved pair forces any replacement into the same line, forbidding an edge of the host. This gives the state count also when one or both binomial terms vanish. For k=2 the horizontal and vertical states are adjacent exactly at a shared incidence, with degrees d_H=2(m-1), d_V=2(n-1) and biadjacency M=B_m tensor B_n^T. The unsigned clique incidences satisfy B_t B_t^T=(t-2)I+J, so their ranks and singular values give all four signed classes and the stated zero multiplicity, including coincident eigenvalues and no zeros at (3,3). The unique top singular value implies one component: each biregular component would otherwise supply an independent top singular vector. In the Laplacian each singular pair contributes d_H d_V-s^2 except for the top pair, which contributes 0 and d_H+d_V. The three nonzero pair products are 2n(m-1), 2m(n-1), and 3mn-2m-2n; the unmatched multiplicities are the two part sizes minus mn. Dividing the nonzero product by the order yields the stated formula and prefactor 4/(mn).

## originality

PASS

The supported contribution is the identification and exact spectral/tree classification of the independent-pair token-sliding graph for categorical clique hosts. Neither the general incidence algebra nor the elementary freeze alone is a novelty claim. No inspected exact prior statement or stronger result giving this host-to-state-graph identification was established.

## value

PASS

The number of tokens marks a natural mobility boundary: two tokens give a connected state graph, while three or more cannot move at all. The incidence factorization then gives the exact spectral and spanning-tree invariants of the last mobile regime for all m,n, rather than a finite table or a generic eigenvalue bound. These identify both the structure and quantitative complexity of a natural reconfiguration family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
