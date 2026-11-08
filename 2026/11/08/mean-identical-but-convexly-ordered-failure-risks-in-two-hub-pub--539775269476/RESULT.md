# Mean-identical but convexly ordered failure risks in two-hub public-goods networks

## Finding

Consider the public-output convention that a network's output after vertex failures is the order of its largest remaining connected component (zero when no vertex remains). A connected network may be capable of financing the same fixed public-good bill and have **the same expected output under every fixed number of random outages**, yet have a markedly different exposure to severe failures.

**Theorem.** For every integer \(n\ge 4\), take nonnegative integers \(a,b\) with \(a+b=n-2\), and form the two-hub tree \(D_{a,b}\) by joining two hubs with an edge and attaching \(a\) leaves to the first and \(b\) to the second. The endpoints \(a=0\) and \(b=0\) are stars. Let \(L_m^{a,b}\) be the largest connected-component order when exactly \(m\) of the \(n\) vertices survive, sampled uniformly without replacement.

1. For every \(0\le m\le n\), the expectation \(\mathbb E L_m^{a,b}\) is **independent of the split** \((a,b)\). Using the convention that out-of-range binomial coefficients vanish, it equals

\[
\mathbb E L_m^{a,b}=\frac{m\binom{n-2}{m-2}+(m+1)\binom{n-2}{m-1}+\mathbf1_{\{m\ge1\}}\binom{n-2}{m}}{\binom nm}.
\]

2. If \(a\ge b\) and \(a'\ge b'\) satisfy \(a+b=a'+b'=n-2\) and \(a\ge a'\), then for every convex real function \(\varphi\),

\[
\mathbb E\varphi(L_m^{a,b})\ge\mathbb E\varphi(L_m^{a',b'})\quad(0\le m\le n).
\]

The expectations of the two arguments are equal. If \(a>a'\), \(3\le m\le n-1\), and \(\varphi\) is strictly convex, the inequality is strict. In particular, the star is the unique maximum and the most balanced two-hub tree is the unique minimum in this convex-risk order, up to graph isomorphism, when the order is nontrivial. The exact variance difference is

\[
\operatorname{Var}(L_m^{a,b})-\operatorname{Var}(L_m^{a',b'})
=\frac{m(m-1)(m-2)(n-m)}{n(n-1)(n-2)(n-3)}
\bigl(a^2+b^2-(a')^2-(b')^2\bigr).
\]

3. If each vertex instead survives independently with common probability \(s\in[0,1]\), write \(L_s^{a,b}\) for the largest surviving component. Its probability generating polynomial is

\[
\begin{aligned}
G_{a,b,s}(z)={}&s^2z^2(1-s+sz)^{n-2}\\
&+s(1-s)z\bigl[(1-s+sz)^a+(1-s+sz)^b\bigr]\\
&+(1-s)^2\bigl[(1-s)^{n-2}+(1-(1-s)^{n-2})z\bigr].
\end{aligned}
\]

Its mean, independent of \((a,b)\), is

\[
\mathbb E L_s^{a,b}=s(2+(n-2)s)+(1-s)^2\bigl(1-(1-s)^{n-2}\bigr).
\]

The same convex order holds for all \(s\), strictly for distinct unordered splits and strictly convex \(\varphi\) when \(0<s<1\). Its variance gap is

\[
\operatorname{Var}(L_s^{a,b})-\operatorname{Var}(L_s^{a',b'})
=s^3(1-s)\bigl(a^2+b^2-(a')^2-(b')^2\bigr).
\]

4. In the connected-public-good participation model with per-unit benefit \(v>0\), every full-participation tree \(D_{a,b}\) has the same aggregate unilateral-withdrawal responsibility \(R(D_{a,b})=2n-2\), so its largest financeable fixed bill is exactly \(v(2n-2)\). The stochastic statements above are assessments of **external random outages**, not additional Nash-equilibrium assertions.

## Assumptions and scope

Graphs are finite, simple, undirected trees of the specified two-hub form; the set of surviving vertices induces the functioning network. In the fixed-size model, every \(m\)-subset has probability \(1/\binom nm\). In the independent-survival model, all vertex indicators are independent with the same parameter \(s\). All functions in the convex-order assertion have finite values on \(\{0,\ldots,n\}\). The stochastic analysis is for exogenous failures rather than a stochastic model of strategic participation. Financing assumes full participation before failures, a common linear per-unit output benefit, nonnegative budget-balanced charges, and the commitment assumption in the cited public-goods model.

## Proof

Put \(N=n-2\) and label the two hubs \(u,v\). Classify a surviving vertex set by the hub indicators. If both hubs survive, all survivors are connected and output is \(m\). If exactly one survives, output is one plus the number of surviving leaves adjacent to it; leaves adjacent to the failed hub are isolated. If both hubs fail, output is one if any leaf survives and zero otherwise.

For a uniform \(m\)-subset, the first class contains \(\binom N{m-2}\) sets of output \(m\). The two one-hub classes contain \(\binom N{m-1}\) sets each; summing their outputs across both possible hubs yields \((m+1)\binom N{m-1}\), because any selected \((m-1)\)-leaf set contributes the two hub vertices plus all its \(m-1\) selected leaves. The no-hub class contributes \(\mathbf1_{\{m\ge1\}}\binom Nm\). Division by \(\binom nm\) proves the first formula, including all boundaries.

For convex order, condition on an exactly-one-hub surviving event and set \(r=m-1\). Sample uniformly a size-\(r\) set of the \(N\) leaves. For \(0\le k\le N\), define

\[
f(k)=\mathbb E\varphi\bigl(1+H_k\bigr),\qquad
H_k=\sum_{i=1}^k I_i,
\]

where \((I_1,\ldots,I_N)\) is an exchangeable zero-one vector with exactly \(r\) ones. For \(0\le k\le N-2\), exchangeability yields

\[
f(k+2)-2f(k+1)+f(k)
=\mathbb E\Big[I_{k+1}I_{k+2}\Delta^2\varphi\bigl(1+H_k\bigr)\Big]\ge0,
\]

where \(\Delta^2\varphi(t)=\varphi(t+2)-2\varphi(t+1)+\varphi(t)\). For \(r\ge2\) and strictly convex \(\varphi\), this is positive because the probability that both indicated leaves are sampled is positive. Conditional contributions from the one-hub cases to an unnormalized convex expectation are \(\binom Nr\,[f(a)+f(b)]\). The both-hub and no-hub cases are independent of \((a,b)\). Discrete convexity of \(f\) implies that redistributing a leaf from the smaller to the larger hub weakly increases \(f(a)+f(b)\), strictly in the stated interior range. Repeating such moves establishes the convex order and strictness. At the empty or extreme survivor counts, all mentioned formulas continue to hold by direct inspection.

To obtain the variance difference, use the hypergeometric factorial moments

\[
\mathbb E H_k=\frac{rk}{N},\qquad
\mathbb E[H_k(H_k-1)]=\frac{r(r-1)k(k-1)}{N(N-1)}.
\]

In the second moment of the two one-hub contributions, only the quadratic term depends nonlinearly on the split. Multiplication by \(\binom Nr/\binom nm=m(n-m)/(n(n-1))\) gives the displayed variance coefficient. The mean is already split-independent.

For independent survival, the same three hub patterns have probabilities \(s^2\), \(s(1-s)\) each, and \((1-s)^2\). The selected leaves in any surviving hub's branch have binomial counts, proving the probability generating polynomial and its first derivative at \(z=1\). Here \(f(k)=\mathbb E\varphi(1+\operatorname{Bin}(k,s))\) has nonnegative second finite differences \(s^2\mathbb E\Delta^2\varphi(1+\operatorname{Bin}(k,s))\); the same balancing argument proves convex order. A binomial second-moment calculation gives the stated variance coefficient \(s^3(1-s)\). Strictness follows for \(0<s<1\).

Finally, the deletion of the first hub leaves a largest component of order \(b+1\) and has responsibility \(a+1\); the second hub's responsibility is \(b+1\), and each of the \(N\) leaves has responsibility one. Therefore \(R=(a+1)+(b+1)+N=2n-2\). The financing interpretation is the already established supportability identity of Angulo, rather than a new equilibrium theorem.

## Verification

Run `python verify.py` with Python 3 and the standard library. The verifier enumerates all surviving subsets for every two-hub tree with \(4\le n\le9\), compares their empirical counting formulas, checks convex hinge inequalities for every survivor count and integer hinge threshold, and checks exact variance differences. It separately compares independent-survival generating laws at three rational survival probabilities. The actual run passed 265 histogram/mean checks, 830 convex-order hinge inequalities, 98 variance-difference identities, and 99 generating-function comparisons. These finite computations independently check edge cases; they do not replace the algebraic proof for arbitrary \(n\).

For a scale illustration, choose even \(N=n-2\), compare the star \((N,0)\) with the balanced double star \((N/2,N/2)\), and set \(s=1/2\). Both have identical mean output, but their variances differ by exactly \(N^2/32\). This quadratic gap shows that identical mean curves can obscure substantial disparity in risk.

## Relationship to prior work

Angulo (2026) defines output as the largest connected active component, identifies individual withdrawal ceilings, and proves that the aggregate responsibility is the financeable capacity; it analyzes expected surviving output after one uniform withdrawal and a path extremal theorem. The present finding uses those definitions but concerns the **entire fixed-survivor-count mean curve**, split-invariant percolation means, and an exact convex-risk ordering on the two-hub tree family. The original paper's sections on coordinated withdrawal and nonlinear benefits do not state these stochastic laws. The financeable-capacity identity here is an acknowledged application of its theorem, not an independently new result.

Shang (2022) studies the branch-weight sequence of individual tree vertices, which supplies relevant background on deletion profiles but not the claimed all-survivor-count mean degeneracy or convex-order risk classification. General site-percolation theory and convex-order tools predate this work; the new claim is the exact combination of the structural family, full reliability mean degeneracy, and sharp risk ordering in the connected-public-good setting.

## Limitations

This is a family-specific theorem, not a universal comparison of arbitrary networks. Failure events are independent and homogeneous only in the Bernoulli version; neither contagion nor targeted attack is modeled. The result does not identify a uniquely optimal financial allocation or establish equilibrium selection under failures. Searches of accessible primary literature and research records cannot exclude unindexed equivalent reliability theorems. The scientific assessment is same-model only; independent audit has not yet been performed.

## References

1. M. T. Angulo, *Who Pays for a Connected Public Good?*, first submitted August 27, 2026, arXiv:2609.10565. https://arxiv.org/abs/2609.10565
2. J.-L. Shang, *Branch-Weight Unique Trees*, Discussiones Mathematicae Graph Theory 42 (2022), 405–416. https://doi.org/10.7151/dmgt.2264
3. D. S. Callaway, M. E. J. Newman, S. H. Strogatz and D. J. Watts, *Network Robustness and Fragility: Percolation on Random Graphs*, Physical Review Letters 85 (2000), 5468–5471. https://doi.org/10.1103/PhysRevLett.85.5468
4. C. Gu and L. Yuan, *Size distribution of clusters in site-percolation on random recursive tree*, arXiv:2408.12515 (2024). https://arxiv.org/abs/2408.12515
