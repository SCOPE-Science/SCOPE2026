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

At eta=zeta criticality the physical quadrant is invariant and y activity bounded; x decreases under x’=-zeta*x*(x+s*y)/(1+s*y), forcing x->0 and y->0. For r=y/x, r’=kappa*k-(kappa-q)r with q=-x’/x->0, so r->k, establishing x~1/[zeta(1+s*k)t]. Differentiation yields V=((1+s*y)/x)’=M+s(zeta-kappa)(y/x-k), M=zeta(1+s*k); hence V is exactly affine when kappa=zeta. For U=(c+d*y)/x, all-state constancy first forces eta=zeta from the y=0 1/x term, then comparing y-coefficients forces d=c*s and kappa=zeta. Off resonance delta=y-kx solves delta’+kappa delta=-k x’; stable convolution gives delta=(k*M/kappa)x²+O(x³). This yields V’=M+s*k*(zeta/kappa-1)/t+O(log t/t²), which integrates to the finite-limit log correction. Independent symbolic derivative and coefficient calculations produced exact zero residual. Finite numerics do not prove these asymptotics.

## originality

PASS

Broader critical adaptive-SIS literature proves inverse-time decay and log corrections in a different contact-density system, but its hypotheses and vector field do not contain this positive relaxing activity/inhibitory rational transmission law as a direct specialization. The new exact all-state reciprocal affine identity and rigidity at kappa=zeta are nontrivial additional structure. Full motivating primary text inaccessible, so this is a qualified best-of-knowledge originality judgment, not confirmed historical priority.

## value

PASS

The invasion-threshold extinction rate and first logarithmic correction are natural dynamic quantities. A precise activity/recovery rate resonance exactly linearizes reciprocal prevalence, with a rigidity theorem and log-term sign reversal under detuning, providing a reusable solvable benchmark in inhibitory epidemic activity feedback rather than just a scalar SIS textbook limit.

The dated certificate retains the supplied scientific assessment, sources and limitations.
