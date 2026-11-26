# Independent mathematical audit

## correctness

PASS

At a deterministic horizon, reversing the iid copying arrows traces each site back either to a correct source or to an initially incorrect ordinary site. Consensus is absorbing, so T≤t is exactly the event of no unanchored lineage after t reversed arrows. At j distinct unanchored sites, selecting one of the j sites and copying one of the z+j−1 source/other occupied sites drops the count by one with probability p_j. Positions may otherwise move, but the count kernel does not depend on them. The strong Markov property gives independent geometric waiting times with support starting at 1, including the case m=1. Partial fractions of (1−E[s^T])/(1−s) give the survival coefficients; the j=1 coefficient is the telescoping product m(z+1)/n. All rates are strictly ordered and less than 1. For fixed z, scaling each fixed waiting time by n² gives its exponential limit and the uniform remainder bound is the convergent tail sum of 1/[j(j+z−1)]. This proves the limit, with finite mean and nonzero variance. Splitting off E_1 and using an exponential moment for the remaining sum above rate z proves the limiting tail, whose product coefficient tends to z+1. Euler's sinh product evaluates the one-source transform; shared copying preserves sitewise order and proves worst-case dominance. A separately written exact-rational finite check passed 770 forward/geometric CDF and 770 spectral-survival comparisons over 55 populations 2≤n≤11, 1≤z<n and 0≤t≤13, plus 55 leading-coefficient comparisons. Replay procedure: propagate the count distribution from j=m using up and down probabilities j(m−j)/n² and j(n−j)/n²; independently propagate a pure-death chain with decrements p_j, and compare both CDFs and the displayed survival sum at each tick. The tridiagonal comparison in the frozen verify.py follows the same finite scope; neither finite test proves the limit.

## originality

FAIL

The exact source-anchored count kernel is already known. Its transient spectrum is a direct boundary specialization of Corujo's explicit neutral Moran spectrum, and Fill's exact birth–death passage-time theorem gives the claimed independent geometric sum from those eigenvalues. The sharp finite coefficient is its first partial-fraction coefficient. The fixed-source limit follows directly by scaling these factors with a summable mean bound and is the classical absorption law of the coalescent with mutation after deterministic time rescaling. No material distinct scientific claim was established in the frozen finding; this does not depend on access to the zealotry paper.

## value

FAIL

The absorption distribution is a meaningful invariant and the graphical proof is concise. The frozen contribution, however, consists of an equivalent specialization of a known finite spectrum and passage law, followed by direct moment, residue, and fixed-rate scaling computations into a known limit law. The graphical proof uses the standard arrow construction with sources treated as absorbing ancestors and does not establish a separate new structural claim on other graphs or protocols. A convenient derivation of the exact specialization does not on its own establish scientific value at the required bar.

The dated certificate retains the supplied scientific assessment, sources and limitations.
