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

Rechecked the marked-process claim in /workspace/repairs/5/RESULT.md. From G=1+U_(i+1)−U_i, the tail triangle has area δ²/2; consecutive exceedances at δ≤1/2 require incompatible values of the shared uniform. Nonadjacent indices use disjoint uniforms. Thus for fixed L and sufficiently large n the one-point mark density is exactly t/n on [0,L]. For a nonnegative compactly supported continuous f, h_i=E[1−exp(−f(i/n,T_i))]≤L²/(2n). The finite Laplace product expansion equals the product for independent entries except for subsets with neighboring indices. Charging their absolute contributions to an adjacent pair gives bound exp(sum h_i) sum_i h_i h_(i+1)=O_L(n^−1); the independent product then converges by a Riemann sum to the Poisson Laplace functional with intensity ds t dt. This directly proves the vague convergence for the actual spatial grid and deficit normalization. On bounded mark windows the ordering is continuous in the absence of ties or cutoff points, which holds almost surely in the limit; letting the cutoff grow captures each fixed rank. Product intensity makes the minimum location uniform independent of its mark, and the kth survival is the Poisson count probability below t for mean t²/2. Boundaries have scaled length at most one, while floor(n/2) disjoint internal pairs independently beat one with probability 1/2. The contextual finite law is correct: only independent subsets contribute moments, variance subtracts twice the adjacent q² covariance, and z=0 uses a threshold ≥3/2 so endpoints cannot exceed it. Independently evaluated the n=10, δ=1/3 example with rational arithmetic, giving 1097009/1889568=0.5805607419261969. Inspected the original checker and VERIFICATION.md without executing the uploaded script; numeric comparisons and simulation do not test the marked theorem.

## originality

PASS

Applies to the revised Finding only: the design-specific marked location–deficit process and resulting joint extremes. The original foregrounded the finite polynomial; its finite hard-core counting form is already an immediate consequence of known one-dependent hard-core inclusion probabilities (or independent thinning in the known void formula), and Watson's theorem gives the single univariate Rayleigh maximum once the model tail is supplied. The repair removes those from the originality claim and credits them in context. The inspected same-design source treats discrepancy, the strongest analogous marked record uses unstratified spacings and a different intensity, and neither the inspected hard-core nor dependent-maxima statement supplies the joint marked law for this sampling model. This is not a claim to invent general Poisson approximation for dependent sequences.

## value

PASS

The surviving result answers where the largest uncovered intervals are, not just how large the single largest one is, in the widely used one-site-per-equal-cell design. Its intensity specifies multiple extreme ranks and their joint spatial allocation on the correct deficit scale, unlike the univariate theorem and the older unstratified design. The finite formulas remain useful context, not the basis for this value decision.

The dated certificate retains the supplied scientific assessment, sources and limitations.
