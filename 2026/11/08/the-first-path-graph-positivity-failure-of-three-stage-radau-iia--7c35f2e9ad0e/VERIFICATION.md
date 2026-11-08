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

The standalone `verify.py` reconstructs all coefficients in the exact identity \(Q(hL)N(h)=D(h)P(hL)\), including the trailing three coefficients, for each unweighted path on two through fourteen vertices. Every required coefficient of \((1+h)^{M_n}N_{ij}(h)\) is checked nonnegative for \(2\le n\le13\), with at least one strictly positive; the denominator remains positive for every real \(h\ge0\). At \(n=14\), direct exact-rational elimination independently verifies the negative endpoint entry at \(h=5/2\). The one-vertex case is immediate analytically.

Run `python3 verify.py` using standard Python 3. The verification is exact, with no floating-point tolerance, external input, network fetch, symbolic-algebra package or finite sampling of real steps. Expected terminal marker: `VERIFY_OK 111905 exact coefficient/sign checks`. The proof is limited to the specified path family and completed Radau IIA update; no independent review has been conducted.
