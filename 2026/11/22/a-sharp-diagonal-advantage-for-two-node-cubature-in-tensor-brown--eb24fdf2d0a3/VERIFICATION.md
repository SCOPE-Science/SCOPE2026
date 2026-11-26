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

The integrated kernel is v(x)/2 in one coordinate, v(x)=x(1−x), with total one-dimensional representer energy 1/12. Completing the square in the weights gives capture gᵀG⁻¹g; distinct interior sites give a nonsingular Gram matrix since the kernel correlation in at least one coordinate is strictly less than one. For the one-axis family the capture factorizes, with each shared coordinate contributing v(c)/4≤1/16, uniquely at c=1/2. Independently, the 1D subspace vanishing at both sites splits into three Dirichlet intervals. On an interval of length h the integral representer u(s)=s(h−s)/2 has energy ∫u=h³/12, proving the residual formula. Strict Jensen gives trisection and Q₁=2/27; optimal weights are 1/3 times 1/2 per shared coordinate. Degenerate pairs give at most the best one-site capture 16^(−d) and are strictly worse. For the diagonal pair, equal kernel means p/2^d and Gram correlation s^d give the stated weights and capture; the log derivative has the sign of 1−s−2s^(d+1), which decreases through zero exactly once. Under s=exp(−ℓ/d), normalized capture is 2 sech^(2d)(ℓ/(2d))/(1+exp(−ℓ)). Strict convexity of log cosh makes it strictly increasing at each fixed ℓ>0 with d; comparing attained maxima at the earlier maximizer gives strict increase. At d=1 the normalized maximum is 32/27. Its upper bound is 2, attained in the limit by ℓ=d^(1/4), so the ratio tends to 27/16. Writing α=−d log s_d gives α→∞, α/d→0 and α exp(α)~2d; inversion gives α~W₀(2d) and 1−2t_d~W₀(2d)/(2d). Independent numerical substitution gives t₂=0.3709720637607637, capture 0.005050140888736467 and error 0.001894303555707977. Symmetry here means reverse the same chosen coordinate orientation for both nodes (as in the stated equivalent-diagonal class), not reflecting one node alone. The claim does not extend to unrestricted site pairs. The supplied script and output were inspected, not run.

## originality

PASS

The one-dimensional fixed-pair error and the general tensor-kernel cubature machinery are already available; the independent increment is the exact restricted-family tensor comparison including the optimizing diagonal separation and strict dimensional law. No compared statement covers that conjunction or demonstrably implies it without the geometry-specific optimization. This is provisional as to historical priority.

## value

PASS

One extra evaluation is the smallest budget for choosing between a one-coordinate split and a genuinely multivariate placement. Optimizing both classes proves a strict loss for every one-axis design, even with arbitrary weights, and the separation and monotone gain quantify the mechanism as more coordinates are used. The 27/16 factor is for captured representer energy, not total-error improvement or practical speedup; both captured fractions decay exponentially.

The dated certificate retains the supplied scientific assessment, sources and limitations.
