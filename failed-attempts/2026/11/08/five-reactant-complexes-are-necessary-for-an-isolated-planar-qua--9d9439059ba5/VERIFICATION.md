---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Positive diagonal rescaling to (1,1) preserves the nonzero vector-monomial slots. The zero value and full zero Jacobian leave only the three homogeneous Taylor terms. Any two of the six coefficient rows are independent, so two vanishing slots force both output components to be multiples of the same real homogeneous quadratic. A nondefinite such quadratic has a real zero line (or is identically zero). For a definite one, after choosing its sign, the x², y² and constant slots are nonzero. If the mixed coefficient vanishes, both linear coefficients are nonzero; if it does not, vanishing of both linear coefficients would make the form a multiple of (u−v)². Thus at most four slots cannot give an isolated positive equilibrium. Counting distinct aggregate support slots separately from directed reactions is correct. Direct stoichiometric expansion gives ((x−1)²,(y−1)²) for the stated five positive-rate reactions, so the witness is isolated with full zero Jacobian. This is an analytic check of the universal statement and witness, not a general finite enumeration or a claim for a nonzero nilpotent Jacobian.

## originality

FAIL

An independently indexed Resultary record already states the same sharp reaction and active-reactant minimum and proves a stronger polynomial obstruction. This is demonstrated coverage, not a judgment based on similar titles, dates or a failed lookup. The alternate proof and alternate attaining network do not change the stated theorem.

## value

FAIL

The minimum is a motivated question, but this submission adds neither a new threshold, a broader obstruction, nor an additional constrained realization. A second elementary proof and a different example under the same allowed stoichiometries do not, by themselves, establish an independently useful new claim. No substantive surviving repair was established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
