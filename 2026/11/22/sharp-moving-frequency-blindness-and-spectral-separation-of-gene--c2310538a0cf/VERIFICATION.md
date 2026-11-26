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

For the stated full Bernoulli-kernel statistic, the absolutely convergent even Bernoulli Fourier series contributes two equal conjugate terms per positive frequency, giving weight 2n/(2πj)^(2m) on the squared empirical Fourier mean. The population mean is ε/2 at k_n and zero elsewhere, and expansion across diagonal and off-diagonal sample indices gives 1+(n-1)|θ_n(j)|² for n times the expected square. Once k_n>2J all real low-frequency covariances are exactly I/2, so the bounded-array CLT gives the stated independent Gaussian pairs. The omitted nonexceptional part has expectation bounded by 2 times the summable weight tail, independently of n. The exceptional term divided by s_n converges in probability to ε²/[2(2π)^(2m)] by a variance bound, giving a deterministic translation at finite s (including zero) and divergence at infinite s. The null law is atomless; its independent remainder after the first exponential term can be arbitrarily small with positive probability by truncation, independence and the summable tail mean. Hence the upper-tail quantile and power formula are valid, with power one also when the translation reaches the critical value. At k_n=floor(n^(1/3)) the signs of 1-2m/3 give the hierarchy. Hoeffding at cosine-average threshold ε/4 gives each error at most exp(-nε²/32) and the indicated TV lower bound. This is for fixed m and ε and known uniform null, not for increasing order or a truncated statistic.

## originality

PASS

Best of current knowledge: pass only the growing-harmonic critical law and ensuing comparison across fixed orders. The prior statistic, Bernoulli and spectral identities, null spectrum, and Hoeffding separation technique are not the contribution. The closest identified indexed findings either concern a different test or only null behavior. Primary-paper access was partial; this is not a priority certificate.

## value

PASS

This gives a usable scale and critical power formula for named, increasingly smoothed diagnostics. Unlike a fixed-mode noncentral limit, the deterministic shift captures energy in a moving harmonic. One common, strongly separated sequence distinguishes the first order from every fixed higher order, which quantifies a real sensitivity tradeoff even though it is not a minimax theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
