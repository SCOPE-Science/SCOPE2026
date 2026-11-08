# Sharp realizability of three spectral thresholds by binary-or-unary trees

## Finding

**Theorem (spectral-triple realization).** For every triple of real parameters \(0\le a\le c\le b\le1\) with \(b>0\), there is an explicit rooted, leafless, spherically homogeneous directed tree \(\mathcal T\), with every vertex having either one or two children, whose unweighted backward sum shift \(S\) on \(\ell^2(V(\mathcal T))\) satisfies
\[
 R_-=2^{a/2},\qquad R_+=2^{b/2},\qquad
 \sigma(S)=\{\lambda:|\lambda|\le2^{b/2}\},
\]
\[
 \sigma_{\mathrm p}(S)=\{\lambda:|\lambda|<2^{c/2}\},\qquad
 \sigma_{\mathrm{ap}}(S^*)=\{\lambda:2^{a/2}\le|\lambda|\le2^{b/2}\}.
\]
Every eigenspace of \(S\) is infinite dimensional. In particular, \(S-\lambda I\) is surjective exactly when \(|\lambda|<2^{a/2}\) or \(|\lambda|>2^{b/2}\). Thus eigenvalues and failure of surjectivity may coexist throughout the entire open annulus between the two descendant-growth radii.

For the concrete choice \((a,c,b)=(0,1,1)\), the inner radius is \(1\), the point-spectrum radius and spectral radius are both \(\sqrt 2\), and every \(1\le|\lambda|<\sqrt 2\) is an infinite-multiplicity eigenvalue for which \(S-\lambda I\) is not onto.

## Assumptions and scope

The underlying Hilbert space is complex. For a rooted directed tree \(\mathcal T\), let \(e_v\) be the canonical basis vector at vertex \(v\), and define \(S e_v=e_{\operatorname{par}(v)}\) for nonroot vertices and \(S e_{\rm root}=0\). All branching is by depth: every vertex at depth \(j\) has \(d_j\in\{1,2\}\) children. Denote by \(B_n=\prod_{j=0}^{n-1}d_j\) the number of vertices at depth \(n\), with \(B_0=1\), and by
\[
 K_n^- =\inf_{m\ge0}\prod_{j=m}^{m+n-1}d_j,\qquad
 K_n^+ =\sup_{m\ge0}\prod_{j=m}^{m+n-1}d_j
\]
the extremal descendant counts. The radii \(R_\pm=\lim_{n\to\infty}(K_n^\pm)^{1/(2n)}\) exist by Fekete's lemma. Spectral symbols \(\sigma\), \(\sigma_{\mathrm p}\), and \(\sigma_{\mathrm{ap}}\) respectively denote full, point, and approximate point spectra.

Here is the explicit construction. For \(t\in[0,1]\) set
\[
 w_t(j)=\lfloor(j+1)t\rfloor-\lfloor jt\rfloor\in\{0,1\}\quad(j\ge0).
\]
For every integer \(k\ge2\), let \(N_k=2^{k^5}\), \(L_k=k^2\). Begin with \(\varepsilon_j=w_c(j)\), then replace its values on \([N_k,N_k+L_k)\) by \(w_b(j-N_k)\), and on \([N_k+L_k,N_k+2L_k)\) by \(w_a(j-N_k-L_k)\). These intervals are pairwise disjoint. Finally put \(d_j=1+\varepsilon_j\). The construction is exact for all real parameters; no computational approximation to a slope is assumed.

## Proof

**1. Three growth parameters.** A mechanical word obeys, on every integer window, the exact telescoping identity
\[
 \sum_{j=u}^{u+n-1}w_t(j)=\lfloor(u+n)t\rfloor-\lfloor ut\rfloor,
\]
so its count differs from \(nt\) by less than one, unless the difference is zero. For the edited word, each length-\(n\) window splits into subwindows of mechanical words with slopes in \(\{a,c,b\}\). The maximum possible number \(\nu(n)\) of piece boundaries in a length-\(n\) window is \(o(n)\): boundary gaps tend to infinity, so outside any fixed finite initial set they exceed an arbitrarily prescribed constant. Therefore, uniformly in the starting index,
\[
 an-o(n)\le\sum_{j=u}^{u+n-1}\varepsilon_j\le bn+o(n).
\]
Since the pure \(a\)-blocks and \(b\)-blocks have unbounded lengths, for each fixed \(n\) they contain windows achieving respectively \(an+O(1)\) and \(bn+O(1)\). Thus
\[
 \lim_{n\to\infty}\frac1n\inf_u\sum_{j=u}^{u+n-1}\varepsilon_j=a,
 \qquad
 \lim_{n\to\infty}\frac1n\sup_u\sum_{j=u}^{u+n-1}\varepsilon_j=b.
\]
Taking powers of two gives \(R_-=2^{a/2}\) and \(R_+=2^{b/2}\).

Write \(M(n)=\sum_{j=0}^{n-1}\varepsilon_j\). Up to \(n\), the total number of replaced entries is at most \(2\sum_{k\le(\log_2 n)^{1/5}}k^2=O((\log n)^{3/5})\). The unedited word has count \(\lfloor nc\rfloor\). Hence
\[
 M(n)=cn+O((\log(n+2))^{3/5})=cn+o(\log n),\qquad B_n=2^{M(n)}.
\]
This logarithmic error bound is the reason for using very widely separated editing sites: it controls the point-spectrum boundary, not just the open disk.

**2. Exact eigenvalue criterion.** For every complex \(\lambda\), the vector with value \(\lambda^n/B_n\) at each depth-\(n\) vertex satisfies \(Sx=\lambda x\) formally. It belongs to \(\ell^2\) precisely when
\[
 F(\lambda):=\sum_{n=0}^{\infty}\frac{|\lambda|^{2n}}{B_n}<\infty.
\]
Conversely, suppose \(Sx=\lambda x\) and some coordinate \(x_v\ne0\) occurs at depth \(t\). Iterated Cauchy--Schwarz on the \(B_{t+n}/B_t\) descendants of \(v\) yields
\[
 \sum_{u:\,u\text{ descends }n\text{ levels from }v}|x_u|^2
 \ge |x_v|^2\frac{B_t|\lambda|^{2n}}{B_{t+n}}.
\]
The left-hand sides occupy pairwise disjoint depth levels as \(n\) varies. Therefore the tail of \(F(\lambda)\) must converge. The criterion is necessary and sufficient.

The relation \(M(n)=cn+o(\log n)\) implies convergence for \(|\lambda|<2^{c/2}\) and divergence for \(|\lambda|>2^{c/2}\). At equality the summand is \(2^{cn-M(n)}=\exp(o(\log n))\), and eventually exceeds \(n^{-1/2}\); hence the series diverges there as well. We obtain the claimed strict point-spectrum disk.

Because \(b>0\), the sequence has infinitely many binary levels. Along an infinite ray choose infinitely many disjoint side subtrees; in each there is a later binary split. Put opposite coefficients on the two children of that later split and extend uniformly to their descendants using the eigenvalue recurrence. The preceding series criterion applies to every fixed-depth tail, giving a square-summable eigenvector, with all coordinates outside this side subtree zero. These vectors have pairwise disjoint supports. Thus each eigenspace has infinite dimension, including at \(\lambda=0\).

**3. Radial approximate eigenvectors.** Let
\[
 u_n=B_n^{-1/2}\sum_{|v|=n}e_v.
\]
These form an orthonormal basis of a reducing subspace for \(S\) and \(S^*\), and \(S^*u_n=\sqrt{d_n}\,u_{n+1}\). Write \(W\) for this forward weighted shift. Fix \(z\ne0\) with \(2^{a/2}<|z|<2^{b/2}\). On the consecutive \(b\)-block and \(a\)-block of length \(L_k\), choose a coefficient \(x_j=1\) at their junction. Extend to the left by \(x_j=(z/\sqrt{d_j})x_{j+1}\), and to the right by \(x_{j+1}=(\sqrt{d_j}/z)x_j\). All other coefficients are zero. On the upper block, backwards coefficients decay geometrically because \(2^{b/2}>|z|\); on the lower block, forward coefficients decay geometrically because \(2^{a/2}<|z|\). This follows uniformly from the less-than-one mechanical-word discrepancy. The residual \((W-zI)x\) is supported only at the two ends and tends to zero, while \(\|x\|\ge1\). Hence \(z\in\sigma_{\mathrm{ap}}(W)\subseteq\sigma_{\mathrm{ap}}(S^*)\).

At \(|z|=2^{b/2}\), take a vector supported on one arbitrarily long pure \(b\)-block, with the same recurrence. Its coefficients have moduli bounded above and below by constants independent of block length, again by the balanced-word discrepancy. The norm is of order \(\sqrt{L_k}\) while the two residual boundary coefficients remain bounded. Thus this circle belongs to \(\sigma_{\mathrm{ap}}(S^*)\). A pure \(a\)-block proves the same for \(|z|=2^{a/2}\). These arguments also cover \(a=b\), where the two circles coincide. This proves inclusion of the closed annulus.

**4. Excluding the complementary regions.** For each depth-\(j\) vertex, \(SS^*e_v=d_je_v\). Consequently \(R=S^*(SS^*)^{-1}\) is a bounded right inverse of \(S\), and direct iteration on disjoint descendant sets gives
\[
 \|R^n\|^2=(K_n^-)^{-1},\qquad r(R)=R_-^{-1}.
\]
For \(|\lambda|<R_-\), the operator \(I-\lambda R\) is invertible and \(R(I-\lambda R)^{-1}\) is a right inverse of \(S-\lambda I\). Conversely, \(\|S^n\|^2=K_n^+\), hence \(r(S)=R_+\); for \(|\lambda|>R_+\), \(S-\lambda I\) is invertible. Both regions are therefore excluded from \(\sigma_{\mathrm{ap}}(S^*)\), and \(S-\lambda I\) is onto there. On the closed intermediate annulus, approximate eigenvectors for \(S^*\) at \(\overline\lambda\) show that \((S-\lambda I)^*\) is not bounded below; the closed-range theorem excludes surjectivity. This proves the exact surjectivity and approximate-point statements. Combining the disk of eigenvalues with the intervening annulus proves \(\sigma(S)=\{\lambda:|\lambda|\le R_+\}\).

## Verification

The accompanying `check.py` uses only Python standard-library rational arithmetic. It performs 46,378 finite assertions checking mechanical-word telescoping, finite homogeneous-tree eigenvector coefficients and layer normalizations, and edited-window arithmetic in representative rational-slope cases. Run with `python3 check.py`; the expected final line is `EXACT_SPHERICAL_TREE_CHECK_OK 46378`. These checks corroborate identities but do not prove the asymptotic or infinite-dimensional assertions. The proof above is independent of the computations.

## Relationship to prior work

Buckley and Seco's 2026 Theorem 1 obtains surjectivity/universality for \(|\lambda|<R_-\) and identifies \(R_+\) as the spectral radius, explicitly raising the question of spectrum in the intervening annulus. The present theorem provides exact full, point, and adjoint approximate-point spectra and an exhaustive realization of the three normalized logarithmic radii in a spherically homogeneous binary-or-unary subclass. Their binary regular-tree example has \(R_-=R_+\) and cannot exhibit this separation.

Jabłoński--Jung--Stochel's general directed-tree shift theory supplies spectral circularity. Chavan--Trivedi's analytic model establishes the familiar spectral disk for the adjoints of left-invertible tree shifts and studies their spectral parts; its detailed finite-branching-index model does not cover trees with branching at unbounded depths, and its general inclusions do not give this exact triple or realization. Budzyński--Dymek--Planeta--Ptak give Wold-type structural decompositions of balanced shifts, which may offer an alternative reduction to one-dimensional models. D'Aniello--Maiuriello's unilateral weighted-shift theory explains the analogous one-dimensional radial eigenvalue series. The present tree claim additionally requires the nonradial eigenvalue necessity, infinite eigenspace multiplicity, precise surjectivity obstruction and combinatorial realization. These classical tools are credited, not presented as novel in isolation.

## Limitations

The claim concerns rooted, spherically homogeneous unweighted shifts with branching numbers at most two. No analogue is asserted for arbitrary nonhomogeneous directed trees. The notation \(\sigma_{\mathrm{ap}}(S^*)\) refers to the adjoint, not the approximate-point spectrum of \(S\). The construction has extremely sparse edits and is not claimed optimal in complexity. It settles a structured realizability problem and exhibits intermediate-annulus behavior; it does not establish a classification for every bounded-degree tree. Priority against all possible older weighted-shift spectral realizability results has not been independently certified.

## References

1. Jeremiah Buckley and Daniel Seco, *Rota universality of shifts on trees*, arXiv:2610.40089v1, publicly submitted October 29, 2026, https://arxiv.org/abs/2610.40089 (especially Theorem 1, Remarks, and Sections 2--4).
2. Zenon Jabłoński, Il Bong Jung, and Jan Stochel, *Weighted shifts on directed trees*, arXiv:0911.3821, https://arxiv.org/abs/0911.3821 (especially Section 3.3, Corollary 3.3.2).
3. Emma D'Aniello and Martina Maiuriello, *On the spectrum of weighted shifts*, arXiv:2210.01510, https://arxiv.org/abs/2210.01510 (especially Section 3, classical unilateral backward-shift eigenvalue criterion).
4. Sameer Chavan and Shailesh Trivedi, *An Analytic Model for Left-Invertible Weighted Shifts on Directed Trees*, arXiv:1510.03075, https://arxiv.org/abs/1510.03075 (especially Section 5, Theorem 5.1 and its hypotheses).
5. Piotr Budzyński, Piotr Dymek, Artur Planeta, and Marek Ptak, *Weighted shifts on directed trees. Their multiplier algebras, reflexivity and decompositions*, arXiv:1702.00765, https://arxiv.org/abs/1702.00765 (especially Section 6).
6. William C. Ridge, *Approximate point spectrum of a weighted shift*, Transactions of the American Mathematical Society (1970), DOI:10.1090/S0002-9947-1970-0254635-5 (historical weighted-shift background; full text not inspected).
