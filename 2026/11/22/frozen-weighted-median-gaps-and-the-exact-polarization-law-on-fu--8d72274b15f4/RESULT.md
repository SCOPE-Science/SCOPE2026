# Frozen weighted-median gaps and the exact polarization law on fully connected influence networks

## Finding

Consider the synchronous weighted-median model of Cheng and Mei with a **common, strictly positive influence profile**: each of \(n\ge 2\) individuals assigns weight \(w_j>0\) to individual \(j\), where \(\sum_{j=1}^{n}w_j=1\). Every individual uses the median response and has a fixed adjustment coefficient \(0<\gamma_i<1\). For an initial vector \(x(0)\in\mathbb R^n\), let \([\ell,u]\) be the (possibly singleton) minimizer interval of \(z\mapsto\sum_j w_j|z-x_j(0)|\), and set \(p_i=\operatorname{proj}_{[\ell,u]}x_i(0)\).

**Exact trajectory theorem.** At every integer time \(k\ge0\), the weighted-median interval remains **exactly** \([\ell,u]\), and

\[
x_i(k)=p_i+(1-\gamma_i)^k\bigl(x_i(0)-p_i\bigr),\qquad i=1,\ldots,n.
\]

Consequently the limiting opinion diameter is exactly \(G=u-\ell\). Consensus occurs precisely when \(\ell=u\); otherwise two distinct opinion values persist, one for each positive-weight half of the population. The global convergence rate to this limiting vector is bounded by \((1-\min_i\gamma_i)^k\).

**Exact random-initialization law.** Suppose the initial opinions are independent and identically distributed from any continuous distribution. Define the family of weight-balanced coalitions

\[
\mathcal B=\left\{S\subseteq\{1,\ldots,n\}:\sum_{i\in S}w_i=\tfrac12\right\}.
\]

The probability of persistent disagreement is precisely

\[
p_{\rm pol}=\sum_{S\in\mathcal B}\binom n{|S|}^{-1}.
\]

When the initial opinions are independent uniform random variables on \([0,1]\), the final diameter has an atom of size \(1-p_{\rm pol}\) at zero and, conditional on being positive, the distribution \(\operatorname{Beta}(1,n)\). Equivalently, for \(0\le t\le1\),

\[
\Pr(G>t)=p_{\rm pol}(1-t)^n,
\qquad \mathbb E[G]=\frac{p_{\rm pol}}{n+1}.
\]

Thus uniform influence weights yield **certain polarization** for even \(n\) with atomless independent initial opinions, but **certain consensus** for odd \(n\). For positive integer input weights encoded in binary, deciding whether \(p_{\rm pol}>0\) is weakly NP-complete, even though every network edge has positive weight.

As a comparison within the same mixed-response model, converting any one individual to the weighted-average rule eliminates the non-consensus possibility: convergence to consensus then holds for every initial vector. This last structural consequence follows from the published general cohesive-set criterion; the explicit orbit and random-gap distribution above are the additional results.

## Assumptions and scope

The population size is finite, \(n\ge2\). The row-stochastic influence matrix is rank one, with \(a_{ij}=w_j>0\) for all \(i,j\), including possible self-influence. All adjustment coefficients are constant and strictly between zero and one. Each weighted-median response is the projection of the individual's current opinion onto the **entire** weighted-median minimizer interval, exactly as in the 2026 source, including half-weight ties. The exact-orbit theorem permits arbitrary real initial opinions and arbitrary heterogeneous adjustment coefficients. The probabilistic conclusions additionally require independent identically distributed continuous initial opinions, with the Beta law requiring uniform \([0,1]\) initial opinions. The computational statement concerns positive integer weights supplied in binary, and the standard decision problem \(p_{\rm pol}>0\).

## Proof

**1. Weighted-median interval structure.** Since every weight is positive, the minimizer interval \([\ell,u]\) is nonempty and its endpoints are observed opinion values. If \(\ell<u\), there is no observed value in \((\ell,u)\), and the total weight on each side is exactly one half:

\[
\sum_{i:x_i(0)\le\ell}w_i=\sum_{i:x_i(0)\ge u}w_i=\tfrac12.
\]

This follows by considering the one-sided slopes of the convex, piecewise-linear absolute-deviation objective. If \(\ell=u=m\), the strict weight below \(m\), and also the strict weight above \(m\), is smaller than one half. At least one positive-weight individual is located at \(m\).

**2. The median interval is frozen.** Suppose \(\ell<u\). Each individual initially at either endpoint stays there: its projection response is its current opinion. Every individual strictly below \(\ell\) moves by a strict convex combination toward \(\ell\), remaining below \(\ell\) at every finite step, and the analogous statement holds above \(u\). Thus the two half-weight groups remain separated, and the largest lower-group value and smallest upper-group value remain \(\ell\) and \(u\). The entire median interval is therefore unchanged after one step. Induction proves it remains unchanged for all steps.

If \(\ell=u=m\), individuals at \(m\) remain fixed. Every opinion below \(m\) stays strictly below and moves toward \(m\), and every opinion above stays strictly above. The weights on either strict side remain less than one half, so the unique weighted median remains \(m\) for all steps. This also proves interval invariance in the singleton case.

**3. Exact orbits and limits.** Since the interval stays fixed, each response is always the fixed projection \(p_i\) of the initial opinion, and the update is a scalar affine recursion:

\[
x_i(k+1)-p_i=(1-\gamma_i)\,[x_i(k)-p_i].
\]

Iteration proves the exact displayed formula. If \(\ell<u\), some agents remain exactly at both endpoints, and every other agent approaches one of them, so the limiting diameter equals \(u-\ell\). If \(\ell=u\), every opinion converges to \(m\). The uniform rate bound follows by taking the largest coordinate error.

**4. Polarization probability.** With independent continuous initial values, all opinions are almost surely distinct and their rank permutation is uniform over the \(n!\) permutations, independently of the ordered values. The median interval has positive length if and only if there is a cut between two consecutive order statistics for which the cumulative influence weight of the lower-ranked agents is exactly one half. Positivity of all weights makes the cut unique whenever it exists. For a fixed balanced subset \(S\), the probability that precisely the elements of \(S\) form the lowest \(|S|\) ranks is \(\binom n{|S|}^{-1}\). Events corresponding to different balanced subsets are disjoint, so their probabilities add to give \(p_{\rm pol}\).

For independent uniform initial opinions, the ordered values are independent of their rank permutation. Every adjacent spacing of the \(n\) order statistics, including the two exterior spacings, has marginal distribution \(\operatorname{Beta}(1,n)\): the \(n+1\) spacings have constant density on the simplex, hence each spacing has survival function \((1-t)^n\) on \([0,1]\). On the polarization event, \(u-\ell\) is exactly the spacing at the unique balanced rank cut. The conditional gap distribution is therefore the same \(\operatorname{Beta}(1,n)\) law, regardless of which balanced cut occurred. The survival function and mean follow. For uniform weights, a balanced subset exists as a ranked prefix precisely when \(n\) is even; every ordering then has the same central cut.

**5. Complexity and one averaging node.** For positive integers \(a_i\) with \(w_i=a_i/\sum_j a_j\), the event \(p_{\rm pol}>0\) holds if and only if some subset sums to exactly half the total, the standard PARTITION decision problem. The subset provides a polynomial-time verifiable certificate, and this is an identity-size polynomial reduction from PARTITION. The hardness is weak: integer dynamic programming is pseudopolynomial in the total weight.

Finally, for this strictly positive rank-one matrix, a proper type-dependent cohesive set cannot include a weighted-average agent, because that agent puts positive weight outside the proper set. Every cohesive set containing only weighted-median agents must carry weight at least one half. Two disjoint nonempty such sets would have to partition the entire population into two half-weight groups, which is impossible if a weighted-average individual lies outside both. The general criterion of Cheng and Mei (Theorem 11) therefore gives universal consensus as soon as at least one individual is weighted-average. This uses a previously established theorem and is not a separately asserted novelty result.

## Verification

The standalone Python 3 program `verify_rankone.py` reconstructs the weighted-median minimizer interval using exact rational arithmetic, performs actual synchronous projection updates for every individual, and separately evaluates the predicted closed-form trajectory at each step. It checks interval invariance for heterogeneous damping on \(3{,}267\) configurations and compares the exact balanced-subset formula against exhaustive rank permutations in \(1{,}089\) configurations, for populations through six individuals and integer weights in \(\{1,2,3\}\). It checks the probability values \(1/2\) for weights \((1,1,1,3)\), \(2/3\) for \((1,1,2)\), and \(4/5\) for \((1,1,1,1,2)\), along with uniform-weight parity for sizes two through seven. These finite tests support the algebra but do not substitute for the proof for arbitrary population size. Reproduce with `python3 verify_rankone.py`.

## Relationship to prior work

Cheng and Mei (2026, arXiv:2610.16406v1) introduce the synchronous model, its closest-point median-tie selection, global convergence, and the type-dependent cohesive-set criterion. Their global criterion already implies the existence/nonexistence of dissensus on this rank-one network and the one-averaging-agent consequence when specialized, so **neither consequence alone is claimed as new**. Their inspected text does not provide the exact invariant median interval, coordinate-by-coordinate closed-form orbits for heterogeneous adjustment, or the full distribution of the final polarization gap under random initial opinions.

Mei et al. (arXiv:2212.08808, published 2024) analyze a different, random asynchronous, neighbor-valued weighted-median process and prove NP-hardness of a different almost-sure dissensus test on general directed networks. They do not supply this rank-one, deterministic, synchronous orbit law or the balanced-subset probability formula. Han et al. (arXiv:2404.16318) study continuous-time weighted-median compromise and general cohesive-set dynamics; these strongly related ideas delimit the present claim. The essential distinction is the **explicit discrete-time rank-one solution and random-limit law**, not the generic existence of consensus or the generic idea of median ties. The order-statistic spacing and PARTITION facts are classical and are used, not presented as discoveries.

## Limitations

The all-median exact trajectories require identical positive influence rows and the closest-point tie rule; heterogeneous network rows can make median intervals move and can invalidate the formula. The Beta law requires independent uniform inputs and does not describe correlated, discrete, or nonuniform input distributions. The exact polarization probability remains valid for all independent, identically distributed continuous inputs. NP-completeness is weak, and the general directed-network computational problem has earlier hardness results. The one-averaging-node conclusion relies on the existing general criterion, while its convergence rate and limiting consensus value are not specified here. This is a deterministic model result, not an empirical prediction. Historical priority for exact rank-one specializations has not been independently certified.

## References

1. Junkai Cheng and Wenjun Mei, *Equilibria and consensus in discrete-time opinion dynamics with mixed weighted-averaging and weighted-median mechanisms*, arXiv:2610.16406v1 (first public 2026-10-12). https://arxiv.org/abs/2610.16406
2. Wenjun Mei, Julien M. Hendrickx, Ge Chen, Francesco Bullo, and Florian Dörfler, *Convergence, Consensus, and Dissensus in the Weighted-Median Opinion Dynamics*, IEEE Transactions on Automatic Control 69 (2024), 6700–6714; arXiv:2212.08808. https://arxiv.org/abs/2212.08808
3. Yi Han, Julien M. Hendrickx, Ge Chen, and Wenjun Mei, *Modeling, Analysis, and Control of Continuous-Time Weighted-Median Opinion Dynamics*, arXiv:2404.16318, first public 2024-04-25. https://arxiv.org/abs/2404.16318
4. M. R. Garey and D. S. Johnson, *Computers and Intractability: A Guide to the Theory of NP-Completeness*, Freeman, 1979 (classical PARTITION hardness).
5. Classical uniform order-statistic spacing theorem: the \(n+1\) spacings have symmetric Dirichlet distribution with all parameters one; the required marginal law is proved above from the uniform simplex density.
