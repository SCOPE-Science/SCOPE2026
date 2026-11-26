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

I reconstructed the stationary pair covariances by a different moment representation. A pair of independent exponential energies of means s_i,s_j, after uniform redistribution, is a mixture of two independent exponentials with common mean w uniform between s_i and s_j: the old total has Laplace transform [(1+zs_i)(1+zs_j)]^{-1}, which is the segment average of (1+zw)^{-2}, and splitting at a fresh uniform fraction gives the independent exponential pair conditional on w. Each complete refresh sets its hidden mean to the reservoir mean. The hidden process on [T,T+Δ]^N is compact Feller, yielding a stationary exponential mixture with finite moments. Common-clock coupling of the energies cannot increase the L1 distance at an exchange and removes the refreshed coordinate's distance at rate g. The conditional expected distance decays at least as exp(−gt) from each fixed pair of initial states; bounded truncation of the resulting probability estimates gives uniqueness even for arbitrary a priori stationary laws. Normalize hidden means by subtracting T and dividing by Δ, so their resets are to 1 at the hot site and 0 elsewhere. Exchange replaces both by a common convex combination; on a hot–cold edge its second moment is (E S_H²+E S_C²+E S_H S_C)/3. The analogous cold–cold term and the rate-one counts of other neighbors give an independent four-equation solve. Because energies are conditionally independent given means, off-diagonal covariances are Δ² times the normalized hidden covariances. Independent replay: python /workspace/independent_checks.py (kmp routine) yields exactly the reported quartic P_N and cubic Q_N after multiplying by the reported D_N and taking the indicated signs. The original generator moments agree using E U²=1/3 and E U(1−U)=1/6. The positive denominator, strictly positive coefficients of Q_N, and (+,+,−,−,−) coefficients of P_N in descending order for N≥3 establish the signs and one simple critical root. Substituting g=Ns gives N^{-4}P_N(Ns)→2s(3s+1)(2s²−1); signs at fixed positive ratios straddling 1/√2 bracket the unique root for large N. This uses unit rate per unordered edge, not a unit total rate at each vertex. The submitted notes and code were read, not executed.

## originality

PASS

The exchange, reset operator, and hidden-temperature method are prior material. The complete-graph, one-impurity result supported as distinct is the explicit stationary pair-covariance classification (hot–cold zero and sign orientation, cold–cold positivity, and the critical scaling), not a new general mixture representation or moment closure. The reset-boundary version of prior KMP is a genuine derivation route, but no inspected result gives this graph-specific classification. The closest same-day comparison uses the identical local transition but different adjacency and sign-changing pair class.

## value

PASS

The theorem resolves which pair class reverses under increasing thermostat strength even on the most symmetric interaction graph with a single temperature defect. It distinguishes a genuine anticorrelation from a general positive-fluctuation intuition and predicts how per-site thermostat strength must grow relative to unit-per-edge exchange. This system-specific classification is useful beyond the routine act of deriving second-moment equations, and the stated scope keeps it separate from other reservoir mechanisms.

The dated certificate retains the supplied scientific assessment, sources and limitations.
