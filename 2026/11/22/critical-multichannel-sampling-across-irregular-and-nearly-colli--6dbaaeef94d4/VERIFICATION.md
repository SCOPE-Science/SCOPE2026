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

For x₀≥d and x gaps ≥L>2d, s_(kσ)≤e^(−kL), so the sensor is Hilbert–Schmidt. With t_j=e^(x_j) and weight t_j, the exact analysis block is U_k diag φ(x_j−x_k−δ_(kσ)); its diagonal has least singular value ≥ma_d and norm ≤M/√(2e). Since φ(u)≤e^(−|u|/2), both block Schur sums of the off-diagonal part are bounded by ε. Neumann inversion gives an isomorphism onto the full coefficient space, not merely a lower frame inequality. For finite supports, geometric summation gives the integer-time Gram form; each diagonal block is bounded between m²/2 and M²/(1−e^(−2)) by the bound on s/(1−e^(−2s)). Concavity gives 1−e^(−(a+b))≥(a+b)(1−e^(−2))/2, and the separated logs give √(min(a,b)/max(a,b))≤e^d q^|k−ℓ|, so the off-block operator norm is ≤η. The estimates extend by density (coordinate evaluations agree with CA^n). In the counting argument only the unique cluster interval intersecting log R can contribute a discrepancy, of at most r, also at endpoints; repeated eigenvalues count with multiplicity. The formal theorem has r modes per cluster and does not assert uniform invertibility for arbitrary varying cluster cardinalities. Independently recalculating the example at d=1/4,L=12,m=M=1,r=4 gives a_d≈0.3137918482, ε≈0.0056315476 and η≈0.0590414234. The supplied checker was inspected, not executed; its 27 real-orthogonal finite sections do not verify arbitrary complex mixing or the infinite theorem.

## originality

PASS

The supported distinction is the explicit real-time weighted Riesz isomorphism with one time per full r-mode cluster for arbitrary uniformly invertible complex U_k and bounded internal offsets, jointly with explicit bounds for the original integer-time frame. Neither the rank-r lower bound, scalar Riesz sampling, nor a characterization of the unthinned integer orbit supplies that simultaneous construction. The counting lower-bound principle, scalar designs, and Schur/Neumann methods are not original here.

## value

PASS

The meaningful gap is between a necessary sampling count for several sensors and stable, onto data at that count, as ordinary scalar mode separation breaks at close or repeated eigenvalues. The explicit mixed-channel construction provides both bounds with no within-cluster spacing lower bound, and permits logarithmic centers without uniform upper gap control. It is a useful model class and a quantitative witness to rank-r critical sampling, not a proof of universally optimal designs or best separation constants.

The dated certificate retains the supplied scientific assessment, sources and limitations.
