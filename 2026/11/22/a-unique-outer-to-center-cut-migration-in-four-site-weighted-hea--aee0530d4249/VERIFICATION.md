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

Write f as a constant plus its three adjacent jumps times their step functions. The ℓ¹ norm on jumps gives the exact maximum of column norms, attained by a maximizing step. For u>0 the connected heat kernel is strictly positive and stochastic, so the step residual has strictly negative signs before its edge and strictly positive signs after; two distinct jumps, irrespective of their signs, conflict at a coordinate. Thus even a tie creates no multi-step extremizer. Reflection splits the generator into the even block with eigenvalues 0,2 and odd block [[1,−1],[−1,1+2r]]. The coefficients follow from twice the cross-cut leakage, giving end loss 2(1−H_11) and middle loss 2−(1,1)e^{−uA_r}(1,1)^T. Independently, writing Q=s²+2(1+r)s+2r, the Laplace transform of the difference is (s+1)/(s(s+2))−(s+3)/Q, which gives the positive-convolution identity with transforms ĝ=1/Q and q̂=1/(s(s+2)). At r≥1 both contributions are nonnegative with the convolution strictly positive. For 0<r<1 the ratio (q*g)/g rises strictly since log g has strictly negative second derivative, so each fixed-v integrand q(v)g(u−v)/g(u) increases and the integration interval expands. The ratio starts as u²/6 and tends to infinity since (q*g)(u)→1/(4r) whereas g→0. This proves the unique positive crossing and its sign order. Continuity in r at fixed u>0 forces u*→0 as r↑1, where the local expansion is uniform. For r↓0 use u=x/r and the substitution y=rs in the convolution; g_r(y/r)→e^{−y}/2 and q((x−y)/r)→1/2 for 0<y<x, with a uniform bounded integrand. This gives r(q*g)(x/r)→(1−e^{−x})/4 and the strictly increasing scaled root limit log 3. All conclusions use counting ℓ¹, unweighted jump variation, and positive time. The script and its reported finite tests were inspected but not executed.

## originality

PASS

The unweighted four-site case is exact indexed overlap and the generic path step reduction is not counted as new. The audited distinct claim is the weighted comparison, especially that the weak central edge causes exactly one switching time with specified sides, strict one-step rigidity through the tie, and two threshold asymptotics. Other inspected heat-gradient or graph-cut records do not cover this setting. Same-day indexing of the exact r=1 overlap does not determine priority.

## value

PASS

The four-site reflection-symmetric path is the smallest such path with competing balanced and outer cuts. The perturbation exposes a genuine finite-time effect that the unweighted norm cannot see: fast-time sensitivity to conductance initially favors an outer edge when the middle is weaker, but late-time mass balance favors the middle. The record shows a single switch, identifies every equality case even at the tie, and quantifies the separate nearly unweighted and nearly disconnected regimes. This is a complete exact classification within its natural model, not merely a matrix-exponential example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
