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

For three loopless balanced directed contacts every row and column stochastic matrix is A_p with clockwise rate p and reverse rate 1-p. Its Perron root is 1, so beta/gamma=b is fixed. Initially transmission before recovery has probability b/(1+b). After the second infection, two memoryless unit-recovery infectious individuals contact the remaining susceptible with rates bp and b(1-p); failure probability is 1/[(1+bp)(1+b(1-p))]. This yields P(K=1)=1/(1+b), P(K=2)=b/[(1+b)(1+b+b²p(1-p))], and P(K=3) the complement. The sole varying upper tail strictly increases with p(1-p), establishing first-order stochastic domination, extrema at p=0,1 and p=1/2. Extreme risk gap Delta=b³/[(1+b)²(b+2)²] has unique positive critical point b=(3+sqrt33)/2 and sharp maximum (33sqrt33-189)/8. Independently checked 20 exact rational Markov-state recursions. The competing-risk proof is valid for all b>0 and 0<=p<=1.

## originality

PASS

Best-of-knowledge PASS for the full balanced directed triangle distribution and fixed spectral risk ordering, not for the already known undirected symmetric triangle. The full McCulloch–Roberts–Laing 2016 PDF includes the symmetric endpoint; Ueki–Thompson–Banaji 2026 full HTML and appendix study broader network SIR vulnerability but do not state this explicit one-parameter weighted directed stochastic order. Generic finite-chain solvers can compute instances, not logically imply an optimized all-p theorem. Residual possibility: unindexed directed-three-node table or stronger exact SIR theorem.

## value

PASS

Epidemic networks with exactly the same reproduction-matrix Perron root can have differing exact final-outbreak risk. The smallest loopless doubly-stochastic directed family provides a natural complete benchmark, with a sharp global risk gap and genuine stochastic order rather than one numerical example. Scope is deliberately three individuals and independent exponential recovery.

The dated certificate retains the supplied scientific assessment, sources and limitations.
