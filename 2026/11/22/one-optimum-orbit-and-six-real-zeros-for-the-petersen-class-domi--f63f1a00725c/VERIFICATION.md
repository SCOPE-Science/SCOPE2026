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

## Reproduction

From this directory run `python3 verify_matching.py` and `python3 verify_partitions.py` with a standard Python 3 installation. They require no dependencies outside the standard library. The first program implements the exact deletion recurrence for matching polynomials of \(T_5\), checks the \(30\) optimal configurations and their \(S_5\) orbit, and certifies six negative real roots by rational signs. The second program independently enumerates all \(115975\) set partitions and checks the open-neighborhood condition directly for every block, obtaining the same coefficients. Compare their output with `verification_matching.txt` and `verification_partitions.txt`. Neither program samples or truncates the finite universe.

## Scope and limits

The computation is exhaustive **only** for the indicated ten-vertex graph; it is not evidence of a general theorem for arbitrary graphs. The general facts about allowable classes and the symmetry orbit are established in RESULT.md. Historical novelty is a literature comparison, not computationally certified uniqueness. This package has not undergone independent external mathematical review.
