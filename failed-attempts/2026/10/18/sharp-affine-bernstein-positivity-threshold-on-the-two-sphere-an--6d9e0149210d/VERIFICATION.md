---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Schoenberg reduces the cone to nonnegative summable coefficients of the normalized Gegenbauer kernels; the Bernstein operator is continuous in sup norm, so checking all basis kernels suffices. For the top coefficient, the exponential response of the signed centered n-difference is (2sinh(z/n))^n. Its first two even-spaced nonzero powers give D_n(t^n)=n!(2/n)^n and D_n(t^(n+2))/D_n(t^n)=(n+1)(n+2)/(6n). The two top normalized Gegenbauer coefficients contribute L_(n+2) times the difference of this ratio and (n+1)(n+2)/[4(n+λ+1)]. Dividing the top monomial coefficient by L_n, using L_m=2^m(λ)_m/(2λ)_m, gives the published-in-record formula and sign d+1−n. At d=2, n=4 it is −9/256; at n=d+1 the zero coefficient gives no positivity conclusion in higher dimensions. For n=1,2,3 I verified the parity reductions and all low-degree coefficient formulas; for n=3 odd the P_3 coefficient is (1−3P_m(1/3))/10. Laplace's integral gives |P_m|≤1 and for m≥9 at 1/3 an upper bound by the fourth moment of 1−(8/9)sin²u, namely 1921/6561<1/3. The exact m=1,3,5,7 evaluations fill in every smaller odd degree. Thus the iff on S² and the necessary higher-dimensional bound hold with the stated dot-product nodes and normalization.

## originality

FAIL

Full equivalent claim coverage is established in a distinct indexed finding, not just a similar title or the shared n=4 example. The November 2 degree-frontier Finding states the same operator, cone, S² iff, witness and exact Legendre coefficient, and the same all-dimensional normalized coefficient and obstruction on the identical parameter domain. No remaining distinct mathematical claim is identified in the frozen Finding. A second indexed record states the stronger all-dimensional iff, reproduces the obstruction, and explicitly cites the degree-frontier work by title as a preceding mathematical finding. This FAIL is for distinctness on the inspected evidence, not a finding that either indexed record was available before October 18, nor a claim about historical authorship or the truth of the theorem. The different folders' dates cannot settle the underlying provenance: the November 1 text itself cites the title indexed on November 2. Otten–Nguyen–Watts is the verified earlier publication for just the n=4 case, not evidence of earlier publication of the entire classification.

## value

PASS

The underlying question is a useful sharp preservation classification for a standard approximation operator and a meaningful kernel cone. A connected family of explicit witnesses settles all high degrees rather than just one counterexample, and the dimension-dependent sign is informative about the obstruction boundary. The small-degree positive direction matters to making the S² statement exact. This judges the scientific value of the mathematical conclusion, not whether the frozen presentation contributes distinct content beyond the indexed matches.

The dated certificate retains the supplied scientific assessment, sources and limitations.
