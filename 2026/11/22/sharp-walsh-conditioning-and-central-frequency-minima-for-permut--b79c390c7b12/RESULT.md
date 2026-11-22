# Sharp Walsh conditioning and central-frequency minima for permutation two-cycle supports

## Finding
For every integer \(n\ge 1\), let \(\sigma\) range uniformly over the symmetric group \(S_n\). Define \(J(\sigma)\subseteq[n]\) to be the union of the vertices in the cycles of length exactly two in its disjoint-cycle decomposition. Let \(p_n(x)\) be the probability that the incidence vector of \(J(\sigma)\) equals \(x\in G_n=(\mathbb Z/2\mathbb Z)^n\). Let \(P_n f=p_n*f\) on \(\ell^2(G_n)\), with counting-measure convolution.

For \(A\subseteq[n]\), write \(k=|A|\) and \(\chi_A(x)=(-1)^{\sum_{i\in A}x_i}\). The Walsh multiplier of \(P_n\) at \(\chi_A\) is \(\theta_{n,k}=\Lambda_{n,k}/n!\), where
\[
\Lambda_{n,k}=k!(n-k)!\sum_{j=0}^{\min(k,n-k)}\frac{(-2)^j}{j!}\binom{n-2j}{k-j}.
\]

The complete invertibility, strict central-minimum, and stability conclusions are:

1. \(P_2\) is singular, with its two weight-one Walsh eigenvalues equal to zero. Every \(P_n\) with \(n\ne2\) is strictly positive definite (including \(n=1\)).
2. For every \(n\ge6\), \(\Lambda_{n,0}>\Lambda_{n,1}>\cdots>\Lambda_{n,\lfloor n/2\rfloor}>0\), and \(\Lambda_{n,k}=\Lambda_{n,n-k}\). Thus the minimal eigenvalues occur **exactly** at the central weight(s). For \(n=3,4,5\), the minimal unnormalized eigenvalues are respectively \(2,12,72\); the exceptional order-four minimum is at weights one and three.
3. Writing \(m=\lfloor n/2\rfloor\), for \(n\ge6\) the exact Euclidean condition number is \(\kappa_2(P_n)=n!/\Lambda_{n,m}\). At orders \(3,4,5\) the respective values are \(3,2,5/3\). Consequently \(\sup_{n\ge3}\kappa_2(P_n)=3\), sharply attained at \(n=3\), and \(\lim_{n\to\infty}\kappa_2(P_n)=e^{1/2}\).
4. If \(k_n/n\to\alpha\in[0,1]\), then \(\theta_{n,k_n}\to\exp(-2\alpha(1-\alpha))\). Consequently the empirical probability measure of all \(2^n\) Walsh eigenvalues of \(P_n\) converges weakly to the point mass at \(e^{-1/2}\). This is a bulk spectral statement; the constant Walsh eigenvalue remains one at every order.

## Assumptions and scope
The underlying permutations are **all** labelled permutations, without restrictions and without Ewens reweighting. A two-cycle means a cycle of **exact length two in the final permutation**, not an arbitrary transposition in a factorization. The incidence vector records only the endpoints of those cycles and not their pairing. All formulas use the probability kernel \(p_n\); multiplying the convolution kernel by \(n!\) gives the integer counting version. At \(n=2\), \(\kappa_2\) is not defined because of singularity.

## Proof

**Signed cycle enumeration.** Split the vertex labels into \(A\), of cardinality \(k\), and its complement, of cardinality \(n-k\). A two-cycle with one vertex of each colour contributes sign \(-1\) to \(\chi_A(J(\sigma))\); every other cycle contributes sign \(+1\). If the two sorts of labels are marked by formal variables \(u,v\), the ordinary two-sort exponential generating function, with the usual labelled factorial denominators, is
\[
F(u,v)=\exp(-2uv)\exp\!\left(\sum_{r\ge1}\frac{(u+v)^r}{r}\right)
=\frac{\exp(-2uv)}{1-u-v}.
\]
The factor \(\exp(-2uv)\) changes the cross-colour two-cycle weight from \(+uv\) to \(-uv\) while leaving all other cycle types unchanged. Coefficient extraction gives \(\Lambda_{n,k}=k!(n-k)![u^kv^{n-k}]F\), which expands to the displayed formula. Symmetry under swapping colours gives \(\Lambda_{n,k}=\Lambda_{n,n-k}\). The row at weight zero is \(\Lambda_{n,0}=n!\).

**Strict positivity and a sharp dimension-free bound.** Let \(X\) count the two-cycles of \(\sigma\) crossing from \(A\) to \(A^c\). Then \(\theta_{n,k}=\mathbb E(-1)^X=1-2\Pr(X\text{ odd})\). Each specified unordered cross pair forms a two-cycle with probability \(1/[n(n-1)]\), so \(\mathbb E X=k(n-k)/[n(n-1)]\). For \(n\ge4\),
\[
\theta_{n,k}\ge1-2\mathbb EX\ge 1-\frac{n}{2(n-1)}=\frac{n-2}{2(n-1)}\ge\frac13.
\]
For \(n=3\), a crossing two-cycle is unique if present and the weight-one and weight-two frequencies have multiplier \(1/3\); the zero and full weights have multiplier one. At \(n=2\) the weight-one multipliers vanish, whereas \(n=1\) has only unit multipliers. Thus positive definiteness holds exactly as claimed. Since \(|\theta_{n,k}|\le1\) and the constant multiplier is one, the bound gives \(\kappa_2(P_n)\le3\) for all \(n\ge3\), with equality at \(n=3\).

**Coefficient-unimodality lemma (the nontrivial finite-order step).** Define \(q_{n,k}=[u^kv^{n-k}]F\), extending it by zero when \(k<0\) or \(k>n\), and put \(D_{n,k}=q_{n,k}-q_{n,k-1}\). The identity \((1-u-v)F=\exp(-2uv)\) yields
\[
q_{n,k}=q_{n-1,k}+q_{n-1,k-1}+\mathbf1_{n=2j,\ k=j}\frac{(-2)^j}{j!}.
\]
The coefficients are symmetric in their two indices, so \(D_{2j-1,j}=0\). Directly from the recurrence, the rows for orders four, five and six begin (up to symmetry) as
\[
(q_{4,0},q_{4,1},q_{4,2})=(1,2,4),\quad
(q_{5,0},q_{5,1},q_{5,2})=(1,3,6),\quad
(q_{6,0},q_{6,1},q_{6,2},q_{6,3})=(1,4,9,32/3).
\]
Hence \(D_{n,k}\ge2/3\) for \(4\le n\le6\) and \(1\le k\le\lfloor n/2\rfloor\). Inductively, for any noncentral entry, or for an odd row, \(D_{n,k}=D_{n-1,k}+D_{n-1,k-1}\), with \(D_{n-1,0}=1\); the bound is preserved. At the central index \(j=n/2\) of an even row \(n=2j\ge8\), symmetry and the preceding odd row give
\[
D_{2j,j}=D_{2j-1,j-1}+\frac{(-2)^j}{j!}
=D_{2j-2,j-1}+D_{2j-2,j-2}+\frac{(-2)^j}{j!}.
\]
The first two terms are each at least \(2/3\), while \(2^j/j!\le2/3\) for every \(j\ge4\). Thus \(D_{2j,j}\ge2/3\) too, completing the induction. In particular, \(q_{n,k}\) strictly increases in \(k\) up to the centre for every \(n\ge4\).

**Passage from coefficient unimodality to the sharp Fourier minimum.** Fix a character \(A\) of weight \(k<n\) and add one vertex from the complement to it. The difference between the signed permutation sums is twice the signed sum over permutations in which that vertex belongs to a two-cycle. Pairing it with a vertex outside \(A\), or inside \(A\), and deleting the two-cycle gives
\[
\Lambda_{n,k}-\Lambda_{n,k+1}
=2\left((n-k-1)\Lambda_{n-2,k}-k\Lambda_{n-2,k-1}\right)
=2k!(n-k-1)!D_{n-2,k}.
\]
For \(n\ge6\) and \(0\le k<\lfloor n/2\rfloor\), the last expression is strictly positive (take \(D_{m,0}=1\)). Symmetry then locates all minimizers at central weight. The order-three through order-five values follow from direct cycle enumeration. The preceding positivity bound makes the resulting ratios legitimate Euclidean condition numbers.

**Poisson-scale Fourier limit and bulk spectral concentration.** The exact falling-factorial moments of crossing two-cycles are
\[
\mathbb E(X)_{\underline r}=\frac{(k)_{\underline r}(n-k)_{\underline r}}{(n)_{\underline{2r}}},
\qquad 0\le r\le\min(k,n-k),
\]
with value zero when \(r>\min(k,n-k)\). Here \((a)_{\underline r}\) denotes a falling factorial. Since \((-1)^X=(1-2)^X\),
\[
\theta_{n,k}=\sum_{r\ge0}\frac{(-2)^r}{r!}\frac{(k)_{\underline r}(n-k)_{\underline r}}{(n)_{\underline{2r}}}.
\]
Each moment ratio is between zero and one; hence the series is uniformly dominated by \(\sum_{r\ge0}2^r/r!=e^2\). If \(k/n\to\alpha\), the individual ratios converge to \([\alpha(1-\alpha)]^r\); dominated convergence gives the announced exponential limit. The same compactness argument makes convergence uniform over all weights when the limiting expression uses \(\alpha=k/n\). Evaluating at the proven central minimizer gives \(\kappa_2(P_n)\to e^{1/2}\). Finally, under uniform sampling of all Walsh characters, \(k\sim\operatorname{Binomial}(n,1/2)\), so \(k/n\to1/2\) in probability. Uniform convergence of multipliers then proves empirical spectral concentration at \(e^{-1/2}\).

## Verification
The accompanying standalone `checker.py` constructs every permutation and its two-cycle-support incidence vector for orders one through eight and independently computes the complete Walsh transforms. It compares the results against the closed formula. Separately, it computes the two-sort coefficient table through order 100 by the recurrence, verifies every coefficient against the exact factorial formula, verifies all centre-difference inequalities and tests the singularity and minimum claims. All assertions use integer or rational arithmetic. The finite tests corroborate, but do not replace, the all-order arguments above.

## Relationship to prior work
The decomposition of permutations into labelled cycles and the exponential generating function for marked short cycles are classical; see Flajolet and Sedgewick, chapters II and III. Ford's work gives broad exact and asymptotic facts about uncoloured random permutation cycle counts, including Poisson limits. The signed two-sort generating function above is a direct specialization of the classical cycle-index formalism and is **not** itself asserted to be new. The assessed contribution is the all-order sign classification, the strict shell-minimum theorem, exact finite-dimensional recovery condition numbers and their sharp uniform maximum, and the corresponding high-dimensional spectral conclusion. Classical fixed-point statistics address cycles of length one, not the endpoint union of length-two cycles.

## Limitations
The construction concerns **two-cycle vertex supports** only and uniform permutations only. It does not claim a similar monotonicity law for three-cycle supports, Ewens-weighted permutations, arbitrary finite groups or non-Euclidean inverse operator norms. The comparison with the literature is bounded, and exact priority against all equivalent weighted-cycle-index specializations is not certified. The empirical spectral concentration is in distribution, not convergence of \(P_n\) to a scalar in operator norm: the constant character always has eigenvalue one.

## References
- P. Flajolet and R. Sedgewick, *Analytic Combinatorics*, Cambridge University Press, 2009, particularly the cycle-construction rules and marked-permutation-cycle generating functions in Chapters II–III. Public electronic edition announced 26 June 2009: https://algo.inria.fr/flajolet/Publications/AnaCombi/anacombi.html .
- K. Ford, *Cycle type of random permutations: A toolkit*, arXiv:2104.12019 (submitted 24 April 2021), especially sections 1–3 on cycle counts and factorial moments: https://arxiv.org/abs/2104.12019 .
- P. Diaconis, J. Fulman and R. Guralnick, *On fixed points of permutations*, arXiv:0708.2643 (submitted 20 August 2007); nearby but different statistics: https://arxiv.org/html/0708.2643v1 .
