---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For every labelled 3-by-n periodic Moore torus n>=3, a centre column of b live cells has eight distinct neighbours and depends only on u=a+c; the four exact local fixed conditions are b=0:u!=3, b=1:u=3, b=2:u=2, b=3:u<=1. Weighting each legal (a,b)->(b,c) transition by binom(3,b) exactly enumerates column placements, hence N_n=tr(T^n). Independently reconstructed the full 16-state integer transfer, the 10-state primitive block, determinant x^3(x^3-27)P(x), exact traces n=3..10, and the positive Collatz-Wielandt vector giving 2.70<rho(B)<2.71<3. The weighted 3-cycle contributes 3^(n+1) only for 3|n; the other transient states contribute no trace. This proves both all-n exact formula and two subsequential growth scales; finite enumeration alone would not.

## originality

FAIL

FAIL: the mathematical main claim is an explicit specialization of an already published comparison theorem for Conway Life versus HighLife on the identical labelled 3-by-n Moore torus. That source has exactly the Life polynomial P, the 3^(n+1) indicator term, and the Perron root near 2.70363. Its 30-state block with 20 zero roots and the target's 10-state quotient are spectrally equivalent on trace powers. The comparison even provides a stronger two-rule contrast. Both published on 2026-11-17, so no individual or temporal precedence between same-day records is asserted; implication-level coverage is decisive for this standalone claim.

## value

FAIL

FAIL: the small-state occupancy transfer is correct and useful as an alternative derivation, but its complete stated theorem, count sequence, sharp mod-three effect, and spectral scales are already in the stronger published Life/HighLife formula. The state compression by itself is not developed as a distinct motivated classification, new invariant or independent result; reproducing a known exact table with a smaller matrix does not make the original claim valuable as a new finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
