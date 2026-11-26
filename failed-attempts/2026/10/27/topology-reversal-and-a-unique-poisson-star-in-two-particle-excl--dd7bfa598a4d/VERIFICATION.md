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

Independent event-pair proof: if W is the off-diagonal jump-rate matrix and lambda=W1, the stationary ordered-pair event density at positive lag u is pi W exp(uQ) W1. Reversibility gives (pi W)_i=pi_i lambda_i. Subtracting the squared mean yields Var(C_T)=mu T+2 times the integral of (T-u)<f,exp(uQ)f>_pi from 0 to T for f=lambda-mu. The centered finite-chain inverse gives the asserted Green identity and long-time ratio. Every hop changes shore count. The three rates of departure are 2m,N-2,2n in order of 0,1,2 particles on the m shore, with hypergeometric equilibrium weights. Set the middle Poisson potential to zero; the two end potentials are [N plus/minus (m-n)(N-2)]/[N(N-1)]. The Dirichlet terms after division by the mean and multiplication by two have weights (n-1)/(N-2), (m-1)/(N-2) respectively, so an absent endpoint contributes zero. Expanding their squares gives N^2+(m-n)^2[(N-2)^2-2N] over N^2(N-1)^2. The sign change is exactly between 5 and 6. The energy can vanish only for constant jump intensity, which requires m=1,n=3 up to exchange; then each holding time is independently exponential of rate 2 and the full process is Poisson. At N=3 there is only K_1,2 with F=10/9. Central and star large-N claims follow directly. `python3 /workspace/reviews/replay_finite.py 2` independently solved exact grounded linear systems on all 19 unordered full configuration graphs for 3<=N<=9, with agreement. The frozen verifier was inspected, not run.

## originality

FAIL

Demonstrable result-level overlap, not an inference about priority. The distinct catalogue record 3986b056b986 states the identical evaluated formulas, fixed-order reversals and unique star exception for N>=4 under the same dynamics, and its conclusions imply the frozen asymptotic comparisons. The additional N=3 boundary is the lone two-state case, not a distinct substantive claim. The full Poisson-process characterization also follows from the independently indexed general finite-graph theorem 016805168b38. Thus no supported distinct main claim remains against the verified catalogue coverage. The calendar paths alone do not establish who obtained the theorem first or whether the overlap reflects independent derivations.

## value

FAIL

The reversal and the exact invariant are substantively interesting, but they are already represented by a distinct, statement-equivalent catalogue finding. The only extension in the frozen scope is the graph K_1,2, which has no topology comparison and is an immediate two-state calculation; it does not supply an independently useful remainder.

The dated certificate retains the supplied scientific assessment, sources and limitations.
