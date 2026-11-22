---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

Fourier transforming g_w gives nonzero-scaled exp(-2pi w|xi|). Parseval over integer translates of the transformed window yields two parity-channel Laurent symbols with common D=(1-rz)(1-r/z), r=e^(−2pi w), and numerator Laurent binomials A0+B0 z, A1+B1 z^(−1) for fibers x∈(0,1/2). Independently checked nonzero algebraic determinant A0 A1−B0 B1=√r(1−r)²(1+r), and conjugate Zak coefficient orientations; the upper half swaps orientations. Coprimality forces any null fiber U=D R with Laurent polynomial R; its extreme exponents require four erased rows precisely consecutive if R is a monomial, and at least five if R has wider support because simultaneous internal cancellation contradicts determinant. Thus classification holds for all finite E of size at most four, not a truncated test. Canonical consecutive block {−1,0,1,2} forces R constant only for x∈(0,1/2) and three taps (−r,1+r²,−r); norm gives L² defect. For three consecutive holes, residual coefficient 2r sinh(lambda x) tends to zero as x↓0 despite trivial kernel, ruling out a positive lower frame bound. This is completeness, separate from the existing frame criterion.

## originality

PASS

Belov and Semenov provide a general Poisson-window frame criterion for irregular modulation sets, but frame failure does not imply incomplete span or identify the four-row threshold/defect. The full relevant primary manuscript was inspected. Resultary finite translation-column erasure is the opposite erasure orientation, and its strong frame theorem does not cover this completeness classification. Historical unpublished completeness special cases remain a bounded risk.

## value

PASS

Exact minimum erased modulation rows for loss of completeness, full infinite-dimensional defect space, and sharp complete/nonframe borderline reveal a natural stability-versus-uniqueness separation for time-frequency sampling; this is more than a routine finite erasure fact.

The dated certificate retains the supplied scientific assessment, sources and limitations.
