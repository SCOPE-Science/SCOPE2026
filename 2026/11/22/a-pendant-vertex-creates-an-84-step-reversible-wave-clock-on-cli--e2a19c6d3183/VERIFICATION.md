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

The executable `verify_kite_wave.py` uses only the Python standard library. Running `python3 verify_kite_wave.py` produced `verification_run.txt` with `ALL_CHECKS_PASSED`.

For every integer clique size 3 through 18, it independently built the complete adjacency and second-order wave matrices over the prime field, checked all predicted fixed-space dimensions up to the asserted global order by modular Gaussian elimination, verified that the claimed power is the identity and that the order cannot be divided by any prime factor. It also exhaustively followed all 6,561 states at size 3, all 59,049 at size 4, and all 531,441 at size 5 using direct vertex updates, recovering the exact temporal orbit histograms.

The proof's critical algebraic steps are the published characteristic-polynomial identity, a new direct kernel calculation of the modular adjacency Jordan structure, and the exact temporal cyclotomic factorization. The finite program does not certify every graph size or extension field; the all-size statement relies on those mathematical derivations. Independent audit of the theorem and historical priority has not been performed.
