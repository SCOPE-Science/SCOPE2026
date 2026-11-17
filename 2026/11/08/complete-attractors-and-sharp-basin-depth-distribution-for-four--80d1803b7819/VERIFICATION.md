---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

For base twelve width four, K=1727(d-a)+132(c-b) on sorted digits; 77 states (u,v) with 1<=u<=11, 0<=v<=u. J(u,v) is injective on these pairs. The actual 77-row gap_table.csv lists every graph arrow and hitting distance and certifies exactly one 3-cycle and one 6-cycle; the fibre formula W(u,v)=(12-u)*[4(3u-1) if v=0, 6 if v=u, 24(u-v) otherwise] counts all padded strings, with one cycle-member correction for t=0. Independent enumeration of all 12^4=20736 padded strings confirms nonzero basin sizes 4712 and 16012, both complete entry-time histograms, sharp h=7 and the separate twelve repdigits mapping to zero. This finite proof is exhaustive.

## originality

PASS

Kay–Downes-Ward provide general even-base gap principles and classifications of selected smaller bases, not the 77-state exact base12 weighted basin distribution; Hanover focuses primarily on three-digit radix change; published odd-base entrance laws cannot cover base12. Searches for exact cycles and numerical populations found no covering prior table, with unindexed numerical lists remaining a risk.

## value

PASS

The natural four-digit Kaprekar problem in base twelve is the first substantial even-base census beyond cases 4,6,8 surveyed in the primary literature and familiar decimal; the exact full basin populations and hitting-time law for all raw padded strings are valuable as a finite complete dynamical classification. The gap method itself is prior, but sharp two-basin weighted distribution is not a textbook routine.

The dated certificate retains the supplied scientific assessment, sources and limitations.
