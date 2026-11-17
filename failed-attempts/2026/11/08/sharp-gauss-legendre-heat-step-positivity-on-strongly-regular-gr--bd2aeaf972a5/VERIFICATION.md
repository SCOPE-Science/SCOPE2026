---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The assigned RESULT.md proves the all-step finite-SRG classification by reducing A^2=(k−μ)I+(λ−μ)A+μJ to two positive nonzero Laplacian eigenvalues a,b with a+b=s=2k−λ+μ, ab=μv. Exact [2/2] Padé spectral interpolation gives edge 12h(12+6μh−μΔh²)/D and nonedge 12μh²(6+sh)/D, D=(12+6ah+a²h²)(12+6bh+b²h²)>0, Δ=v−s. Diagonals are positive as F(z)=((z−3)²+3)/(z²+6z+12)>0 on z≥0. Thus Δ≤0 gives positivity at all h; for Δ>0 edge entries vanish once at (3+sqrt(9+12Δ/μ))/Δ then turn negative. At h=0 identity; graph hypotheses exclude complete, disconnected and arbitrary feasible-parameter tuples. Actual source verifier verify_srg.py was inspected; independent comparison with the complete earlier proof and rational Petersen witness corroborates algebra; no finite test was used as a universal proof.

## originality

FAIL

Decisive exact prior coverage: the complete Oct 25 2026 Resultary RESULT.md states the same end-step matrix, identical edge/nonedge rational coefficients, Δ sign dichotomy, sharp positive crossing, spectral stability and Petersen/conference/triangular examples. Nov 2 2026 independently states the same theorem with arbitrary common edge conductance c and large-step asymptotic expansions. The submitted Nov 8 theorem is a duplicate theorem/special case rather than a distinct new mathematical result; no disclaimer or new numerical verifier can repair it.

## value

PASS

The parameter-only sharp positivity horizon is a meaningful complete graph-heat numerical-analysis classification that separates spectral stability from cone preservation, yields all-timestep families and exact loss-of-positivity times. Its scientific usefulness survives even though its content is previously published.

The dated certificate retains the supplied scientific assessment, sources and limitations.
