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

The factorial basis, Gaussian weight, 1/√M and two-channel unitary DFT give residue blocks with columns √p_n(1,(n−x)/√x)^T for n=k,k+M, p_n=e^{−x}x^n/n!. Their positive determinants M√(p_k p_{k+M})/√x establish interpolation, and their Gram determinants multiply to M^{2M}e^{−2Mx}x^{2M(M−1)}/∏n!, maximized uniquely at x=M−1. For x/M in a compact positive interval the unweighted 2×2 block has operator norm O(√M) and determinant M/√x of order √M, so its least singular value is bounded below by a positive constant. This quantitatively reduces the squared condition exponent to the extremal Poisson-weight ratio, uniformly with log-error O(log M) before division by M. Stirling yields I_ρ(s)=ρ−s+s log(s/ρ), whose oscillation on [0,2] is the displayed F (the mesh endpoint error is O(1/M)); endpoint balancing gives the unique ρ=2/e. No escaping radii improve the rate: with N=2M−1, r=x/N and d_n the squared column norm, d_N/d_0 ≤(1+N)e^N r^{N−1} when r≤1 (N!≥(N/e)^N) and d_N/d_0≥r^N/4 when r≥2 (N!≤N^N). Either escape makes the scaled log squared condition diverge. The uniform compact estimate and the trial x=(2/e)M then justify the infimum limit and localize every rate-optimal sequence. Independent direct complex value/derivative matrix checks matched the full block SVD and log Gram determinant in 20 cases across M=2–12. Those cases do not certify the asymptotics.

## originality

PASS

The same rate curve, optimized exponent, and radius scale are already obtained for the point-only design on the same polynomial space by rescaling its exact earlier formula; these numerical facts are not new in isolation. The supported distinct result is that the critically sampled first-jet design, with half as many sites on that space, has the same rate despite aliasing, with an exact coupled spectrum and a different determinant objective. The point-only result supplies the rate function after, not before, establishing control of the new residue blocks and exclusion of escaping jet radii.

## value

PASS

First jets allow exact recovery with half the sites but that alone says nothing about noise amplification. Quantifying the sharp obstruction for the actual normalized sampling operator shows that derivative enrichment does not improve the leading conditioning exponent per coefficient and specifies the required radius scale. Comparing to the exact determinant optimum also rules out determinant tuning as a surrogate for worst-case conditioning at exponential order in this design. This is a useful negative design result despite the shared point-only exponent.

The dated certificate retains the supplied scientific assessment, sources and limitations.
