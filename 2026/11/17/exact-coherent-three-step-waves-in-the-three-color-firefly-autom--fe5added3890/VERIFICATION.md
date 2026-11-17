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

# Verification and limits

Use `python3 check_transfer.py` and `python3 check_direct.py`, which require only Python 3 standard library. `check_transfer.py` exhaustively constructs the 729-vertex six-word overlap graph from all 2187 seven-letter words. Tarjan SCC analysis gives the unique cyclic component with 65 vertices and 118 edges; Newton identities on the first 65 integer traces prove the stated degree-four nonzero spectral factor. This certificate covers every ring length and is not a finite-size extrapolation.

`check_direct.py` independently applies the update to all labelled states of lengths 3 through 10 and checks the two directional locks, their intersection and exact temporal periodicity. Both programs were executed in the package directory and their captured output records are included; their claims can be replayed from the included sources.

The independent external audit has not been performed. The proof does not claim every temporally recurrent state is a coherent wave, and the literature search cannot absolutely establish historical priority.
