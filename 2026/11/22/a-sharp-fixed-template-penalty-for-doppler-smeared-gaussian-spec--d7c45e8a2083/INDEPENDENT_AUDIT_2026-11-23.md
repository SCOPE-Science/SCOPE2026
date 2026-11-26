# Independent mathematical audit

## correctness

PASS

For unit L² norm g, Gaussian overlap gives exp[-u²/(4σ²)], hence the fixed projection √π erf(βt)/(2β), and pairwise integration gives squared matched norm 2∫₀ᵗ(t-u)exp(-4β²u²)du. Independent white noise with variance proportional to t gives the respective squared SNRs after division by t, with wall-time cost t+h. Heterogeneous durations give a cost-weighted average rate, not a higher optimum. For x=βt and d=βh, the fixed root equation compares 2/[∫₀¹exp(x²(1-v²))dv], strictly decreasing from 2 to 0, with 1+x/(x+d), strictly increasing from 1 to 2. This proves unique optimality and monotonicity in h, and gives the finite limit x_* when d diverges. In the matched case F=||S_t||²/t is increasing and strictly concave, by strict decrease of the autocorrelation kernel; (t+h)F'-F decreases strictly from h to -2M₀ and its zero increases and diverges with h. Both numerators equal t-(2/3)β²t³+O(t⁵) near zero and both optimizers tend to zero as h↓0, giving the common cube-root coefficient via stationarity. For the matched optimum, h/t²→M₀/M₁=2β√π; the h-scaled maximal rates yield the quoted large-overhead ratio. Strict Cauchy–Schwarz holds at every t>0 since the averaging multiplier in Fourier space is nonconstant, so the strict optimized penalty is not limited to the asymptotic case. An independently evaluated Gaussian integral and bracket solve gave x_*≈0.9899390828419043, R_*≈0.6293963793249795, and example durations 343.9137776 and 346.2406090 seconds. The supplied checker was read, not executed. The limiting ratio is not asserted to be the finite-h ratio or to model a real transit pipeline.

## originality

PASS

The matched-only uniqueness and overhead laws are already present in the distinct exact benchmark; empirical spectroscopy cadence and general matched-filter theory are also established. The supported distinct claim is the all-overhead unbroadened Gaussian-template optimizer and its exact comparison with the matched policy, including the finite-versus-diverging duration and limiting relative squared-SNR rate. Neither the matched benchmark nor the inspected primary astronomical analyses give that fixed-template policy. This is bounded evidence, not a claim to priority for scalar Gaussian aperture optimization or for the benchmark.

## value

PASS

The comparison isolates a choice made in Doppler-smeared line detection: retaining the intrinsic template rather than adapting it. It changes the large-overhead optimizing strategy from unbounded duration to finite saturation and leaves about a 37.1% loss in optimized squared SNR per wall time, despite equal leading small-overhead duration laws. This is a sharp model benchmark, not a marginal numerical improvement. Its use is as an idealized comparison for white photon noise and constant drift, not as a recommended cadence for a finite transit or an estimate of a real instrument's losses.

The dated certificate retains the supplied scientific assessment, sources and limitations.
