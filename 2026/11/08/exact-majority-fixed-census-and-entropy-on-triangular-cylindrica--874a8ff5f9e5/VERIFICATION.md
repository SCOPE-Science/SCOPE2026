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
# Reproduction instructions

Use Python 3 and SymPy to run `python3 check_transfer.py`. This constructs the local 64-state matrix from the stated majority rule, verifies exactly 182 nonzero entries, verifies the characteristic-polynomial factorization over integers, then checks the strict Schur reductions and the trace formula for columns \(3\le n\le11\). The observed output is supplied as `transfer_output.txt`.

Use Python 3 (no nonstandard dependencies) to run `python3 check_direct.py`. This independently applies the synchronous four-neighbor majority rule with tie retention to every labelled configuration for \(3\le n\le7\). It tests 2,396,672 binary configurations and verifies all exact fixed-state counts. The observed output is supplied as `direct_output.txt`.

The transfer characteristic-polynomial identity and Schur inequalities are finite exact algebraic computations included in the proof; their reproducible checker is needed for the explicit spectral formula. Direct enumeration by itself establishes only the checked finite cases and does not certify the infinite statement. No separate external review or independent audit has been performed.
