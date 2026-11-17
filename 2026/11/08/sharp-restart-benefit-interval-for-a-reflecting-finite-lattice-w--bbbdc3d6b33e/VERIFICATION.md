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

PASS: For rate-one continuous-time 0..L reflecting path with absorbing 0, initial/reset site 2, the Laplace transform hitting recursion (2+r)phi_i=phi_{i-1}+phi_{i+1}, boundary (1+r)phi_L=phi_{L-1}, gives phi_2=D_{L-2}/D_L and renewal M=(1-phi_2)/(r phi_2). D_k coefficients binom(k+j,2j) obey the recurrence, and M(0)=2L-1. Coefficient cancellation makes Q_L=r^(L-1)-sum_{j=1}^{L-3}c_{L,j}r^j, c>0, hence precisely one positive root for L>=4 and no benefit for L=2,3. For L=4 Q=r(r^2-7), so rho_4=sqrt7. The hyperbolic continuant limit m_infty=y(y+1)/(y-1), y+y^-1=2+r, uniquely minimized at y=1+sqrt2, and monotone finite-L control gives convergence of all minimizers. Bounded exact symbolic checks agree for L=2,3,4,5,6,9 and do not prove the infinite statement.

## originality

PASS

PASS best-of-knowledge: generic renewal identities and reflected diffusion/lattice reset methods preexist. The inspected relevant Resultary theorem s2 is a discrete-time geometrically restarted reflecting chain with a different clock and boundary rule, so its inequality does not imply this continuous-time exact polynomial crossover. No prior full classification with the stated CTMC edge-rate normalization and exact first beneficial five-vertex path was found. Christou-Schadschneider 2015 remains inaccessible beyond abstracts; institutional retrieval returned vpn_disconnected, a material priority risk.

## value

PASS

PASS: It gives a complete all-rate improvement classification for each finite natural reflecting path, locates the sharp minimal state size for acceleration, and derives the exact infinite-volume optimal rate and finite expected time. These resolve a meaningful stochastic resetting boundary rather than merely restating renewal theory.

The dated certificate retains the supplied scientific assessment, sources and limitations.
