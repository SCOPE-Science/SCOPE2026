# An exact hypergeometric law for mutual row–column maxima

## Finding

Let \(r,c\geq 1\) be integers, and let \((X_{ij})_{1\leq i\leq r,\ 1\leq j\leq c}\) consist of independent draws from any common atomless real distribution. Define \(S\) to be the set of cells \((i,j)\) that are **strictly largest in their row and strictly largest in their column**; put \(K=|S|\). Then, without any limit or approximation,

\[
K\ \stackrel{d}{=}\ \operatorname{Hypergeom}(r+c-1,\ r,\ c).
\]

Here the three arguments denote population size, number of marked population elements, and number of draws without replacement. In particular, \(1\leq K\leq\min(r,c)\) almost surely, and for every integer \(1\leq k\leq\min(r,c)\),

\[
\Pr(K=k)=\frac{\binom r k\binom{c-1}{k-1}}{\binom{r+c-1}{c}}.
\]

The full **random set** of mutual maxima is also specified: conditional on \(K=k\), \(S\) is a uniformly distributed \(k\)-edge matching of the complete bipartite graph with \(r\) row vertices and \(c\) column vertices. Equivalently, for each prescribed \(k\)-edge matching \(M\),

\[
\Pr(S=M)=\frac{1}{c\,(k-1)!\binom{r+c-1}{c}}.
\]

For \(r+c>2\), the exact first two moments are

\[
\mathbb E K=\frac{rc}{r+c-1},\qquad
\operatorname{Var}(K)=\frac{rc(r-1)(c-1)}{(r+c-1)^2(r+c-2)}.
\]

For \(r=c=1\), \(K\equiv1\) has variance zero. All statements are distribution-free within the atomless i.i.d. model.

## Assumptions and scope

The entries are independent and identically distributed, with no atoms. No equality of the two dimensions is assumed. Both row- and column-maximality are required; the statement does not apply to two independently sampled payoff matrices, dependent entries, or possible ties without additional assumptions. A cell adjacent to a second mutual maximum would share a row or column, which is impossible. Thus \(S\) is always a matching. The globally maximal entry belongs to \(S\), proving nonemptiness. Replacing all entries by their common increasing distribution-function ranks permits assuming independent \(\operatorname{Uniform}(0,1)\) scores, since only ordering matters.

## Proof

Fix \(1\leq k\leq\min(r,c)\) and a *specified* matching \(M\) of \(k\) distinct cells. Write their independent uniform scores as \(x_1,\ldots,x_k\). Each selected cell's row and column must contain no larger score. Entries outside all selected rows and columns impose no condition. For each selected cell \(i\), the \(r+c-2k\) cells in its row or column but outside all other selected rows and columns must be smaller than \(x_i\). For each pair of distinct selected cells \(i,j\), the two cross-cells joining their rows and columns must be smaller than \(\min(x_i,x_j)\). All those unconstrained-entry scores are independent. Therefore the conditional probability that *all* selected cells are mutual maxima is

\[
\prod_{i=1}^{k}x_i^{\,r+c-2k}
\prod_{1\leq i<j\leq k}\min(x_i,x_j)^2.
\]

This expression is symmetric in the selected scores. Integrating over their unit cube is \(k!\) times the integral over \(0<x_1<\cdots<x_k<1\). On that simplex the integrand is

\[
\prod_{i=1}^{k}x_i^{r+c-2i}.
\]

Successive integration, from \(x_1\) upwards, yields

\[
\int_{0<x_1<\cdots<x_k<1}
\prod_{i=1}^{k}x_i^{r+c-2i}\,dx_1\cdots dx_k
=\frac{1}{\prod_{j=1}^{k}j(r+c-j)}.
\]

For clarity, after the first \(t\) variables have been integrated with upper bound \(u\) in place of \(x_{t+1}\), the result is

\[
\frac{u^{t(r+c-t)}}{\prod_{j=1}^{t}j(r+c-j)};
\]

its recursion proves the displayed integral also at the boundary \(r=c=k=1\). Multiplying by \(k!\) therefore gives the exact joint inclusion probability

\[
\Pr(M\subseteq S)=\frac{1}{(r+c-1)(r+c-2)\cdots(r+c-k)}.
\tag{1}
\]

Because a matching is the only possible set of distinct simultaneous maxima, the number of **ordered** \(k\)-tuples of cells in \(S\) is \((K)_{\underline k}\). There are \((r)_{\underline k}(c)_{\underline k}\) ordered row/column matchings, and each has probability (1), hence

\[
\mathbb E(K)_{\underline k}
=\frac{(r)_{\underline k}(c)_{\underline k}}
{(r+c-1)_{\underline k}},\qquad 0\leq k\leq\min(r,c).
\tag{2}
\]

For a hypergeometric random variable \(Y\) obtained by drawing \(c\) elements from a population of \(r+c-1\) with \(r\) marked elements, the standard ordered marked-draw count gives precisely the same factorial moments as (2). Since \(K\) and \(Y\) are supported on the finite set \(\{0,\ldots,\min(r,c)\}\), their factorial moments uniquely determine their distributions: expanding \(\mathbb E(1+t)^K\) in powers of \(t\) shows equality of their probability-generating polynomials. This proves the hypergeometric law and the displayed mass function (including its necessarily zero mass at zero).

Row and column relabelling acts transitively on all matchings of the same size, and preserves the iid joint distribution. Consequently all prescribed sets \(M\) with \(|M|=k\) have the same probability. Their number is \(\binom r k\binom c k k!\). Dividing the above value of \(\Pr(K=k)\) by this count proves conditional uniformity and the stated exact probability for a particular full matching. Finally, the hypergeometric expectation and variance give the moment identities in the Finding section. No asymptotic argument is required.

## Verification

The standalone `verify_rook_maxima.py` independently enumerates all \((rc)!\) distinct rank assignments for each of the boards \((r,c)\in\{(1,1),(1,2),(1,3),(1,4),(2,2),(2,3),(2,4),(3,3)\}\). For each, it reconstructs all mutual maxima directly, tabulates the entire exact law and all feasible marked matching sets, and checks the proposed mass function, factorial moments, uniformity across matchings, and mean and variance using exact rational arithmetic. The checker reports 68 verified assertions. For instance the \(3\times3\) board has probabilities \((3/10,3/5,1/10)\) for exactly one, two, or three mutual maxima. Run with `python3 verify_rook_maxima.py` using Python's standard library. Enumeration is only a finite corroboration; the general infinite family is established by the integral and factorial-moment proof above.

## Relationship to prior work

The square-board local-maxima model was explicitly studied by Baldi, Rinott and Stein in 1989, including the mean, variance and a normal-approximation bound; these are **not** claimed here as new. Bhamidi, Dey and Nobel (2012) cover square Gaussian local maxima (including the one-cell case) and central-limit behavior, but the inspected statements do not give the rectangular exact hypergeometric count law or complete matching-set distribution. Mimun, Quattropani and Scarsini (2022) study random two-player games with correlated payoffs, notably the common-potential case, focusing on equilibrium dynamics and first-order counts; Collevecchio et al. (2024) study the basins of equilibria of the same random-potential model. Their stated results do not supply the exact finite-size count and labelled-set probabilities derived here. The common-interest game interpretation is a mathematically equivalent description of the same object, not an independent novelty claim.

## Limitations

The exact law assumes common atomless iid entries: dependence or ties can change it. The event of simultaneous row/column maximality is not the general best-response equilibrium event for *independent* players' payoff arrays. The matching-set law describes the locations of maxima, not their numerical heights or dynamic attraction basins. Although inspected literature does not directly cover the finite formula, a broader historic theorem or an alternative classical enumeration might subsume it; the originality assessment therefore remains provisional pending independent scholarly review. The 1989 source supplies a publication year but no individually verified exact first-public day; the archival dating for this analysis uses a separately verified 2012 first-submission date.

## References

1. P. Baldi, Y. Rinott and C. Stein, *On the Distribution of the Number of Local Minima of a Random Function on a Graph*, NeurIPS proceedings (1989), especially section 3, example 2, equations (6)–(7). https://papers.nips.cc/paper_files/paper/1989/file/d947bf06a885db0d477d707121934ff8-Paper.pdf
2. S. Bhamidi, P. S. Dey and A. B. Nobel, *Energy Landscape for Large Average Submatrix Detection Problems in Gaussian Random Matrices*, arXiv:1211.2284, first submitted 2012-11-10, especially section 2.5 and Theorem 2.10. https://arxiv.org/abs/1211.2284
3. H. A. Mimun, M. Quattropani and M. Scarsini, *Best-Response Dynamics in Two-Person Random Games with Correlated Payoffs*, arXiv:2209.12967 (2022), sections 3–4. https://arxiv.org/abs/2209.12967
4. A. Collevecchio, H. A. Mimun, M. Quattropani and M. Scarsini, *Basins of Attraction in Two-Player Random Ordinal Potential Games*, arXiv:2407.05460 (2024), especially sections 1–3. https://arxiv.org/abs/2407.05460
