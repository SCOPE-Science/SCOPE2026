# A third-moment defect for non-Pareto point counts at the sparse Poisson threshold

## Finding

Let \(X_1,\ldots,X_n\) be independent uniformly sampled points of \([0,1]^d\). Write \(N_{n,d}\) for the number of points \(X_i\) for which another point \(X_j\) is coordinatewise strictly smaller. Thus \(N_{n,d}\) is the number of non-Pareto-minimal points. For a nonnegative integer \(z\), let \((z)_r=z(z-1)\cdots(z-r+1)\). Along any sequence of integer dimensions satisfying
\[
n\to\infty,\qquad n^2 2^{-d_n}\longrightarrow\lambda\in(0,\infty),
\]
the known Poisson limit and convergence of the first two factorial moments are accompanied by a **different third factorial-moment limit**:
\[
\boxed{\mathbb E(N_{n,d_n})_3\longrightarrow\lambda^3+\lambda^2.}
\]
In contrast, \(\operatorname{Poisson}(\lambda)\) has third factorial moment \(\lambda^3\). Thus the third factorial moments are not uniformly integrable even though \(N_{n,d_n}\Rightarrow\operatorname{Poisson}(\lambda)\), \(\mathbb EN_{n,d_n}\to\lambda\) and \(\operatorname{Var}(N_{n,d_n})\to\lambda\). The additional \(\lambda^2\) comes from the rare event that one observation lies below three specified others in every coordinate. The result is valid also for independent continuous coordinates with arbitrary coordinatewise marginal distributions, using monotone quantile transforms.

## Assumptions and scope

The sample has independent points and independent continuous coordinates, with the uniform-cube representation used in the proof. Every comparison is componentwise. All limit orders refer to the entire integer sequence or subsequence satisfying the displayed condition. For example, \(n=2^m\), \(d_n=2m+c\) with fixed integer \(c\) gives \(\lambda=2^{-c}\). The theorem concerns the **unweighted number of non-Pareto vertices**, not the number of ordered comparable pairs. The latter statistic has a different previously established third factorial-moment defect \(2\lambda^2\); its conclusion alone does not imply the present claim.

## Proof

For each \(i\), define \(D_i=\sum_{j\ne i}{\bf1}\{X_j<X_i\text{ coordinatewise}\}\), where comparisons are almost surely strict. Thus \(N=\sum_i{\bf1}\{D_i\ge1\}\). Define the witness-weighted third count
\[
R_3=\sum_{\substack{i,j,k\in[n]\\\text{pairwise distinct}}}D_iD_jD_k.
\]
We show, in order, \(\mathbb ER_3=\lambda^3+\lambda^2+o(1)\) and \(\mathbb E[R_3-(N)_3]=o(1)\).

**1. Order constraints and their exact one-coordinate probabilities.** Every term of \(R_3\) selects three distinct targets \(i,j,k\) and one predecessor of each, possibly selecting the same predecessor several times. The resulting directed graph has exactly three directed edges and at most six vertices. In a single coordinate, the probability of all comparisons is \(L/v!\), where \(L\) is the number of linear extensions of the directed constraints on its \(v\) involved vertices; a directed cycle gives zero. Independence of coordinates makes the probability \((L/v!)^d\).

All witness-identification types can be exhausted by fixing targets \(0,1,2\), and taking their three predecessor indices from \(\{0,1,2,3,4,5\}\), excluding equality with their respective target. This produces 51 distinct canonical constraint types. An exhaustive linear-extension enumeration gives the following *maximum* possible one-coordinate probability at each vertex count:

| Number of vertices \(v\) | 3 | 4 | 5 | 6 |
|:--|--:|--:|--:|--:|
| Maximum \(L/v!\) | 0 | \(1/4\) | \(1/6\) | \(1/8\) |

The unique four-vertex type achieving \(1/4\) is one external predecessor lying below all three targets. The six-vertex type consists of three disjoint directed pairs and has one-coordinate probability \(1/8\). These two contributions to \(\mathbb ER_3\) are exactly
\[
(n)_4 4^{-d}\qquad\text{and}\qquad(n)_6 2^{-3d},
\]
respectively. The remaining types contribute at most \(O(n^5 6^{-d}+n^4\eta^d)\) for some \(\eta<1/4\); the table permits the simpler bound \(O(n^5 6^{-d})\) for all non-leading positive types. Under \(d_n=2\log_2 n+O(1)\), this tends to zero because \(5-2\log_2 6<0\). The two displayed contributions tend to \(\lambda^2\) and \(\lambda^3\), proving
\[
\mathbb ER_3\longrightarrow\lambda^3+\lambda^2.\tag{1}
\]

**2. Removing repeated witness choices.** For every nonnegative integer \(z\), \(0\le z-{\bf1}\{z\ge1\}\le\binom z2\). Applying the elementary product-difference inequality to the three factors gives
\[
0\le\mathbb E[R_3-(N)_3]\le 3\sum_{\substack{i,j,k\in[n]\\\mathrm{distinct}}}\mathbb E\!\left[\binom{D_i}{2}D_jD_k\right].\tag{2}
\]
Each term on the right selects four directed comparison edges: two *distinct* predecessors of target \(i\), one predecessor of \(j\), and one of \(k\). Every possible witness-identification pattern is represented, up to relabelling external vertices, by choosing four witness slots from \(\{0,1,2,3,4,5,6\}\) with targets \(0,1,2\), prohibiting self-comparisons and equality of the two witnesses of target \(0\). There are exactly 124 distinct canonical directed-constraint types. Exhaustive linear-extension counting gives:

| Number of involved vertices \(v\) | 4 | 5 | 6 | 7 |
|:--|--:|--:|--:|--:|
| Maximum one-coordinate probability | \(1/8\) | \(3/20\) | \(1/9\) | \(1/12\) |

The finite enumeration is reproduced in full by the standalone `verify.py`, which generates *all* target/predecessor identifications, counts linear extensions as exact fractions, and checks both tables. No statistical sampling or numerical tolerance is used. Consequently the right side of (2) is bounded by a constant times
\[
n^4 8^{-d}+n^5(3/20)^d+n^6 9^{-d}+n^7 12^{-d}=o(1).
\]
Indeed, each exponent \(v+2\log_2 p_v\) is strictly negative for the listed probabilities \(p_v\). Combining this with (1) proves the theorem. The previously established Poisson limit and first-two-moment convergence are used only for contextual comparison, not to deduce the third moment. \(\square\)

## Verification

Run `python3 verify.py` from the extracted package directory. The standard-library script exhaustively enumerates 51 three-edge witness-identification types and 124 four-edge types; it computes all coordinate-order linear-extension fractions exactly, checks the two complete maxima tables and uniqueness of the four-vertex dominant star, and independently enumerates the non-Pareto third factorial moment for small samples. The recorded execution passed 15 groups of exact-rational checks. The infinite limiting argument is analytic; the finite program establishes the two explicitly finite constraint lemmas, not an inference from bounded sample size.

## Relationship to prior work

Ilienko and Jin [1] prove the Poisson limit of the unweighted non-Pareto count at the same dimension scale and convergence of its expectation and variance (Theorem 2.1). Their Section 3 also studies the *weighted* comparison count, which is a different random variable. Their statement does not give the third factorial moment of the unweighted count, nor its precise failure to converge to the Poisson value. Bhattacharjee, Ilienko, Jin and Molchanov [2] extend the phase diagram and recover the critical Poisson law without a higher-factorial-moment calculation for the unweighted binomial count. An earlier separately established comparable-pair moment formula identifies a distinct third-factorial defect of \(2\lambda^2\) for the **edge count**; high-probability agreement between edge and vertex counts cannot transfer unbounded moments, so the present proof controls the weighted/unweighted difference at third-moment level. The unrelated mixed covariance at fixed sample size in [3] also does not imply this result.

## Limitations

The theorem identifies only the third factorial moment at the sparse threshold; it does not determine fourth or higher moments, their divergence or exact rates. It does not extend to dependent coordinates or alternate scaling windows. Finite poset enumeration is used solely for two completely specified finite lemmas, with all types generated and their exact probabilities checked; it is not presented as a computational proof of the asymptotic limit. Full historical priority cannot be independently guaranteed: the complete text of the earlier Bollobás–Brightwell random-order study [4] was not accessible in this investigation, so an equivalent older factorial-moment identity remains a residual risk.

## References

1. A. Ilienko and B. Jin, *Pareto points in growing dimensions*, arXiv:2603.18698v1, first posted 2026-03-19. https://arxiv.org/html/2603.18698v1. Relevant: Theorem 2.1, Section 3.
2. C. Bhattacharjee, A. Ilienko, B. Jin and I. Molchanov, *From Gaussian to stable and back: Non-Pareto points in growing dimension*, arXiv:2611.01096v1, first posted 2026-10-31. https://arxiv.org/html/2611.01096v1. Relevant: Introduction, Theorem 2.6, Section 10.
3. *Exact Pareto-frontier–comparability covariance and three high-dimensional scales*, 2026-11-02. https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-exact-pareto-frontier-comparability-covariance-and-three-high-di--c663d8d03f4e/RESULT.md.
4. B. Bollobás and G. Brightwell, *Random high-dimensional orders*, Advances in Applied Probability 27 (1995), 161–184. https://doi.org/10.2307/1428102.
