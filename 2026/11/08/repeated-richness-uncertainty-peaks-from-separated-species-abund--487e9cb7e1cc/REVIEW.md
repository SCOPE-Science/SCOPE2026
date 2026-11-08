# Scientific review: repeated richness uncertainty peaks

## Correctness — PASS

For finite iid-with-replacement species sampling, the occupied-indicator formula follows by complement probabilities for one or two species. Two species reduce to a Bernoulli distribution with increasing success probability, giving at most one strict discrete variance peak. The separated family \(p_0=1-\sum_{j=1}^{m-1}\varepsilon^j\), \(p_j=\varepsilon^j\) has explicitly ordered rare-species discovery scales. At depth \(\lfloor\log(2)/\varepsilon^j\rfloor\), the richness is asymptotically a fixed count plus a fair Bernoulli, so its variance tends to \(1/4\); at each intermediate geometric-mean depth it converges to a deterministic count. Since adjacent-depth variance differences are nonzero integer polynomials in \(\varepsilon\), a sufficiently small transcendental value excludes ties at every depth, and the separated high/low points force at least \(m-1\) strict maxima. Four rational difference calculations rigorously establish two peaks for the concrete three-species vector \((7,7,1)/15\). The attached checker independently verifies exact formulas and exact-state dynamic programming for a finite set of instances; no infinite conclusion depends on those tests.

## Originality — PASS, with historical-priority risk

The indicator variance formula is classical and is **not** asserted novel. Heck, van Belle and Simberloff (1975) address finite-collection rarefaction without replacement, and Ugland, Gray and Ellingsen (2003) address sample-based accumulation variance; the accessible Ugland full text, including Appendix I, was inspected. Bogachev, Gnedin and Yakubovich (2006), *On the variance of the number of occupied boxes* (arXiv:math/0609498), was inspected as highly relevant primary full text: its infinite-box variance analysis and oscillatory geometric-frequency examples may imply a related weaker finite-truncation phenomenon. Its inspected results do not give the cardinality-sharp three-species cutoff together with a \(m-1\)-peak finite construction and limiting peak/valley heights. Archibald, Knopfmacher and Prodinger (2006), *The number of distinct values in a geometrically distributed sample*, is a plausible related source whose abstract but not full text could be inspected. A broader exact or implicit coverage by lesser-known finite occupancy literature remains a risk. The independent novelty assessment has not occurred.

Actual semantic-index searches compared variance oscillation, unimodality, finite supports, aliases such as occupied boxes/distinct values and variance versus sampling effort, as well as available earlier private claims. Closest published indexed records concern covariance between successive discoveries, richness-frequency covariances and occupied-indicator precision geometry, none of which implies a count of sampling-depth variance peaks.

## Value — PASS

Uncertainty bands around a species-accumulation curve can undergo repeated high-low-high transitions even as expected richness increases monotonically. The exact three-species obstruction and an explicit witness locate the first possible double peak, while the arbitrary-richness construction demonstrates a whole cascade of separated uncertainty regimes, each with near-Bernoulli variance \(1/4\). This is a structural caution for interpreting sampling-effort uncertainty, not a routine computation of a known moment formula. The result does not claim an upper bound at fixed richness or direct field applicability under spatial dependence.

## Related sources and limitations

- Heck, van Belle and Simberloff (1975), https://doi.org/10.2307/1934716 (accessible abstract; original article inaccessible in this check).
- Ugland, Gray and Ellingsen (2003), https://doi.org/10.1046/j.1365-2656.2003.00748.x (full HTML and Appendix I inspected).
- Bogachev, Gnedin and Yakubovich (2006), https://arxiv.org/abs/math/0609498 (full primary text and variance-related sections inspected).
- Archibald, Knopfmacher and Prodinger (2006), https://doi.org/10.1016/j.ejc.2006.06.007 (abstract inspected; hosted PostScript extraction unavailable).

Self-review: passed. Independent audit: not yet performed.
