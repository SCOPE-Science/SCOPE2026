---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

At run starts the affine update contracts by exp(−R−T), with strictly negative mean log multiplier; the bounded backward solution is unique. The stationary marked cycle sequence is an ergodic function of independent cycles. Occupation with the finite-mean roof R+T yields a unique stationary position marginal, including for rest laws with an atom at zero; position itself need not regenerate independently at cycle boundaries. Fair sign draws give symmetry. In RESULT.md lines 46–73 the mean run occupation at order j is z_j/a by exponential survival, and the rest reward is (1−t_j)z_j/j. Combining these with the end-of-run recursion cancels the same-order factors 1−t_j a/(a+j). In fact M2=1/[(a+1)(1+aμ)] and M4=6/[(a+1)(a+3)(1+aμ)(a+2−a t2)], so the claimed dependence on (μ,t2,t4) is true but not minimal. These formulas give the stated positive-denominator Erlang-2 cumulant, with exactly one positive simple zero by Descartes counting and the opposite endpoint signs. The comparator polynomial E_a(c) also has one positive zero. At matched μ=1/c, (c/(c+1))²<c/(c+2), so the Erlang fourth cumulant is strictly lower at every matched rate, independently confirming the claimed threshold ordering. This is an analytic check; the frozen rational generator checks are recorded corroboration only and were not executed.

## originality

PASS

Credit prior exact memoryless-rest moments and the explicit exponential-rest threshold overlap. The supported distinct result is the dependence on Laplace statistics for arbitrary independent finite-mean zero-velocity rests, together with the simple Erlang-2 cumulant crossing and its strict shift relative to the mean-matched exponential law. The primary and indexed comparisons below do not supply that combined claim or a prior theorem covering it.

## value

PASS

This gives an exact test of how changing inactive-time variability while preserving the mean changes stationary fourth-order shape in a natural active-particle model. The finite statistic reduction is useful without fitting a whole rest law, and the unique Erlang-2 crossover and strict shift give a quantitative benchmark beyond the known memoryless moments. Neither modality nor a thermodynamic transition follows.

The dated certificate retains the supplied scientific assessment, sources and limitations.
