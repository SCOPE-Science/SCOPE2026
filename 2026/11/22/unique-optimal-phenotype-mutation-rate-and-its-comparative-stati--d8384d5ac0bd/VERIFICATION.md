---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Kroumi v1 Eqs. (22), (24), (28), and (29) give the claimed two-mode reduction in precisely the large-population normalization of the frozen result: L=2,n=1 leaves correlation exponents 0 and -2, and their recognition weights are 1-xi and xi. Thus the Laplace substitution has poles c_j and c_j+4nu after canceling 2nu. Independently, for v=4nu, p=1+2mu, r=3+2mu, the denominator of Eq. (29) divided by 2nu is xi*v*2mu*(1+mu)/(1+v)*(1/(p+v)+1/(r+v)), strictly positive in the claimed domain; symbolic partial fractions recover the frozen threshold. For F=xi times the nu derivative, the derivative F_nu is strictly greater than (2B-A/2)/nu^3>0. F changes sign from negative infinity to 4(1-xi)>0, proving global strict convexity and a unique nondegenerate minimum. At its root, 0<A/(mu+2nu+1)^2<A/(4nu^2) yields both strict bounds. F_mu<-1/(2nu^2), while F_xi=-4 and xi strictly increases with finite alpha. Implicit differentiation therefore gives both claimed signs. The private replay `python /workspace/branches/review_recomputation.py` verifies the denominator factorization, partial fractions and calibration quartic exactly and computes nu*=0.462745752709218835593102 with threshold 23.7659359834690658531126 at mu=1/2, xi=1/4. The frozen checker was read as text, not run. The conclusion concerns the limiting weak-selection abundance threshold, not finite-N fixation, stronger selection, alpha=0, or larger phenotype spaces.

## originality

PASS

Kroumi already derives the general threshold and proves interior minimum existence; those are not new. The supported distinct claim is the binary all-positive-parameter strict convexity, unique root and bracketing, and both comparative statics of the argmin. Neither the primary passages inspected nor the closest distinct indexed findings establish these consequences with matching assumptions.

## value

PASS

Exactly two recognition states is the minimal nontrivial finite torus and the first case in which the general proof of endpoint divergence leaves open the number and location of minima. The global classification identifies a nondegenerate optimizer with usable bounds and shows how two distinct parameters move it. These signs are not the known pointwise threshold signs, and matter for reasoning about this abstract model without drawing any finite-population or intervention inference.

The dated certificate retains the supplied scientific assessment, sources and limitations.
