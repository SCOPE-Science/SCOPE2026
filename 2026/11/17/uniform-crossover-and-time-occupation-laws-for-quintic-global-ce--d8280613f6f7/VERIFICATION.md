---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

The RESULT.md Hamiltonian H=(1/2)exp(alpha*x^4/2)*v^2+int_0^x exp(alpha*s^4/2)(s+beta*s^5)ds has zero derivative; potential is even and coercive for beta>0, so every positive level is a regular oval. The exact physical-time quadrature after x=Au gives scaled period 2sqrt(2) int exp(q*u^4/4)/sqrt(I_q+epsilon*J_q)du. I_q/J_q is the q-exponential tilt expectation of r^4 on [u,1], hence nondecreasing in q; at q=0 it equals (1+u^2+u^4)/3 >=1/3. This proves the novel global J/I<=3 for all q,u, and two-sided period bound uniformly even q=alpha*A^4 -> infinity. Direct logarithmic differentiation gives strict Phi decrease; endpoint beta integral and q(1-u) layer dominated convergence give 2pi and turning-layer density. The normalized quarter-time integral proves physical occupation. Independent symbolic conservation, 20 tilt kernel comparisons, and verified RESULT/code paths corroborate, not replace these infinite proofs. Boundary beta=0 is excluded; q is nonnegative, A>0.

## originality

PASS

PASS solely for the q-independent all-amplitude relative-period bracket. The previously published November 1 matched-crossover result already has exactly the same Phi(q), rho_q law (in stronger total-variation form), strict Phi monotonicity and turning-point layer, plus likelihood-ratio ordering and overshoot; none of those parts receives independent novelty credit. Its relative-error bound requires a bounded q-range and grows as exp(Q/2), whereas the current positive-tilt monotonicity yields the new sharp simple q-uniform kernel cap 3. The 2026-10-11 fixed-parameter theorem supplies the endpoints, not the all-q bracket.

## value

PASS

PASS: there is a genuine natural gap between the pure-quintic and velocity-coupled asymptotics when alpha*A^4 varies without bound, not covered by bounded-q matched expansions. A nonasymptotic two-sided relative bound holding uniformly for all A, alpha, beta provides a useful stability/control estimate for original-time periods, even though most accompanying asymptotic statements are prior work.

The dated certificate retains the supplied scientific assessment, sources and limitations.
