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

# Reproduction

Run `python3 verify_twisted_ladder.py` from the directory containing the program. Only the Python 3 standard library is used. The shipped `verification_output.txt` contains its actual output, including `TWISTED_LADDER_STABLE_RIPS_CHECKS_OK`.

The finite verifier independently constructs the graph from a cyclic vertex description and the infinite ladder from Cartesian coordinates. It tests every ordered pair of graph vertices against the deck-quotient distance formula; every radius-adjacent pair against uniqueness of its lifted edge; and every graph-metric Rips triangle against compatibility of the three lifted vertices. Twelve stable cases cover \(r=2,3,4,5\) and \(n=3r,3r+1,3r+2\). Ten cases additionally enumerate every clique and check reduced Euler characteristic \(-1\). The last two cases have too many faces for the chosen exhaustive Euler test but still pass all metric and triangular lifting tests. Independent binary boundary-rank reductions establish the reduced mod-two Betti profiles of the strict-boundary examples \((n,r)=(5,2)\) and \((8,3)\).

No finite computation proves the all-parameter assertion. The uniform proof uses contractibility of the infinite-strip Rips complex, uniqueness of lifts from \(n>2r\), and impossibility of a row-flipping triangle at \(n=3r\). It also separately proves the persistence-map statement by commuting deck actions and an explicit graph loop. Neither an external certification nor an independent audit has been performed.
