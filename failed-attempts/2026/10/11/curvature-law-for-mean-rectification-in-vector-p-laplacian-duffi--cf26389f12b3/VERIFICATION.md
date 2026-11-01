---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-25.md",
      "INDEPENDENT_AUDIT_2026-10-25.json"
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

Using the exact printed system (3.1), periodicity removes the time-average of the p-Laplacian-flux derivative and of each velocity derivative, yielding mean(g_j(u_epsilon,j))=bar e_j=g_j(alpha_j). The source Proposition 3.1 provides delta_j=u_epsilon,j-alpha_j=epsilon^gamma(w_j+r_epsilon,j) with ||r_epsilon,j||_infty->0 and mean(w_j)=0. Thus mean(delta_j^2)=epsilon^(2 gamma)(mean(w_j^2)+o(1)) and mean(delta_j^3)=O(epsilon^(3 gamma))=o(epsilon^(2 gamma)). The exact cubic Taylor identity gives 0=g_prime(alpha)mean(delta)+0.5 g_doubleprime(alpha)mean(delta^2)+b mean(delta^3); dividing by the assumed nonzero g_prime(alpha) yields the claimed formula. Sympy independently checked the polynomial expansion and simplification (3b alpha+c)/(3b alpha^2+2c alpha+d). This is a valid p>2, epsilon->0+ asymptotic on any local solution family with the source leading profile; no uniqueness or finite-experiment extrapolation is used.

## originality

FAIL

The exact same-model source arXiv:2610.02155v1 already establishes the C^1 leading profile u_epsilon=alpha+epsilon^(1/(p-1)) K(e-e_bar)+o(epsilon^(1/(p-1))), with K(e-e_bar) of zero mean, and prints the exact vector equation (3.1), whose period average is mean(g_j(u_j))=g_j(alpha_j). Substitute this profile into the elementary cubic Taylor identity and divide by the nonzero simple-root slope: the audited curvature/variance coefficient follows immediately and without a new lemma, estimate or analysis. Although the prior article does not print the derived coefficient, the complete mathematical assertion is a mechanically implied corollary of its explicit hypotheses and formulas; matching wording is not required for coverage.

## value

FAIL

The mean displacement is a naturally motivated physical observable and the formula is informative as exposition. As a proposed independent mathematical finding, however, it contains no independently needed nonstandard lemma, classification, genuine boundary or new calculation beyond the main source: it is the routine exact period-average identity and elementary second-order Taylor/Jensen correction applied to the already proved leading profile. The coefficient and sign follow mechanically, without overcoming an unsolved mathematical obstacle. It therefore falls on the textbook-deduction side of the shared value threshold. The source remains valuable; this separate one-line extracted corollary does not establish a standalone mathematical contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
