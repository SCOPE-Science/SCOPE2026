# Independent mathematical audit

## correctness

PASS

Unit-circle scaling and rotation, followed by nonzero nodewise multipliers on the Wirtinger derivative rows, reduce to the DFT blocks by signed frequency mod M. A positive-frequency block with p distinct positive degrees has derivative-row rank min(p,k): the polynomials (u)_j, j=1,…,k, span u times the polynomials of degrees ≤k−1. The negative-frequency block has the corresponding q rank with disjoint support. The value row adds one if the block contains the constant mode, or if one sign count exceeds k (a zero-constant polynomial of degree ≤k cannot equal 1 on >k nodes); otherwise it is in the span. Thus the formula holds with empty blocks, k=0, and k>L, where the harmonic jet channel count is an ambient dimension and does not mean all high-order derivative functionals are nonzero on the band. Arbitrary nodes require M(2k+1)≥2L+1 by rank. Under that inequality the zero residue has ≤k of each sign, other residues have ≤k+1 of each sign and ≤2k+1 total, and every block is full column rank by the formula. Tangential-only rows are degree-0-through-k Vandermonde rows in each residue, yielding the separate threshold. Inspected the checker and recorded 10,514 assertions; an independent unreduced complex-matrix check matched all 252 bounded cases L≤6, k≤3, M≤9, with floating-point tolerance 10⁻⁹. The block proof, not the finite checks, establishes the exact theorem.

## originality

PASS

Pass for the full planar harmonic jet theorem: simultaneous attainment of the dimension bound on one regular circle and the exact all-residue rank even below that bound. Unit-circle Laurent Hermite interpolation is direct background for the tangential-only comparison; existing general derivative interpolation in available passages does not give this split rank theorem. The inaccessible closely titled 2026 paper is a stated limitation rather than a negative result.

## value

PASS

The result answers a concrete minimal-experiment question for harmonic-field recovery and determines exactly how many degrees of freedom are lost below that optimum. The sign-sector and shared-value calculation gives an actionable structural reason that full jets can saturate the universal dimension bound, and a block reconstruction rather than just a count. It does not claim robustness or conditioning from injectivity alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
