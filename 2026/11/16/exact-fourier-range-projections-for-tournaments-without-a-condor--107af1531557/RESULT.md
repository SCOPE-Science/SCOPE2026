# Exact Fourier range projections for tournaments without a Condorcet winner

## Finding
For each integer \(n\ge3\), let \(E=\binom n2\) and let \(\mathcal T_n\subseteq\mathbb F_2^E\) be the edge-orientation vectors of all labelled tournaments on \(n\) vertices **without** a Condorcet winner (a vertex beating every other vertex). For \(f_n=\mathbf1_{\mathcal T_n}\), let \(C_n h=f_n*h\) be unnormalized convolution on \(\ell^p(\mathbb F_2^E)\). Write \(\Omega_n=\{u:\widehat f_n(u)\ne0\}\).

**Theorem.** Denote by \(S_v\) the \(n-1\) coordinates of the edges incident to vertex \(v\). Then
\[
\Omega_n=\{0\}\cup\bigcup_{v=1}^n\{u:\operatorname{supp}(u)\subseteq S_v,\ |\operatorname{supp}(u)|\ge2\},
\quad |\Omega_n|=1+n(2^{n-1}-n).
\]
All nonzero-frequency Walsh multipliers have absolute magnitude \(2^{E-n+1}\), and the zero-frequency multiplier is \(2^E-n2^{E-n+1}\). Consequently, \(\|C_n^\dagger\|_{2\to2}=2^{n-1-E}\), and the positive spectral condition number is \(2^{n-1}-n\).

Let \(\Lambda_n\) be the least \(\ell^1\)-operator norm of **any real or complex linear projection** onto \(\operatorname{ran}C_n\), equivalently the least \(\ell^\infty\)-projection norm. Let \(H(G)\) be the number of isolated vertices of an ordinary simple graph \(G\) on \(n\) labelled vertices, and \(e(G)\) its number of edges. Then the exact finite formula is
\[
\boxed{\ \Lambda_n=2^{-E}\sum_{G\subseteq K_n}\left|2^{n-1}H(G)+4e(G)-n^2+1\right|\ }.
\]
More explicitly, define \(a_{r,k}=\sum_{s=0}^r(-1)^s\binom rs\binom{\binom{r-s}{2}}{k}\), with out-of-range binomial coefficients taken to be zero. This is the number of graphs on \(r\) labelled vertices with exactly \(k\) edges and no isolated vertices (including \(a_{0,0}=1\)). Thus
\[
\boxed{\ \Lambda_n=2^{-E}\sum_{j=0}^n\binom nj\sum_{k=0}^{\binom{n-j}{2}}a_{n-j,k}\left|2^{n-1}j+4k-n^2+1\right|\ }.
\]
In particular,
\[
\Lambda_3=1,\qquad\Lambda_4=\frac{101}{32},\qquad\Lambda_5=\frac{355}{64},\qquad\Lambda_6=\frac{73287}{8192}.
\]
The sharp large-size growth is
\[
\boxed{\ \lim_{n\to\infty}\frac{\Lambda_n}{n}
=1+\mathbb E|Z-1|
=1+\frac{2}{\sqrt\pi}e^{-1/4}+\operatorname{erf}(1/2)
=2.3992824567\ldots,\quad Z\sim N(0,2).\ }
\]
The exact coefficient in this asymptotic is part of the claim; it does not follow from the trivial count of winner-free tournaments.

## Assumptions and scope
A tournament assigns one direction to each unordered pair of distinct labelled vertices. To fix a binary encoding, for \(i<j\) set the bit of \(\{i,j\}\) to one when \(i\) beats \(j\), and to zero otherwise. The additive group is \(\mathbb F_2^E\); characters are \(\chi_u(x)=(-1)^{u\cdot x}\) and transforms are **unnormalized**, \(\widehat f_n(u)=\sum_xf_n(x)\chi_u(x)\). Convolution is unnormalized, and counting-measure \(\ell^p\) norms are used. All frequency supports and projection norms are invariant under reversing chosen reference edge directions.

Here \(\operatorname{ran}C_n\) is the finite-dimensional range of convolution, and \(C_n^\dagger\) is its Moore–Penrose inverse on \(\ell^2\). The projection minimum is over all linear projections, not just convolution operators or orthogonal projections. Real and complex scalars give the same minimum.

## Proof
**1. Tournament characters.** A vertex \(v\) is a Condorcet winner precisely on one face \(F_v\subseteq\mathbb F_2^E\) fixing all \(n-1\) incident bits and leaving the other \(E-n+1\) bits free. The faces \(F_v\) are pairwise disjoint: two vertices cannot both win the edge between them. Consequently, \(f_n=1-\sum_v\mathbf1_{F_v}\), and every face has cardinality \(B=2^{E-n+1}\). For nonzero \(u\), the Walsh sum over \(F_v\) vanishes unless \(\operatorname{supp}(u)\subseteq S_v\); if contained, its value is \(B\chi_u(x_v)\) for any \(x_v\in F_v\). The two faces associated with the endpoints of a single edge contribute opposite signs, so all singleton-edge frequencies vanish. Any set of at least two distinct edges is contained in at most one star \(S_v\), so every star-supported frequency of size at least two has multiplier \(\pm B\), and all other frequencies vanish. At zero frequency, \(\widehat f_n(0)=2^E-nB=B(2^{n-1}-n)>0\). The nonempty star subsets of size at least two are disjoint across vertices, and number \(2^{n-1}-n\) per vertex. This proves the Fourier support, exact convolution rank, and positive multiplier bounds. Since \(2^{n-1}-n\ge1\) for \(n\ge3\), the smallest nonzero magnitude is \(B\).

**2. Why the range projection is globally minimal.** Let \(P_n\) be the Fourier projection with multiplier \(\mathbf1_{\Omega_n}\). For any projection \(Q\) onto \(\operatorname{ran}C_n\), average the conjugates \(T_g^{-1}QT_g\) over all translations \(T_g\) of \(\mathbb F_2^E\). Because translations are isometries on each \(\ell^p\) and preserve this range, the average is a translation-commuting projection onto the same range and has norm no larger than \(Q\). The only translation-invariant projection onto a given character span is \(P_n\): its scalar multiplier must equal one on the span and zero outside. Thus \(P_n\) is minimum-norm over all projections, simultaneously for \(p=1\) and \(p=\infty\), over real or complex scalars. If \(K_n\) denotes its convolution kernel, then \(\|P_n\|_{1\to1}=\|P_n\|_{\infty\to\infty}=\sum_z|K_n(z)|\).

**3. Exact kernel and finite counts.** Fourier inversion of \(\mathbf1_{\Omega_n}\) gives \(2^E K_n(z)=1+\sum_v\sum_{U\subseteq S_v,\,|U|\ge2}(-1)^{\sum_{e\in U}z_e}\). The inner sum equals \(2^{n-1}\mathbf1_{\{z_e=0\ \forall e\in S_v\}}-1-\sum_{e\in S_v}(-1)^{z_e}\). Identify \(z\) with the simple graph \(G_z\) whose edges have bit one. Summing over vertices counts isolated vertices, while every edge belongs to exactly two stars. Therefore
\[
2^E K_n(z)=2^{n-1}H(G_z)+4e(G_z)-n^2+1.
\]
Taking absolute values and summing gives the exact graph-sum formula. For the binomial formula, choose the \(j\) isolated vertices and let the remaining \(n-j\) vertices span a graph with no isolates. Inclusion–exclusion over an additional set of isolated vertices shows that the number of such graphs with \(k\) edges is exactly \(a_{n-j,k}\). This proves the second formula without relying on computation.

**4. Sharp asymptotic.** Let \(G\sim G(n,1/2)\), put \(M=e(G)\sim\operatorname{Bin}(E,1/2)\), \(H=H(G)\), and \(X=4M-n^2+1\). Then \(\Lambda_n=\mathbb E|X+2^{n-1}H|\). For all \(n\ge7\), \(2^{n-1}>n^2-1\), so \(X+2^{n-1}H>0\) whenever \(H\ge1\). The identities \(\mathbb EH=n2^{-(n-1)}\) and \(\mathbb P(H\ge1)\le n2^{-(n-1)}\) give
\[
\Lambda_n=\mathbb E|X|+n-2\mathbb E[(-X)_+\mathbf1_{\{H\ge1\}}],
\qquad 0\le\mathbb E|X|+n-\Lambda_n\le2n^3 2^{-(n-1)}.
\]
The binomial central limit theorem implies \(X/n\Rightarrow Z-1\) with \(Z\sim N(0,2)\). Since \(\mathbb E(X/n)^2=4E/n^2+(1-1/n)^2\) is uniformly bounded, absolute values are uniformly integrable, so \(\mathbb E|X|/n\to\mathbb E|Z-1|\). Direct integration of the Gaussian density yields \(\mathbb E|Z-1|=2e^{-1/4}/\sqrt\pi+\operatorname{erf}(1/2)\). Together with the exponentially small correction, this proves the displayed constant.

## Verification
The standalone `check_tournaments.py` constructs the orientation indicator independently, computes its full integer Walsh transform by the butterfly algorithm, and checks the star-frequency formula, all multiplier magnitudes, rank, the inverse-Walsh projection kernel and its \(\ell^1\) norm for every labelled tournament at orders \(3\) through \(6\). It also independently calculates the no-isolates binomial sum, reproduces each finite projection constant, and evaluates the exact formula through order \(20\). Run `python3 check_tournaments.py`; successful output ends with `NO_CONDORCET_TOURNAMENT_WALSH_PASS`. The all-order statements are proved symbolically above; these finite checks are corroboration, not infinite proofs.

## Relationship to prior work
Altman and Kleinberg (2010) formalize tournament winner selection, including Condorcet-consistency, but study incentives and randomized selection rules rather than Fourier support or operator projection constants. Kolesnik and Sanchez (first posted 2020) characterize score-sequence geometry and realizability of tournaments, not character sums over the no-winner subset. The classical Fourier averaging technique used in Step 2 is known, including Zippin (2004); it is a proof tool, not a novelty claim. The novelty assessed here is the specific Fourier support and exact range-projection formula and the explicit Gaussian-plus-isolated-vertex asymptotic constant. General Fourier-transform operator norm work, such as Gilbert and Rzeszotnik (2010), does not provide this graph-specific idempotent projection norm.

## Limitations
The theorem concerns the condition **no vertex wins all matches**, not absence of a Condorcet loser or general tournament solution concepts. The asymptotic is for the endpoint \(\ell^1\) and \(\ell^\infty\) projection constants; no sharp \(\ell^p\) values for \(1<p<\infty\), \(p\ne2\), are asserted. The paper does not establish how these constants change under biased orientations or noncomplete underlying graphs. Historical priority remains subject to unindexed or inaccessible character-weighted tournament literature; independent mathematical validation has not been performed.

## References
- A. Altman and R. Kleinberg, *Nonmanipulable Randomized Tournament Selections*, Proc. AAAI 24 (2010), 686–690, first openly dated 2010-07-04, https://doi.org/10.1609/aaai.v24i1.7613. The complete five-page paper was inspected.
- B. Kolesnik and M. Sanchez, *The Geometry of Random Tournaments*, arXiv:2009.09322 (first posted 2020-09-19), https://arxiv.org/abs/2009.09322. Open full text: https://link.springer.com/article/10.1007/s00454-023-00571-4.
- M. Zippin, *A variant of Rudin's inequality for translation invariant projections on group algebras and its generalization to finite dimensional Banach spaces*, Arch. Math. 82 (2004), 61–67, https://doi.org/10.1007/s00013-003-0582-x.
- J. Gilbert and Z. Rzeszotnik, *The norm of the Fourier transform on finite abelian groups*, Ann. Inst. Fourier 60 (2010), 1317–1346, https://doi.org/10.5802/aif.2556.
