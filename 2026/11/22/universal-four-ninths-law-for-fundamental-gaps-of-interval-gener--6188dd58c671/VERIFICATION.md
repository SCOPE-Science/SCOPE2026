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

At fixed summand count m the represented integers form the entire interval [ma,m(a+k)]. For n=qa+r no m>q works; if any m<=q works, q also works, because n>=qa and n<=q(a+k). Thus membership is exactly r<=qk and the genus is the stated residue sum. For the j-fold test, the carry c=floor(jr/a) changes r to jr-ca and q to jq+c. Below ceil(a/2) the double has no carry and still fails. In the bands [ceil(a/2),ceil(2a/3)) and [ceil(2a/3),a) the carries (c2,c3) are (1,1) and (1,2); comparison of c2/2 to c3/3 gives respectively the triple and double as the stronger restriction. This proves both integer bands, also when a band or an admissible q interval is empty. To verify the uniform estimates, the genus ceiling error relative to a²/(2k) is -a/(2k) plus a quantity in [0,a-1). For a>=3k neither lower bound needs clipping, and each count is within one of (a+k)/(3k) or (a+k)/(2k); the difference of the arguments is positive so the raw difference of ceilings cannot be negative. The band lengths differ from a/6 and a/3 by less than one; rounding the summands costs less than a, the +k numerators add at most a/2, and rounding the lengths against a/(3k) and a/(2k) costs at most a/(3k)+a/(2k). The resulting error is <3a. For a<3k, both F<=g<5a/2 and the nonnegative main term <2a/3 bound the absolute difference by <3a. Relative errors vanish when k/a→0, giving 4/9. At k=a-1 the membership test also gives directly FG=[ceil(a/2),a) as integers. VERIFICATION.md and check_fundamental_gap_bands.py were inspected, not run; the recorded unbounded-coin checks only compare the finite set of parameters and use a proven cutoff. Replay of the unrestricted result is the interval and carry argument above, not an extrapolation from those counts.

## originality

PASS

The supported distinct claim is the full two-band fundamental-gap classification with a uniform linear absolute counting error and a width-independent 4/9 ratio for sublinear width. The basic semigroup membership and genus machinery, fundamental-gap predicate, and general finite algorithms are antecedent, not standalone novelty. No claim of exhaustive historical priority is made.

## value

PASS

Fundamental gaps are a standard semigroup invariant. A complete parameter-uniform classification and a natural density among gaps, holding for fixed and growing sublinear widths with the same constant, add information beyond a genus count or a finite algorithm. The two competing carry boundaries explain where the limit comes from; no broader proportional-width claim is needed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
