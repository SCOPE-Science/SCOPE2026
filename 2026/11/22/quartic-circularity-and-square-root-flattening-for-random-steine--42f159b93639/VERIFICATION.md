---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification of the stated theorem

**Analytic normalization.** The squared semiaxes of the optimal inellipse have the eigenvalue ratio of \(S=\sum_j(p_j-g)(p_j-g)^{\mathsf T}\). Its trace is the sum of three squared chords divided by three, and its determinant is four thirds of the squared triangle area. This yields \(K=2R/(1+R^2)\), with \(K=\sqrt3\,\ell_{12}\ell_{23}\ell_{31}/\sum\ell_{ij}^2\) for unit-circle vertices.

**Small eccentricity.** After fixing the first vertex, each of the two equilateral configurations produces the same positive definite form \(u^2+v^2-uv\); the local scaled region has area \(9\pi/(8\sqrt3)\). Multiplying by its two branches and the angular density \((2\pi)^{-2}\) gives \(3\sqrt3/(16\pi)\).

**Small axis ratio.** The shortest-chord lower bound excludes any exceptional configurations away from pair collisions. Every pair contributes a signed angular gap \((-4\eta/\sqrt3,4\eta/\sqrt3)\), hence coefficient \(4/(\pi\sqrt3)\); multiplying by three possible pairs gives \(4\sqrt3/\pi\). Pair-overlap probability is \(O(\eta^2)\). The ordinary eccentricity relation \(e^2=1-R^2\) gives the \(4\sqrt6/\pi\) square-root coefficient.

**Numerical diagnostics.** Running `python checker.py` with the dependencies in `requirements.txt` passed 1000 independent deterministic matrix/chord comparisons, six collision-local derivative checks and deterministic \(2^{22}\)-point Sobol checks. The simulation coefficients at \(e<0.14\) and \(R<0.04\) were approximately \(0.10550593\) and \(2.20032930\), respectively, versus analytic limits \(0.10337417\) and \(2.20531558\). Such finite diagnostics are *not* infinite proofs, and they do not independently certify historical novelty.

**Unproved extensions.** No uniform estimates are asserted for nonuniform circle sampling, arbitrary convex ovals, random interior triangle vertices, or varying numbers of vertices. The mathematical literature comparison is nonexhaustive; independent audit has not been performed.
