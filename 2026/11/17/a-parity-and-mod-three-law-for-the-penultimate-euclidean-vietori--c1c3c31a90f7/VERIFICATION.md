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

# Verification and limitations

The included `verify.py` checks direct three-dimensional coordinates against the closed-form squared-distance shells for every integer \(4\le n\le60\). It independently recomputes the forbidden pairs at the penultimate distance, checking exactly a matching for odd order and one cycle for even order. For \(4\le n\le9\) it exhaustively constructs the corresponding independence complexes and reduces simplicial boundary matrices over \(\mathbb F_2\), comparing all positive-degree Betti ranks with the theorem. Run `python3 verify.py` and check that the last line equals `VERIFY_OK`; `verification_output.txt` contains the recorded output.

The infinite-family assertion, its integral coefficient strength, and its precise endpoint inclusivity depend on the analytic shell-order proof and the established ordinary-cycle independence-complex homotopy recurrence, not on bounded numeric tests. This package does not verify other Rips scales or their persistence maps; no independent external validation has been performed.
