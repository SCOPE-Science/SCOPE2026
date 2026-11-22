# A parity-plateau law for path variation under local symmetric Markov filters

## Finding
For integers \(n\ge 2\) and \(r\ge1\), let \(\mathcal S_{n,r}\) be the class of real \(n\times n\) matrices \(K\) with \(K_{ij}\ge0\), \(K=K^{\mathsf T}\), \(K\mathbf1=\mathbf1\), and \(K_{ij}=0\) when \(|i-j|>r\). Write \(V(x)=\sum_{i=1}^{n-1}|x_{i+1}-x_i|\). The **attained sharp uniform operator seminorm** is
\[
\sup_{K\in\mathcal S_{n,r}}\sup_{V(x)>0}\frac{V(Kx)}{V(x)}
=\min\!\left\{n-1,\,4\left\lceil\frac r2\right\rceil-1\right\}.
\]
Every sharp value is attained by an explicit symmetric banded permutation matrix (an involution). In particular, increasing the bandwidth from any odd \(r\) to \(r+1\) does not increase the worst possible variation amplification, whereas increasing it from an even bandwidth to the next odd bandwidth raises the unconstrained-size maximum by four.

## Assumptions and scope
Indices are \(0,\dots,n-1\); bandwidth is in the ordinary index distance (not cyclic distance). Variation is the **open-path** first-difference seminorm. Matrices are entrywise nonnegative and row-stochastic, hence also column-stochastic by symmetry. No positive-semidefiniteness, irreducibility, strict positivity of allowed entries, monotonicity or translation invariance is assumed. The supremum is over both the matrix and all real nonconstant input vectors. Matrix symmetry is essential for the parity-plateau statement; unrestricted banded doubly-stochastic matrices have a different extremal profile.

## Proof
**1. Reduction to a unit step.** Since \(K\mathbf1=\mathbf1\), the decomposition \(x=x_0\mathbf1+\sum_{m=1}^{n-1}(x_m-x_{m-1})h_m\), with \((h_m)_i=\mathbf1_{\{i\ge m\}}\), gives \(V(Kx)\le\big(\max_m V(Kh_m)\big)V(x)\). Conversely any \(h_m\) has variation one. We may replace \(h_m\) by the complementary prefix indicator \(u_m=\mathbf1_{\{i<m\}}\), since \(Ku_m=\mathbf1-Kh_m\), preserving variation.

**2. Integral cross-boundary reduction.** Fix \(m\) and partition indices into \(A=\{0,\dots,m-1\}\), \(B=\{m,\dots,n-1\}\). Put \(E=(K_{ij})_{i\in A,j\in B}\). The entries of \(Ku_m\) are \(1-\sum_{j\in B}E_{ij}\) for \(i\in A\) and \(\sum_{i\in A}E_{ij}\) for \(j\in B\). Thus the output depends only on \(E\), whose entries are nonnegative, vanish if \(j-i>r\), and whose row and column sums are at most one. Conversely any such \(E\) extends to a matrix in \(\mathcal S_{n,r}\): put \(E\) and \(E^{\mathsf T}\) into the off-diagonal blocks and fill the unused row masses on the diagonal. The bipartite matching polytope (nonnegative edge variables with all vertex sums at most one) is integral: its vertices are incidence matrices of matchings, by total unimodularity of a bipartite incidence matrix. Since variation is convex in \(E\), its maximum occurs at a matching vertex. Thus it suffices to inspect disjoint transpositions swapping indices across the cut, with displacement at most \(r\), leaving every other index fixed.

**3. Counting the switched runs.** For such a matching, its binary output equals the prefix \(u_m\) with some positions on the left changed from one to zero (holes), and an equal number of positions on the right changed from zero to one (islands). Every hole and island has distance at most \(r\) from the cut, since it is the endpoint of a cross-cut pair of length at most \(r\). Let \(p\) be the number of maximal consecutive left-hole runs and \(q\) the number of maximal consecutive right-island runs. Let \(e_L\) be one if the left site immediately adjacent to the cut is a hole, and \(e_R\) one if the right adjacent site is an island. Counting transitions within the two sides and at the cut, allowing for missing endpoint transitions, gives
\[
V(Ku_m)\le
\begin{cases}
2(p+q)+1,&e_L=e_R=0,\\
2(p+q)-1,&\text{otherwise}.
\end{cases}
\]
As switched sites on either side lie among the \(r\) nearest cut positions, each side has at most \(\lceil r/2\rceil\) runs; if its adjacent-to-cut site is not switched, it has at most \(\lfloor r/2\rfloor\) runs.

Let \(k=\lceil r/2\rceil\). For odd \(r=2k-1\), if either adjacent site is switched, the preceding bound is at most \(4k-1\); if neither is switched it is at most \(4(k-1)+1\). For even \(r=2k\), if either adjacent site is switched it is at most \(4k-1\). If neither is switched, reaching more than \(4k-1\) would force \(p=q=k\), hence all left-hole and right-island runs must occupy alternating depths \(2,4,\dots,2k\). In particular a left hole is at depth \(2k\) and every right island is at depth at least two. That left hole cannot be paired to any right island: its pair would have index distance at least \(2k+1>r\). Hence this case is impossible, again yielding \(V(Ku_m)\le4k-1\). Also trivially \(V(Ku_m)\le n-1\), proving the upper bound.

**4. Constructed equality cases for every \(n,r\).** Let \(k=\lceil r/2\rceil\), \(s=\min(n,4k)\), and \(m=\lceil s/2\rceil\). Start from the prefix input \(u_m\). On the first \(s\) coordinates prescribe alternating output entries \(1,0,1,0,\dots\) (one at even zero-based indices), with zeros at all remaining coordinates. Let \(L\) be the odd indices below \(m\), and \(R\) the even indices from \(m\) through \(s-1\). These sets have equal size. Pair their elements in increasing order and transpose each paired pair, fixing all other indices. The pair displacements are at most \(2\lceil s/4\rceil-1\), as follows by listing the two arithmetic progressions (or considering \(s\) modulo four). This is at most \(2k-1\le r\). The resulting permutation matrix is symmetric, stochastic and banded. Its output alternates on \(s\) sites; when \(s<n\) it ends with a zero followed by further zeros. Consequently its output has exactly \(s-1=\min(n-1,4k-1)\) variation, whereas the input has variation one. This proves equality and completes the result.

## Verification
Run `python3 verify_bandwidth.py` with Python 3 and no third-party dependencies. The checker exhausts 1,373 feasible cross-cut binary output profiles over thirty small \((n,r)\) pairs, using the exact sorted-matching feasibility criterion, checks the formula, and independently constructs explicit involutions at additional dimensions and radii. All calculations are integer-valued. This finite enumeration is not offered as an infinite-dimensional proof; Steps 1–4 above cover every integer \(n\ge2,r\ge1\).

## Relationship to prior work
Local symmetric stochastic averaging is central to the filter-symmetrization setting discussed by Milanfar (2013). The full-text 2012 Nochetto–Salgado treatment constructs a particular total-variation-diminishing interpolation operator; it neither ranges over all symmetric banded stochastic matrices nor determines a sharp worst-case path-variation norm. Girdziušas (2008, chapter 2, accessible text) studies double stochasticity, cyclic variation and positivity in diffusion scale spaces; the inspected sections do not state the parity-plateau operator norm. The general Birkhoff and bipartite matching-polytope facts are used as standard tools, not claimed as novel. The new statement is the exact all-size, all-bandwidth open-path seminorm envelope and its matching obstruction. Historical priority for that specific envelope remains to be checked independently, especially against wider matrix-analysis literature.

## Limitations
This is a supremum over a broad class containing permutation matrices; a particular strongly smoothing, positive-definite, totally positive, or Markov-semigroup filter may have a much smaller norm. The theorem neither characterizes every extremizer nor covers cyclic variation, weighted path variation, asymmetric filters or higher-dimensional lattices. No independent audit has been performed.

## References
- R. H. Nochetto and A. J. Salgado, *A Total Variation Diminishing Interpolation Operator and Applications*, arXiv:1211.1069, first posted 2012-11-05; https://arxiv.org/abs/1211.1069.
- P. Milanfar, *Symmetrizing Smoothing Filters*, SIAM Journal on Imaging Sciences 6 (2013), 263–284; https://doi.org/10.1137/120875843.
- R. Girdziušas, *Stability and Inference in Discrete Diffusion Scale-Spaces*, Helsinki University of Technology dissertation (2008), chapter 2; https://aaltodoc.aalto.fi/bitstreams/17a8a51d-faa0-43f1-938c-70b39e16a100/download.
- Standard bipartite matching polytope integrality and symmetric stochastic matrix theory (classical facts used in the proof).
