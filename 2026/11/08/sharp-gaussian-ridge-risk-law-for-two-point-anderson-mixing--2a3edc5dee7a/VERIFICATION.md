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

The frozen ratio formula and tail are correct, but their inclusion in the finding created demonstrated prior coverage. The complete replacement restricts its finding to positive-ridge risks. Reconstructing the ridge minimizer gives γ=-WT/(T²+λ), with W and T independent by Gaussian sum/difference orthogonality, yielding E=θ+Whλ(T) with hλ(t)=(dt-λ)/(t²+λ). The regularized moments are finite. For fixed σ, substituting T=√λ s gives the integrable kernel s²/(1+s²)² with integral π/2; splitting off the bounded part of hλ and using Cauchy–Schwarz bounds all mixed and linear terms by O(λ^(-1/4)). This gives the claimed positive inverse-square-root coefficient also at θ=0. For λ=cσ² the Gaussian mass away from the nonzero mean of T is exponentially small against the bound on hλ. Expanding the squared conditional bias and the conditional noise variance locally gives the replacement’s displayed derivative formula for Q, including the c² contribution solely from the deterministic ridge bias. A separate bounded SymPy expansion gave zero difference for both A and Q and, at r=1/2 and θ=d=1, yields A=10, c*=21, Q(c*)=-1140. Strict convexity gives uniqueness on the specified fixed-c domain only; compact-positive-c uniformity follows from the same remainder bound. The frozen script/output were inspected, not executed; the saved 155 assertions are not proof of either limit.

## originality

PASS

The original Finding fails originality in part: 30f28a658eb2 items 1–2 give exactly the unregularized tail coefficient and moment classification at ρ=0, independently of any priority inference from dates. The replacement removes these from the finding, describes them only as credited background, and keeps the exact positive-ridge blow-up and fourth-order fixed-scale risk calibration. Those surviving claims were compared separately; the inspected stronger unregularized coupling law and iterative regularization bounds do not give either coefficient.

## value

PASS

The surviving claim quantifies two effects not captured by knowing the unregularized moment cutoff: exactly how regularization restores finite mean-square risk, and which fixed ridge/noise-variance ratio minimizes the first coefficient that distinguishes such choices. In a natural benchmark where the leading small-noise risk is common to all fixed c, the fourth-order coefficient gives meaningful information rather than a generic stability bound. The fixed-site and fixed-positive-scale restrictions are explicit.

The dated certificate retains the supplied scientific assessment, sources and limitations.
