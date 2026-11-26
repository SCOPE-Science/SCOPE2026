---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The six autocorrelation representatives and their negatives exhaust the nonzero differences. Squaring and summing with Haar probability gives equation (1); each two-term modulus is majorized by its phase-aligned value. At S=1 the magnitude expression is 1+2[A(s+2q+2t)+q²+t²+xy+4qt]. Replacing q,t by their AM–GM upper bounds x/2,y/2 produces exactly twice the bracket with h,v, which is nonnegative including at zeros. Then xy=(s²−(x−y)²)/4 and completing the square yield coefficients 11/4 and 3/4 and the sharp ratio 27/11. Vanishing of the squares fixes s=8/11, x=y=4/11 and A=3/11; the bracket then forces four equal nonzero arm magnitudes. Phase saturation of the two center-arm sums says each pair product has the phase of the center squared, which also aligns both cross sums. This gives precisely the listed affine phases and attains the bound. S=0 is trivial. Distinct lags in [-2,2]² remain distinct at independent orders N,M≥5, so the same formula/equality holds there without discretizing coefficient phases.

## originality

FAIL

A separate signed-coordinate-cross record in the current corpus covers the sharp norm and equality cases verbatim after specialization to d=2. Its exact fourth-moment expansion and exact square completion also imply the full five-point deficit, not just the lower bound stated there; the derivation is below. Unequal sufficiently large cyclic orders have exactly the same requisite character moments. This is demonstrable current-corpus coverage, not a claim that the covering record was discovered or appeared first.

## value

FAIL

The five-site cross and its sharp coefficient certificate are useful in themselves, but the submitted narrow result is already recovered by specializing a broader exact invariant and retaining its explicit differences. An unequal rectangle of nonaliasing orders only repeats the same scalar moments. No new structural or quantitative result in the package survives the coverage check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
