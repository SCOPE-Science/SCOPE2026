# Review of the eventual Fermat-quotient pair-image theorem

## Correctness — PASS

The claim is precisely a finite-level fiber-multiplicity classification for each odd prime, each unit shift, and all exponents at or beyond the explicit cutoff. The argument uses the exact quotient map on each Teichmüller residue branch, not a limiting heuristic. A unit determinant gives exactly one intersection per pair of branches. A three-branch coincidence would produce three distinct points on two distinct complex circles, hence a nonzero cyclotomic integer. Its field norm is bounded by the product of archimedean estimates, ruling out high-order congruences. The quotient-coordinate valuation loss of exactly one is accounted for in the cutoff. Exact Python enumeration confirms small cases but is not substituted for the proof.

Risk: the effective threshold is intentionally not optimized, and no claim is made below the cutoff. The counterexample of triple fibers at the first level for prime eleven confirms why that distinction matters.

## Originality — PASS (best-knowledge, priority-qualified)

The closest full-text comparison is Ostafe–Shparlinski (arXiv:1001.1504, Section 4.1, Theorem 11), which controls joint distributions of short sequences with Fourier sums and discrepancy bounds, not exact multiplicities of the pair image over all prime powers. Shparlinski (arXiv:1104.3909) primarily estimates one-dimensional image sizes and exponential sums. Chen–Winterhof (2012, DOI 10.1142/S1793042112500352) investigates joint vectors for generalized Euler–Fermat quotients; available abstracts discuss discrepancy, while its full text could not be inspected. Published-record comparisons found no statement with equivalent unit-shift, prime-power, pairwise-intersection, or cutoff implications. These are comparisons of implications rather than merely titles.

Risk: a general historical result on intersections of cyclotomic residue graphs or a later version of the 2012 vector paper might imply this theorem; historical priority is therefore not independently established.

## Mathematical value — PASS

The simultaneous image of consecutive Fermat quotients is a natural arithmetic invariant already motivating joint-distribution studies. This result replaces approximate distribution information with an eventual *complete fiber-multiplicity profile* for every odd prime and every coprime shift. The surprising stabilization is exact: all distinct branch pairs contribute exactly one collision, independent of the exponent, while no higher collisions survive beyond an explicit bound. The explicit norm argument supplies a uniform effective cutoff rather than a purely qualitative existence theorem.

Risk: the bound is conservative, and minimal stabilization exponents and short-interval behavior remain unknown.

Self-review: passed. Independent audit: not yet performed.
