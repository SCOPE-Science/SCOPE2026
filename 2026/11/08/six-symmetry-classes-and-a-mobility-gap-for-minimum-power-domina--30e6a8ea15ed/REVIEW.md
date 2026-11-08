# Scientific review — minimum power domination on the five-cube

## Correctness (PASS)

The known cardinality \(\gamma_P(Q_5)=4\) follows from the sharp dimension-five specialization of Dean et al.'s 2011 bounds. The finite claim concerns \(\binom{32}{4}=35960\) possibilities, all of which are checked by two independent implementations of the standard power-domination closure. The six explicit symmetry orbits partition exactly the 3600 successful states; every possible one-token exchange is tested. Six representative breadth-first searches determine eccentricity through group invariance, and a separate C++ all-sources BFS checks the same histogram. Explicit deterministic programs and actual output files are included. Nothing is extrapolated to infinite graph families.

## Originality (PASS with historical-priority risk)

The nearest historically relevant full text, Dean et al. (2011), computes power-domination *cardinality bounds*, not the distribution of minimum sets or the reconfiguration graph. The 2015 Benson et al. full text applies a general zero-forcing lower-bound framework, not this state-space classification. The 2026 open-access full text by Bjorkman et al. initiates general PDS token-jump analysis and identifies token sliding as an avenue for further study; it does not imply the 3600-state five-cube certificate or its metric. Searches under five-cube, hypercube, sensor relocation, and token-jump/slide aliases found no exact matching classification. A 2012 Pai–Chiu hypercube note is a plausible but incompletely accessible source; its abstract concerns the power-domination number and a conjecture, not the specific claims. An unindexed equivalent enumeration remains possible. The known minimum cardinality is excluded from the originality claim.

## Value (PASS)

The first five-dimensional binary cube requires four minimum monitoring vertices, an instructive natural next case after the two-sensor four-cube. A complete description of the optimal placements is relevant to network reconfiguration and monitoring resilience: 3600 optimal placements are all locally slide-frozen yet form a connected nontrivial exchange network of diameter six. The six full Hamming-isometry orbits, exact degree/eccentricity spectra, and independent exhaustive certificates supply reusable benchmark data for constrained relocation and symmetry-based enumeration rather than an arbitrary finite curiosity. There is no claimed theorem for larger dimensions.

## Closest literature and limits

Sources inspected: Dean et al., 2011, https://kjtian.github.io/PDSHypercube.pdf (all four pages); Benson et al., 2015, https://ar5iv.labs.arxiv.org/html/1510.02421 (full article); Bjorkman et al., 2026, https://link.springer.com/article/10.1007/s44007-025-00187-5 (full open-access article). The Pai–Chiu (2012) full paper was not retrieved; only bibliographic/abstract content was examined. The residual risk is historical priority, not an unproved finite enumeration. Independent scholarly assessment is outstanding.

Self-review: passed. Independent audit: not yet performed.
