# Bipartition balancing orders rooted-forest component counts in likelihood ratio

## Finding
Fix an integer \(N\ge 4\), a root fugacity \(q>0\), and positive integers \(a,b\) with \(a+b=N\) and \(b-a\ge2\). Let \(K_{a,b}\) be the complete bipartite graph with the stated part sizes. Give every *rooted spanning forest* \(F\) probability proportional to \(q^{r(F)}\), where \(r(F)\) is the number of components (equivalently the number of distinguished roots). Let \(R_{a,b;q}\) denote its number of components.

Then the root-count law on the more unbalanced graph dominates the one-step-balanced law **in monotone likelihood-ratio order**:
\[
\Pr(R_{a,b;q}=k+1)\Pr(R_{a+1,b-1;q}=k)
\ge \Pr(R_{a,b;q}=k)\Pr(R_{a+1,b-1;q}=k+1)
\quad(1\le k<N).
\]
In particular, there is *strict* first-order stochastic domination at every nontrivial threshold:
\[
\Pr(R_{a,b;q}\ge k)>\Pr(R_{a+1,b-1;q}\ge k)
\quad(2\le k\le N).
\]
Thus, at fixed vertex number and every fixed \(q>0\), the star uniquely maximizes and the maximally balanced complete bipartite graph uniquely minimizes the root-count law in both orders (up to interchanging the parts). The complete finite law is
\[
R_{a,b;q}\ \overset{d}=\ 1+ B_N+
\sum_{j=1}^{b-1}H_j+\sum_{j=1}^{a-1}L_j,
\]
where all Bernoulli variables are independent and
\[
\Pr(B_N=1)=\frac q{q+N},\qquad
\Pr(H_j=1)=\frac q{q+a},\qquad
\Pr(L_j=1)=\frac q{q+b}.
\]
The strict mean gap for one balancing move is
\[
\mathbb E R_{a,b;q}-\mathbb E R_{a+1,b-1;q}
=\frac{q(b-a-1)(N+2q)(N+q-1)}{(a+q)(b+q)(a+q+1)(b+q-1)}>0.
\]

## Assumptions and scope
Forests are spanning, acyclic undirected subgraphs with one distinguished root in each connected component. All original graph edges have unit weight. Equivalently, an unrooted forest carries mass proportional to \(q^{r(F)}\prod_{C}|C|\), one factor of component size for its possible root. The only random variable being compared is its *number of roots*, not its edge set or complete partition. The conclusion covers all real \(q>0\) and all admissible finite bipartitions, including the star and near-balanced boundaries; it does not claim a graph-level coupling or an ordering for arbitrary non-complete graphs.

For distributions \(X,Y\) supported on the same finite consecutive integers with positive probabilities, \(X\ge_{\mathrm{lr}}Y\) means \(\Pr(X=k)/\Pr(Y=k)\) is nondecreasing in \(k\). This entails ordinary stochastic domination, but the converse is false in general.

## Proof
**1. Exact law from the rooted matrix-forest identity.** The rooted-forest partition function for a finite undirected graph with Laplacian \(L\) is \(Z_G(q)=\det(qI+L)\). The Laplacian spectrum of \(K_{a,b}\) is \(0\) once, \(N\) once, \(a\) with multiplicity \(b-1\), and \(b\) with multiplicity \(a-1\): the sum-zero subspaces within the two parts give the repeated eigenvalues, and the remaining two-dimensional part-constant subspace gives \(0,N\). Consequently,
\[
Z_{a,b}(q)=q(q+N)(q+a)^{b-1}(q+b)^{a-1},
\quad \mathbb E[z^{R_{a,b;q}}]=\frac{Z_{a,b}(qz)}{Z_{a,b}(q)}.
\]
Factoring this probability-generating function gives the independent Bernoulli representation above and full support \(\{1,\ldots,N\}\).

**2. A likelihood-ratio comparison for one complementary Bernoulli pair.** Set
\[
h=\frac q{q+a},\quad \ell=\frac q{q+b},\quad
h'=\frac q{q+a+1},\quad\ell'=\frac q{q+b-1}.
\]
A sum of independent Bernoulli variables with parameters \(h,\ell\) has probabilities in degrees \(0,1,2\) proportional to
\[
(ab,\ qN,\ q^2).
\]
For the pair with parameters \(h',\ell'\), the corresponding probabilities are proportional to
\[
((a+1)(b-1),\ qN,\ q^2).
\]
Because \((a+1)(b-1)=ab+b-a-1>ab\), the old-to-new probability ratios are strictly smaller at degree zero than at degrees one and two (where the ratios agree). Thus \(\operatorname{Bern}(h)+\operatorname{Bern}(\ell)\ge_{\mathrm{lr}}\operatorname{Bern}(h')+\operatorname{Bern}(\ell')\). Also \(h>h'\) and \(h>\ell'\), so each corresponding single Bernoulli comparison is strictly ordered in likelihood ratio.

**3. Match every factor.** Disregard the common \(1+B_N\) temporarily. Match \(a-1\) independent old pairs with parameters \((h,\ell)\) to \(a-1\) new pairs \((h',\ell')\). There remain \(b-a\) old variables with parameter \(h\), compared with \(b-a-1\) new variables of parameter \(h'\) and one of parameter \(\ell'\). Pair these singly, using \(h>h'\) and \(h>\ell'\). This matches every independent factor once.

**4. Convolution preserves likelihood-ratio order here.** If \(U\ge_{\mathrm{lr}}V\) and \(W\) is independent with a log-concave probability mass function and interval support, then \(U+W\ge_{\mathrm{lr}}V+W\). Indeed, the Toeplitz kernel \(T(k,i)=\Pr(W=k-i)\) is totally positive of order two by log-concavity; multiplying a two-row likelihood-ratio-ordered matrix by this kernel preserves nonnegative \(2\times2\) minors. Equivalently, expand the determinant of the two convolved mass sequences and pair summands with indices \(i>j\): both the original likelihood-ratio minors and the Toeplitz minors are nonnegative. Independent sums of Bernoulli variables, including each two-Bernoulli pair, have log-concave mass functions because their generating polynomials have only real nonpositive zeros. Changing one matched factor at a time, holding the rest of the sum fixed, therefore proves the stated likelihood-ratio order; adding the common \(1+B_N\) preserves it as well.

**5. Strict tails and mean.** In the matching in Step 3 at least one single Bernoulli parameter decreases strictly (in fact all remaining single pairs decrease), while all other replacements are stochastically non-increasing. Keeping the other summands fixed in that single replacement, their distribution has positive mass at every integer in its support, so the upper-tail inequality is strict for every threshold \(2,\ldots,N\). The mean follows by summing the independent Bernoulli means and simplifying the difference. Chaining all admissible balancing moves proves the unique extremizers.

## Verification
Run `python3 verify.py` from the directory containing the attached file. The checker enumerates every acyclic spanning subgraph and its root choices for all complete bipartite graphs of total order at most eight, reproducing the spectral partition coefficients. It then verifies the independent Bernoulli factorization, all adjacent likelihood-ratio inequalities, strict upper tails, and the exact mean gap for all total orders from four through thirty-one and five positive rational fugacities. Recorded output: `VERIFY_OK 46928 exact rational checks`. These finite checks corroborate, but do not replace, the all-parameter proof above.

## Relationship to prior work
The rooted matrix-forest theorem and Bernoulli eigenvalue law are established general background, explicitly appearing in Avena, Driessen and Koperberg (2021), equations (1.2), (1.5) and the discussion after (1.7). Their monotonicity concerns changing fugacity at fixed graph, not balancing graph bipartitions. Székely (2004), building on Jin and Liu, enumerates rooted forests on complete multipartite graphs with prescribed root counts in each class; summing those formulas gives input enumeration, but the inspected full paper does not state the likelihood-ratio comparison of root-count distributions across bipartitions. Wang, Zhang and Zhu (2017) concern asymptotic normality and Poisson behavior of Laplacian coefficient sequences, not finite all-fugacity ordering. D'Achille, Enriquez and Melotti (2026) study exact local structure on complete graphs rather than cross-bipartition ordering on complete bipartite graphs. The contribution asserted here is the **likelihood-ratio balancing order**, not the classical spectral factorization or counting formulas.

## Limitations
This is a same-author mathematical proof and computational cross-check, not an independent audit or historical-priority certification. Earlier enumeration formulas could in principle be combined with standard total-positivity facts to yield the ordering, and an unlocated historical statement remains possible. The theorem concerns the rooted (component-size-weighted) forest measure; it is not proved for the uniform *unrooted* forest. It does not order component sizes, partitions, or individual edge indicators and does not extend automatically to other graph families. The case \(q=0\) is excluded; its weak limit is a spanning tree with exactly one component and therefore has no strict comparison.

## References
- L. Avena, J. Driessen, T. Koperberg, *Loop-erased partitioning of a network: monotonicities & analysis of cycle-free graphs*, arXiv:2103.14436, initially public 2021-03-26. https://arxiv.org/html/2103.14436v2
- L. A. Székely, *Counting rooted spanning forests in complete multipartite graphs*, Ars Combinatoria **73** (2004), 97–100. https://combinatorialpress.com/article/ars/Volume%20073/volume-73-paper-11.pdf
- Y. Wang, H. Zhang, B. Zhu, *Asymptotic normality of Laplacian coefficients of graphs*, arXiv:1709.03407, initially public 2017-09-11. https://arxiv.org/abs/1709.03407
- M. D'Achille, N. Enriquez, P. Melotti, *Massive Spanning Forests on the Complete Graph: Exact Distribution and Local Limit*, Random Structures & Algorithms (2026). https://doi.org/10.1002/rsa.70048
