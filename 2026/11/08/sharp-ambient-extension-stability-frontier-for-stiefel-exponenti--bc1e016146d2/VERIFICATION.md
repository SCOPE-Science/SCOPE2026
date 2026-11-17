---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

All F_c(x)=x_2+(c/2)(||x||^2-1)exp[-(||x||^2-1)^2] restrict to the identical circle objective -cos(phi). The ambient gradient at the constrained minimizer is (0,1-c). Direct differentiation of the actual EMA-before-projection and normalized retraction gives z_{t+1}=(I+beta_t A+beta_t^2 C)z_t with beta_t=t^-1/2, A=[[-theta(1-c),-theta],[c,-1]], C=[[-theta c,theta],[0,0]], normal memory factor 1-beta_t. det A=theta>0, tr A=theta(c-1)-1, giving the exact Hurwitz threshold c<1+1/theta. A positive definite Lyapunov metric makes sufficiently late updates contract by order beta_t in the stable region; for c>threshold, -A is Hurwitz and metric expansion of every nonzero active perturbation follows. Sum beta_t diverges. Independently differentiated the original nonlinear update and checked its Jacobian. Critical equality not classified; full nonlinear attraction not claimed.

## originality

PASS

PASS best-of-knowledge: the Yuan-Sun-Yuan original RGR paper supplies the actual ambient EMA method and broad convergence under parameter/regularity hypotheses; its theorem 4.3 and appendices do not state the exact local ambient-extension parameter c boundary or invariant-objective opposing-stability witness. The inspected source also explicitly contrasts tangent-space REMA memory, showing that ambient normal memory is distinctive. Other Riemannian momentum sources concern transported tangent gradients. No relevant prior Resultary theorem on this exact normal-extension-dependent local frontier was found.

## value

PASS

PASS: the same constrained objective and strict minimizer can have locally stable or unstable ambient EMA trajectories solely through off-manifold extension. This is a substantive modeling and stability-obstruction witness for an actual contemporary algorithm, not a cosmetic change of normalization. The exact threshold identifies what a convergence theorem must control, without claiming to contradict existing small-stepsize guarantees.

The dated certificate retains the supplied scientific assessment, sources and limitations.
