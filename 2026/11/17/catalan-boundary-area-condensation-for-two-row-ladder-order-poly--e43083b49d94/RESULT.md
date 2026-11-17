# Catalan boundary-area condensation for two-row ladder order polytopes

## Finding
For an integer \(n\ge 2\), take the product poset \(P_n=[2]\times[n]\), with elements \(A_1,\ldots,A_n,B_1,\ldots,B_n\), relations \(A_i\prec A_{i+1}\), \(B_i\prec B_{i+1}\), and \(A_i\prec B_i\), and transitive closure. Let \(\mathcal O_n\subset\mathbb R^{2n}\) be its ordinary, unscaled Euclidean order polytope
\[
\mathcal O_n=\{(a,b)\in[0,1]^{2n}:a_i\le a_{i+1},\ b_i\le b_{i+1},\ a_i\le b_i\},
\]
with the consecutive-coordinate inequalities imposed for \(1\le i<n\). Write \(C_j=\frac1{j+1}\binom{2j}{j}\), including \(C_0=1\), and \(D=2n\). Then
\[
\operatorname{Vol}_{D}(\mathcal O_n)=\frac{C_n}{D!},\qquad
\boxed{\frac{\operatorname{Area}_{D-1}(\partial\mathcal O_n)}{\operatorname{Vol}_D(\mathcal O_n)}=D(2+n\sqrt2).}
\]
There are precisely \(3n\) facets: two unit-normal coordinate facets; \(2(n-1)\) horizontal cover facets; and \(n\) vertical cover facets \(F_{n,i}=\mathcal O_n\cap\{a_i=b_i\}\). These three classes contribute respectively \(2D\), \(D\sqrt2(n-1)\), and \(D\sqrt2\) to the Euclidean surface-area/volume ratio. Each vertical facet has the **exact individual** intrinsic Euclidean area
\[
\boxed{\frac{\operatorname{Area}_{D-1}(F_{n,i})}{\operatorname{Vol}_D(\mathcal O_n)}=D\sqrt2\,\frac{C_{i-1}C_{n-i}}{C_n},\quad 1\le i\le n.}
\]
Consequently its share of the total vertical-facet area is
\[
p_{n,i}=\frac{C_{i-1}C_{n-i}}{C_n}.
\]
The values are symmetric, and strictly decrease moving inward from either endpoint except for the equal middle pair when \(n\) is even. For every fixed \(i\ge1\),
\[
\lim_{n\to\infty}p_{n,i}=q_i=\frac{C_{i-1}}{4^i},\qquad \sum_{i\ge1}q_i=\frac12.
\]
Thus half the area within the entire vertical-facet family concentrates asymptotically in any sufficiently wide, fixed-order left endpoint neighborhood, and the other half in the right endpoint neighborhood; in particular the first and last facets alone carry asymptotically half of the vertical-facet area. For fixed \(0<t<1\), with \(i_n/n\to t\),
\[
\boxed{n^{3/2}p_{n,i_n}\longrightarrow \frac1{4\sqrt\pi[t(1-t)]^{3/2}}.}
\]
The two endpoint tails have a universal power-law profile: after taking \(n\to\infty\), the vertical-area proportion outside the first and last \(K\) facets is \(\frac1{\sqrt{\pi K}}(1+o(1))\) as \(K\to\infty\).

## Assumptions and scope
All dimensions and measures are intrinsic to the standard Euclidean coordinate embedding, not normalized lattice facet volume. The theorem holds for every integer \(n\ge2\), with no parameter tending to infinity in the exact equalities. The limiting assertions require fixed endpoint index \(i\), or \(i_n/n\to t\in(0,1)\), or the successive limits first \(n\to\infty\) and then \(K\to\infty\), as stated. A facet normal of a coordinate bound has length one; a facet normal for a cover equality has length \(\sqrt2\). The polytope is full-dimensional and its cover inequalities are irredundant.

## Proof
**1. Canonical triangulation and Euclidean facet measure.** A linear extension of \(P_n\) is encoded by a word with \(n\) letters \(U\) (for consecutive \(A_i\)) and \(n\) letters \(D\) (for consecutive \(B_i\)), with every prefix containing at least as many \(U\)'s as \(D\)'s. These are the \(C_n\) Dyck words of semilength \(n\). For each word \(w=(w_1,\ldots,w_D)\), the simplex \(0\le x_{w_1}\le\cdots\le x_{w_D}\le1\) has Euclidean volume \(1/D!\). Their interiors are disjoint and they cover \(\mathcal O_n\), proving the volume formula.

For a coordinate-minimum or coordinate-maximum facet, the boundary face in each simplex has \((D-1)\)-area \(1/(D-1)!\). If a cover pair appears consecutively in the word, its equality face has area \(\sqrt2/(D-1)!\): subtracting one of the two equal-coordinate order-statistic directions, its Gram determinant equals \(2\), whereas the coordinate-bound Gram determinant is \(1\). A cover pair not adjacent in the word contributes no boundary face of full facet dimension in that simplex. Relative interiors of the facet simplices are disjoint up to lower-dimensional boundaries. It follows that, for any cover \(u\prec v\),
\[
\frac{\operatorname{Area}_{D-1}(\mathcal O_n\cap\{x_u=x_v\})}{\operatorname{Vol}_D(\mathcal O_n)}
=D\sqrt2\,\Pr\{u,v\text{ consecutive in a uniformly chosen linear extension}\}.
\]
The unique minimum \(A_1\) and maximum \(B_n\) give two coordinate facets with area/volume ratio \(D\) each.

**2. Comparable consecutive letters.** For a Dyck word \(w\), let \(P(w)\) be the number of peaks \(UD\), and let \(H(w)\) be its number of *hills*, that is, peaks \(UD\) starting and ending at height zero. Consecutive equal letters are always a horizontal cover pair. Every consecutive \(DU\) is an incomparable pair; a consecutive \(UD\) is a vertical cover pair if and only if it is a hill (at higher height, its \(A\)-index exceeds its \(B\)-index). Since a Dyck word begins with \(U\) and ends with \(D\), it has \(P(w)\) peaks, \(P(w)-1\) valleys \(DU\), and \(D-2P(w)\) consecutive equal-letter pairs. Therefore the number of its cover-adjacent positions is exactly
\[
D-2P(w)+H(w).
\]
The number of Dyck paths of semilength \(n\) with \(k\) peaks is the Narayana number \(\frac1n\binom nk\binom n{k-1}\), symmetric under \(k\leftrightarrow n+1-k\). Thus \(\mathbb E P=(n+1)/2\). The number of words having the hill \(U_iD_i\) is \(C_{i-1}C_{n-i}\), by independent Dyck prefixes and suffixes. Catalan convolution gives \(\sum_{i=1}^n C_{i-1}C_{n-i}=C_n\), whence \(\mathbb E H=1\). The expected number of cover-adjacent positions is then \(D-(n+1)+1=n\), and multiplying by \(D\sqrt2\) yields all cover-facet area divided by volume. Exactly one expected adjacency is vertical, leaving \(n-1\) horizontal. Adding the two coordinate facets proves the surface-area formula and all class totals. The same hill bijection proves the individual vertical-facet formula.

**3. Endpoint condensation and bulk scale.** The Catalan asymptotic \(C_j\sim4^j/(\sqrt\pi j^{3/2})\) gives \(C_{n-i}/C_n\to4^{-i}\) at fixed \(i\), and the stated bulk asymptotic when \(i_n/n\to t\). The generating series identity \(\sum_{j\ge0}C_j4^{-j}=2\) gives \(\sum_{i\ge1}C_{i-1}4^{-i}=1/2\). Symmetry proves left/right concentration. More precisely, for fixed \(K\), the limiting fraction outside indices \(1,\ldots,K\) and \(n-K+1,\ldots,n\) equals \(1-2\sum_{i=1}^Kq_i=2\sum_{i>K}q_i\); as \(q_i\sim1/(4\sqrt\pi i^{3/2})\), the integral test gives \(2\sum_{i>K}q_i\sim1/\sqrt{\pi K}\). Finally, \(C_i/C_{i-1}=2(2i-1)/(i+1)\) increases strictly in \(i\), so \(p_{n,i+1}/p_{n,i}=(C_i/C_{i-1})/(C_{n-i}/C_{n-i-1})\) is below one when \(i<n/2\), equals one when \(i=n/2\), and exceeds one past the center.

## Verification
The standalone `verify.py` enumerates every Dyck word up to semilength ten (23,713 words in total), checks all relevant peak and hill expectations and all exact vertical-facet counts, and checks the sum of cover-adjacent positions. For semilengths one through five it also reconstructs the actual Euclidean simplex facets in ambient coordinates and computes 414 exact rational Gram determinants, verifying the required determinants \(1\) and \(2\). This finite check tests the formulas and Euclidean normalization; it does not replace the all-parameter proof above. Run `python verify.py` from the extracted package.

## Relationship to prior work
The 2021 paper of von Bell and collaborators studies generalized snake and ladder posets, provides the canonical order-polytope triangulation and the Catalan normalized volume of the ladder case, and studies circuits, flips and volume extremality. The earlier work of Santos, Stump and Welker studies the two-chain product order polytope and its Catalan/Narayana triangulations. Lee, Vindas-Meléndez and Wang study the Ehrhart and \(h^*\)-data of generalized snake, in particular ladder, order polytopes. These known combinatorial, volume and lattice-enumeration facts are inputs; the result here concerns **actual Euclidean codimension-one facet areas**, their complete vertical-family distribution, and its two-endpoint concentration with a sharp bulk scale. None of the cited inspected materials states these Euclidean identities. A generic lattice boundary-volume computation may recover an aggregate lattice-normalized boundary coefficient but does not by itself give the individual Euclidean vertical-facet spectrum or its condensation.

## Limitations
The asymptotic claims concern the share within the vertical-facet family, not all boundary facets: the entire vertical family contributes only a fraction \(\sqrt2/(2+n\sqrt2)\) of total Euclidean boundary area. The horizontal facet areas are aggregated, not individually classified; the theorem makes no claim about higher Steiner coefficients or other ladder metrics. Literature priority is provisional, particularly for unindexed sources and lattice-boundary techniques, and an independent mathematical audit has not been performed.

## References
1. M. von Bell, B. Braun, D. Hanely, K. Serhiyenko, J. Vega, A. R. Vindas-Meléndez, and M. Yip, *Triangulations, order polytopes, and generalized snake posets*, arXiv:2102.11306 (first posted 2021-02-22), especially Sections 2–3. https://arxiv.org/abs/2102.11306
2. F. Santos, C. Stump, and V. Welker, *Noncrossing sets and a Graßmann associahedron*, arXiv:1403.8133 (first posted 2014-03-31), especially Sections 1 and 3. https://arxiv.org/abs/1403.8133
3. E. Lee, A. R. Vindas-Meléndez, and Z. Wang, *Generalized snake posets, order polytopes, and lattice-point enumeration*, arXiv:2411.18695 (first posted 2024-11-27), especially Sections 2–4. https://arxiv.org/abs/2411.18695
4. R. P. Stanley, *Two poset polytopes*, Discrete Comput. Geom. 1 (1986), 9–23. https://doi.org/10.1007/BF02187680
