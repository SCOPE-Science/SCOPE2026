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

Each bond of the simple prism line graph belongs to just one base-vertex triangle, valid also for n=3. A triangle costs -J for not-all-equal edge spins and 3J otherwise. Opposite signs on the rungs and rails attain the lower bound everywhere, so the full ground-state set is exactly the NAE assignments at energy -2nJ. Conditioning on two incoming and two outgoing rail spins and summing the allowed rung spin gives the displayed entries with weight z^(outgoing rail sum+rung). Closing with a trace counts labeled assignments with every spin weighted once. Rail exchange splits off a one-dimensional eigenvalue -(z+z^-1); the complementary three-dimensional block has the stated cubic. At z=1 its roots are -1 and (5±sqrt(17))/2. At fixed n, fluctuation–dissipation and the finite positive excitation gap reduce T chi_n to the ground-state variance of M divided by 3n, exactly the second log-fugacity derivative shown. Near zero log fugacity the four eigenvalues admit analytic branches on a complex disk (they are simple at 0), with the ratios of the three subleading eigenvalues to L_+'s branch uniformly smaller than one in modulus on a sufficiently small disk. Thus n^-1 log trace differs from log of the leading branch by an analytic exponentially small correction, whose derivatives at zero tend to zero by Cauchy's estimate. Implicit differentiation of the cubic gives zero first derivative and the stated radical second derivative divided by 3; this justifies the stated order of limits only. Independent replay: python3 /workspace/checks/frozen_replay.py 5; weights constructed from the constraints, exact cubic and radical, and separate bit-enumerated NAE counts 86, 450, 1942 at n=3,4,5 with sum M^2 of 150,1152,5990 and exact weighted checks at z=2. The radical evaluates to 0.20787388005845981757.

## originality

PASS

The supported distinct claim is the spin-magnetization Laurent polynomial and resulting ordered longitudinal Curie limit for the specified classical zero-field prism-line ensemble. Do not assign originality to the transfer method or to the shared entropy growth base. The retrieved same-day ice record establishes overlap in that base but not chronology.

## value

PASS

Complete magnetization weights of a natural frustrated cubic line-graph family give exact finite-circumference responses and higher moments, not just unweighted degeneracy. The nontrivial limiting longitudinal Curie coefficient is independent information from the residual entropy and useful as a finite-width benchmark with a specified order of limits. It makes no assertion about quantum transverse response, other couplings or the reverse order of limits.

The dated certificate retains the supplied scientific assessment, sources and limitations.
