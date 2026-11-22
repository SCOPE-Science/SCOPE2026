# Scientific review

## Correctness

PASS. The phase integral reduces to an explicit one-sided clipped-quadratic expression. Its derivative has the sign of a single unimodal function \(K(t)-m/(1-m)\), since the auxiliary numerator obeys \(P'(t)=-4t\alpha(t)<0\). The full-support arcsine integral strictly decreases for large amplitudes. The ratio of the nonzero local maximum to the baseline equals \(R(t)\), whose derivative factors into a strictly signed multiple of \(-P(t)\). This proves both distinct thresholds, all optimizer counts, and their equality cases. The standalone checker reproduces the displayed constants and representative regimes; finite tests are not treated as proof of the all-parameter theorem.

## Originality

PASS, provisional. Martin and Huey (2008) optimize mean preferred temperature, not a fixed-mean amplitude. Paaijmans et al. (2013) numerically compute mean fitness and thermal safety margins with a different daily waveform, not this closed-form global amplitude bifurcation. Bozinovic et al. (2011) provide experimental evidence of mean–variance interaction, while Kingsolver et al. (2015) distinguish nonlinear and time-dependent growth. An accessible earlier result on the same clipped parabola assumes means outside its viability interval, where there is only one positive optimum; the interior-mean global jump and metastability interval are additional and not implied. The broad risk of an equivalent result in arcsine-convolution or parametric optimization literature remains.

## Value

PASS. The two universal dimensionless constants identify a genuine structural boundary in thermal-rate summation: small fluctuations initially depress average response at any interior mean, yet larger fluctuations become globally advantageous sufficiently near a viability cutoff. A discontinuous optimum and a separate metastability window give information not supplied by the usual pointwise Jensen sign, including when local optimization will return the wrong globally preferred amplitude. This is a motivated benchmark for interpreting variance effects and an exact target for testing more realistic thermal performance models; no empirical universality is claimed.

## Scope and residual risk

Only a prescribed sinusoid, constant instantaneous response, symmetric hard-truncated quadratic, no physiological memory and unconstrained nonnegative amplitude are covered. Broader mathematical literature may subsume the special response; the 2011 study was accessible at abstract level only. The 2015 experimental study expressly observes time-dependent mechanisms outside this model.

Self-review: passed. Independent audit: not yet performed.
