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

The included standalone checker `verify_pair_fourier.py` uses only the Python standard library. Run it as `python3 verify_pair_fourier.py` in the extracted package directory.

The checker exhaustively enumerates \(S_n\) for \(4\le n\le8\), independently counts permutations without short cycles by recursion, checks the exact character signs and norm expression, and tests the analytic exponential-generating-function coefficient identity to order eleven. It independently checks \(\chi*\chi=(n!/d_n)\chi\) by exact permutation multiplication for \(n=4,5\). The accepted symbolic proof, not the enumeration, establishes all integers \(n\ge4\).

The exact computed norms for \(n=4,5,6,7,8\) are respectively \(4/3\), \(25/6\), \(117/20\), \(406/45\), and \(850/63\). The asymptotic coefficient was cross-checked numerically as approximately \(0.3346952402226447434\). Higher-rank absolute-norm claims are established analytically, not exhaustively enumerated.
