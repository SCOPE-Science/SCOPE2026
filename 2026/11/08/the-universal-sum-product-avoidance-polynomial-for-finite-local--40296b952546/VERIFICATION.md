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

# Verification
The standalone `verify.py` constructs the forbidden-pair graph from literal ring arithmetic and counts its admissible subsets componentwise; it compares all polynomial coefficients, highest-degree coefficients, total counts, and component type counts to the stated formula. For rings of order at most 13 it also exhaustively enumerates all subsets using the sum/product equations directly. The deterministic output is included as `verification_output.txt` and was reproduced from the standalone checker.

Rings tested: prime fields of orders 5, 7, 11, 13; residue rings of orders 25, 49, 125; the extension field of order 25; the dual-number ring over the field of five elements; and a non-chain local algebra of order 125 with square-zero radical.

The proof relies on the complete symbolic graph classification and simple-root lifting, not on extrapolation from tested ring sizes. Characteristic 2 or 3, nonlocal rings, and noncommutative rings are outside scope. Independent audit: not performed.
