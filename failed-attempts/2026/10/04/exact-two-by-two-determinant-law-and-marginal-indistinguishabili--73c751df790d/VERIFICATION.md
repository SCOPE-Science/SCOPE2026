---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

For a,b,c,d≥0 and S>0, (a+b)(a+c)/S−a=(bc−ad)/S; conservation of row and column sums forces the other entries to alternate signs. Thus P(V)=V iff ad=bc, equivalent to rank-one for nonzero 2×2 V. The diagonal D_M gives underestimation ratio 1/(1+M), and the strictly positive symmetric V_ε gives overestimation 1/(2ε); both are unbounded as M→∞ or ε→0. The positive pair V_ε,W_ε has exactly equal one-one marginals, so any common h within factor K must satisfy (1−ε)/ε≤K²; choosing small ε refutes any finite K. For β∈(0,1), linear exponential averaging with zero start gives the full bias-corrected target cell (β A_11+c)/(1+β), with identical compressed states under same marginals and common second gradient. Taking c=ε² produces ratio [β(1−ε)+ε²]/[βε+ε²]→∞. The proof is symbolic in all permitted real parameters, not inferred from samples.

## originality

FAIL

The submitted mathematical components are already implied by two older primary results: Shazeer–Stern (2018), Section 3 Lemma 1 and Algorithm 2, gives precisely the normalized marginal outer product and says row/column marginalization commutes with exponential smoothing; the classical sharp Fréchet cell bounds for fixed row/column totals, stated explicitly in Uhler–Richards (2017), equation (2.2), give the entire unconstrained 2×2 cell interval. Specializing to equal one-one marginals immediately produces the same V_ε/W_ε indistinguishability, unbounded relative fidelity, and exact one-dimensional checkerboard error upon subtracting the independence reconstruction. The two-step variant is one iteration of the pre-existing linear EMA recursion. These are covering mathematical implications, although the newer Adafactor wording and assembled toy examples need not appear verbatim. No distinct nonstandard theorem beyond these routine specializations was established.

## value

PASS

The target is a natural performance-relevant invariant: whether a memory-efficient factored adaptive moment can recover per-coordinate scales at bounded distortion. The sharp 2×2 information-loss demonstration and its dynamical persistence isolate exactly what compression cannot preserve, independently of optimizer convergence and empirical clipping remedies. This is mathematically relevant as a cautionary lower-bound example even though the proof is elementary and the components were already implied by general prior fixed-margin theory. Value does not confer novelty.

The dated certificate retains the supplied scientific assessment, sources and limitations.
