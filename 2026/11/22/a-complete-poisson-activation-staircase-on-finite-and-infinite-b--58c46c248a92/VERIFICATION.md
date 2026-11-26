---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

For the corrected claim, Parseval for the square counts singleton diagonal pair sums and double ordered off-diagonal pairs, giving F=Σw_i²p_i²+4Σ_{i<j}w_iw_jp_ip_j, equivalently 2S²−Σw_i²p_i²; phases cancel. The uniform L⁴ tail for ρ<1 is at most (Σ_{i≥J}ρ^(2n_i))^(1/2) on the L² unit ball, summable by integer separation. Finite coordinate projections take weak convergence to norm convergence, so the tail estimate and weak sequential compactness give global attainment. For any optimizer transfer mass from an active p_i; active coordinate derivatives agree and inactive derivatives are no larger. Euler's relation λ=Σp_i∂_iF=2F>0 is valid by absolute convergence, so t=λ/(4S)>0 and p_i=2S(w_i−t)_+/w_i² follow, with finite support. Summing w_i p_i yields the continuous strictly decreasing waterline equation on 0<t<1; its range contains 1/2. Normalization gives 2SD=1 and sharp value t/D. Existence and uniqueness of this necessary profile prove global optimality without a false concavity assumption. At t=w_k the waterline left side equals k−Σ_{i<k}ρ^(2(n_k−n_i)), so mode k is active exactly when G_k>0; at equality it is zero. The stated shift identity compares adjacent thresholds strictly; n_k−n_i≥k−i proves accumulation only at 1 for infinite E. Immediately above ρ_k, w_k−t_{k+1}=w_kG_k/(k+1/2+G_k); Taylor with D_k>0 gives the claimed positive squared-energy slope. At ρ=1 the L⁴ bound on differences of finite truncations proves density and the extended exact fourth-moment identity. Its strict deficit is Σ|c_i|⁴>0 for all nonzero infinite-spectrum vectors, while flat finite vectors approach ratio 2, i.e., norm 2^(1/4). Finite endpoint equality is precisely flat in magnitude by Cauchy–Schwarz. Positive pair coefficients give monotonicity in ρ. The independent bounded replay found no violations in 3,960 simplex points and 12 exact Gaussian-rational convolutions; reproduced all four quoted thresholds and sequential active sizes for {0,1,3,9,27}; onset finite differences agreed within 7.32e−7 relative error at offset 1e−8.

## originality

PASS

Best-of-knowledge pass for the exact weighted scalar optimum/unique profile and the ordered finite and infinite activation law with onsets, after separating the norm from its fourth power. The classical Λ(4) bound and unweighted endpoint, nonresonant three-frequency laws, and hypercontractivity context are antecedents, not separate priority claims. Treat a general weighted synthesis solution as a material equivalence risk, rather than taking absence of a search match as proof.

## value

PASS

The underdamped frequency-selection exercise becomes a sharp arbitrary-spectrum theorem: from a single scalar equation one learns not just a norm but exactly which modes contribute and how a new mode appears. The countably infinite support cascade and finite support at every strictly damped radius distinguish this from a small finite computation or a routine unweighted Λ(4) bound. Properly normalizing the endpoint is necessary for this interpretation, not itself the contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
