---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

For occupation-density normalization, the standard local-time law gives Var(L)=1−2/π. Gaussian projection gives conditional mean q_s y/(t+η) and conditional variance s−q_s²/(t+η), where q_s=min(s,t). The latter is at least ηs/(1+η), justifying integration of the conditional density via local-time mollification and L² conditional-expectation contraction. Two copies conditionally independent given the observation have off-diagonal covariance q_s q_u/(t+η), giving the stated second moment after integration. The binomial expansion and explicit s-integral give exactly A_k and the 1/(2π) factor; the series extends to t=0. Near t=1, all required derivatives are dominated by a polynomial in k times a geometric factor at every fixed η>0, using q_s²/s≤t and the explicit A_k derivatives. Since A_k'(1)=0, the denominator derivative alone gives I_η'(1)<0; I_η(0)=0<I_η(t) for t>0. The termwise lower bound makes I_η increasing for t≤1/2 at high noise; η² I_η converges in C² on [1/2,1] to A_1²/(4π). Its derivative is strictly positive through 3/5, and its second derivative is strictly negative on [3/5,1] (16−35√t+18t has no zero there). This gives exactly one high-noise maximum. The proof's short bootstrap in Step 5 can be made explicit without assuming the desired order: the endpoint formula gives I_η'(1)=O(η^−3), while −I_η''≥cη^−2 on [3/5,1] for large η. The mean-value theorem between the maximizer and 1 gives δ=1−t_η=O(η^−1). Now A_k'(1)=0 makes the k≥2 derivative tail O(η^−5). Near 1 the derivative of the leading information term has slope bounded away from zero on the η^−2 scale, so removing that tail moves the root by O(η^−3). Setting u=√t in the leading equation gives 2η(1−u)=u²(u−2/3); matching powers yields u=1−1/(6η)+5/(36η²)+O(η^−3) and the stated t_η. The leading squared term has A_1=2/3+O(η^−2) there, so its denominator supplies −2/(9πη³) and the other terms are O(η^−4). This closes the expositional bootstrap without changing the claim. An independent analytic check is recorded in /workspace/branches/cc46b511-15b3-4a7d-ba4e-6a7b7a9b5a9b/ordinal-2-verification.md. The frozen checker and numerical output were inspected, not rerun; its low-noise stationary-point bisection cannot prove uniqueness there.

## originality

PASS

Conditional expectation and Gaussian conditioning are existing tools. The exact noisy single-time risk and its endpoint optimizer address a different design question from dense noiseless sampling of local time or noisy sampling for a linear Gaussian path target. No checked source gives the same risk or implies the optimizer expansion.

## value

PASS

Estimating a realized nonlinear path functional from a sparse noisy observation is a natural design problem distinct from estimating a mean or reconstructing a linear Gaussian path. The exact finite-noise risk and strict endpoint exclusion show that the practical terminal-reading heuristic is never exactly optimal, even though it becomes asymptotically close. The high-noise uniqueness and explicit placement gap give a quantitative prescription in this regime, not merely a numerical optimum. The theorem deliberately stops short of all-noise uniqueness or optimal adaptive sensing.

The dated certificate retains the supplied scientific assessment, sources and limitations.
