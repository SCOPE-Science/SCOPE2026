# Leaf-twin bias induces strict likelihood-ratio ordering in uniform labeled trees

## Finding

For every integer \(n\ge4\), a uniformly random labeled tree on \(n\) vertices has a strictly increasing expected number of leaf-twin pairs conditional on the number of leaves. More precisely, if \(L\) is the number of leaves, \(C\) the number of unordered pairs of leaves with a common neighbor, and \(S(a,b)\) the Stirling numbers of the second kind, then

\[
\mathbb E[C\mid L=\ell]=\binom{\ell}{2}\frac{S(n-3,n-\ell)}{S(n-2,n-\ell)},\qquad 2\le\ell\le n-1.
\]

The right-hand side increases **strictly** for consecutive integer values of \(\ell\) on its full support. The size-biased tree has an exact *Palm construction*: choose two unordered distinct labels, draw a uniform Cayley tree on the other \(n-2\) labels, choose an independent uniform attachment vertex of that smaller tree, and attach both selected labels as leaves to it. Equivalently, under cherry bias, \(L-2\) is the number of empty boxes after \(n-3\) independent uniform balls are placed into \(n-2\) boxes, so its exact law is

\[
\mathbb P^*\{L=\ell\}=\frac{\binom{n-2}{\ell-2}(n-\ell)!S(n-3,n-\ell)}{(n-2)^{n-3}},\qquad3\le\ell\le n-1.
\]

Therefore weighting each tree by its number of leaf-twin pairs produces a leaf-count distribution strictly larger in monotone likelihood-ratio order. In particular, \(\operatorname{Cov}(C,L)>0\), and more generally \(\operatorname{Cov}(C,f(L))>0\) for every nonconstant nondecreasing \(f\) on the possible leaf counts.

## Assumptions and scope

Trees are simple, unrooted, labeled by \(\{1,\dots,n\}\), and uniformly distributed among the \(n^{n-2}\) Cayley trees. A leaf has graph degree one. A **leaf-twin pair** or **cherry** is an *unordered* pair of distinct leaves with the same neighbor; the common neighbor may have any degree at least three. Write \(b_v\) for the number of leaf neighbors of vertex \(v\), so \(C=\sum_v\binom{b_v}{2}\). Each such pair supports an automorphism interchanging its two leaves and fixing the remaining vertices. For clarity, this is the unrestricted cherry definition of Erdős and Rényi, not the more restrictive degree-three-center definition used in some later literature.

Let \(S(a,b)\) count set partitions of \(a\) labeled objects into \(b\) nonempty unlabeled blocks, with \(S(a,b)=0\) for \(b>a\) or \(b<0\). The leaf count can take precisely \(\ell=2,\ldots,n-1\). The \(C\)-size-biased law \(\mathbb P^*\) is defined by \(\mathbb P^*(T=t)=C(t)\mathbb P(T=t)/\mathbb E C\), and is well-defined because \(\mathbb E C>0\).

## Proof

**1. Degree-prescribed count.** Given a prescribed degree sequence \(d_1,\ldots,d_n\) of a labeled tree, put \(t_v=d_v-1\), so \(\sum_v t_v=N=n-2\). Prüfer's bijection counts the trees with this sequence by \(N!/\prod_v t_v!\). Its leaves are precisely those vertices with \(t_v=0\). Fix two distinct such leaves \(a,b\), and a proposed common neighbor \(v\), necessarily distinct from \(a,b\). Removing \(a,b\) yields a tree on \(n-2\ge2\) vertices with adjusted degree \(d_v-2\) at \(v\) and all other degrees unchanged. Conversely, attaching the two fixed leaves to \(v\) reverses this operation. For \(t_v\ge2\), the number of such trees equals \((N-2)!/((t_v-2)!\prod_{w\ne v}t_w!)\), where the product is taken over the remaining vertices; it is zero when \(t_v<2\). Thus

\[
\mathbb P\{a,b\text{ have neighbor }v\mid(d_w)_w\}=\frac{t_v(t_v-1)}{N(N-1)}.
\]

Summing over possible centers and the \(\binom{\ell}{2}\) pairs of leaves gives

\[
\mathbb E[C\mid(d_w)_w]=\binom{\ell}{2}\frac{\sum_v t_v(t_v-1)}{N(N-1)}.\tag{1}
\]

**2. Surjective Prüfer words.** Conditional on \(L=\ell\), a uniform Prüfer word has exactly \(k=n-\ell\) distinct symbols among its \(N=n-2\) positions. The occupied alphabet is uniform among the \(k\)-subsets; conditional on it, the word is uniformly surjective. There are \(k!S(N,k)\) such words. For two fixed distinct positions, the words in which their symbols agree are in bijection with surjective length-\(N-1\) words, obtained by merging the two positions. Their count is \(k!S(N-1,k)\). Therefore

\[
\mathbb E\left[\sum_v t_v(t_v-1)\mid L=\ell\right]
=N(N-1)\frac{S(N-1,k)}{S(N,k)}.\tag{2}
\]

Combining (1) and (2) proves the conditional regression formula, including \(\ell=2\) where its numerator vanishes.

**3. Strict Stirling-ratio monotonicity.** For each integer \(m\ge1\), the Stirling polynomial \(B_m(z)=\sum_{j=0}^{m}S(m,j)z^j\) has only real, simple, nonpositive zeros. Here is a short induction: \(B_1(z)=z\), while the Stirling recurrence gives \(B_{m+1}(z)=z(B_m(z)+B'_m(z))\). If \(B_m\) has \(m\) distinct nonpositive zeros, then the derivative of \(e^z B_m(z)\) has a zero between each adjacent pair and a further zero to the left of its smallest zero, since \(e^zB_m(z)\) tends to zero as \(z\to-\infty\). These \(m\) zeros of \(B_m+B'_m\) are distinct and negative. Multiplication by \(z\) completes the induction. By Newton's inequalities, the nonzero coefficients \(S(m,j)\) are log-concave in \(j\), so \(S(m,j-1)/S(m,j)\) is nondecreasing for admissible positive denominators.

For fixed \(N\ge2\), write \(r_k=S(N-1,k)/S(N,k)\), for \(1\le k\le N\). The endpoint is \(r_N=0\), and for \(1\le k<N\), the Stirling recurrence gives

\[
\frac1{r_k}=k+\frac{S(N-1,k-1)}{S(N-1,k)}.
\]

The first summand strictly increases with \(k\), and the second is nondecreasing, so \(r_k\) strictly decreases in \(k\), including the zero endpoint. As \(\ell\) increases, \(k=n-\ell\) decreases. Thus both the positive combinatorial factor \(\binom{\ell}{2}\) and the nonnegative Stirling ratio increase, with the ratio strictly increasing. The product is strictly increasing from zero at \(\ell=2\) to \(\binom{n-1}{2}\) at \(\ell=n-1\).

**4. Likelihood-ratio and covariance consequences.** Every \(2\le\ell\le n-1\) has positive probability, since a surjective word exists for each possible occupied-alphabet size. Writing \(g_n(\ell)=\mathbb E[C\mid L=\ell]\), Bayes' rule gives

\[
\frac{\mathbb P^*\{L=\ell\}}{\mathbb P\{L=\ell\}}
=\frac{g_n(\ell)}{\mathbb E C},
\]

which is strictly increasing by Step 3. Hence the biased law dominates in likelihood-ratio order and therefore in first-order stochastic order, strictly at every nontrivial upper threshold. For any nonconstant nondecreasing function \(f\) on the support,

\[
\operatorname{Cov}(C,f(L))
=\operatorname{Cov}(g_n(L),f(L))
=\frac12\mathbb E[(g_n(L)-g_n(L'))(f(L)-f(L'))]>0,
\]

where \(L'\) is an independent copy; the final inequality uses strict increase of \(g_n\) and full support of \(L\). This concludes the proof.

**5. Exact cherry-Palm construction.** The trees with a *marked unordered cherry* are in one-to-one correspondence with a choice of two labels \(\{a,b\}\), a Cayley tree \(R\) on the other \(m=n-2\) labels, and one distinguished vertex \(v\) of \(R\): attach \(a,b\) to \(v\) and mark their pair. Thus choosing uniformly among marked cherries is exactly the sampling scheme described in the Finding, and its unmarked tree has the \(C\)-size-biased law. This immediately gives the classical unconditional normalizing constant \(\mathbb E C=\binom n2m^{m-1}/n^{n-2}\). If \(W\) is the uniformly random Prüfer word of \(R\) of length \(m-2\) and \(v\) is an independent uniform vertex, then \(L(T)=2+\#\{x\in[m]:x\text{ is absent from }(W,v)\}\): the two added vertices become leaves, and the center \(v\) loses leaf status precisely when it was absent from \(W\). Since \((W,v)\) is an iid uniform word of length \(m-1\), the exact occupancy distribution yields

\[
\mathbb P^*\{L=\ell\}
=\frac{\binom m{\ell-2}(m-(\ell-2))!S(m-1,m-(\ell-2))}{m^{m-1}}
=\frac{\binom{n-2}{\ell-2}(n-\ell)!S(n-3,n-\ell)}{(n-2)^{n-3}},
\]

for \(3\le\ell\le n-1\). This exact structural identity is a second representation of the same leaf-twin size-bias finding, not an assumption or a separate unrelated theorem.

## Verification

The complete script `verify.py` uses only the Python 3 standard library. Execute `python verify.py` after extracting this finding's files. It enumerates all Prüfer codes for \(4\le n\le8\), checks every leaf stratum using exact rational arithmetic, and checks strict increase for every \(4\le n\le100\). It reports 280,388 fully enumerated labeled trees and 4,850 finite strict-ratio checks. These are finite corroborations; the proof of the all-\(n\) claim is analytic and combinatorial.

As an independent consistency check, direct counting of the common neighbor of a *fixed* unordered leaf pair gives the known unconditional mean

\[
\mathbb E C=\binom n2\frac{(n-2)^{n-3}}{n^{n-2}},\qquad n\ge4.
\]

The unconditional mean and the classical leaf marginal are established older results, not originality claims here.

## Relationship to prior work

Rényi (1959, §2, formula (2.1)) enumerates the leaf count in uniform labeled trees using Stirling numbers. Erdős and Rényi (1963, §5, Theorem 6 and formulas (5.1)–(5.3)) define the same unrestricted cherry statistic and derive unconditional cherry moments and high-probability existence. Pitman (1997, Theorem 6) reviews classical labeled forest degree-profile enumerations. These establish key ingredients but the inspected statements do not give the conditional regression \(\mathbb E[C\mid L=\ell]\), its strict monotonicity, or the induced likelihood-ratio ordering. A later study of tree symmetries uses a narrower degree-three-center cherry definition, so its statistic is not interchangeable with the one used here.

## Limitations

The claim concerns **uniform labeled Cayley trees only**, with \(n\ge4\), and counts all leaf-twin pairs even when a center has more than two leaf neighbors. The proof does not apply automatically to uniformly random unlabelled, plane, recursive, conditioned Galton–Watson, or phylogenetic binary trees. It establishes a one-dimensional likelihood-ratio order under \(C\)-bias, not a joint positive-association theorem for arbitrary tree observables. Earlier general counting identities might contain an implicit equivalent of the displayed conditional formula; an exhaustive historical novelty guarantee is not claimed, and independent audit has not been performed.

## References

1. A. Rényi, “Some Remarks on the Theory of Trees” (1959), §2, esp. (2.1). https://real.mtak.hu/200905/1/cut_MATKUTINT_4_1_1959_pp73_-_85.pdf
2. P. Erdős and A. Rényi, “Asymmetric Graphs” (1963), *Acta Math. Acad. Sci. Hung.* 14, 295–315, §5. https://doi.org/10.1007/BF01895716 ; accessible full text: https://static.renyi.hu/renyi_cikkek/1962_asymmetric_graphs.pdf
3. J. Pitman, “Enumerations of Trees and Forests Related to Branching Processes and Random Walks” (1997), Technical Report 482, Theorem 6. https://statistics.berkeley.edu/sites/default/files/tech-reports/482.pdf
4. “Almost all trees have quantum symmetry” (2020), §3 and Definition 3.1 (a different restrictive cherry convention). https://link.springer.com/article/10.1007/s00013-020-01476-x
