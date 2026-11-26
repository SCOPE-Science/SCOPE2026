# Independent mathematical audit

## correctness

PASS

The Jordan variation dominates variation along the actual sampling nodes. On that finite path, splitting positive and negative levels into contiguous components expresses the nodal vector as a signed mixture of interior blocks, with total block weight half its nodal variation (each component has two jumps). The Bernstein derivative of a nonzero unimodal block has coefficients with exactly one sign change after removing the positive binomial prefactor and using odds x/(1-x); it is positive near zero and negative near one. Sampling and iteration preserve unimodality and the two zero endpoints. Thus each block's output variation is twice its peak. The full block peaks at 1/2 by symmetry and the same derivative argument; a proper block has strictly smaller peak, since every interior node has positive mass from any interior start at any r >= 1 and each nonzero block peaks in the interior. This proves the norm, its attainment and equality classification, including no excess between-node variation. Binomial conditioning gives both small-power formulas and the transient-matrix formula. Applying positivity to 4h <= u <= n^2 h/(n-1) on the grid, where h(x)=x(1-x), and checking B_n h=(n-1)h/n proves the rate bounds. The positive transient matrix has Perron eigenvalue (n-1)/n and normalization q^T h=(n-1)/(4n), giving the stated asymptotic constant. Next-step absorption proves strict decrease. For n >= 4 a nonconstant symmetric strictly unimodal output from the maximizing plateau has unequal interior samples, so cannot maximize the next iterate's quotient; n=3 gives (3/4)(2/3)^(r-1) and n=2 gives 2^(-r). These prove the claimed strict versus exact multiplicativity. All degrees and powers are covered analytically; the frozen script was inspected, not run, and its finite tests are not needed for the theorem.

## originality

PASS

No inspected prior establishes the specific sharp Jordan-variation coefficient, attained midpoint survival, and rigidity. Related exact Bernstein iteration and survival results are credited, including the distinct Resultary record with the same transient matrix; publishing chronology is not inferred from their listed dates.

## value

PASS

Matching the endpoints removes the reproducing affine direction, so contraction in Jordan variation is intrinsic to the remaining error. The exact coefficient at every power, plateau rigidity and strict versus exact multiplicativity determine whether one-step error guarantees compound sharply; the unit variation bound or spectral radius cannot answer this. The survival representation also gives exact rational coefficients without optimizing over functions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
