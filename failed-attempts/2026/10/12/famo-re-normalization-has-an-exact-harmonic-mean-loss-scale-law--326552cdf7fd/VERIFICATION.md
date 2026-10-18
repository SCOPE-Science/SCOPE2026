---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

From FAMO Eq. (11), c=(sum z_i/l_i)^(-1), d=c sum_i(z_i/l_i)grad l_i. Under l_i->s_i l_i and g_i->s_i g_i at matched state, log-gradient summands z_i*g_i/l_i remain invariant; w_i=c z_i/l_i define positive simplex weights and c_new/c=(sum_i w_i/s_i)^(-1), so d_new=H_w(s)d. Min/max scale bounds and equal weights (s,1) ->2s/(1+s) follow. Common s gives d_new=s d, hence α_new=α/s and unchanged log-loss differences imply entire same-state model/logit trajectories coincide by induction, if positive adjusted objectives rescale as whole and other hyperparameters match. Direct exact-rational independent worked case and primary verifier formulas corroborate.

## originality

FAIL

REJECT. The defining NeurIPS 2023 FAMO paper ALREADY gives the stronger exact source direction as its Eq. (11) with both numerator and scalar denominator explicit. The claimed weighted harmonic scaling is the immediate quotient of that published normalizer under multiplication l_i->s_i l_i: the exact equation determines the transformed direction without an extra nonstandard lemma, model-specific invariant, or new parameter boundary. By the required stronger-coverage/implication bar, an unstated one-line corollary from published defining formula is covered. No novelty granted merely because source omits the words harmonic mean.

## value

FAIL

REJECT as standalone mathematical value: the exact scale law repackages an elementary substitution into the published normalization formula, with common s learning-rate compensation and min/max harmonic inequalities automatic. It does not identify an algorithmic failure, nontrivial sharp stability threshold, convergence implication or intrinsic new exact invariant beyond Eq. (11). The unit-sensitivity observation is an understandable implementation note, but not a substantively motivated new mathematical gap separate from routine algebra; correctness and numerical demonstration alone do not confer value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
