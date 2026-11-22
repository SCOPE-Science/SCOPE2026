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
# Verification scope

`verify.py` uses only Python standard-library exact integers and rational arithmetic. It builds two-token graph edges by symmetric difference of literal pairs and constructs each triangle independently. For every \(2\le r\le8\) and every \(\max\{1,r-1\}\le n\le r+3\), it verifies that all proposed triangles are present, every edge load is at most one, the sum of triangle weights equals \(|E_{AA}|+|E_{BB}|\), and the mixed-versus-pure cut realizes the claimed value.

The checker also exhaustively evaluates every unordered cut at \((r,n)=(2,1),(2,2),(3,1),(3,2),(3,3),(4,2),(4,3)\), including cases outside the theorem's value range, and tests parity-lift separation for \(3\le r\le9\). The saved `verification_log.txt` records the actual output. Invoke `python3 verify.py` from a directory containing the script; the last line must be `VERIFY_OK`.

Finite brute force does not prove an all-parameter statement, historical priority or independence. The proof is the weighted capacity argument and parity lifting documented in `RESULT.md`.
