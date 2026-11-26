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

Composition mod t⁶ gives the coefficient pair (A,B)=(a(a²+b),b(a²+b)), with the last two input coordinates free. The degree-4/5 subgroup is central and additive; the squares from a=0 generate its vertical axis and those from a=1 give every first coordinate. For A≠0 setting u=a²+b makes the fibers exactly q² times the number of rational roots of u³+Bu+A², with inverse formulas a=A/u, b=u+a². The derivative test excludes multiple roots. The distinct rational-root triples are {r,s,r+s}, yielding (q−1)(q−2)/6 such targets; there are (q−1)² target-root incidences, giving q(q−1)/2 one-root targets and (q²−1)/3 unattainable ones. On A=0 the identity has q³ roots and each B≠0 has q² by bijectivity of Frobenius. Truncation to N≤3 annihilates squares, and at N=4 a=1 gives every possible fourth coefficient. At q=2 the candidate 3q² is numerically distinct but occurs zero times, as the table says. The frozen script and recorded exhaustive outputs at q=2,4,8,16 corroborate only those cases; the uploaded script was not executed.

## originality

PASS

Pass for the uniform extension-field square-image and nonidentity fiber theorem, not novelty of the q=2 case, the identity fiber in isolation, the coefficientwise root equations as a method, or the depressed-cubic split-type count. Earlier Riordan-matrix calculations explicitly cover the prime-field slice. The strongest inspected statements do not give the all-field histogram or its group-image consequence by specialization alone.

## value

PASS

The first failure of the square image to fill the square-generated subgroup is an intrinsic cutoff of the characteristic-two substitution filtration. The full nonidentity-fiber profile over extension fields, including the governing cubic test and the precise fraction of missing squares, is a reusable invariant beyond an exponent, a conjugacy census, or the F₂ calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
