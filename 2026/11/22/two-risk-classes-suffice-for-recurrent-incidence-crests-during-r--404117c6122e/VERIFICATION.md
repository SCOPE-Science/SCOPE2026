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

In cumulative pressure x, I'=A−γ/β and J'/β=A(A−γ/β)−IB. Independent rational log enclosures obtained by integrating alternating geometric bounds on 1/(1+u) certify +,−,+,− at the four ordered points of the frozen witness (replay: python /workspace/checks/reproduce.py 1). A decreases and is still above γ/β at the last point, hence prevalence is positive and increasing on the entire witnessed interval and all four points are reached in finite time. Analyticity and the alternating signs give two strict interior maxima separated by a strict minimum. The unique crossing A=γ/β is later and is also reached with positive prevalence; no subsequent maximum is possible. Strict margins give a relatively open set in the admissible parameter space. In a single occupied class the bracket λ(S−I)−γ/β is strictly decreasing while λS>γ/β and negative afterward, so there is at most one strict incidence maximum. If the susceptible mass is zero, incidence is constant zero; the informal strictly-decreasing-or-unimodal description is for positive susceptible mass. The count in the example is a lower bound, not an exhaustive count.

## originality

PASS

The model, multiple incidence peaks through other mechanisms, and aggregate prevalence unimodality have precedents. The inspected evidence does not cover the sharp minimum for two strict aggregate incidence peaks before the unique prevalence maximum under fixed susceptibility and time-constant shared-pool SIR. This is a bounded best-of-knowledge judgment.

## value

PASS

The sharp minimal heterogeneity threshold identifies a genuine limitation of inferring the number or ordering of incidence peaks from unimodal prevalence. Robustness to parameter perturbation rules out a fine-tuned coincidence. The value is as a structural result for a deterministic mathematical model, not as an outbreak prediction or claim about measured epidemic curves.

The dated certificate retains the supplied scientific assessment, sources and limitations.
