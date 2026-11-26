# Complete spectral and dual classification of interlaced-character Gabor sampling masks

## Finding

Let \(p\ge 2\) and \(1\le m\le p\) be integers and let \(N=pm\). Choose any injection \(\sigma:\{0,\ldots,m-1\}\to\mathbb Z_p\) and form the unimodular window \(g\in\mathbb C^N\) by
\[
g(u+mt)=\exp(2\pi i\sigma(u)t/p),\qquad 0\le u<m,\quad 0\le t<p.
\]
Fix all \(p\) subgroup translations \(K=\{0,m,\ldots,(p-1)m\}\), but allow **any** modulation-frequency mask \(L\subseteq\mathbb Z_N\). Put
\[
c_a=\#\{\ell\in L:\ell\equiv a\pmod p\},\qquad a\in\mathbb Z_p,
\]
so \(0\le c_a\le m\). The frame operator \(S_L\) of the labelled vectors \(M_\ell T_k g\), \(k\in K\), \(\ell\in L\), is unitarily diagonalizable as
\[
S_L=p^2\sum_{a=0}^{p-1}c_a P_a,
\]
where \(P_a\) are mutually orthogonal rank-\(m\) projections that sum to the identity and depend on \(\sigma\) but **not** on \(L\). Every Gabor atom \(M_\ell T_k g\) lies in \(\mathrm{ran}(P_{\ell\bmod p})\). Thus:

1. The complete spectrum is \(\{p^2c_a:a\in\mathbb Z_p\}\), each listed with multiplicity \(m\), including zeros. The rank is \(m\#\{a:c_a>0\}\), and the system spans \(\mathbb C^N\) exactly when every \(c_a>0\). Then the sharp frame bounds are \(p^2\min_ac_a\) and \(p^2\max_ac_a\).
2. For every spanning mask, the **canonical dual atom** is exactly \((p^2c_{\ell\bmod p})^{-1}M_\ell T_k g\). Its canonical Parseval atom is \((p\sqrt{c_{\ell\bmod p}})^{-1}M_\ell T_k g\). In particular, an arbitrary non-subgroup mask produces a tight frame precisely when all \(c_a\) coincide.
3. Two masks have isospectral frame operators exactly when their occupancy vectors \((c_a)\) have the same multiset of entries, regardless of the injected phase labels \(\sigma\). If \(h_j=\#\{a:c_a=j\}\), \(0\le j\le m\), the number of masks belonging to that spectral class is
\[
\frac{p!}{\prod_{j=0}^m h_j!}\prod_{j=0}^m\binom mj^{h_j}.
\]
Consequently the exact number of spanning masks of size \(k\) is the coefficient \([z^k]((1+z)^m-1)^p\). For \(1\le r\le m\), exactly \(\binom mr^p\) masks of size \(pr\) give tight frames.
4. Fix a feasible cardinality \(p\le k\le pm\) and write \(k=pq+s\), \(0\le s<p\). Among all spanning masks with \(k\) frequencies, the sharp smallest possible spectral condition number \(B/A\) is \(1\) if \(s=0\), and \((q+1)/q\) if \(s>0\). The minimizing masks are **exactly** those with \(p-s\) residue classes occupied \(q\) times and \(s\) residue classes occupied \(q+1\) times. Their exact number is
\[
\binom ps\binom mq^{p-s}\binom m{q+1}^{s},
\]
with \(s=0\) interpreted through \(\binom m{q+1}^{0}=1\). The largest number of arbitrarily deleted frequency labels that is guaranteed to preserve spanning is \(q-1\), attained by the same balanced masks (among possibly additional masks).

All assertions hold for composite \(p\) and masks \(L\) that need not be subgroups, cosets, or unions thereof.

## Assumptions and scope

Use the unnormalized Euclidean inner product \(\langle x,y\rangle=\sum_{j=0}^{N-1}x_j\overline{y_j}\), linear in the first variable. The cyclic operations are \((T_kx)(j)=x(j-k\bmod N)\) and \((M_\ell x)(j)=\exp(2\pi i\ell j/N)x(j)\). The frame operator \(S_Lx=\sum_{k\in K}\sum_{\ell\in L}\langle x,M_\ell T_k g\rangle M_\ell T_k g\). The mask contains distinct frequencies and may be empty for spectral/rank assertions; spanning and dual assertions require \(c_a\ge1\) for every \(a\). The integer \(p\) need not be prime. No assertion is made for windows that are not interlaces of distinct characters, for arbitrary translation erasures, or for nonrectangular time-frequency masks.

## Proof

Write \(\zeta=\exp(2\pi i/p)\). For \(u\in\{0,\ldots,m-1\}\) and \(a\in\mathbb Z_p\), define a vector \(v_{u,a}\) by
\[
v_{u,a}(u'+mt)=p^{-1/2}\mathbf1_{u'=u}\zeta^{(\sigma(u)+a)t}.
\]
For each fixed \(u\), the \(p\) vectors \(v_{u,a}\) constitute the orthonormal Fourier basis of the coordinates with residue \(u\pmod m\). The full \(pm\)-vector collection \(\{v_{u,a}\}_{u,a}\) is thus an orthonormal basis. Let \(P_a=\sum_{u=0}^{m-1}v_{u,a}v_{u,a}^*\), where \(v v^*\) denotes the orthogonal rank-one projection.

For \(k=bm\in K\), \(\ell\in L\) and \(a=\ell\bmod p\), the atom has the exact expansion
\[
M_\ell T_{bm}g
=\sqrt p\sum_{u=0}^{m-1}
  \exp(2\pi i\ell u/N)\zeta^{-b\sigma(u)}v_{u,a}.
\]
It belongs entirely to \(\mathrm{ran}(P_a)\). Sum its outer products over \(b=0,\ldots,p-1\); by injectivity of \(\sigma\) and character orthogonality,
\[
\sum_{b=0}^{p-1}\zeta^{b(\sigma(v)-\sigma(u))}
=p\mathbf1_{u=v}.
\]
Therefore the frame operator contributed by one individual frequency \(\ell\) in residue class \(a\) is exactly \(p^2 P_a\). Summing over all frequencies gives \(S_L=p^2\sum_a c_aP_a\). This proves the complete spectrum, rank, sharp bounds, and membership of each atom in one eigenspace.

If every \(c_a>0\), invert on each \(\mathrm{ran}(P_a)\): \(S_L^{-1}=p^{-2}\sum_ac_a^{-1}P_a\) and \(S_L^{-1/2}=p^{-1}\sum_ac_a^{-1/2}P_a\). Applying these operators to an atom gives the stated exact canonical dual and Parseval formulas. Constancy of all \(c_a\) is necessary and sufficient for tightness.

Each residue class \(a\pmod p\) contains exactly \(m\) frequency labels of \(\mathbb Z_N\). Consequently a fixed ordered occupancy vector \((c_a)\) is realized by precisely \(\prod_a\binom m{c_a}\) masks. Two occupancy vectors give the same multiset of eigenvalues precisely when their histograms \((h_j)\) agree: every spectral level has eigenspace multiplicity \(mh_j\). There are \(p!/\prod_jh_j!\) arrangements of a prescribed histogram, giving the spectral-class count. Restricting to positive occupancies and using ordinary generating functions yields the coefficient count for spanning masks. Tightness requires \(c_a=r\) in all \(p\) classes, giving \(\binom mr^p\).

For the optimal design, write \(k=pq+s\) with \(0\le s<p\). If \(s=0\), \(B/A\ge1\), and equality is equivalent to all \(c_a=q\). If \(s>0\), at least one occupancy is \(\le q\) and another is \(\ge q+1\). Hence \(B/A\ge(q+1)/q\); equality forces every occupancy to belong to \(\{q,q+1\}\), with precisely \(s\) of the larger kind. There are \(\binom ps\) choices of those classes and \(\binom mq^{p-s}\binom m{q+1}^s\) ways to select their frequency labels. For a mask whose smallest occupancy is \(d\), deleting \(d-1\) arbitrary frequency labels cannot empty a class; deleting all \(d\) labels of a least-occupied class does. The best possible minimum occupancy at size \(k\) is \(q\), completing the erasure statement.

## Verification

The standalone script \(\texttt{check.py}\) constructs the Gabor synthesis matrix directly (using cyclic shifts and complex exponentials, not the proof's Fourier basis), computes its frame-operator spectrum, and verifies the eigenvector relation for each atom. It reports **1,281 passing cases** across integer periods \(p=2,\ldots,6\), with multiple interlaced injections and frequency masks including deficient masks. A separate exhaustive binary-mask count for periods \(p=2,3,4\), interlace widths \(m\le3\), verifies generating-function counts and the sharp condition-number optimizer census in **63 cardinality cases**. Numerical tests supplement, and do not substitute for, the all-parameter proof above. Run with \(\texttt{OPENBLAS_NUM_THREADS=1 python check.py}\) and NumPy installed.

For a quick trace check, the frame consists of \(p|L|\) vectors each of squared norm \(pm\). The predicted spectral trace is \(\sum_a m\,p^2 c_a=mp^2|L|\), exactly matching the atom trace.

## Relationship to prior work

Asipchuk, De Carli and Rodriguez, *Block-equivalent finite Gabor frames* (arXiv:2605.16139, first submitted May 15, 2026), prove block equivalence for subgroup translation sets (Theorem 1.1), provide explicit block transforms (Corollary 5.1), and give a single interlaced-character tight example for a non-subgroup mask (their Section 4 example with \(N=12\)). Those results supply the broader structural framework and motivate the window family. Their published theorems do not state the unrestricted exact occupancy spectrum, atom-wise scalar canonical dual, all-mask isospectral census, or globally sharp cardinality-constrained design count established here. The proof above derives them explicitly rather than treating the prior block decomposition as sufficient verification.

General finite Gabor frame and dual-window theory provides the abstract inversion identity used here; the special no-inversion scalar dual for every mask is a property of this interlaced character family. Previously indexed exact translation-erasure laws for one-defect windows and geometric-taper windows concern different window profiles, mask types, and spectral invariants, and do not imply the present occupancy classification. The new result is a complete special-family classification, not a new general finite Gabor block-decomposition theorem.

## Limitations

No claim of priority against every unindexed dissertation, chapter, or alternate terminology is made. General subgroup-frame formulas in the motivating paper are close enough that this exact evaluated specialization should be regarded as an explicit structural refinement, not a result independent of that framework. The combinatorial counts assume distinct labelled frequency indices and all subgroup translations; masks deleting individual time-frequency pairs are not classified. The numerical certificate covers finite samples only. External independent audit has not been conducted.

## References

- O. Asipchuk, L. De Carli, and L. Rodriguez, *Block-equivalent finite Gabor frames*, arXiv:2605.16139, initial public submission May 15, 2026, https://arxiv.org/html/2605.16139v2 . Especially Theorem 1.1, Corollary 4.3, Corollary 5.1, and the example after Corollary 4.3.
- A. Iosevich, M. Kolountzakis, Yu. Lyubarskii, A. Mayeli, and J. Pakianathan, *On Gabor orthonormal bases over finite prime fields*, arXiv:1712.09120, https://arxiv.org/abs/1712.09120 . Different prime-field orthonormal-window setting.
