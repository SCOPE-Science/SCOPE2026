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

For any active prefix set P, the largest compatible suffix set comprises all pairs not in P whose final symbol is not a first symbol of P. Saturating with balanced completions preserves both forbidden overlaps. An independent exact enumeration over all nonempty subsets of the 16 prefix pairs, taking this maximal suffix set, gave maxima (20,36,36) for f₂, f₁+f₂+f₃ and sum f_j. Exactly twelve choices attain f₂=20, all of profile (0,8,20,8,0); their four-symbol codebooks are distinct and all their boundary pairs occur at length four. This directly addresses n=4, where only the f₂ bound constrains equality. For L=n−4, a boundary with j class symbols has 2^L binom(L,n/2−j) completions. Dividing by 2^L binom(L,L/2) yields a nonnegative weighted sum of the three bounded statistics with weights 1−r₁, r₁−r₂ and r₂, r₁=L/(L+2), r₂=L(L−2)/((L+2)(L+4)), with out-of-range binomials zero. Since 1−r₁>0, every maximizer is among the twelve enumerated sets. Every allowed boundary of these sets is completable for n≥6, so distinctness persists. This establishes the formula and census at all lengths, not by extrapolation. The central-binomial ratio tends to 1/16, and including 2^(n−4)/2^n gives density 36/256=9/64.

## originality

PASS

Pass applies to the all-even exact-composition formula and optimizer census extending beyond length four. The n=4 value and equality cases are materially covered by the earlier length-four full-non-overlap census, and the unbalanced optimum and restricted-boundary reduction are prior ingredients. The closest exact-composition article could not be read in full; the available evidence does not establish that it covers the all-length theorem.

## value

PASS

Exact composition and two forbidden overlaps are natural simultaneous constraints of finite-word extremal combinatorics. The result identifies a sharp capacity at every length in this setting and shows that conditioning on composition selects the same twelve boundary patterns rather than changing the optimizers with length. That all-length dependence and equality information go beyond the known short instance and an unrestricted bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
