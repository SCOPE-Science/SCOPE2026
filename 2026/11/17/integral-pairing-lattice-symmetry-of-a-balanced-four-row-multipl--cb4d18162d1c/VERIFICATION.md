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

# Reproduction and limits

Run `python3 verify.py` in a directory containing `verify.py` and `verification_output.json`; the script uses Python's standard library. Its final JSON object must agree byte-for-byte with the supplied reference output after stripping a terminal newline. It exhaustively enumerates all admissible faces and checks them against a second scan of every twenty-bit mask. It builds the full matching and verifies its global acyclicity by topological sort, calculates all integral Morse boundary coefficients, explicitly constructs signed cycles, verifies integral row/column group actions, derives all thirty-five rational Lefschetz character values and Specht multiplicities, and independently checks mod-two boundary ranks. The check is exhaustive for this finite object, not a certificate for other parameters.

The package establishes an integral third-homology module and a rational fourth-homology module. It does not establish the integral fourth-homology representation, a group-equivariant homotopy equivalence, or a formula for arbitrary board dimensions. Nonequivariant homology ranks admit a duality comparison with an existing complementary calculation; the integral low-degree lattice computation is the specific additional result.
