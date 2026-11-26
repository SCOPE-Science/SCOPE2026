# Independent mathematical audit

## correctness

PASS

Atomlessness makes the probability-integral transform uniform, with almost-sure order preservation even when the CDF has flat intervals. A prescribed k-matching has Q=k(2n-2k-1) distinct touched edges. Its marked success requires all Q clocks to exceed t. After t the first touched edge must be one of the k selected edges. Its identity is uniform and independent of the waiting time; after removing its endpoints, memorylessness recurses on the surviving touched edges. Thus the marked probability has the exact product in (2), and conditional on success the largest selected weight minus t is the sum of independent exponential waiting times of rates j(2n-2j-1). The ordered matching count is (n)_(2k)/2^k; the count touching r specified isolated vertices is rn-r(r+1)/2. These give the claimed marginal factorial-moment normalizations. For disjoint configurations, isolation leaves the complement clocks unconditioned. Its matching success upper-bounds full matching success, and matches it whenever the selected edge weights are at most u. The probability of the excluded tail, relative to complement matching success, is O(1/log n) by the conditional O(1/n) total waiting time and u-t asymptotic to log(n)/(2n). For j shared endpoints, at least one selected clock must exceed u, costing the same vanishing factor conditional on matching success; independently, the other r-j isolated vertices require edges to wholly unmarked vertices to exceed u, costing O(n^{-(r-j)}). Combined with O(n^{r+2k-j}) configurations and O(n^{-2k}) marked matching probability, this is o(1). The resulting all-orders mixed factorial moments determine the independent Poisson pair (tightness and moment convergence follow from the higher moments). The joint zero event gives the Gumbel law. The formula includes the empty matching; n=2 is valid and the threshold argument only needs large n for fixed x,y. The source checker was inspected, not run, and the limit does not depend on its finite tests.

## originality

PASS

The prior unmarked matching law and the isolated-vertex marginal are credited. The supported distinct claim is the calibrated joint Poisson/Gumbel limit for both clocks in the same symmetric random-link graph. The inspected sources do not provide their mixed-moment decoupling or an equivalent joint theorem. The two clocks can be expressed in the Erdős–Rényi process, but the last birth of a two-vertex component is not the time at which no such component remains.

## value

PASS

The two maxima depend on the same edge array and have different characteristic scales. The joint result resolves whether that dependence survives at the extremes; the mixed rare-configuration argument explains why it disappears. This is more than reproducing two Gumbel marginals.

The dated certificate retains the supplied scientific assessment, sources and limitations.
