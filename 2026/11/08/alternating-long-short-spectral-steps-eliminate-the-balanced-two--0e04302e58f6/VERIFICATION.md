---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

Frozen RESULT.md uses two positive SPD eigenvalues a>b>0 and delayed BB1 on odd k, BB2 on even k with an undelayed first BB1. Exact mode ratio epsilon_k=||P_a r_k||^2/||P_b r_k||^2 obeys epsilon_1=1/epsilon_0 and epsilon_(k+1)=c_k epsilon_k/epsilon_(k-1)^2, c_odd=1,c_even=(b/a)^2, verified independently by Fraction iterates for three (a,b) and nine mixed initials through seven delayed steps. Thus phi_(k+1)=phi_k-2phi_(k-1)+{0,-2log(a/b)}. The bounded forced 2-cycle p_even=-L/4,p_odd=-3L/4 is incompatible with phi1=-phi0 when L>0, so a genuine homogeneous oscillation with roots sqrt2 e^{±i theta} remains. Every four phases contain positive and negative excursions bounded below relative to (sqrt2)^k since theta∈(pi/3,pi/2), yielding two-sided exp(-C(sqrt2)^k) mode norm bounds and double-log exponent log(sqrt2). Pure eigenspace terminates in first step. Finite computation not used as proof of asymptotic.

## originality

PASS

BB1/BB2 and two-eigenmode superlinear phenomena are classical; Yang–Yuan arxiv:2609.12100 proves R-linear global bounds for each FIXED BB spectral weight, not the alternating parity-dependent weight and its sharp all-initial double-log exponent. The published Resultary same-day unmixed BB1 log-periodic envelope explicitly retains an exceptional balanced geometric orbit. No prior inspected theorem supplies this exact alternating-delay escape and sharp exponent; priority remains best-of-knowledge.

## value

PASS

The exceptional balanced orbit is a genuine dynamical obstacle to superlinear BB1 convergence on an entire class of two-eigenmode systems. A precisely specified alternate long–short history eliminates it for every mixed starting residual, with a sharp asymptotic decay rate. This is a motivated structural algorithmic result rather than renaming an existing recurrence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
