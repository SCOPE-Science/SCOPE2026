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

RESULT.md lines 4–22 and 41–57 reconstruct by parsing uniquely into ground flats and arches UF^aD. Splitting t arches at the h−1 positive intervening gaps, marking q positive interiors, and positively composing f flats across the s ordered marked runs are independent choices. The unigram counts must be U=D=t and F=f; with these counts the displayed nine digram values are necessary and the construction is sufficient. The all-flat case includes the empty word. For singleton size, h=1 or t and q=0 or t (without duplication at t=1); the flat allocation is unique for s=f=0, s=1, or f=s≥2. Summing these cases gives the displayed series, including the unrestricted one-run correction for t=2,h=2,q=0. Its only double pole is at 1, with coefficient 1 of (1−z)^{-2}. Independently, choosing the positions of an even number of vertical steps determines the source, giving 2^{n−1} for n≥1. Fresh bounded corroboration: iterate masks of n vertical positions through n=17, fill the marked positions alternately U,D, and tally all 12 raw multiplicities. Across 1,709 realized profiles the counts agreed with the binomial law; the singleton values matched the series and table. UFDFF and UFFDF collide at length five, and no binomial factor can exceed one below five. Inspected frozen VERIFICATION.md and verify.py; their status is not an independent audit, and the script was not executed. The reconstruction proves the all-length claim, separately from enumeration.

## originality

PASS

Best of the inspected evidence, the distinct content is the explicit restricted 2-Abelian fiber factorization and its complete singleton series, not the definition, realizability framework, or elementary source count. Same-day analogues were compared by statement without assuming their relative priority.

## value

PASS

The first bounded-height path class with genuine two-gram ambiguity gives a natural test for lossy readout. The exact factorization distinguishes block arrangement, marked interiors and flat allocation; the singleton law answers how many sources can be reconstructed uniquely, including its linear growth against an exponential source count. These are useful exact invariants of the stated source and observation, not a claim about unrestricted heights or independent experimental performance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
