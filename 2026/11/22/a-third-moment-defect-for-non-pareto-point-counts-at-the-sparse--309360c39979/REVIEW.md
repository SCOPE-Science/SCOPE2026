# Scientific review of the non-Pareto third-factorial-moment result

## Correctness

**PASS.** The random variable is explicitly the count of non-Pareto-minimal vertices, distinguished from the comparable-pair count. Each of the three selected targets contributes an incoming coordinatewise comparison in a witness-weighted count. The 51 possible three-edge directed-constraint types give exactly two leading contributions at critical dimension: three disjoint directed edges, with \(\lambda^3\), and a common external predecessor of all three targets, with \(\lambda^2\). The second, 124-type four-edge enumeration exhausts all repeated-witness corrections and shows the expectation of the correction tends to zero. Both finite poset tables were reproduced exactly by the included standalone checker; the asymptotic powers are strictly negative for every omitted type. Boundary conventions and factorial normalization are explicit. The finite checker is not presented as an infinite proof.

## Originality

**PASS against the inspected scientific record.** Ilienko–Jin (2026) proves the Poisson limit and convergence of the mean and variance of the non-Pareto count, not its third factorial moment. Bhattacharjee–Ilienko–Jin–Molchanov (2026) treats its broader phase diagram without the claimed third-moment coefficient. The known critical third-moment defect for *comparable pairs* has coefficient \(2\lambda^2\), not the \(\lambda^2\) asserted for the number of non-Pareto *vertices*; one result does not imply the other because third powers are not uniformly integrable. The published Pareto-frontier/comparability mixed-covariance result considers a different joint statistic at fixed sample size. Older random-order full-text coverage was incomplete, and unseen equivalences remain a priority risk.

## Value

**PASS.** Third factorial moments are a natural test of whether an apparently Poisson sparse count is supported by sufficiently uniform tail estimates. The motivating Pareto papers establish both the Poisson law and variance convergence, so the exact obstruction at the very next factorial moment is a mathematically meaningful boundary. The coefficient distinguishes vertex counting from edge counting and identifies a specific rare three-leaf common-predecessor geometry; it is not a routine corollary of weak convergence or of the comparable-pair calculation.

## Limitations

The result does not establish a general higher-moment phase diagram, and older high-dimensional random-order literature remains a historical-priority uncertainty. The finite exact enumeration only certifies two small directed-poset lemmas; the infinite-domain theorem is proved by their exhaustive reduction and strict asymptotic exponents.

Self-review: passed. Independent audit: not yet performed.
