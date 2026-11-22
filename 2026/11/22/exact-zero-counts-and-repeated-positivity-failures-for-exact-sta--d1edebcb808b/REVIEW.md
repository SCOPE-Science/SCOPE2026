# Review of the exact-start BDF2 positivity phase theorem

## Correctness — PASS

For real positive scalar decay, the characteristic roots are explicitly real-positive through \(z=1/2\) and complex conjugates beyond that threshold. The exact starter \(e^{-z}\), rather than backward Euler, produces the stated phase shift \(\phi(z)\). Direct differentiation proves the strict inequality \(\theta'(z)-\phi'(z)>0\) for every \(z>1/2\), using \(e^{-z}+z-1>0\). The phase therefore crosses precisely \(\lfloor k/2\rfloor\) cosine zeros, all transversely. There are no other zeros. The spectral mass of a star-center basis vector proves each scalar negative interval yields a separated negative finite-graph self-return interval for sufficiently large star size, with positivity between and outside. At the second stage the unique minimum of \(g_2\), spectral-mass lower bound, and explicit thirteen-vertex star show sharp diagonal positivity through twelve vertices. The proof covers all positive timesteps and all indicated integer stages; finite scans do not substitute for its quantifiers.

## Originality — PASS, with publication-priority limitations

Hundsdorfer (1998), *Partially Implicit BDF2 Blends for Convection Dominated Flows*, analyzes general positivity and starting procedures but not the exact-stage zero count as timestep varies under exact exponential startup. Hundsdorfer, Ruuth and Spiteri (2002), *Monotonicity-Preserving Linear Multistep Methods*, prove step restrictions and address starter choices, not separated graph-star negativity windows or the sharp exact-start diagonal cutoff. A public record, *Exact delayed sign loss just beyond BDF2's positivity boundary* (2026), obtains the first negative **stage index** at fixed timestep with **backward-Euler startup**: neither its starter nor quantified independent variable matches this theorem, and its statement does not imply this exact-start all-index zero count. A Richardson-extrapolated backward-Euler record gives a network diagonal extremum for a different one-step transfer function, and TR-BDF2 literature concerns another one-step method. The root-count derivative cancellation and its graph consequence were not found in the inspected primary full texts or searched published records. Historical equivalent formulas in older multistep literature remain a real priority risk; absence of search hits alone is not treated as novelty proof.

## Value — PASS

The result provides a complete all-index zero-count theorem for the classical multistep response with a physically natural exact heat-step starter. It shows an unbounded number of separated failures and restorations of nonnegative self-transition on finite networks despite scalar absolute stability, with a constructive graph family, and a sharp finite-size 12/13 boundary at the first BDF2 output. These phenomena matter when assessing positivity by isolated timestep tests or short-horizon numerical experiments; they are not arbitrary parameter substitutions or isolated floating-point artifacts.

## Boundaries and closest literature

The diagonal criterion is not a claim of full matrix positivity. The all-stage root theorem is for exact startup; it cannot be transferred to backward-Euler startup without a new proof. The star theorem establishes existence and a lower bound on the number of negative components, not a complete fixed-star classification. Published investigations of BDF2 positivity precede this result; future specialist literature review could still identify equivalent zero-count theorems.

- W. Hundsdorfer, CWI report MAS-R9831 (1998): https://ir.cwi.nl/pub/4596/04596D.pdf
- W. Hundsdorfer, S. J. Ruuth, R. J. Spiteri, CWI report MAS-R0210 (2002): https://ir.cwi.nl/pub/4231/04231D.pdf
- L. Bonaventura, A. Della Rocca (2015): https://arxiv.org/abs/1510.04303
- Related BDF2 stage-index result: https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-delayed-sign-loss-just-beyond-bdf2-s-positivity-boundary--cf66315c5a14
- Related Richardson graph-diagonal result: https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-the-sharp-28-29-self-transition-barrier-for-richardson-accelerat--56edd79ad0f3

Self-review: passed. Independent audit: not yet performed.
