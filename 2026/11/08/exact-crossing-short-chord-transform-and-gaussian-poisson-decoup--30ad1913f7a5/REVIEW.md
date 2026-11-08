# Review: exact crossing–short-chord transform

## Correctness

**PASS.** The complete bivariate polynomial identity is obtained by double counting a marked subset of mutually disjoint boundary edges. Every specified boundary edge is noncrossing, and deletion preserves all crossings of the remaining chords, giving a bijection to unrestricted smaller diagrams. The classical cycle-matching number supplies the exact coefficient. The binomial identity then gives the exact joint enumerator, and the stated mean, variances, and covariance reduce algebraically to the exact correlation \(-\sqrt{5/(n+3)}\). The joint weak limit follows from a summably dominated binomial-transform identity plus the established univariate crossing CLT. The exceptional \(n=1\) case is excluded from the correlation theorem. The executable integer verification independently enumerates all diagrams through six chords, checks the cycle coefficients through five chords, and reports 385 exact assertions.

## Originality

**PASS, with residual priority uncertainty.** The 2013 Pilaud–Rué full paper analyzes fixed-crossing perfect-matchings without marking matched adjacent endpoints. The 2000 Flajolet–Noy study gives crossing marginal moments and the Gaussian limit, and studies components rather than the exact joint simple-chord/crossing enumerator. The 2015 Acan study develops the same random chord model and component/degree results but not this bivariate transform. The 2021 Paguyo study explicitly treats crossings and simple chords in separate normal- and Poisson-approximation sections; these separate laws do not entail the finite transform, exact negative correlation, or independence of the joint limit. A conditional crossing-degree calculation for one prescribed chord is insufficient to determine the number of simultaneously occurring simple chords or its mixed distribution with total crossings. Searches did not find a directly covering bivariate statement. Possible unindexed historical joint enumerators or implicit coefficient identities remain a priority risk; novelty is provisional and not independently certified.

## Value

**PASS.** Crossing count measures intersection-graph complexity, whereas simple chords are the ubiquitous isolated local components in a random chord diagram. Their complete joint distribution is a natural invariant, not an arbitrary parameter slice. The simple exact negative correlation quantifies a finite-order tradeoff and the joint Gaussian–Poisson limit identifies independent macroscopic and rare local regimes. The transform efficiently reconstructs every joint probability using pre-existing crossing polynomials; its consequences are not supplied by the two separate marginal limit laws. No downstream theorem beyond these self-contained probability results is claimed.

## Closest literature and limitations

The compared original manuscripts are Flajolet–Noy, *Analytic Combinatorics of Chord Diagrams* (INRIA RR3914, 2000); Acan, *On a uniformly random chord diagram and its intersection graph* (arXiv:1501.01489, 2015); Paguyo, *Convergence Rates of Limit Theorems in Random Chord Diagrams* (arXiv:2104.01134, 2021); Riordan (1975, original crossing enumerator); and Pilaud–Rué (arXiv:1307.6440, 2013, fixed-crossing enumeration). The proof uses the published univariate crossing mean, variance and CLT. It neither supplies new results for nonuniform matchings nor claims quantitative joint convergence rates. Historical-priority coverage outside these inspected works remains possible.

Self-review: passed. Independent audit: not yet performed.
