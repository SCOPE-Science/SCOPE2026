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

For the specified four-term strategy-average drift, derive the switching gaps by comparing each of the four individual health-status payoffs with the opposite strategy's population-weighted payoff. Independently recomputed the two aggregate payoff pairs and the rational logistic arguments in RESULT.md lines 52–59. The individual advantage is instead (11/30)q−1/20, with endpoint values 1/200 and 17/100. The low-noise termwise limit is eq, and the high-noise linear coefficient in q is 257/200, giving the stated negative endpoint comparisons. The strict exponential series bounds give G(q_−)>5193/16000 and G(q_+)<5071/30000 at κ=1/40. Thus the analytic difference has a sign-changing zero on each side of 1/40, with no exact zero count implied. Both risks are in [0,1]; the statement uses fixed risk coordinates, not a pair of states on a single epidemic trajectory. checker.py and VERIFICATION.md were inspected, not executed; the independently reproduced rational argument suffices. Exact attribution of this drift to the cited paper is not independently confirmed.

## originality

PASS

The supported distinct claim is the fixed-risk sign reversal and explicit witness under the displayed SB-RA payoff convention, not the underlying Fermi rule, epidemiological model, or empirical behavior. No distinct covering statement was identified in the inspected material; priority and the exact equation attribution remain bounded by access.

## value

PASS

An explicit and strict counterexample separates a rising personal financial incentive from the instantaneous collective response in a specified behavioral game. The agreement of the endpoint noise limits and opposite intermediate ordering makes the witness useful: neither a limit argument nor the monotonicity of private benefit suffices to rank the two risk states. No policy or trajectory conclusion is inferred.

The dated certificate retains the supplied scientific assessment, sources and limitations.
