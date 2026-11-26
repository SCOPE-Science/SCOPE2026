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

Independent reconstruction gives the reported determinant: with q=1-exp(-rt) and pi_i=lambda_i/r, the total-rate Bernoulli information is t^2 exp(-rt)/q; the species block is q times the multinomial information with determinant 1/product(pi_i); the squared change-of-coordinate determinant is r^(-2(k-1)). The score blocks are orthogonal by conditioning on capture, not in general independent as the proof's wording suggests. The time-resolved likelihood for elapsed time S=min(T,t), capture indicator D and label J has radial score D/r-S, so the radial information is E[D]/r^2=q/r^2 and the conditional categorical block is unchanged. This proves the determinant ratio, not a claim about the efficiency of each species estimator. The time-dependent log derivative is strictly decreasing from positive infinity to -1, is positive at x=2 for k>=3, and increases pointwise with k. The root identity exp(x_k)=1+(k-2)/(1-2/x_k) brackets the root between log(k) and log(k)+1 for large k and gives x_k=log(k)+2/log(k)+O(log(k)^(-2)). Thus k exp(-x_k) tends to one, q^(k-2) tends to exp(-1), and the same-horizon ratio is asymptotic to (log(k))^2/k, without the extra exp(-1) in the normalized optimal determinant. These statements concern a common duration at all stations, conditional on nominal r; they do not optimize mixed-duration designs, cost-normalized designs, or timestamped experiments over their own horizons. Read the supplied diagnostics without executing them.

## originality

PASS

The category likelihood and generic information matrix are established competing-risks methods, including an equivalent one-shot reliability formulation. The narrower surviving contribution is the continuous common-time optimization for arbitrary species/cause count with its logarithmic expansion and exact coarsening comparison. The relevant broader sources that could be read materially do not give a dominating design theorem; the inaccessible reliability full texts leave a specific priority risk.

## value

PASS

One shared duration is a natural logistical constraint. The optimum balances the disappearing information in the empty category against the increasing information in species labels, with roughly one empty station in k at large k. The exact determinant loss at the same horizon is useful for judging when timestamps can matter in the idealized setup. The result is a benchmark, not a field recommendation or a robustness study.

The dated certificate retains the supplied scientific assessment, sources and limitations.
