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

The package includes `verify.py`, an ordinary standalone Python 3 checker with no third-party Python dependencies. Run `python3 verify.py` from the directory containing the extracted files. Assertions compare the closed formula against direct symmetric-block enumeration and compatible central-functional enumeration, including actual matrix-square and rank tests. Tests cover prime fields \(q=2,3,5\) in small dimensions and the extension field \(\mathbb F_4\) in dimension three. A separate direct check enumerates every \(3\times3\) linear map over \(\mathbb F_2\) and \(\mathbb F_3\) against the original derivation identity, then tests whether its square is zero. A rational-integer checker verifies the product simplification over dimensions one through seven. Tail-weight calculations illustrate the proved limiting law. Successful execution prints `VERIFY_OK`.

This is finite exhaustive verification only for the stated small-field cases; it does not constitute an exhaustive check over all dimensions or prime powers. The unbounded-dimensional claims are derived mathematically through symplectic geometry, exact finite-field matrix counts, and dominated convergence. Independent audit and independent validation have not been performed.
