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

The substitution fixed point satisfies p_2j=0 and p_(2j+1)=1-p_j, forbids 11 and 0000. For n>=4, an equal length-n factor at opposite start parities would force four consecutive zeros, impossible. Equal even starts decimate to equal length-floor(n/2) parent factors; odd starts to length-ceil(n/2). Since R is monotone, earliest new repeated start is min(2R(floor(n/2)),2R(ceil(n/2))+1)=2R(floor(n/2)). Bases R(1..3)=2,3,4 determine the exact dyadic staircase and liminf=1, limsup=3/2. Independent direct byte-factor comparison matched the recurrence for n=1..200; the parity argument proves all positive n.

## originality

PASS

Nicholson–Rampersad 2015 defines initial nonrepetitive complexity and gives formulas for Thue–Morse/Fibonacci/Tribonacci, not this sequence in the accessible abstract. Huang–Zhang 2014 and Huang–Wen 2016 study period-doubling factor return occurrences and could implicitly imply first collisions; their full mathematical bodies were not obtained, so their exclusion cannot be certified. OEIS A366462/A367184 give longest no-repeat window anywhere, which differs from first repeat at position zero; some dyadic coincidences are noted. The explicit all-length unshifted first-collision law is not directly located in Resultary.

## value

PASS

The first repeat from the start is a standard well-motivated symbolic-dynamics statistic for a classical substitution fixed point. A complete all-n recurrence and sharp normalized limits fill a natural exact classification gap. This is not the unrelated factor complexity or anywhere-longest-window invariant. Parity synchronization is a reusable structural explanation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
