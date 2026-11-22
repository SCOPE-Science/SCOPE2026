# Scientific review — geometric Mexican-hat scale-channel Riesz bounds

## Correctness (PASS)

The proof derives the normalized covariance between every two heat-Laplacian scales from the exact radial Fourier integral, with exponent \(\nu=(d+4)/2\). It then transforms the Toeplitz Gram kernel through a beta integral and Poisson summation into a uniformly convergent positive Gamma periodization. Crucially, the Euler product represents every Gamma modulus square as a positive Gaussian mixture; the Jacobi product proves all wrapped Gaussian summands strictly decreasing from frequency \(0\) to \(\pi\). Therefore the displayed endpoints are *global* sharp Riesz bounds, not numerically guessed extrema. Fejér packets show optimality also for a one-sided infinite scale family. An exact circular-convolution identity makes dimension improvement strict. Gamma Stirling asymptotics at one zero-frequency and two antipodal-frequency aliases establish both leading constants and their ratio. The supplementary checker passed 442 numerical assertions; no infinite claim is inferred from finite numerics.

## Originality (PASS, provisional historical priority)

The closest accessible Mexican-hat transform paper, Fukuda–Kinoshita–Yoshino (2017), explicitly treats the same mother-wavelet profile but studies wavelet-transform regularity, not the unshifted normalized geometric-scale Gram symbol, the exact extrema or dimensional sharpening. Antezana–Carando–Scotti (2021) work with integer dilations in \(L^2(0,1)\), not the Gaussian heat-Laplacian channels over Euclidean space. The full accessible result on causal differences of exponentials has a conceptually related Mellin/Toeplitz method but different channel overlap and a different condition-number coefficient; it does not imply the present coefficient or dimension monotonicity. Bui–Laugesen (2011) address full Mexican-hat frequency-scale frame completeness, whose published abstract and talk do not prove the current claim; their original full text was not accessible for direct comparison, creating a named residual historical risk. Searches for Mexican-hat dilation Gram eigenvalues, Gamma periodization, sech-power Toeplitz extrema and sharp scale conditioning yielded no source proving this precise result. These searches support best-knowledge originality, not a formal uniqueness certificate.

## Value (PASS)

Closely packed Gaussian heat-derivative channels are a natural scale-space feature family whose synthesis noise amplification cannot be read from the unit norm of each individual channel. The result gives the exact best-possible coefficient-conditioning budget for *every* logarithmic spacing in *every* dimension, reveals that the same frequency is always worst, proves strict conditioning improvement as spatial dimension grows, and quantifies an exponential small-spacing instability with a sharp dimension-specific leading constant. This is a mathematically motivated infinite-family stability result, not a prescribed numerical slice or a restatement of the abstract Riesz criterion. It does not assert completeness or transformed filter-bank frame bounds.

## Closest literature and limitations

- Fukuda, Kinoshita and Yoshino, *Wavelet transforms on Gelfand–Shilov spaces and concrete examples* (2017), https://doi.org/10.1186/s13660-017-1393-0, full article read, §4 relevant.
- Antezana, Carando and Scotti, *Splitting the Riesz basis condition for systems of dilated functions through Dirichlet series* (2021), https://arxiv.org/abs/2110.07659, original preprint sections read.
- Bui and Laugesen, *Frequency-Scale Frames and the Solution of the Mexican Hat Problem* (2011), https://doi.org/10.1007/s00365-010-9098-3, bibliographic abstract available; primary full text not inspected.
- *Sharp dense-scale conditioning of causal exponential-difference dilates*, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-sharp-dense-scale-conditioning-of-causal-exponential-difference--665865eb3d5b, full scientific result and proof inspected.

The bounds concern unshifted normalized scale functions on their closed span, not a full translated-wavelet frame. Finite checks are supplementary, and independent verification is still outstanding.

Self-review: passed. Independent audit: not yet performed.
