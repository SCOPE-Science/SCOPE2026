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

Start empty and add one immature family after reproduction each step, so at n≥1 there is one independent cohort of each age 0..n−1, including the newest singleton. The one-founder iterate satisfies 1/(1-f_a(s))=a+1/(1-s), and the product telescopes to the positive geometric total Y_n of mean n. For an alternative to coefficient differentiation, split Y_n=B+O into the ages ≤m and the independent older ages. The recent total B has the positive geometric law of Y_{m+1} with continuation probability beta=m/(m+1). Given B≥b, the shifted variable B−b+1 still has the law of B for each positive-probability conditioning event. Thus for 1≤b≤k, P(B≥b,Y_n=k)=beta^{b-1}P(Y_n=k−b+1), also when beta=0 by direct inspection of B=1. Dividing by the geometric law of Y_n gives conditional tail q^{b−1}, with q=beta/alpha and alpha=(n−1)/n. Summing tails and dividing by k proves the claimed within-realization sampling law. For 0≤q<1 every next term is strictly below the running average (the q=0 sequence is 1,0,0,..., not literally strictly decreasing as described in the proof, but its averages are exactly 1/k, strictly decreasing). Averaging over Y_n gives the difference of the two logarithmic series and the displayed unconditional CDF. At m=n−1 there is no older block and the probability is one; at n=1 the age is zero. Under a Y_n-size-biased population the denominator Y_n cancels, and every founder has expected family size one, giving uniform age. In the limit q=1−(1−r)/(rn)+o(1/n) at m=floor(nr), so the conditional geometric average with k/n→x>0 converges uniformly on compact x-intervals to the stated conditional kernel. The kernel is a CDF in r since it equals ∫_0^1 exp(−ux(1−r)/r)du and has limits zero and one. Trimming x near zero and infinity using the positive geometric to exponential convergence justifies joint convergence. The exponential density times the kernel gives the stated subdensity; the logarithmic integral gives the marginal, differentiation gives the density, and integrating the CDF expansion gives E[T]=1−∑_{j≥1}(j+1)^{-2}=2−pi²/6. Independently checked 4200 exact conditional cases by the unmarked split-cohort convolution for n=2..16, m=0..n−2, k=1..35; replay python3 /workspace/independent_checks.py 5. The frozen script was read, not executed; the limits are analytical.

## originality

PASS

The supported distinct statement is the joint law of realized population and sampled founder age under population-first uniform sampling, in the exact geometric unit-immigration model, including the conditional population-size ordering and its scaled coupling. Not claimed as new: geometric iterates, marginal population limits, general uniform sampling bias, or the cancellation under size-biasing. Inspected related originals concern unmarked counts, a single family or different sampling/conditioning, rather than the exact age-indexed recent block conditional on realized total. This is bounded scientific evidence, not an absolute priority verdict.

## value

PASS

The age of the immigrant ancestor of an individual selected from a realized population is a natural genealogical observable missed by counts alone. The exact law resolves both a finite population-size monotonicity and a nonindependent joint age–abundance limit; it quantifies how choosing a typical population instead of tilting by size changes the observed age law. The explicit dependence, not the familiar geometric marginal or the size-bias cancellation in isolation, is the useful content.

The dated certificate retains the supplied scientific assessment, sources and limitations.
