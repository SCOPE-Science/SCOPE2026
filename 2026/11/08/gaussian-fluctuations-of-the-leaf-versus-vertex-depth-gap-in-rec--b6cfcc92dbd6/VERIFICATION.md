---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

Reconstructed the exact arrival updates and centering F_n=E_n-L_n(P_n/n)-n/4, W_n=L_n-n/2. The conditional mean includes the nonzero correction in E(C_{n+1}|T_n); checked predictable martingale innovations xi and depth-dispersion Welford update. Uniform recursive-tree depth exponential moments imply height O(log n) moments, Q_n/log n→1 in L2, leaf fraction→1/2 and conditional xi variance/log n→1/4. Weighted predictable variance 1/12 and fourth-moment Lindeberg yield F_n/sqrt(n log n)⇒N(0,1/12); ratio by L_n/n→1/2 doubles variance to 1/3. Independent exact rational checks over all recursive parent choices n=2..7 confirm the local innovation variance identity; they are not an infinite CLT proof.

## originality

PASS

Lundblad–Wagner (2026) Theorem 6 for uniform recursive trees gives the *same mean leaf-depth minus mean vertex-depth statistic* tending to 1/2, with first two moment limits, but no sqrt(n/log n) Gaussian statement; its Lemma14 only provides dominant moments. Grübel–Kabluchko (2015) have a Gaussian martingale-tail result for internal total path length and a separate binary-search-tree external-node statistic, neither matching the coupled actual-leaf/vertex-depth ratio. The submitted Gaussian variance 1/3 is not mechanically implied by these prior statements.

## value

PASS

Sharp second-order law for a naturally motivated statistic already investigated in recent primary literature; identifies nontrivial cancellation of global path fluctuations, the exact residual variance 1/3 and correct sqrt(log n/n) scale.

The dated certificate retains the supplied scientific assessment, sources and limitations.
