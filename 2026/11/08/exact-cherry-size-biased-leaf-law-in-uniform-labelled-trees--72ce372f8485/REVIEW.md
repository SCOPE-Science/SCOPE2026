# Scientific review: exact cherry-size-biased leaf law

## Correctness

**PASS.** The claimed random object is a uniform unrooted labelled Cayley tree, not a phylogenetic-tree model. A marked unrestricted cherry has exactly \((n-2)^{n-4}\) completions; deleting the two specified leaves yields a uniform tree of size \(n-2\). The leaf count under marking becomes two plus the number of absent noncenter letters in the reduced Prüfer code. This proves every stated binomial moment, and hence the complete finite-support size-biased law. The first moment gives the mixed covariance. The function \((1-1/x)^{x-2}\) is strictly decreasing for \(x\ge2\), proving the covariance strictly positive without extrapolation. Ordered overlapping-pair classification gives the exact cherry second factorial moment, including the distinct \(n=4\) case; two-term expansions establish the asymptotic variances and Pearson correlation. A standalone exact checker exhausts \(n\le8\) and performs additional rational boundary checks, reporting `VERIFY_OK 1076`. No inference about an infinite family rests on those computations.

## Originality

**PASS, with priority qualification.** The closest direct source is Junk--Schmidt--Weber, *Almost all trees have quantum symmetry*, arXiv:1911.02952 (first posted 2019-11-07), Section 3. It counts degree-three-center cherries and credits an older *unrestricted* definition; its published formulas concern the former and cannot be substituted for the statistic here. Isaev--Southwell--Zhukovskii, arXiv:1912.09838 (2019-12-20), Section 2, give a strong general tree-pattern counting and normal-approximation method: that machinery covers the elementary marked-pattern probabilities and may yield special moment expressions with further computation. However the inspected paper does not state the all-order leaf--unrestricted-cherry covariance sign, the exact size-biased occupancy law, or the explicit positive limiting correlation. Ekhad--Zeilberger, arXiv:2201.07326 (2022), study degree counts, which cannot determine common-neighbor leaf-pair counts; Choi--Thompson--Wu, arXiv:2002.12643 (2020), study phylogenetic models with different probability spaces. Published-record and related research-record searches found no explicit theorem with the same conclusions. This is a best-knowledge novelty assessment, not a proof of historical uniqueness; old pattern enumerators or Erdős--Rényi-era calculations may contain implicit equivalents.

## Value

**PASS.** The count of unordered pairs of leaves at the same center measures a direct source of combinatorial tree symmetry and is not a function of the number of leaves alone. The result gives its **whole size-biased interaction** with the leaf count, not merely a marginal or a small numeric improvement. The all-size strict sign and nonzero limiting correlation quantify the influence of local sibling-leaf structure on global leaf abundance. It is a natural structural dependence question, and the exact occupancy representation allows mixed leaf moments to be computed without enumerating all trees. No downstream theorem or unsupported application is claimed.

## Limitations and source coverage

The general pattern-moment lemma of Isaev--Southwell--Zhukovskii can recover the basic marked subtree probabilities, so those ingredients are not presented as new. The degree-three-only cherry covariance from other work does not settle the unrestricted leaf-pair dependence. The 2022 degree-count paper was read at abstract/metadata level, not certified against every hidden formula. No bivariate CLT is proved here. Historical priority and independent mathematical validation remain open.

Self-review: passed. Independent audit: not yet performed.
