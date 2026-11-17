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

Execute `python3 verify_direct.py` and `python3 verify_transfer.py`; execute `python3 verify_symbolic.py` with SymPy installed. The actual standard outputs are stored respectively in `direct_output.txt`, `transfer_output.txt`, and `symbolic_output.txt`. The first program simulates all graph vertices from the update definition and exhaustively verifies the local reduction and run formula for \(3\le n\le8\) (\(174720\) labelled states). The second independently implements a transfer automaton and checks every coefficient through \(n=45\), including exhaustive binary rim words through \(n=12\). The symbolic program verifies an exact determinant and the strict-density identity. All three ran successfully.

The proof for every \(n\ge3\) rests on the explicit local necessity/sufficiency, the labelled run bijection, and finite-dimensional Perron–Frobenius arguments in `RESULT.md`; no finite calculation establishes the asymptotic or excludes all previously published equivalents. The chosen dated primary preprint was first publicly posted August 14, 2015. A related 1988 article was read as background without assigning an unsupported day of first public appearance.
