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

For all m>=4 over C, eliminating x=-z^3/y gives u=z/y and u^4-u^2=y^(m-3). Two outer branches and one x-axis branch always exist; the inner quadratic splits into two analytic branches when m odd, and one primitive quadratic-ramified branch when m even. Residue differentials omega=dy/[2z(y^2-2z^2)] yield outer orders -3, axis order -2, inner order -(m+3)/2 each (odd m) or -(m+2) (even m). Gorenstein finite-normalization duality yields the claimed conductor valuation tuple. Sum of exponents equals 2delta and Milnor identity mu=2delta-r+1=m+7. Independent parity, conductor-sum and Milnor-delta arithmetic checked for m4..30. m=4 tuple is earlier known, not independently new.

## originality

PASS

PASS for entire parity-dependent m>=4 classification, excluding the already published m=4 instance. He–Wang Nov4 revision Appendix B.1 gives (2,3,3,6) for m=4; Appendix C provides only aggregate sum(c_i-1)=m+6 for all m, so does not determine individual m>4 conductor partitions. Original Pfister–Schönemann full text remains a risk.

## value

PASS

Branchwise conductor exponents and parity-dependent branch count determine exact local pinching/normalization jet cutoffs, materially finer than the already known Milnor/Tjurina and aggregate conductor lengths. Natural classification of the original analytic family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
