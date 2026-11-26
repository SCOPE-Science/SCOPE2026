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

I reconstructed the all-integer argument by Parseval applied to (Pρ f)^k. The equality j m + ℓ n = j′m + ℓ′n between different multinomial terms is impossible for n>km; at n=km the unique pair is (j,ℓ)=(k,0),(0,1). The resulting cross term gives exactly the phase constraint once all three magnitudes are positive. At criticality for a+bw+cw^k, Cauchy–Schwarz on ordered weak compositions at total degree J and the bound binom(J+k−1,k−1)≤k^J imply contraction. For J≥2 the bound is strict since distinct labelled assignments can yield the same occupancy, and a nonzero coefficient of any positive degree supplies positive mass at J≥k. The nonresonant diagonal sum is bounded by the aligned resonant sum because its third-mode weight is smaller. Aligned and diagonal sums have nonnegative terms and decrease under attenuation, so the critical bound extends below threshold. Critical strictness and compactness localize all global maximizers. The derivative in |c|² at the constant branch is −k+k² k^(−n/m)<0 for n>km, and is also negative at resonance along b=0. Thus b=0 cannot beat the constant, while the lower-mode objective H has local expansion 1+k²δx−(k²−1)x²/4+O(δx²+x³), x=|b|², giving an improving unique branch and the claimed nonresonant asymptotics. At resonance the right c-derivative at c=0 and b>0 is positive. I verified analytic optimization in x by substituting c=b^k u into the c-stationarity equation and dividing by b^k: it is analytic in x=b²,u,s, and at x=0 reads 2k s^k−2k(1−ks^k)u=0, with nonzero derivative in u. Negative transverse curvature gives the unique nearby optimizing c. Substitution gives H(x,s)+[ks^(2k)/(1−ks^k)]x^k+O(x^(k+1)) analytically, so the profile remains strictly concave and the shift in x is O(δ^(k−1)). The unperturbed objective loss from that shift is O(δ^(2k−2)), smaller than δ^k for k≥3. These formulas give the stated amplitude and sharp C_k and permit one unique aligned representative modulo the symmetries. I inspected but did not execute the supplied finite checker; the verification here is analytic, not an inference from finitely many moment orders. The neighborhood may depend on the fixed parameters.

## originality

PASS

Best-knowledge pass for the all-k≥3 near-critical support dichotomy, optimized amplitude and sharp gain, not for the critical Hardy threshold, first phase-sensitive collision as such, or the lower-order analogue. The latter has a different order balance, with an x² resonance gain already affecting the leading low-mode objective when k=2.

## value

PASS

This is a general-in-moment-order structural distinction in the behavior of near-threshold optimizers. At the first arithmetic collision, the suppressed mode becomes mandatory despite contributing at a parametrically smaller amplitude than the lower mode. The size and order of the sharp gain quantify when resonance affects the optimal value, which is not predicted by the known cutoff or by an undamped extremal calculation. The scope is a local three-frequency model, not the full dilation phase diagram.

The dated certificate retains the supplied scientific assessment, sources and limitations.
