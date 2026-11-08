# Scientific review: A Poisson-cut and Poisson-spoke law for near-connected percolated wheels

## Correctness

**PASS.** The finite cyclic-state transfer formula includes the unique double-counted disconnected configuration, and complete exact enumeration verifies it independently at small wheel sizes. The independent point-process coupling gives the full macroscopic hub-fraction weak limit. The limiting connectivity atom follows from the matrix exponential; the tagged-arc length distribution gives the mean and all parameter boundaries. The supplied standard-library checker passes 295 assertions. Finite testing is not offered as a proof of asymptotic convergence.

## Originality

**PASS, qualified.** Exact homogeneous wheel all-terminal reliability is classical and does not form an originality claim. Mann et al. (arXiv:2102.09261v1) analyze cycle component counts in a different network ensemble. Cohen et al. (arXiv:0802.1055v1) introduce a close ghost-link interpretation, but the inspected analysis treats long-range small-world additions and different asymptotic regimes. Neither inspected article states the complete Poisson-cut/Poisson-spoke hub-fraction law with the displayed endpoint atoms, interior mass and expectation. Relevant published mathematical-record searches found no covering statement, but historical priority cannot be certified exhaustively; a differently phrased treatment remains possible.

## Value

**PASS.** In the physically natural competition of rare local breaks and rare long-distance hub repairs, a two-parameter critical window exhibits an explicit *mixed* random macroscopic connected fraction. The formula distinguishes hub isolation, complete connectivity and partial survival and gives their sharp limiting probabilities. This is more informative than a homogeneous reliability polynomial or an average connected size and is meaningful at every fixed pair of finite intensities.

## Closest literature and limits

See Mann et al. (2021), Cohen et al. (2008), and the classical wheel row of MathWorld's *Reliability Polynomial*. The claim assumes independent bonds and finite limiting cut/seed intensities. It does not include growing intensities, correlation, or total-variation convergence of the hub fraction. Unindexed historically equivalent treatments cannot be excluded. The original finite homogeneous wheel reliability recurrence is expressly recognized as known.

Self-review: passed. Independent audit: not yet performed.
