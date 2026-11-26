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

Re-audited the repaired claim under independent exponential lifetimes, no removals at the initial r unobserved failures, and deterministic, noninformative random removals thereafter. Independent ordinary spacings before the first observed failure give H=∑c_ℓE_ℓ; exponential memorylessness gives the independent unit gaps G_j after risk normalization, with common scale canceled. For the left endpoint only the weight-zero gap has negative contrast when t<1/(d−1); its survival transform yields the exact product and r+1+d−2=m−1 vanishing factors. Near the right endpoint, rescaling the d−1 independent gaps conditional on H=s gives a simplex integral with limiting volume 1/(d−1)! and the Jacobian 1/∏(j/(d−1)−t); the scaled probability is dominated by a constant times s^(d−1), which is integrable. Expansion of the moment generating function of H gives E H^(d−1)=(d−1)!h_(d−1)(c), checking the right coefficient and power. This covers d=2 and r=0, including the empty product. Dominance is claimed only for r>0: couple H=E_r+Z with Z>0 independent, and on the positive-probability open G-set where the weighted ratio without the first gap is below u, the crossing E_r<s_*(G)<E_r+Z has strictly positive conditional probability for each u∈(0,1). Normalized unit gaps for r=0 give cumulative uniform order statistics, hence the average-of-uniforms benchmark. As a secondary formula, the halfspace expression recovers the signs and gives continuity at repeated nonnegative coefficients and knots because the contrast has no atom at zero. Independent `python /workspace/independent_replay.py 5` verified 20 exact rational minimal-example CDF values and endpoint constants for three triples via simplex caps and a separate multinomial moment evaluation, including 405/64 and 660241/20250 for (10,6,2). Finite diagnostics do not verify universal quantifiers.

## originality

PASS

Apply this verdict to the repaired sharp paired endpoint asymptotics and the strict stochastic comparison only. The exact CDF and the statistic itself are credited prior or direct prior implications, and the method is classical. No inspected result gives the unequal exponents with their constants or the strict comparison under the specified censoring scheme; see the access limits for the original test and earlier progressive-spacings work.

## value

PASS

Initial missing failures distort the two tails of a published test in different orders even with the same observed sample count. Knowing both exact powers and constants gives the leading extreme critical values on each side, while the strict ordering at all interior thresholds identifies a systematic shift caused by initial censoring rather than by a different count of observed gaps. These are concrete fixed-sample implications, not new general simplex machinery or a claim of numerical stability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
