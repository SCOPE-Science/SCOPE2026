---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

For two equal m-point blocks, quotient-bijective transformations are all regular: each block-restriction has a right inverse. When both blocks map into the same target class, a preserving right inverse exists iff one input-block image contains the other; preimages of the whole target class cannot be distributed among two inverse-image blocks. Given target image rank r, inclusion–exclusion on the two possible nested image containments gives C_r=4 binom(m,r)(r!S(m,r))r^m−2 binom(m,r)(r!S(m,r))². Independent class-bijective maps yield 2P_m(z)². Sangkhanan full-text §3 definitions reduce M1 to quotient-bijective maps plus 2m constants and M2 to common-target regular maps plus 2(m!)² units, with intersection constants + units. Exact rank polynomials follow. E image size ≤3m/4; one-coordinate bounded differences imply Pr(K>7m/8)≤e^(−m/32), giving exponential small nested-image probability and specified asymptotic fractions. Endpoints m=2 and all r are covered. Independent original-map enumeration and literal inverse search at m=2,3 reproduce all rank coefficients; these finite checks do not establish m unbounded.

## originality

PASS

The October 28, 2026 full 19-page Sangkhanan primary article (read in a lawful open-access PDF including its Theorem 3.15, Definitions M1/M2, and full proof) establishes structural maximality/uniqueness but does not enumerate all ranks by Stirling coefficients or analyze exponentially different volumes. The submitted formulas explicitly derive new quantitative invariants from that credited structural theorem. Resultary searches found no earlier exact same-object rank-distribution theorem. Best-of-knowledge only; old literature on rank enumerators might contain equivalent formulas.

## value

PASS

The two maximal unit-containing regular subsemigroups form a natural, already classified pair in finite transformation semigroup theory. Exact labeled rank distributions, their intersection and the striking exponentially divergent asymptotic volumes resolve a genuine quantitative gap, adding more than a textbook restatement of maximality. The full rank enumeration is useful for random maps and semigroup structure even without a larger downstream theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
