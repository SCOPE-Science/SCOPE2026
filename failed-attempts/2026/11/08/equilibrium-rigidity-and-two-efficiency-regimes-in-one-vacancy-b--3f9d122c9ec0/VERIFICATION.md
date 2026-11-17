---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-14.md",
      "INDEPENDENT_AUDIT_2026-11-14.json"
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

For a vacancy in the a-part, a mixed fully occupied b-part would force simultaneously (a-1)y <= (b-1)x <= (a-1)(y-1), impossible. Pure opposite part yields no strictly improving move, including same-part moves. Enumerating the mutually exclusive all-red or all-blue opposite-side cases gives E=a[C(a-1,r-b)+C(a-1,r)]+b[C(b-1,r-a)+C(b-1,r)]. Balanced K_m,m gives 2m colored equilibria and 2/binom(2m,m) probability. On K_{a,2}, the red and blue pair orientations give welfare a+1 and 2+4/(a-1), hence exact PoA (a-1)/2. Independent literal-payoff enumeration checked 2<=a,b<=4 and welfare a=3..7; these finite checks do not establish the all-parameter theorem.

## originality

FAIL

The submitted principal all-biclique equilibrium-iff and exact red-count polynomial are mathematically identical to the previously published 2026-10-26 one-vacancy theorem and are also a q=1 specialization of a 2026-10-25 arbitrary-vacancy theorem. Neither older source appears to state the sharp K_{a,2} welfare counterexample, which is a potentially original motivated remainder, but the intact package presents the covered classification and balanced rarity as its own principal finding. No complete re-scoped corrected research files are staged; the original combined claim is not eligible for PASS through a literature disclaimer.

## value

PASS

The exact K_{a,2} price-of-anarchy family is a motivated counterexample to the hypothesis that large inefficiency requires leaves or a singleton minority: minimum degree and vertex connectivity equal two and both populations have at least two agents. Its welfare distinction is mathematically meaningful, even though the dominant equilibrium classification and enumerator have already been published. Value of that possible narrowed witness does not rescue originality of the submitted unmodified main claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
