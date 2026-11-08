# Scientific assessment

## Correctness: PASS

The reduced transition rates are exact after conditioning on the two fixed voters. The stationarity equations for the two part proportions solve to \(n/(m+n-1)\) and \((n-1)/(m+n-1)\), and therefore the total mean \(n/(m+n)\). A squared-disagreement generator bound proves synchronization of the two part proportions at \(L^2\)-rate \(O(m^{-1}+n^{-1})\). At time scale \(2mn/(m+n)\), the exact midpoint generator converges in stationary expectation to the Jacobi generator \((\theta-x)f'(x)+x(1-x)f''(x)/2\). Polynomial moments recursively identify the unique \(\operatorname{Beta}(2\theta,2(1-\theta))\) law. Every boundary and ratio condition is explicit. The 709 package-based finite assertions corroborate transition and normalization identities but are not the infinite proof.

## Originality: PASS on the examined literature, priority provisional

Mobilia–Petersen–Redner (arXiv:0706.2892, inspected complete text) analyze two opposite zealots on the complete graph and on lattices, not on complete bipartite networks with unequal part sizes. Pickering–Lim (arXiv:1408.2130, examined complete source text) analyze complete-bipartite voter consensus without opposite frozen agents. Mobilia 2015 (arXiv:1506.04911) uses nonlinear copying in a fully mixed population. Mori–Hisakado–Nakayama 2018 (arXiv:1810.05643) consider a different multivoter-per-node preference-noise diffusion model. A 2026 Moran/voter paper (DOI:10.1016/j.jtbi.2026.112517, extensive accessible text) obtains exact Dirichlet–multinomial laws for fully mixed populations and mean-field random graphs, but not this exact bipartite theorem. The 2013 Yildiz–Ozdaglar–Acemoglu–Saberi–Scaglione paper (DOI:10.1145/2538508) was inspected at abstract level only, and may contain relevant general first/second-moment implications. Its abstract promises moment results rather than the full limit distribution, so coverage is not established, but the historical priority risk is retained. Published mathematical-record searches of the joint-beta and opposed-zealot formulations returned no equivalent statement. This is not a proof of global novelty.

## Mathematical value: PASS

Two fixed opposite opinions on a complete bipartite graph are the simplest exact setting where the zealots have opposite vertex degrees. The result gives a nontrivial, full stationary distribution rather than only a mean or a second-moment bound, and determines how degree-class asymmetry transforms a uniform macroscopic law into a skew beta family without changing the numbers of frozen voters. Non-self-averaging and the explicit \(\theta(1-\theta)/3\) variance are quantitatively useful benchmarks for voter-model network heterogeneity and persistent disagreement. The edge behavior and mixing time are intentionally not claimed.

## Source-access and priority limitations

The potentially relevant general-network stubborn-agent paper of 2013 could only be examined through its abstract and bibliographic context; institutional full-text access was unavailable. No claim of exhaustive literature coverage or independent audit is made. See `AUDIT.json` for exact searches, source inspections, comparisons and residual risks.

Self-review: passed. Independent audit: not yet performed.
