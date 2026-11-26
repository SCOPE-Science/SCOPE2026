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

Unrestricted quadratic polynomials force the three moment constraints. For any design, group calls by site: exact worst-case bias in absolute value is (a/6)∑_u |u|³|∑_{δ_j=u} w_j|, attained by assigning aligned remainder signs with disjoint smooth cutoffs away from the anchor. The largest variance is b∑_j w_j² and can be realized with that same function. Averaging repeated-site weights leaves this bias invariant and strictly decreases the variance unless already equal; thus it suffices for the lower bound and is necessary for an optimizer. Equation (2) in the proof uses this averaged-design reduction (the expression with ungrouped absolute weights need not bound the risk of a raw mixed-sign repeated-site design). After this reduction, Hölder yields C≥S⁻²; the zero-sum constraint gives sign totals S/2. Separate Cauchy–Schwarz gives variance at least bS²(1/p'+1/q')/4, uniquely minimized in the counts when all n weights are used with the most balanced split. The positive-scalar minimum for odd n occurs at S⁶=a²/(18bk_n), k_n=n/(n²−1), with the stated exact value. Equality in the slope triangle inequality and Hölder forces sign agreement and a common nonzero |δ|=1/S. Thus only the reflected/permuted replicated two-site designs attain the bound, and they satisfy even the quadratic exactness constraint. A cubic realizes the worst bias at these sites. For n=1 the first two moments conflict; the even-budget formula and both n=3 percentages also check.

## originality

PASS

Lam–Li–Zhang treat precisely the pertinent linear estimation setting and establish the all-budget lower bound and even-budget equality. The sharp odd-budget bound and classification of every optimizer are supported as a distinct refinement, not a new derivation of their established even case.

## value

PASS

Exact odd-budget minimaxity resolves the natural parity gap in an established result, and rigidity tells practitioners exactly how to spend an indivisible extra call. The sharp finite-budget answer and complete equality conditions are meaningful even though the relative penalty tends to one and the refinement admits a short proof.

The dated certificate retains the supplied scientific assessment, sources and limitations.
