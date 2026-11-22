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

For all real nodal data, exact step decomposition y=y0 1+sum Δy_k s^(k), constant reproduction and Jordan variation triangle inequality reduce the operator norm to max variation of the n one-step responses; each step is admissible, so this reduction is equality. For x=m+t the alternating denominator S_m=A_{m+1}(t)+A_{n−m}(1−t)>0, and alternating-tail remainder plus reflection A_inf(t)+A_inf(1−t)=π/sin πt give the C1 reciprocal approximation 1/S_m≈sinπt/π with uniform summable end-cell errors. On non-jump cells, derivative variation differs from (2/π)A_q(d) by O(d^−2+δ_m/d); harmonic double-sum bounds make total error O(1), including the one crossing cell. Summing the A_q(d) parity patterns gives a universal leading bound (2/π)H_n+O(1), while jump k=1 has main sum H_{n−1}, attaining the coefficient 2/π. Independently verified exact barycentric denominator and single-jump formulas for all tested integer n=2..15, every cell m and step k using rational t=2/5. This finite check corroborates algebra, not the uniform n→∞ remainder; the analytic tail and reciprocal estimates provide that.

## originality

PASS

The 2010 Bos–De Marchi–Hormann paper establishes logarithmic Lebesgue (supremum-data-to-supremum-output) growth for the same rational formula, but not the discrete nodal BV-to-continuous Jordan variation norm. A separate all-fixed-positive-degree Floater–Hormann variation theorem has a related 2/π coefficient but explicitly excludes degree d=0 (Berrut) and requires different endpoint weight geometry, so it cannot by specialization supply this result. Bounded monotone overshoot in L∞ does not control accumulated oscillations; the endpoint jump's variation is a distinct derivative integral. No stronger exact Berrut BV theorem was identified in the inspected primary source material; unindexed equivalents remain possible.

## value

PASS

Berrut interpolation is widely used for stability; its precise discrepancy between bounded step overshoot and unbounded total oscillatory variation has clear mathematical and approximation implications. The sharp universal coefficient 2/π is not a table recomputation or an obvious consequence of the known Lebesgue coefficient: its proof exploits alternating-tail cancellation and accumulated derivative variation. Exact extremal reduction and an endpoint-adjacent asymptotic witness make this useful to BV stability analysis.

The dated certificate retains the supplied scientific assessment, sources and limitations.
