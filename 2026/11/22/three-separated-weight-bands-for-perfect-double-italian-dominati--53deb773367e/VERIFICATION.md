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

For vertex a_i the closed sum is A+y_i, and for b_i it is B+x_i, with no constraint at labels >=2. If a layer contains a low label its total is at most 4, while an all-high layer has total at least 2n. In the two-light case total 0 or 1 forces the opposite layer above 4. At total 2, if all entries are low the opposite entries must all be positive; the only remaining boundary is n=4 with four ones, which forces the first layer identically zero. If one entry is 2, the opposite layer has at least n−1 ones or higher; its total is then at least 3, forcing a high entry opposite that 2 and thus a total greater than 4. Therefore both totals are 3 or 4. At (3,3) every column is either low-low or high-high, with at most one high-high column: zero such columns gives binom(n,3)^2, one gives n[(n−1)+1]^2=n^3. At (4,3) every positive entry on the total-3 side must be high and opposite a high digit, hence the lone 3 is matched to 2 or 3 and the other layer's remaining ones are chosen in binom(n−1,2) or n−1 ways. Including the orientation gives n²(n−1). At (4,4) the only nonzero columns are two (2,2) pairs, giving binom(n,2). If exactly one layer is all-high, the light total is 0, 1 or 2. At total 0 the high layer is all 3; at total 1 every high label is free; at total 2 two ones force all high labels to be 2, or a lone 2 frees just its partner. Doubling for the orientations yields the four mixed terms with the stated coefficients. All-high/all-high gives z^(4n)(1+z)^(2n). These cases are disjoint, exhaustive and count labeled functions. The binomial terms fill the two upper intervals, with no other weights; for n>=5 both asserted gaps are nonempty. Independent direct closed-neighborhood enumeration for n=2,3,4,5 returned (min,count,total)=(4,3,71),(5,6,193),(6,80,548),(6,225,1721), matching the full polynomial coefficient by coefficient for n=4,5 and the two small endpoints. The analytic classification is the proof for all n>=4.

## originality

PASS

The supported distinct claim is the complete interval-convention weight polynomial, optimizer census and support gaps on the matched two-clique family. Equal minimum weights under neighboring conventions or for another graph are not claimed as new in isolation. The inspected same-graph lower-only solution and same-convention square-rook and crown results do not give the polynomial or imply the separated spectrum.

## value

PASS

The prism is the natural two-layer case of a Cartesian product of cliques. The upper bound at low sites forces an all-or-nothing layer separation: a constrained layer weighs at most four but an unconstrained layer weighs at least 2n. The exact polynomial converts that structural fact into two forbidden ranges and counts all weight classes, including the distinct structures at the optimum. This supplies information absent from a minimum-weight result and is directly useful for comparison with strict and lower-only domination conventions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
