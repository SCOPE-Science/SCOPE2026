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

# Mathematical verification

The exact finite-tooth first-passage Poisson equation has been solved directly in rational arithmetic, including the single-tooth closed form and the length-increment identity. Full heterogeneous finite-ring Markov generators were assembled independently; their exact stationary currents agree with the theorem. Running the included file with `python3 check_comb_tail.py` prints `PASS 90 exact recurrence / incremental / finite-ring checks`. The code requires only the Python standard library. Additional numerical Riemann sums were evaluated for six tail exponents on decreasing return-rate sequences; their normalized values approached the corresponding theorem constants.

The thermodynamic limit uses an iid strong law and truncation at infinite first moment. The asymptotic theorem requires the uniform hyperbolic increment bounds, Riemann sums and borderline harmonic estimates established in `RESULT.md`. Finite enumeration and numerical convergence are not independent proofs of these infinite statements. No independent audit has been performed. Priority over unindexed or implicit prior work remains unverified.
