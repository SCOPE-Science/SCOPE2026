# Independent mathematical audit

## correctness

PASS

For q(z)=Σ_{j=-m}^m a_j z^j with negative highest a_m and strict negative symbol off zero, F_t(z)=exp(tq(z)) has Laurent coefficients p_j(t), is entire on C\{0}, tends to zero along real z→+∞ yet has an essential singularity at infinity. Infinitely many nonzero positive-index coefficients and an eventually one-sign tail would force F_t(r)→±∞ by comparing polynomial positive/negative contributions, so both signs appear infinitely often for each fixed t>0. The n-cycle kernel is the periodization of p_j and eventually tends to rank-one uniform via its spectral gap. Exponential weighted Laurent bounds control aliasing for t<=c n, while the diagonal spectral mass is at least C/sqrt(t); the small-/intermediate-time sign persists by uniform Taylor bounds and compactness, proving linear delay. For Q=D-D²/12, q(16)=-2475/1024 and elementary majorants permit c=1/500; spectral decay implies strict positivity by n²/16 for n>=5. Independent exact stencil checks and numerical cycles n=5..30 corroborate sign behavior. The infinite/time-uniform result rests on analytic inequalities, not finite simulation.

## originality

PASS

The signed Laplacian theorem of Chen et al implies finite-dimensional eventual exponential positivity for simple zero, which is prior, and fourth-order five-point elliptic inverse-positivity analysis of Cross and Zhang uses exactly the motivating stencil. But inspected papers concern finite eventual positivity or stationary inverse M-matrix, not infinitely many both-sign lattice coefficients at every positive time plus an explicit uniform Ω(n) periodic positivity delay. The related periodized numerical time-stepping results use different operators or discrete-time schemes. Qualified against potentially unindexed older stencil-specific semigroup work.

## value

PASS

High-order accurate finite-difference heat operators may be spectrally stable while violating the continuous-time order-preservation principle. Persistent arbitrarily remote negative lattice propagation for any t and a quantitative finite-grid recovery obstruction at least linear in circumference are substantive structural and numerical-analysis boundaries, not merely a negative one-step coefficient.

The dated certificate retains the supplied scientific assessment, sources and limitations.
