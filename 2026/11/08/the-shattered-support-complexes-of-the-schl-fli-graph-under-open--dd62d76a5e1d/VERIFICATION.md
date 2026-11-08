---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducible verification

Run `python3 verify_schlafli.py` from the same directory as this file. The standalone program requires Python 3 only and returns the exact marker:

`SCHLAEFLI_SHATTER_PASS 27 vertices 351 pairs 2925 triples 17550 quadruples 12 S6 top orbits`

The program constructs the \(27\) graph vertices as \(6\) `a` labels, \(15\) pair labels, and \(6\) `b` labels. It cross-compares adjacency from the Picard lattice intersection form and from the explicit double-six combinatorial rules, verifies \((v,k,\lambda,\mu)=(27,16,10,8)\), and checks all traces on every support of size at most four by two distinct representations.

The checks establish the open polynomial \(1+27z+351z^2+2880z^3+1080z^4\), the closed polynomial \(1+27z+351z^2+720z^3+1080z^4\), every triple/quadruple induced-graph criterion, and the twelve \(S_6\)-orbit sizes of four-cliques. Independently, \(2^5>27\) prevents any five-point shattering; downward closure prevents larger shattering.

This finite exhaustive verification does not establish historical priority or provide an independent mathematical audit.
