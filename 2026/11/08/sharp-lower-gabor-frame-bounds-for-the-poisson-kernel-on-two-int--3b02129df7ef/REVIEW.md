# Scientific review: sharp lower Gabor bound for two translated Poisson grids

## Correctness — PASS

The result specifies the unnormalized Cauchy/Poisson window, exact integer modulation lattice, two translation cosets, all parameter domains and squared frame-bound convention. The Zak-transform Parseval reduction is a standard identity. The Poisson-summed Zak expression is checked by direct real-space evaluation. Its modulus is minimized simultaneously in the frequency variable at the half-frequency because the only variable term has positive multiplier and a strict symmetric minimum. The spatial minimum follows globally from the strict monotonicity and convexity of an explicit rational function, with an exhibited equality point; the formula is therefore sharp. Positive frame bounds, the optimal half-period shift and the quadratic collision coefficient follow without numerical extrapolation. The standalone numerical and symbolic checker corroborates the algebra but is not the proof.

## Originality — PASS relative to inspected material

The closest recent reference is Belov–Semenov, arXiv:2610.30037v1 (2026-10-21). Their criterion is for irregular **modulation** positions and regular translations, whereas the present family uses irregular *translation* positions and regular modulations. Their introduction identifies the reverse orientation as open in general. The proof here gives an exact lower-bound formula for a natural two-coset reverse-orientation family, not a solution of the general question. Kloos–Stöckler, arXiv:1311.7359, concern totally positive windows and regular rectangular Gabor lattices, including a Fourier-dual exponential, but do not entail a sharp continuum of nonlattice shift bounds. Janssen's 2003 work describes critical Zak zeros and tight-frame constructions. The most relevant mathematical-record matches concern tent splines, a different two-sided-exponential sampling problem, and finite-dimensional Gabor structures, without an implication to this theorem. Targeted searches have not located an equivalent formula, while incomplete coverage of older specialized filter-bank literature remains a publication-priority risk.

## Mathematical value — PASS

The exact sharp lower bound is the stability constant that directly controls energy recovery from the two banks. Beyond a frame-existence assertion, it solves the complete offset-design problem among these irregular double grids, identifies the unique optimum and gives a sharp rate of stability loss as the grids collide. The source paper's opposite-orientation gap motivates this specific object. It does not require a broader generalization or an optimal upper bound to be a meaningful finite-parameter theorem.

## Boundaries and residual risks

The window is unnormalized; normalized-window constants differ by its squared norm. The upper bound and condition number are not evaluated. General irregular translation sets and other modulation spacings remain open. The source's general opposite-orientation question is not claimed solved. Independent literature-priority verification remains outstanding, particularly for older filter-bank treatments of interlaced Cauchy or two-sided exponential windows.

Self-review: passed. Independent audit: not yet performed.
