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

Grouping the orthonormal kernel expansion by degree modulo m produces mutually orthogonal one-dimensional blocks; only residue j meets the target, and its squared coefficient divided by the squared block norm gives the stated capture. A common rotation only changes coefficient phases. The logarithmic derivative in u is q minus the tilted mean of the residue quotient; its derivative is minus the strictly positive variance. The mean runs from zero to infinity. Hence q=0 has an unattained supremum 1, and q>=1 has a unique positive maximizer. Independently, the residue generating function equals rho^(-j)/m times the root-of-unity filter of (1-rho)^(-beta) at rho=u^(1/m). Only its k=0 term is singular at u=1, yielding F(u)~m^(beta-1)(1-u)^(-beta) and a tilted mean asymptotic to beta/(1-u). With the coefficient asymptotic and u_*^q -> exp(-beta) this gives the stated Gamma constant at fixed m,j,beta. For beta=2 let a=A/m and delta=1-u. The stationarity equation becomes q=2/delta-2+(1-a)(1-delta)/(1-(1-a)delta); it gives delta=2/q-(2+2a)/q^2+O(q^-3), and logarithmic expansion of the capture yields the relative correction -a/q. The equation also gives the correct B=0 linear case; direct differentiation gives the displayed quadratic for B>0. Replay: from /workspace, python -B branches/independent_reproductions.py 4 (SymPy, mpmath); checks aliasing numerically at 12 parameters and the ordinary Bergman expansions symbolically. The analytic argument, not these diagnostics, covers all positive beta and the limit. No unrestricted-node optimum, double-scaling uniformity, or formal certification is asserted.

## originality

PASS

Pass the explicit regular-orbit monomial optimization and sharp capture asymptotics, particularly the residue-sensitive refinement. Neither the Fourier filter, the general log-partition variance identity nor negative-binomial scaling is itself new. The inspected existence and sampling theorems and the related jet asymptotic do not give these optimized quantities for the conditional residue model.

## value

PASS

The regular orbit is a natural symmetric kernel dictionary for rotationally invariant analytic spaces. The evaluated radius and 1/q capture quantify the best achievable high-degree approximation by this dictionary, and the first correction distinguishes targets in different Fourier residues even though the leading law cannot. This is an independently useful sharp benchmark, not a claim of a new existence or Fourier theorem. Its value is limited to the prescribed dictionary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
