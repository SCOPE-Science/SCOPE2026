# A second-order-statistic law for leftmost-leaf depth at a fixed leaf count

## Finding
Let \(T_n\) be uniformly distributed over rooted plane (ordered) trees with \(n\) edges, \(n\ge 1\). Let \(L\) be the number of leaves (vertices of outdegree zero), and let \(H\) be the distance in edges from the root to the leftmost leaf in depth-first order. For every \(1\le k\le n\), the conditional distribution of \(H\) given \(L=k\) equals the second-smallest value of a uniform \(k\)-subset of \(\{1,\ldots,n\}\), minus one. For \(k=1\), adjoin a sentinel at \(n+1\) to define the second value, yielding \(H=n\).

For \(2\le k\le n\), explicitly,
\[
\Pr(H=h\mid L=k)=\frac{h\binom{n-h-1}{k-2}}{\binom nk},\qquad 1\le h\le n-k+1.
\]
For \(k=1\), \(H=n\) almost surely. In particular, for all \(1\le k\le n\),
\[
\mathbb E[H\mid L=k]=\frac{2n-k+1}{k+1},\qquad
\operatorname{Var}(H\mid L=k)=\frac{2(k-1)(n+1)(n-k)}{(k+1)^2(k+2)}.
\]
A single coupling simultaneously realizes the conditional laws at \(k=1,\ldots,n\) with \(H^{[1]}\ge H^{[2]}\ge\cdots\ge H^{[n]}\) almost surely. Adjacent distributions are distinct and stochastically decreasing; for \(2\le k<n\), the likelihood ratio is decreasing on its common support.

The same law yields three scaling regimes for a sequence \(k_n\): fixed \(k\ge2\) gives \(H/n\Rightarrow\operatorname{Beta}(2,k-1)\); if \(k_n\to\infty\) and \(k_n/n\to0\), then \((k_n/n)H\Rightarrow\operatorname{Gamma}(2,1)\), parameterized by shape and rate; if \(k_n/n\to\rho\in(0,1)\), then \(H\) converges to the integer law \(\Pr(H=h)=h\rho^2(1-\rho)^{h-1}\), \(h\ge1\).

## Assumptions and scope
The root is distinguished and child order is part of the tree; each of the Catalan-number-many trees with exactly \(n\) edges has equal probability. This is not a statement about uniformly labeled trees or unconditioned Galton–Watson trees. The leftmost leaf is reached by repeatedly choosing the first child in the fixed plane order. Each conditional event \(L=k\) has positive probability for \(1\le k\le n\). All binomial coefficients with an out-of-range lower index are zero. The limiting statements use integer sequences with the stated hypotheses and \(n\to\infty\).

## Proof
**Contour encoding.** The depth-first contour bijection sends a rooted plane tree with \(n\) edges to a Dyck word of semilength \(n\). Each leaf corresponds to a consecutive up-down pair (a peak), and the depth of the leftmost leaf is the length of the initial ascent, or height of the first peak.

**Joint counts.** Let \(C(z,u)\) enumerate Dyck paths by semilength and number of peaks, including the empty path. Its first-return decomposition gives
\[
C=1+zC(C-1+u).
\]
A path whose initial ascent has height \(h\) consists of \(h\) opening steps, a peak, and \(h\) ordered Dyck suffixes; its series is \(z^h u C(z,u)^h\). Put \(W=C-1\); then \(W=z(1+W)(u+W)\). For \(N=n-h\ge1\), Lagrange inversion gives
\[
[z^N u^{k-1}]C^h
=\frac{h}{N}\binom{N}{k-1}\binom{n-1}{k-2}
=\frac{h}{k-1}\binom{n-h-1}{k-2}\binom{n-1}{k-2}.
\]
For \(N=0\) the sole word is \(U^nD^n\) and has one peak. The total number of Dyck paths with \(k\) peaks is the Narayana number \(\frac1n\binom nk\binom n{k-1}\). Dividing the joint counts by this total simplifies to the displayed conditional probability.

**Subset identification and coupling.** If \(S\) is a uniform \(k\)-subset of \(\{1,\ldots,n\}\), its second-smallest element equals \(h+1\) exactly when one of its \(k\) elements lies among the first \(h\) positions, position \(h+1\) is present, and the remaining \(k-2\) lie after position \(h+1\). There are \(h\binom{n-h-1}{k-2}\) such subsets. For \(k=1\), set the second order statistic equal to \(n+1\). Take one uniform permutation of \(\{1,\ldots,n\}\) and let \(S_k\) be the unordered set of its first \(k\) entries. Then \(S_k\subset S_{k+1}\), so its sentinel-extended second-smallest element can only decrease. The conditional random variables are thereby coupled simultaneously. Strict stochastic inequality between consecutive leaf counts follows because some choices of the added element lower the second order statistic with positive probability. For \(2\le k<n\), direct division gives, on the common support,
\[
\frac{\Pr(H=h\mid L=k+1)}{\Pr(H=h\mid L=k)}
=\frac{k+1}{n-k}\frac{n-h-k+1}{k-1},
\]
which decreases with \(h\) (and vanishes beyond the new support).

**Moments and tails.** A uniform \(k\)-subset corresponds bijectively to a uniformly distributed weak composition of \(n-k\) unselected positions into \(k+1\) gaps. If \(G_0,G_1\) are the gaps before the first two chosen positions, \(H=1+G_0+G_1\), with the same identity for the sentinel convention at \(k=1\). Aggregating two cells of this symmetric Dirichlet-multinomial occupancy law yields
\[
\mathbb E(G_0+G_1)=\frac{2(n-k)}{k+1},\quad
\operatorname{Var}(G_0+G_1)=\frac{2(k-1)(n-k)(n+1)}{(k+1)^2(k+2)},
\]
proving the claimed moment formulas. Equivalently, for \(1\le h\le n\), the event \(H\ge h\) means at most one of the \(k\) chosen positions lies in the first \(h\) places, yielding the exact tail
\[
\Pr(H\ge h\mid L=k)=\frac{\binom{n-h}{k}+h\binom{n-h}{k-1}}{\binom nk}.
\]

**Limit laws.** For fixed \(k\ge2\), normalized uniform sample positions converge to the order statistics of \(k\) uniform points on \([0,1]\), giving the Beta limit. When \(k\to\infty\) and \(k/n\to0\), the number of sampled positions among the first \(\lfloor tn/k\rfloor\) positions tends by hypergeometric factorial moments to \(\operatorname{Poisson}(t)\); the event that fewer than two points occur gives the Gamma tail \(e^{-t}(1+t)\). When \(k/n\to\rho\in(0,1)\), the occupancy pattern in any fixed prefix converges to independent Bernoulli trials of success probability \(\rho\), so the second success arrives at \(h+1\) with probability \(h\rho^2(1-\rho)^{h-1}\). The mean bound above establishes tightness and excludes lost mass.

## Verification
Run \(\texttt{python3 verify.py}\) with Python's standard library. It independently enumerates every Dyck path of semilength \(1\) through \(10\), compares exact joint frequencies with the closed formula and Narayana counts, verifies exact mean, variance, and tails, and checks all finite-sample stochastic inequalities in this range. It also enumerates uniform subsets and deterministic permutation couplings on smaller ranges. The stored result is 7,672 exact assertions passed. Analytic arguments, not these finite checks, prove the unrestricted and asymptotic claims.

## Relationship to prior work
Janson's account of simply generated and conditioned Galton–Watson trees establishes the uniform plane-tree model as a canonical probabilistic object. Deutsch's 1998 bijection proves that first-peak height and return count have identical *marginal* distributions, but this marginal identity does not determine height conditional on the total number of peaks. Deutsch's 1999 enumeration studies many refinements of Dyck-path statistics, including peaks and returns; its complete text could not be inspected, so an earlier implicit or explicit form of the joint enumeration remains a specific priority risk. The proposed contribution is the order-statistic interpretation, all-level stochastic coupling, and scaling crossover for the **conditional** first-leaf depth; the underlying Catalan, Narayana and gap-counting identities are classical ingredients rather than independent claims of novelty.

## Limitations
The stochastic coupling compares the *one-dimensional conditional depth distributions*; it does not couple complete trees so that subtrees are nested, nor compare arbitrary other tree statistics. The finite verifier is not an infinite proof. The historical scope of Deutsch's broad 1999 survey/enumeration remains incompletely verified because only bibliographic and abstract materials were accessible. The source dated 2011-12-02 provides a verifiable day-level public timestamp for the probabilistic model; older cited papers have earlier years but their original day-level release dates were not established in this study. Independent scientific and historical-priority assessment has not been performed.

## References
- S. Janson, *Simply generated trees, conditioned Galton–Watson trees, random allocations and condensation*, arXiv:1112.0510v1, first posted 2011-12-02, https://arxiv.org/abs/1112.0510.
- E. Deutsch, *A bijection on Dyck paths and its consequences*, Discrete Mathematics 179 (1998), 253–256, DOI 10.1016/S0012-365X(97)00097-6.
- E. Deutsch, *Dyck path enumeration*, Discrete Mathematics 204 (1999), 167–202, DOI 10.1016/S0012-365X(98)00371-9 (full-text comparison unresolved).
