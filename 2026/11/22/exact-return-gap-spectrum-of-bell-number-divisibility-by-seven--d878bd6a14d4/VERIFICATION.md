---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Touchard's recurrence with the correctly reduced Bell seed determines every residue. The shift identity at P=137257 gives a period, also independently certified by exact return of the complete seven-term state. The frozen Step 2 checks least period of the full residues, not automatically that of their zero-indicator. The indicator assertion follows from the certified census itself: if its least period d properly divided P, P/d would divide the zero total 19608, impossible since 7·19608=P−1. The replay additionally checked indicator mismatches at n=9 for shift 29 and n=1 for shift 4733. It traversed every index of [0,P), compared all 50 CSV entries (which agree with the printed table) and counted the wrap gap of 12 once. Counts sum to 19608 and their weighted sum is P. The unique largest gap is 85736→85801, so the given 64-index interval is zero-free and 65 is the sharp universal window. Touchard implies that zeros seven apart force an intermediate zero at the next index, independently proving the exclusion of gap 7. Cyclic repetition gives each limiting frequency with denominator 19608.

## originality

PASS

Best of available evidence, the supported distinct claim is the complete first-return distribution, especially its nonlocal tail and sharp 65-window, including the unique long gap's location. Do not credit the already known residue period, Touchard recurrence, or the trace-zero count as new. Available tables do not supply a full period, and the strongest nearby catalogue statement counts AP incidences without excluding intermediate zeros.

## value

PASS

The residue period and density do not show how long Bell divisibility can be avoided. Seven gives a natural first prime case with a six-digit Bell cycle (the full periods at 2, 3 and 5 are 3, 13 and 781). The complete census yields an exact worst-case spacing, the unique witness, and frequencies usable as a fixed-prime benchmark for trace-sequence run or divisibility-spacing analysis. Those require resolving the order of the zeros, not simply evaluating a known count or lookup table. The merit is that finite invariant, not a claim of a new period theorem or general gap law.

The dated certificate retains the supplied scientific assessment, sources and limitations.
