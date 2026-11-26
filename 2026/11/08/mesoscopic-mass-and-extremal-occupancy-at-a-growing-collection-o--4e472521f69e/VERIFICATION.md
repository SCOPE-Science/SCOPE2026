---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

For the corrected file: on each directed edge, the incoming product-weight flux equals the corresponding next-site outgoing flux, so the canonical weights and conditional uniform weak compositions follow. The sign of the adjacent weight increment is the opposite of the displayed quadratic. For r>1 its values at -1 and N have opposite signs, and for r=1 it factors with larger root N-rho(M-1)>-1; the ceiling yields the first mode, including the zero boundary. A new exact-rational check found 81 ties among 510 finite cases and in each case the ceiling selected the first mode. Asymptotically, the crossing is at s_M(1+O(1/r+sqrt(r/M))) for s_M=sigma sqrt(Mr). The log ratios have a global slope bounded above by -c/M, producing a summable scaled Gaussian weight envelope, and local slope -(2+o(1))/(sigma^2 M), with the discrete crossing within one integer. Summing local log ratios and normalizing gives the Gaussian variance sigma^2/2 and the mass concentration. The weak-composition survival product gives fixed-site independent exponential limits. With the extra growth condition, the jth exceedance factorial moment has log ratio -j(log r+x) with uniform error O_j((log r)^2/r+(r/t)log r) on typical total-mass ranges, giving the Poisson zero-count limit. The relative scale error times log r is O_P(log r/sqrt(r)+log r sqrt(r/M))=o_P(1), permitting deterministic centering and scaling. These are proofs along the stated sequences, not finite-size extrapolation.

## originality

PASS

Credit is for the stationary growing-critical-defect asymptotics in this canonical ensemble, not the usual product law, the use of uniform compositions, or extreme-value asymptotics in the abstract. The strongest available fixed-defect ring comparison treats the exact critical two-defect case and has a different limiting total law. Inspected multiple-defect product and mesocondensation sources do not provide the combination of a diverging count, critical canonical balance, centered aggregate fluctuations and extremes at the scales stated here. The most relevant inaccessible paper remains a concrete priority risk.

## value

PASS

The count of critical defects tends to infinity while their density tends to zero; neither a fixed-defect nor an extensive-defect approximation captures this regime. The result quantifies how a mass of order sqrt(Mr) splits among growing defects, gives the aggregate variance rather than just a typical scale, and resolves the maximum on a third scale with a verifiable growth restriction. Those distinctions survive the corrected finite tie convention and have mathematical use in comparisons of critical finite-size ensembles.

The dated certificate retains the supplied scientific assessment, sources and limitations.
