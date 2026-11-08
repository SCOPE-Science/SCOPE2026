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

Run `python verify_lucas_reciprocal.py` using Python 3.11 or newer. The script constructs \(F_n\) recursively in integers and computes strict partial-sum crossings using exact rational arithmetic. For every \(2\le q\le p\le10\) and odd \(1\le k\le91\) it compares the exact minimum against the published cutoff interval, and calculates the predicted phase with 110-digit decimal precision. It records 2,070 parameter-index cases, 2,069 phase predictions agreeing exactly, and the explicit small equality exception \((p,q,k,J,J_{\mathrm{phase}})=(2,2,1,4,3)\). It also reports sample values of the density parameter \(\vartheta\).

The unrestricted proof uses a convergent Binet-geometric expansion, an \(O_{p,q}(\rho^k)\) relative-error bound, irrationality via conjugation in a quadratic field, and Weyl equidistribution on odd indices. Exact finite computation neither supplies nor replaces the latter infinite argument. The phase formula is not asserted at every odd index. Numerical logarithms in the verifier only evaluate illustrative finite predictions, not the theorem's analytic constants.
