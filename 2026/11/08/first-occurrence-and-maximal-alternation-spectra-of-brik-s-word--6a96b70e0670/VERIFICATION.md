---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

For B_(i+1)=B_i plus suffix beginning at i+1, the length is 2^(i-1)+i+1, no 00 appears, and the stable trailing 1101 for i>=3 forces new (01)^k, k>=3, to cross the unique join starting at length(B_i)-1. The source window first appears at i+1=r_(k-1), giving r3=38 and r_k=2^(r_(k-1)-2)+r_(k-1)-1. The start shift and no-00 extension give all four orientations/parities, and the first-containing stage gives A_i=2K_i+1. Independently constructed stages 1..18, checked full maximal alternating lengths and r3, and the integer r4=68719476773. The unbounded claim is an induction, not a finite extrapolation.

## originality

PASS

Full original Shallit manuscript supplies recurrence and language but no alternating first-hit spectrum. A same-word published factor-completion theorem supplies only global latest-first-occurrence maxima, which do not determine every alternating first position. Own source gives a new exact nested growth and exact first stage of alternation, all k.

## value

PASS

Alternating-factor hitting times are a natural combinatorial statistic in a nonuniformly recurrent word with enormous gaps. The exact tower-like recurrence and complete stage spectrum resolve a meaningful quantitative gap not supplied by mere factor existence or constant-run onsets.

The dated certificate retains the supplied scientific assessment, sources and limitations.
