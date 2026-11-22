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

For the closed two-simplex, the coordinate z=(3(x0+x1)-2)+i√3(x0-x1) rescales Euclidean differences by constant √6. Direct symbolic derivation gives ż=−2z−bar(z)^2/4. Its radius obeys r′≤−2r+r²/4; since all simplex points have r0≤2, scalar comparison gives R(t)=8/(1+3exp(2t)). For two solutions, the factored difference equation w′=−2w−(bar(z1)+bar(z2))bar(w)/4 gives |w|′≤(−2+R/2)|w|; integration yields G(t)=16e^{2t}/(1+3e^{2t})². On z=−r the scalar exact solution r(t;r0)=8r0/[r0+(8−r0)e^{2t}] has derivative at r0=2 precisely G(t), so distinct initial pairs approaching that boundary vertex saturate the Lipschitz supremum. The proof includes t=0 and distinguishes supremum from attainment. Independent symbolic derivative and sample ODE checks support the analytic comparison.

## originality

PASS

The original non-Volterra flow and explicit symmetry-line solutions predate the calculation, but the globally optimal nonlinear time-dependent Euclidean two-point Lipschitz profile is not given by the inspected 2022 source. The 2026 analytic-solutions follow-up may cover quantitative contractivity and was accessible only in abstract, so priority remains best-of-knowledge with that specific risk.

## value

PASS

Computing an exact, time-varying worst-case contraction norm for a nonlinear population flow has direct utility in quantitative mixing/stability and differs materially from qualitative global convergence or a generic e^{-t} bound; the boundary median realizing sharpness identifies the source of loss.

The dated certificate retains the supplied scientific assessment, sources and limitations.
