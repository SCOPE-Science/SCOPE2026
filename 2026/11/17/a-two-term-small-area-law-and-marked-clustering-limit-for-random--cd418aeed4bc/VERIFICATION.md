---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

PASS. With one distinguished circle-uniform vertex, the four gaps in cyclic order are (2π) Dirichlet(1,1,1,1), giving density 6/(2π)³. Shoelace area exactly factors as 2sin((a+b)/2)sin((b+c)/2)sin((c+a)/2). The area-zero locus is the six edges of the gap tetrahedron; outside four vertex neighborhoods the sublevel volume is Oδ(t²) because two transverse gaps must be small. At each vertex put a=Wu,b=Wv,c=Ww. The Jacobian is W², and sine expansions produce A=W³h(1−W²Q/24+O(W⁴)), h=(1-u)(1-v)(1-w)/4 and Q=Σ(1-u)². Solving for W_t³ gives t/h+Q(t/h)^{5/3}/24+..., so radial integration gives t/(3h)+Q(t/h)^{5/3}/72. Unlike an unjustified uniform inversion near simplex corners, h^{-5/3} is integrable (h~distance to a corner on two-dimensional Δ), and capping W≤δ gives O(t²) first-term error; dominated convergence yields t/π+C_*t^{5/3}+o(t^{5/3}). Independently integrated the leading simplex integral π²/4 and the second coefficient C*=0.242278704743 using SciPy, not copied from source output. Radial substitution R=W(h/t)^{1/3} yields R³~Uniform, hence R~Beta(3,1), normalized gaps density h^{-1}/π² and independent uniform gap index/rotation. Boundary concentration and weak convergence are accounted for, not inferred from a simulation.

## originality

PASS

Best-of-knowledge PASS for the explicit positive t^{5/3} lower-tail correction and the full marked clustering limit. A published conditional-on-diagonal-angle area law already determines the entire scalar area marginal via integration, so merely obtaining a marginal distribution is not novel; its main theorem and proof do not state the two-term small-area expansion or normalized clustering marks. General extremal random-inscribed-polygon theory is focused on maximal rather than near-zero area. The exact distribution could in principle permit deriving the scalar coefficients; this implication remains a priority risk.

## value

PASS

PASS. The area-zero set has competing two-gap and triple-gap strata; proving which geometry dominates, quantifying its nonanalytic t^{5/3} correction and obtaining its marked shape law are natural geometrical probability questions. The exact positive coefficient and independent Beta/shape/orientation limiting factors provide sharp conditional information not encoded in the previously known moments or stated diagonal-angle CDF. The nontrivial corner integrability and uniform control distinguish the result from an arbitrary tiny numerical slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
