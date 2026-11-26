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

At zero the factors all equal one; for 0<gamma<1, log(1+q/j^gamma) is bounded below by a positive multiple of j^(-gamma), giving stretched exponential decay. The linear endpoint telescopes to one. Where 3^gamma-1<1, the geometric lower bound exceeds one. In the middle range the factor increases in its numerator j^gamma with q fixed and decreases in q; hence the lower powers at each left endpoint and the upper q at its right endpoint give a lower enclosure throughout the interval. For the near-linear range I checked the log derivative d_j and the beta integral giving the tail of u_k. For termwise differentiation and rearrangement the dominating series obtained from (2 log j+3 log 3)/j^0.99 times the B_j majorant is summable; the endpoint derivative is from the left. The negative numerator bound for the first five terms uses an upper denominator and a lower B_j, with the sign accounted for. Positive terms use a lower denominator and upper B_j. Gamma-moment Jensen with exponent 49/25 and log-convexity of Gamma between 2 and 3 give the claimed power tail, and the integral bound 3213/45125 is less than 0.08. The frozen directed-decimal code and its rounding directions were inspected but not executed. In /workspace/renewal_replay.py, independently certified powers by integer comparisons, logs by a rational atanh series with a geometric bound on its tail, and all enclosures by exact fixed-point arithmetic. It covers the middle range in 14 intervals with smallest certified lower bound 1.001106449194 and gives derivative upper pieces -1.479575503580, 0.801177356182 and 3213/45125. These rigorously imply the claimed -0.58 bound and hence the full strict inequality. The application is a sufficient condition for the one-community theorem, not a necessary condition and not a two-community result.

## originality

PASS

The specific sufficient-condition inequality for every strictly sublinear exponent, and the explicit uniform derivative bound, go beyond the actual statement of the target preprint. Older degree convergence via a branching-process method overlaps the consequence, not the sufficient condition itself.

## value

PASS

It closes an explicitly isolated gap in the domain of a recent coupling theorem by proving its exact sufficient condition on the whole sublinear range, and adds a reproducible quantitative derivative bound. Value does not depend on claiming first degree-distribution convergence or solving a multi-community problem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
