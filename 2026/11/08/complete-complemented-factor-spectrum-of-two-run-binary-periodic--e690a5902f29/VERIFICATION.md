---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

A factor with at least two letter changes contains a full internal run of length a or b; complementing it requires a full run of the opposite letter of the same length, impossible if a!=b. Thus complemented factors have zero or one transition. Both 0^i and 1^i occur iff i<=m=min(a,b); both 0^i1^j and 1^i0^j occur iff i,j<=m. These are exhaustive and disjoint word families, so the length generating polynomial is 2z(1-z^m)/(1-z)+2[z(1-z^m)/(1-z)]²=2z(1-z^m)(1-z^(m+1))/(1-z)²; coefficients are 2n for n<=m, 2(2m-n+1) for m<n<=2m, zero later. Total 2m(m+1), and exact cutoff 2m. For equal runs, shift by m complements the host and all 2m period phases are distinct at length >=m, giving 2min(n,m) for all n. The one-sided word contains every cyclic phase, so no boundary ambiguity. An independent literal factor-language enumeration checks all 100 run pairs a,b<=10 up to length 3(a+b)+2, including complete word sets, not only counts.

## originality

PASS

Currie et al (2022/2025) introduce complemented-factor-avoidance and finite total-number invariants, and investigate critical exponent thresholds in broad infinite-word classes, but the complete special two-run periodic language and sharp min(a,b) count are not their theorems. Earlier same-family Resultary records calculate ordinary, 2-Abelian and closed/open factor complexity, not intersection with the bitwise complementary language. The full family classification therefore survives, although the proof uses elementary run decomposition.

## value

PASS

An exact finite/infinite threshold in a natural complement-avoidance parameter family, with the entire language, sharp maximum common-complement factor length and full enumerator, not just sample counts. This supplies explicit canonical periodic benchmarks for complement-avoidance and factor-language intersections; it is narrow and elementary but the problem's defined invariant and complete answer are mathematically motivated, not an arbitrary slice or recomputation of a known complement table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
