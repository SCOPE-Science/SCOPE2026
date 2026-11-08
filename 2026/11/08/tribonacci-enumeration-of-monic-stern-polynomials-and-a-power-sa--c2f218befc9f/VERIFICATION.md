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

# Verification procedure

Execute `python3 verification/verify.py` using Python 3 with no third-party dependencies. The code checks the algebraic twenty-equation certificate and binary-state closure, reproduces Tribonacci monic and odd-monic block sequences for twenty-two blocks, constructs all Stern polynomials up to index \(32768\), and checks every corresponding state and block count through \(k=15\).

The certificate's finite polynomial equalities and the proof's uniquely solvable formal-power-series recursions together establish the exact generating functions for all \(k\). The independently enumerated polynomials only test the definitions and implementation for a finite range; they cannot establish an infinite-density theorem on their own.

Expected exact check output begins `VERIFY_OK reachable_states=10 formal_transfer_identites=20 polynomial_indices=32767 exact_block_levels=22`.

Known scientific limit: this method bounds reciprocal indices by the larger odd monic set. Priority risk: the full 2016 leading-coefficient chapter was unavailable for close comparison. No independent verification is asserted.
