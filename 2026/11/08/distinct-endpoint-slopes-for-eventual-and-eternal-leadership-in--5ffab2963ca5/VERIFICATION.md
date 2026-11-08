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

Run `python3 verify_endpoint.py` with Python 3. The checker evaluates exact finite-horizon two-color Pólya-urn probabilities using rational arithmetic, exhaustively enumerates all recursive-tree parent-choice histories up to eight vertices under a single deleted edge, independently checks the leading gambler/Beta values, and tests the exponential tail and coefficient identities numerically. It is standalone and requires only the Python standard library.

Analytic proof checks: the initial urn is \((r,1)\), so a strict takeover requires a net challenger gain of \(r\); terminal takeover has probability \(2^{-r}\), and ever-takeover has probability \(2^{-r}+r\int_0^{1/2}x^r/(1-x)\,dx\). The infinite late-challenger estimate begins from \(J\ge8\), uses an independent Bernoulli lower coupling, and separately handles early births by a fixed-history finite-time limit. The coefficients are sums of conditional takeover probabilities, not extrapolations from the diagnostic finite computations.

Limits: the code cannot verify an infinite union or establish publication priority. Full primary text of the closest 2026 source was not obtained in this review, and independent validation has not been carried out.
