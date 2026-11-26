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

The first adjacent one-gap determines which pair of marked positions is seen and the relative left offset then determines the start. Factors with three or more ones cannot have an occurring reversal because their consecutive gaps are strictly increasing. For a gap d≥2 put h=d/2 and u=n−d−1; there are min(h,max(0,u+1)) first-pair factors. The reversible subset is precisely those splits a+b=u with both a,b between 0 and h−1; this also excludes the next one because its gap is 2d. Reflection swaps a,b, so subtracting the floor of half its cardinality removes exactly the duplicates. For u<0, 0≤u<h, h≤u≤2h−2 and u≥2h−1, the resulting count is respectively zero, floor((u+2)/2), floor((u+2)/2) and h. This counts the odd lengths in (d,2d) not exceeding n. The dyadic sum, the zero/single-one factors and the unique initial gap yield r_c. Prefixing zero adds only one possible new factor at each length: it is new for n≥3; at n=3 it is the reverse of 110, at n=4 it is the new palindrome 0110, and for n≥5 its reversal cannot occur. The distinct-factor formula uses the same first-pair count without quotients: smaller gaps saturate, the top gap is truncated, larger gaps contribute zero. The empty word and lengths 1–3 give the stated boundary counts. The normalized factor profile has extrema 3/2 and 5/3 on each dyadic scale asymptotically, attained along powers of two and their 3/2 multiples; taking reciprocals gives the stated ratio endpoints since r_c/n→1.

## originality

FAIL

The distinct indexed geometric-support result covers the shifted word's exact reflection formula as its base-two case. Crucially, its proof Step 4 also gives the exact number U of distinct multiple-one factors before reversal; specializing that explicit count recovers the entire shifted ordinary factor profile. Its uniqueness and reversal lemmas reduce the canonical word to deletion of the one prefix contribution with the listed short-length exceptions. The ratio endpoints are routine extrema of the already supplied profiles. Thus there is no independently supported distinct remainder. The coverage comparison does not purport to establish priority or provenance from catalog dates.

## value

FAIL

Exact complexity for this nonrecurrent word is a motivated question. However, after the exact all-base reflection theorem and its ordinary factor count are credited, specializing them, removing one leading position, and taking extrema of the corresponding two dyadic branches do not establish a distinct valuable result. Keeping only the rewritten factor formula or the resulting ratios would not be a genuine repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
