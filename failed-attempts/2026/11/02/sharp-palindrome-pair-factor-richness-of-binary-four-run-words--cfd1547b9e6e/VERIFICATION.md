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

The count is for distinct contiguous factors and includes the empty word. Every factor with at most three runs splits into two palindromes. For a four-run factor 0^x1^b0^c1^y, no cut inside a run or at the central boundary can make both pieces palindromic; the other two boundaries give exactly x=c or y=b. The two 0-to-1 transition rectangles overlap in the rectangle with the two coordinatewise minima, which accounts for all duplicates. Substitution in the count gives the three quadratic upper bounds after reversal and bit exchange; in the remaining strict case a<c, b>d, putting x=b+c gives Q<=2-n+(n+2)x-3x^2/4<=(n^2+n+10)/3. Integrality gives the claimed ceiling. The explicit triples of residue-class witnesses attain the bound and cover n=8,9,10 and all larger lengths. For a three-run host, reverse to a<=c; the count is 1+(a+1)b+(a+1)c+bc, maximized by balancing the three arguments of sum n+1. This verifies the benchmark and the stated gap without an unrestricted extremum claim. No bundled script was executed; the proof is decisive.

## originality

FAIL

A distinct indexed Resultary theorem expressly covers the exact four-run maximum for n>=8, the three-run benchmark, and hence their gap. It also classifies all maximizing quadruples and handles n=4,5,6,7. The catalogue paths differ; that establishes distinct documents, not authorship, priority, or independent discovery. The failure is for demonstrated equivalent coverage, not a chronology inference.

## value

FAIL

The run-constrained extremum is a natural boundary for the unrestricted palindrome-pair factor problem, but the frozen record supplies no additional exact fact beyond the indexed stronger theorem. Its explicit witnesses are instances of that theorem's full equality characterization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
