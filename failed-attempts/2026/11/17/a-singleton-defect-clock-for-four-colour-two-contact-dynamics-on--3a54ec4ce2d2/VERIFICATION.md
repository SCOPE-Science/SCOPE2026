---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

The exact simultaneous count recurrence m_i′=m_i 1_(m_(i+1)<2)+m_(i-1)1_(m_i>=2) yields an autonomous 0/1/heavy threshold signature. Exhaustive 3^4=81 signature transitions (independently recreated and checked) show only HHHH has genuine primitive period four, all others freeze in ≤3 steps, with sole depth-three patterns rotation of 1HHH. Counting labelled assignments with EGF weights 1,z,H=e^z−1−z yields the five Q_(t,p) polynomials; direct symbolic sum equals (1+z+H)^4=e^(4z). Sharp first entry min(3,floor((n−1)/2)), primitive-four onset n=8, and depth-three onset n=7 follow by minimum populations. From one-small-class binomial asymptotics, conditional depth-three proportion n/(n+3)+O(n^2(2/3)^n) follows. Finite signature exhaustion is legitimate as a proof of the all-n model because the autonomous category map is exact; full direct microscopic n<=9 tests corroborate only.

## originality

FAIL

Decisive broader published same-model theorem for every color count q>=3 and threshold theta>=1 on labelled simple complete K_n covers q=4,theta=2 verbatim. Its general active-run erosion formula yields all five entry-time classes and precise maximum delay; its complete labelled EGF is a strict generalization of the submitted five Q-polynomials, from which the sharpened conditional asymptotic is elementary coefficient arithmetic. Same publication calendar date 2026-11-17 means intra-day priority order cannot be proved, but mathematical implication/coverage is decisive regardless of wording.

## value

FAIL

Although exact finite-state laws are mathematically correct and the class of models is naturally motivated, as a separate claim the q4/theta2 entry clock and full labelled census are already mechanically extractable from a stronger all-q/all-threshold theorem. The sole extra-looking n/(n+3) asymptotic is elementary coefficient extraction from its exact EGF; no independent new structural, classification, or invariant fact remains.

The dated certificate retains the supplied scientific assessment, sources and limitations.
