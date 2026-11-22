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

The closed-neighborhood formula for every vertex is explicitly proved in `RESULT.md`. The three small block templates have complete nonzero, distinct bit-mask matrices in that proof; the block-composition argument extends them to every integer alphabet size at least three. The general lower bound is by contradiction using empty rows and columns of the selected ordered-pair matrix.

Run `python3 check_bounds.py` and `python3 check_adjacency.py` in the same directory. The standard-library script exhaustively checks all \(84\), \(1820\) and \(53130\) size-\(q\) candidates for \(q=3,4,5\), respectively. It also checks the explicit block constructions for alphabet sizes \(3\) through \(100\). The finite tests are supplementary to the unrestricted mathematical proof and do not establish optimality for larger alphabet sizes.

No independent audit has been performed. Literature coverage may be incomplete, and the present work does not assert an exact formula for the unrestricted optimum above alphabet size five.

The second script independently builds the undirected graph adjacency and checks every vertex neighborhood for alphabets 3 through 100.
