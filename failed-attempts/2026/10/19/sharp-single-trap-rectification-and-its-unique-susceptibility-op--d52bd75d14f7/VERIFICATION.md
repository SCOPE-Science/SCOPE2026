---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

An independent symbolic check uses the physical backward generator, its centered Poisson problems at zero bias, and left boundary current (rho_L-E[n_1])/2, rather than the uploaded forward bond-flux perturbation code. Stationarity conserves flux and makes these currents equal. It verifies both rational coefficient identities, positive polynomial coefficients, and exactly one derivative root on (0,1) by Sturm counting, with negative/positive endpoint signs. The verified optimum is u=0.318913576516811551474..., magnitude 0.00323613399987347948353..., and -log(u)=1.14283513291274316975.... At u=1 the first-moment equations are the linear current equations of five unit-resistance links (three interior and two reservoir), giving d/10. Reflection makes the three-site centered-defect current odd, and there is no interior site on shorter chains. Positive transition rates under the stated hypotheses imply analyticity at d=0 via the normalized finite stationary system. Replay: python3 /workspace/reviews/evidence/trap_response.py; output reviews/evidence/trap_response.txt. The proof verifies near-equilibrium optimization only, not optimal finite bias.

## originality

FAIL

The distinct Resultary record on minimal one-defect exclusion gives exactly the same two rational coefficients, sign theorem and minimal channel, in time units doubling all rates. Its coefficient determines the entire one-variable susceptibility curve, including the same critical-point equation; root counting and numerical isolation add a check and the evaluated optimizer, not a different response law or optimization problem. The duplicate coverage is demonstrated in the current corpus, not asserted as earlier priority: the matched record path date is November 2, the assigned path October 19. Earlier same-model primary literature establishes the phenomenon and symmetry obstruction, not the exact polynomial found here.

## value

PASS

As an exact benchmark the full claim isolates the smallest asymmetric interior trap, supplies a sign diagnostic and quantifies the most sensitive trap rate in the stated dynamics. These are useful checks on approximations and distinguish the quadratic response from finite-driving efficiency. Re-evaluating the bare optimizer from the already indexed curve is not a separate valuable repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
