---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

Expanded S=(1−z)^3 Q=A(z)+z^N B(z) and checked the elimination identity zBS′−(NB+zB′)S=−N(N+1)(z−1)²[α(N+α+1)z+(1−α)(N+α−1)]. For z=−1−y, coefficient ratios V_j/U_j from binomial coefficients strictly decrease; monotone-likelihood-ratio weighting and direct boundary coefficients establish at most two positive-y roots for odd N or one for even N via Descartes. Even N has opposite endpoint signs and hence exactly one simple root; alpha=1 gives z=−1. Odd N has α=R_N(x), x>1, R positive and tends zero at both endpoints; max α_N exists, Descartes bound forces exactly two simple below, one unique double at max, none above; upper bound (N−1)/(2N+1) and fixed-x limit R_N(x)→1/(1+x) give α_N→1/2. Derivative elimination excludes nonreal repeats. Independently checked both algebraic identities and strictly decreasing coefficient ratios for N=2..15 with exact symbolic and rational arithmetic, and representative rational Sturm root counts N≤9. These samples supplement full all-N sign reasoning, not substitute for it.

## originality

PASS

Best-of-knowledge PASS for all-degree root-count parity diagram and unique collision parameter, narrowly excluding previously established polynomial construction and possible-double-root lemmas. Fu arXiv:2611.15406v1 itself defines precisely δQ, proves vertex-section convergence and at most one double negative root, exhibits N=3 threshold. Those are acknowledged as prior. Its cited results do not state or imply by themselves that all even degrees always have one root, all odd degrees one unique collision, or lim α_N=1/2; this review verifies the new coefficient-sign monotonic argument. Deng-Fu gap-polynomial setting is distinct.

## value

PASS

Complete real-root transition for a naturally occurring Bergman-kernel vertex polynomial answers a parameter classification left by Fu’s existence/multiplicity bounds. All-degree unique collision and its asymptotic limiting location are meaningful exact invariants beyond the previously known cubic instance; not a claim of all 2-variable Bergman zeros.

The dated certificate retains the supplied scientific assessment, sources and limitations.
