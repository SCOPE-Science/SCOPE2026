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

The finite count is correct: subtract the maximum enforced multiplicity independently for each permitted part. Each integer layer j is supported precisely on allowed sizes through max_(r≥j)t_r, so the resulting weight is S. This is reversible, including n=0 and S>n. RESULT.md lines 47–55 omit the complex-sector hypothesis of corrected Ingham; the radial estimate plus coefficient monotonicity would not suffice alone. The missing estimate holds here. Write P(z)=prod_(a≥1)(1−exp(−az))^(−1); Dedekind inversion gives P(z)=sqrt(z/(2π)) exp(π²/(6z)−z/24)P(4π²/z) on Re z>0. Hence P(z)/P(ell z)=ell^(−1/2) exp(μ_ell/z+(ell−1)z/24)(1+O(exp(−c/|z|))) as z→0 in each fixed sector |Im z|≤Δ Re z. Since Re(1/z)≤1/|z|, this gives the correct sector bound of Bringmann–Jennings-Shaffer–Mahlburg Theorem 1.1, with γ=μ_ell, λ=ell^(−1/2) and both power/log exponents zero. Multiplication by the allowed part 1 shows coefficients are nondecreasing; the analytic product has radius at least one. Thus the asserted coefficient asymptotic holds, with the missing hypothesis verified independently. Taylor expanding sqrt(n−S) for S=O(sqrt n) gives the claimed ratio and rate. The floors and arithmetic progression omission give A_ell(t)=(1−1/ell)t²/2+O(t+1), including zero thresholds. Independent exponentials have exactly the stated suffix-max survivor after squaring, and continuous coordinate marginals imply weak convergence via orthant inclusion–exclusion; this is not a proof of exact coincidence probabilities. Replay: python /workspace/reproductions/frozen_checks.py, third check, verifies 270 bounded exact cases at four levels. Frozen recorded 9600-case evidence and script inspected but not executed.

## originality

FAIL

The frozen identities are mathematically true, but inspected pre-existing results make the asserted joint dependence and counting rule a routine transfer. The old joint laws already give the mandatory-copy rule, suffix maxima and running-minimum coupling, including in another partition measure. Deleting the forbidden indices in that rule and applying the known regular-part univariate scaling gives the full asserted law with no new dependence calculation. This is demonstrable prior implication, not a judgment based on any unavailable source.

## value

FAIL

Joint multiplicity gaps are a natural statistic, but the submitted increment over the explicit ordinary and overpartition joint laws is only deleting forbidden terms from an already known shift and changing an already known marginal scaling constant. It establishes no new regular-partition dependence feature beyond a scale change, no arithmetic or finite correction and no exact tie limit. The parameter transfer does not meet the independent mathematical-value bar; no different surviving claim is submitted as a repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
