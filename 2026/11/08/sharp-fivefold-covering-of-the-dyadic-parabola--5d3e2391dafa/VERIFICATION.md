---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

For every k>=1 and targets (s,t) modulo 2^k of matching parity, the 5-term mixed-parity base at k=2 lifts via two independent top-bit toggles (add 2^k to one entry; move +/-2^(k-1) between opposite-parity entries). Each operation preserves lower bits and both tuple parities, proving all k by induction. The target (2,0) is not a 4-fold sum modulo 8: square-sum zero forces every entry even and the first coordinate divisible by 4. k=1 gives order 1 and k=2 gives order 3 (explicit 3-term construction). Confirmed exhaustive finite sumsets k=1..7 in independent program; not used as infinite proof.

## originality

PASS

Best-of-knowledge original exact fivefold dyadic parabola covering order and sharp obstruction; the full published triple-convolution theorem and older quadratic congruence and finite-group cover sources do not state the universal fivefold basis result.

## value

PASS

The exact universal additive covering order of a natural polynomial graph over every 2-power ring is a motivated invariant; the mixed-parity lift and modulo-8 obstruction settle a structural local two-moment existence question not a routine table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
