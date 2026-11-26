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

The feasible measures are nonnegative and locally finite on the line, T-periodic with finite mass M per period. The fixed-budget renewal integral shows convexity. For strictness, the periodic primitive of a zero-total difference of two measures would have to agree at almost every pair of endpoints for equality in exponential convexity; a right-continuous primitive constant almost everywhere is constant everywhere. Differentiating the renewal kernel and splitting the past/future factors gives the directional derivative −∫SP d(perturbation), with the pulse mass included on the state side only. Hence a candidate whose support attains the global maximum of Q=SP beats every other feasible measure, including singular competitors; strict convexity gives uniqueness. At a pulse, Q is continuous. In an untreated constant-transmission interval e^{δt}Q′=δCe^{2δt}+Aβ with A>0, so the signs at the high-season left and low-season right endpoints give the required full-interval signs. They are exactly exp(−M)≥max(x/H,L/x). For any fixed pulse mass the unique best phase maximizes the forward discounted transmission integral B(τ), decreasing in the high and increasing in the low season; thus no other phase rescues a single pulse past M_0. For the mixed candidate, putting r=ba and w=1−ca gives exp(−p)=w/(1−r) and δ/(δ+η)=w(1−r)/(1−r−rw). These close the periodic state and its adjoint with S=δ/(δ+η) and P=H/(δ+η) on the active interval. Q decreases on the rest of the high season, and increases on the low season precisely with the required endpoint sign H exp(−p)−L exp(p)≥0. This holds through p=(1/2)log(H/L), including equality at M_1. The root y_* lies strictly inside (0,h) under x>sqrt(HL); p′=η>0 and M′=2η+yη′>0. At y=0 the support reduces to the boundary pulse; M=0 is the unique zero measure. No higher-budget or other mixed ordering is asserted. Independent state/adjoint replay at H=4,L=1,h=1,T=2,δ=log 2 gave M_0≈0.287682, M_1≈1.476487 and, at y=0.5, M≈0.900802 with closure residual 5.6e−17 and no positive off-support Q gap above 2.2e−16 in a 401-point sample. Replay: /workspace/branches/addce1e1-6ee4-4d19-9ca2-096e1ac9f1d8/record5_independent_check.py. The example checks one case; the pointwise analytic sign and convexity arguments prove the general result.

## originality

PASS

The same model, general optimization machinery, qualitative pulse regimes, and the numerical example are prior work. The verified distinct claims are the sharp finite-budget single-pulse cutoff for all stated parameters and the increasing parametric pulse-mass law through the first mixed-regime endpoint under x>sqrt(HL). The main prior paper explicitly leaves the one-sided mixed pulse-mass question open; a bounded literature and catalogue comparison did not establish equivalent analytic coverage.

## value

PASS

For the established deterministic invasion objective under a fixed hazard budget, M_0 answers whether a single pulse suffices globally and gives the first point where another allocation strictly improves it. When the high-season constraint binds first, the evaluated branch fixes the pulse-versus-continuous split at every intermediate budget and explains the next endpoint in the published numerical example. This is a motivated finite-budget classification, not a clinical timing recommendation or a statement about infections or distinct vaccine recipients.

The dated certificate retains the supplied scientific assessment, sources and limitations.
