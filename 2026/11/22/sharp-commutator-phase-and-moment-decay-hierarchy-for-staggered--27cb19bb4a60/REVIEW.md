# Scientific review

## Correctness

**PASS.** The normalized overlaps of adjacent length-\(p\) blocks are exactly \(1-r/p\) and \(r/p\), giving the coarse compression \(I-\tau\Delta\) with \(\tau=r(p-r)/p^2\). The Fourier symbol has full range \([1-4\tau,1]\). Rank-one fiber projection geometry gives the entire imaginary commutator spectrum and the \(\tau=1/8\) norm transition. The multiplicity assertion distinguishes the two-dimensional fibers when \(p=2\) from the \(p-2\)-dimensional joint complement otherwise. Gaussian rescaling of the Fourier integral proves the displayed hierarchy for every nonzero finitely supported coarse input; finite numerical checks support but do not replace these arguments.

## Originality

**PASS, with residual historical-priority risk.** Borodin–Kopecká and Badea–Seifert give general convergence-rate theorems, without this period-\(p\) overlap symbol or explicit stagger-dependent constants. Loring and Dou–Du–Wang give general two-projection spectral tools; those tools do not specialize themselves to the integer-offset geometry. A related unshifted, unequal-block calculation has finite essential spectral sets and no local diffusion law. Available comparisons did not disclose a published equivalent concrete staggered-grid theorem, although older numerical multigrid and Markov-chain literature may contain an equivalent interpretation. This review does not claim that an unsuccessful search establishes absolute historical novelty.

## Mathematical value

**PASS.** Alternating block projections are a natural repeated-reconciliation operation on two incompatible coarse partitions. The exact lazy-heat identification both explains loss of uniform convergence and yields the full hierarchy of sharp localized decay coefficients; the commutator's sharp phase threshold identifies when staggering reaches maximal noncommutativity. These results form a complete spectral-and-iterative description of the natural equal-width bilateral model rather than an isolated arbitrary parameter computation.

## Closest literature and scope

The general two-subspace theory is essential background, and the result is limited to equal-width bilateral blocks. The source-specific \(O(N^{-1/2})\) estimate for inputs from a sum of orthogonal complements does not imply the \(N^{-1/4}\) block-impulse asymptotic: that impulse lies outside the stated input class. No half-line or irregular-grid assertion is made.

Self-review: passed. Independent audit: not yet performed.
