# Scientific review

**Correctness — PASS.** Conditioning on a single iid chord gives explicit quadratic projection polynomials. Their means, squares, and mixed products are evaluated exactly by uniform-triangle integration. In the covariance sum the same label-pair contribution is \(-1/9\), a single shared-chord contribution vanishes by orthogonality, and disjoint pairs are independent. The stated combinatorial multiplicities recover the exact finite identities for every \(n\ge2\). The Hoeffding decomposition's degenerate remainder has variance \(O(n^2)\), so the projection CLT proves the independent Gaussian limit. A standalone rational checker passed 75 assertions including complete enumeration up to seven chords.

**Originality — PASS, with a historical-priority risk.** Paguyo (2021) provides the marginal crossing CLT and a separate crossing/simple-chord comparison; Flajolet–Noy (2000) contains known marginal crossing moments; Chen et al. (2005/2007) and Baik–Jenkins (2011) study the sizes of maximal crossing/nesting systems. Their statements do not logically give the mixed covariance of total *two-chord pair counts* or the independent joint Gaussian limit. Actual targeted literature and mathematical-record searches identified no explicit equivalent theorem, but this does not establish unique historical priority. The corresponding old marginal claims are excluded from the new contribution.

**Value — PASS.** The sharp exact correlation and its \(n^{-1}\) decay settle a natural second-order dependence question not answered by marginal laws or maximal-pattern symmetry. Orthogonality of the first Hoeffding projections explains why finite anticorrelation coexists with joint Gaussian independence. This distinction remains meaningful for inference on two distinct chord-pattern totals, and the aligned-count covariance matrix is determined in the same theorem.

The theorem is restricted to uniform matchings, addresses totals of two-chord patterns rather than maxima, and asserts no multivariate convergence rate. It has no independent validation.

Self-review: passed. Independent audit: not yet performed.
