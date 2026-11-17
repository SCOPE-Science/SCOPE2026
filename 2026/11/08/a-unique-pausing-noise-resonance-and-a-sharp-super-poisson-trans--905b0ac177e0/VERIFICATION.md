---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

The explicitly inspected nine-state generator has all allowed entry, active hop, exit, and per-particle switching transitions. For the tilted exit matrix C, stationary pi and unique mean-zero Poisson solution h give J=1^T C pi and F=1+2(1^T C h)/J; this is standard perturbation of a finite irreducible generator. The supplied rational polynomials A(p,q) and P(p,q)>0 define F=A/P^2, and current J is explicitly rational. Reconstructed full verification code builds Q,C and checks exact positivity/negativity of differentiated polynomial coefficients: ∂p J<0, ∂q F<0. The degree-14 numerator for ∂pF has signs + at p^0 through p^2, - at p^14; each coefficient p^3 through p^13 has one positive q-zero in explicitly disjoint increasing rational brackets. Therefore for every q the p coefficients have one sign transition, giving one and only one positive critical point by Descartes plus endpoint signs. The Sturm count at q=0.33646 with an exact positive witness at q=0.33645 yields unique super-Poisson threshold via strict ∂qF<0. Symbolic p=qt and p=q²t limits and derivative-sign trapping give p*~tau q and p*~4q². The paper reports 16 numerical tilted-eigenvalue checks but the universal proof is exact algebra. The inspected script, not its claimed PASS log, shows the substantive certificates; finite samples alone are not the proof.

## originality

PASS

Thommen 2026 arXiv:2608.08074v1 investigates the same physical pausing TASEP with exit-count Fano statistics, but full paper Sections II-IV and Appendix focus on simulation of L=50-500 and collective large-system pause-number noise, with a minimal birth-death approximation. It does not derive the exact L=2 nine-state rational Fano formula, all-q unique positive pausing-rate maximum, a uniquely bracketed super-Poisson q_c, or the two-site vs one-site sharp smallest-chain contrast. Keisers et al. 2024 and Wang et al. 2014 establish related models/mean-current tools, not this full parameter-global exit-count noise theorem in available material. Generic tilted-generator formalism does not imply the exact Descartes/Sturm classification without dedicated algebra. Best-of-knowledge residual specialized literature risk remains.

## value

PASS

The two-site system is the smallest chain capable of a pausing-rate noise maximum for every positive unpausing rate, unlike its one-site counterpart. The exact all-parameter uniqueness certificate and sharp transition to super-Poisson exit fluctuations provide a meaningful finite-state benchmark for stochastic transport and counting statistics. It is a natural complete parameter classification of a physically motivated observable, not an arbitrary selected numeric case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
