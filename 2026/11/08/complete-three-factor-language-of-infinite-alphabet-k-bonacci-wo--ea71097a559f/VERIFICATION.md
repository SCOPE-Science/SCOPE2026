---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

For every k>=3, the published W_n block recursion and suffix pair (t_k(j),j) allow an exhaustive classification of all length-three factors: factors within blocks are inherited or k-shifted, and a triple crossing boundaries meets only one ordinary boundary except the separately analyzed early W1|W0|n transition. The six listed families A0,A1,I1,I2,T1,T2 contain all such boundary triples, with witnesses at stages 2,j,j+1,k+j-1 respectively; shifting whole embedded W_m by hk establishes the reverse inclusion and the exact finite-iterate stage formula. Independent direct-morphism vs stage-expression tests passed 44 (k,n) cases for k=3,4,5,6. This finite corroboration is not the proof for all k,n.

## originality

PASS

Best-of-knowledge originality PASS: the 2020 primary paper establishes two-letter suffix and length-two factor description; the 2026 original article explicitly lists classification of length m>=3 as Problem 1(i). The submitted complete length-three language and finite-iterate witness stages answer that open case. A rationality proof attempt for occurrence generating functions addresses multiplicities, not the triple membership sets.

## value

PASS

An explicit solution of a naturally posed factor-language problem for an infinite-alphabet morphic word, including an all-iterate finite-stage version and constant-case membership algorithm, supplies nontrivial combinatorics directly useful to symbolic dynamics and automata. No unsupported claim to all longer lengths or occurrence counting is made.

The dated certificate retains the supplied scientific assessment, sources and limitations.
