---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-19.md",
      "INDEPENDENT_AUDIT_2026-11-19.json"
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

For every q>=3 the complete outgoing closed radius-two ball is {abc} union {bcz:z in A} union {cuv:u,v in A}; for a!=c, comparing abc and cbc gives singleton symmetric difference {abc}, forcing all q^2(q-1) endpoint-unequal words. For differing final symbols q(q-1)>q witnesses in Q_c; for same final but differing middle symbols q-1>=2 witnesses in R_{b,c} with <=1 potential collision; for same middle/final but different first symbols the forced self-word separates. q=2 additional differences force 010,101 and one of 000,111; direct exhaustive eight-vertex enumeration establishes exactly two size-seven optima. Reversing triples gives incoming-ball equivalence. Independently written enumeration reconstructed forward balls via two-step BFS and reverse balls via predecessor formulas for 2<=q<=7 and checked all forced singleton differences, all signatures and all 256 binary subsets; finite checks corroborate, not replace the all-q proof.

## originality

PASS

The primary 2019 full manuscript proves the lower bound, binary q=2 exception and radius-one endpoint code, but its radius-two sharpness constructions exclude n=3 and its critical n=2t-1 construction starts at n>=5. Other full relevant published SCOPE results have t=3/4 or the no-repeat Kautz graph. Searches did not find a theorem implying the complete nonbinary q>=3,n=3,t=2 sharp uniqueness; conclusion is best-of-knowledge with explicit unread-source risks.

## value

PASS

The length-three radius-two case is the first natural n=2t-1 boundary excluded from established sharp directed de Bruijn constructions. The result settles an infinite family of alphabets, exhibits a sharp q=2 to q>=3 optimum-size transition, and uniquely classifies labeled optimal sensor configurations; neither a mere textbook deduction from the lower bound nor an arbitrary finite slice. It does not claim higher-radius or longer critical-length cases.

The dated certificate retains the supplied scientific assessment, sources and limitations.
