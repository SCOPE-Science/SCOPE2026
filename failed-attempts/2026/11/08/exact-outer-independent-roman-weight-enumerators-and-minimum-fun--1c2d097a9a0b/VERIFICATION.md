---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Zero labels form k nonattacking rooks, in R(k)=binom(m,k)binom(n,k)k! ways. Any t of them have a union of t(m+n-t-1) nonzero neighbors; inclusion-exclusion gives exactly the displayed generating polynomial because the actual summand has z^a(z+z²)^(N-k-a)=z^(N-k)(1+z)^(N-k-a). Each defender can cover at most two zeros, giving minimum N-floor(s/2); even and odd defender pairing/path cases yield stated coefficients. At m=n=2 totality excludes precisely 4z³+2z⁴; elsewhere every positive label has a positive neighbor. Independent literal brute force verified ordinary/total counts 46/40 for (2,2), 310/310 for (2,3), and min coefficients (3,4) and (5,12). The proof, not finite counts, supports every m,n>=2.

## originality

FAIL

FAIL: a published November 2, 2026 Resultary theorem gives the *complete labelled outer-independent total Roman polynomial* for every rectangular rook graph, all minimum-function multiplicities and exactly the exceptional 2x2 correction. For every other (m,n) the ordinary and total versions coincide; for 2x2 the submitted ordinary polynomial equals that earlier total polynomial PLUS its stated correction. Factoring powers shows identical inclusion-exclusion formula term by term; both even and odd optimal multiplicity expressions are identical. Nothing beyond prior complete formulas remains after such routine rearrangement.

## value

FAIL

FAIL: the natural complete weight census and optimizer classification were already provided by stronger directly relevant prior work. Reversing the known 2x2 correction to recover ordinary Roman functions is a trivial exceptional-boundary algebra adjustment, not a distinct valuable classification. Correctness and exhaustive reproducibility cannot rescue a table already fully determined.

The dated certificate retains the supplied scientific assessment, sources and limitations.
