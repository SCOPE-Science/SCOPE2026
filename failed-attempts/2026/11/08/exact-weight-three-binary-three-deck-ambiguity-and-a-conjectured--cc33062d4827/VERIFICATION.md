---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

Three two-one deck entries constrain two gap vectors to displacement t(1,-3,3,-1). Equality of 001 changes by t(g2-g1+3t), so nonzero partner exists only for t=(g1-g2)/3 with nonnegative outer gaps. Conserved first two prefix-zero moments determine other deck entries. Each ambiguous pair has unique parametrization (u,h+3t,h,v+t), yielding z^7/((1-z)^2(1-z^2)(1-z^4)); independent full direct deck enumeration for n=3..12 reproduced class sizes and counts.

## originality

FAIL

FAIL. The complete October 25 published Resultary proof gives exactly the same gap involution, all eight deck coordinate conditions, doubleton parametrization, and identical generating function. November 2 papers independently repeat the all-length theorem. The conjecture was already proved before the target November 8 record.

## value

FAIL

FAIL as an independent contribution: the same all-length proof, classification, and generating function were published October 25; the extra period-four coefficient extraction and fixed-weight code-size corollary are direct routine consequences.

The dated certificate retains the supplied scientific assessment, sources and limitations.
