---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

The exact scalar epoch map has common A=product(q_i) and exchangeable permutation offset B. Full-epoch RR equals A^m x0 + sum_{j<m} A^j B_j with iid B_j; SO equals A^m x0 + S_m B_0. For 0<A<1, A^j/S_m are positive weights summing to one: convex Jensen gives RR <=cx SO. For -1<A<0 and m>=2, S_m in (0,1), so the signed normalized vector has largest entry >1, majorizes (1,0,...,0), and Schur convexity for iid B_j gives SO <=cx RR. Bounded support justifies all convex expectations and stationary limits. Covariance factors sum A^{2j} versus S_m^2 give strict square-loss separation when tr Cov(B)>0. Independent exact-rational stop-loss enumeration verified 20 1D choices across positive/negative A and m; this is corroboration only. Example A=-1/8, offsets -3/8 and 15/8 gives Var_RR=9/7, Var_SO=1, and strongly convex objective gap 3/14. No within-epoch or noncommuting matrix assertions.

## originality

PASS

On the inspected prior work and Resultary findings, the sharp sign-dependent, all-convex-loss comparison for exactly completed scalar-affine RR versus fixed SO remains an identifiable specialization. The probabilistic Schur/Hardy–Littlewood–Pólya comparison is classical, not claimed new. Safran–Shamir and Mishchenko et al. bound shuffling convergence under distinct observables/stepsizes; Domingo-Enrich gives noise-spectrum and phase-averaged stationary covariance under an approximation, not the signed full-epoch convex order; Resultary's 2026-10-12 two-sample stationary-risk envelope compares fixed/alternating-order couplings rather than the claimed every-epoch, every-convex-loss relationship. Residual risk of an equivalent general exchangeable affine-recursion theorem remains.

## value

PASS

The common epoch multiplier's sign creates a sharp, model-relevant reversal in *every convex risk*, despite stable scalar epochs, rather than a mere variance example. The theorem covers arbitrary finite permutation support, all dimensions with scalar multipliers, all epoch counts, stationarity, and a concrete strongly convex SGD witness. General convex-order technology is standard, but its sharp shuffling-policy implication is a meaningful algorithmic boundary, not a renamed inequality without motivated application.

The dated certificate retains the supplied scientific assessment, sources and limitations.
