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

For m≥2, a>0, m−2<α<m−1 and η>−a, b_n=(n+a)^{α−1}(n+a+η)>0 and the weights tend to one. Telescoping makes the defect diagonal with entries Δ⁺ᵐb_n/b_n. The m-fold fundamental theorem of calculus writes the forward differences as cube averages of derivatives; the two falling factorials for α and α−1 have opposite signs (negative and positive, respectively). Hence the entry sign is exactly sign(η−τ_n). Writing c=α/(m−α), r=α−m−1, Y=x+Σu_i and weighting cube measure by Y^r, τ(x)=c E_xY. Differentiation gives τ′/c=1+r(1−E_xY E_xY⁻¹)>1 by strict Cauchy–Schwarz. Uniform expansion over the cube gives τ(x)=c(x+m/2)+O(1/x); thus gaps are strictly greater than c and approach c. The sign pattern yields the exact concavity interval, each positive rank and kernel, and an infinite negative tail for every η. Inverting the threshold asymptotic gives r_+(η)=η/c+O(1), with strict index counting at equality. For fixed η the entries equal α^{↓m} n^{−m}+O(n^{−m−1}); closure yields a compact diagonal defect. For the sorted absolute values, sandwich the tail between (|α^{↓m}|±ε) times decreasing power sequences, then shift the indices by at most the finite prefix length. This justifies the leading singular-value constant even without assuming the original absolute entries are already ordered. The p-series test includes divergence at p=1/m. A separate bounded Decimal check for m=2, α=1/2, a=1 found initial thresholds about 0.5907703, 0.9519487, 1.2978908; its finite checks are not all-index evidence. The frozen verification script was inspected, not run.

## originality

PASS

Credit the diagonal finite-difference reduction, integral identity, and operator lifting theory as established. The distinct supported result is the classification of the two-power fractional family with explicit strict threshold separation, positive ranks and kernels, and sharp defect-ideal cutoff. The strongest retrieved broader and close-family statements do not supply that classification.

## value

PASS

The neighboring-power perturbation preserves the large-index leading moment but can reverse the sign of the finite head of the operator defect. The exact parameter region tells when higher-order concavity and its lifting hypotheses apply, the thresholds tell precisely how that structure fails, and the parameter-independent ideal cutoff quantifies the remaining infinite negative tail. This is a motivated sign and spectral classification rather than a finite test of a single shift.

The dated certificate retains the supplied scientific assessment, sources and limitations.
