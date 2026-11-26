# A logarithmic dihedral-angle crossover in sparse partial permutohedra

## Finding
For integers \(m\ge4\), \(2\le n\le m-2\), define the **canonical partial permutohedron**
\[
\mathcal P(m,n)=\operatorname{conv}\bigl\{x\in\{0,1,\ldots,n\}^{m}:\text{nonzero entries of }x\text{ are pairwise distinct}\bigr\}\subset\mathbb R^m.
\]
Endow it with the unscaled Euclidean metric. A *ridge* is a face of codimension two, and its *interior dihedral angle* is the supplement of the angle between its two outward unit facet normals.

Its complete multiset of ridge angles is as follows. For every \(1\le s<t\le n-1\), include
\[
\binom mt\binom ts\text{ copies of }\pi-\arccos\sqrt{\frac st}.
\]
For every \(1\le s\le n-1\), include
\[
\binom ms\text{ copies of }\pi-\arccos\sqrt{\frac sm}.
\]
There are furthermore exactly
\[
R_{m,n}=\binom m2+\sum_{t=1}^{n-1}(m-t)\binom mt
\]
copies of the right angle \(\pi/2\), and exactly \(m\) copies of the acute angle \(\arccos(1/\sqrt m)\). All remaining listed angles are obtuse. In particular, the three counts are
\[
\boxed{A_{m,n}=m,\qquad R_{m,n}=\binom m2+\sum_{t=1}^{n-1}(m-t)\binom mt,\qquad
O_{m,n}=\sum_{t=1}^{n-1}(2^t-1)\binom mt.}
\]
Coincident numerical angle values, if any, are combined with their stated multiplicities.

**Sharp logarithmic crossover.** Let \(m\to\infty\) and let the positive integers \(n=n(m)\to\infty\) satisfy \(n=o(m)\). If
\[
\rho_m=\frac{2^{n-1}}m\longrightarrow\rho\in[0,\infty],
\]
with the endpoint \(\rho=\infty\) allowed, a uniformly sampled ridge angle \(\Theta_{m,n}\) converges in distribution to
\[
\boxed{\frac{1}{1+\rho}\,\delta_{\pi/2}
+\frac{\rho}{1+\rho}\,\delta_{3\pi/4}.}
\]
At \(\rho=\infty\), the displayed measure means \(\delta_{3\pi/4}\). Thus, when \(n-\log_2m\) is bounded, neither class need disappear, while below and above that window the typical angle is respectively \(\pi/2\) and \(3\pi/4\). Moreover, for a uniformly sampled **obtuse** ridge, irrespective of the behavior of \(\rho_m\),
\[
\boxed{\sqrt n\left(\Theta_{m,n}-\frac{3\pi}{4}\right)
\xrightarrow{\mathrm d}N\!\left(0,\frac14\right).}
\]
This conditional central limit theorem is different from the variance \(3/8\) of the published generalized-parking-polytope ridge law: sparse partial permutohedra have a distinct face-regime and a two-class crossover.

## Assumptions and scope
The finite classification holds exactly for all integers \(m\ge4\) and \(2\le n\le m-2\). The asymptotic statements additionally require \(n\to\infty\) and \(n/m\to0\); no statement is made in a regime where \(n/m\) approaches a positive constant. The distribution is uniform by **ridge count**, not weighted by ridge areas. The metric is the standard coordinate metric; arbitrary affine transformations need not preserve angles. The normal law is a conditional distribution given that an obtuse ridge was selected, not an unconditional normal law in the transition window.

## Proof
**1. Complete facets and simple vertices.** The established facet descriptions and vertex classification of Heuer–Striker and Behrend et al. give precisely the following irredundant facets in the stated sparse range:
\[
L_i:\ x_i=0\quad(i\in[m]);\qquad
U_S:\ \sum_{i\in S}x_i=|S|n-\binom{|S|}{2}
\quad(\varnothing\ne S\subset[m],\ |S|\le n-1);\qquad
G:\ \sum_{i=1}^{m}x_i=\frac{n(n+1)}2.
\]
Here the polytope lies on the nonnegative side of each \(L_i\) and the nonpositive side of each upper facet. The outward normal vectors are respectively \(-e_i\), \(\mathbf1_S\), and \(\mathbf1_{[m]}\). For clarity, the cited facet theorem is used for completeness: these equations alone, without the assertion that there are no additional facets, would not prove the result.

Every vertex is obtained by choosing an ordered support of some size \(0\le r\le n\), placing the values \(n,n-1,\ldots,n-r+1\) in the chosen order, and setting the remaining entries to zero. If \(r<n\), its tight upper facets are precisely those indexed by nonempty prefixes of the decreasingly labeled support (exactly \(r\) facets); the other \(m-r\) tight facets are coordinate lower facets. If \(r=n\), there are \(n-1\) prefix upper facets, the global facet \(G\), and \(m-n\) lower facets. Thus every vertex has exactly \(m\) incident facets. Each listed facet is a genuine facet by the cited theorem, and the polytope is full-dimensional; consequently it is simple, and any two distinct facets meeting at a vertex meet along a unique ridge.

**2. Classification of every ridge.** Both lower facets \(L_i,L_j\) meet at the origin when \(i\ne j\). A lower facet \(L_i\) meets an upper facet \(U_S\) at a vertex exactly when \(i\notin S\): equality at \(U_S\) forces all \(|S|\) peak labels to occupy coordinates of \(S\), so no coordinate of \(S\) can vanish; conversely place these labels in \(S\) and zero elsewhere. A lower facet \(L_i\) meets \(G\), since there are \(n\) positive slots but \(m>n\) coordinates. Two proper upper facets \(U_S,U_T\) meet at a vertex if and only if \(S,T\) are strictly nested; their tightness requires them to be initial segments of the same unique decreasing sequence of positive labels. All proper upper facets meet \(G\), by completing any initial sequence of labels through support size \(n\). This exhausts every facet pair and hence every ridge.

For nested upper facets with \(S\subsetneq T\), their outward normals have cosine
\[
\frac{\mathbf1_S\cdot\mathbf1_T}{\sqrt{|S||T|}}
=\sqrt{\frac{|S|}{|T|}}.
\]
The same formula holds for a proper upper facet and \(G\) with \(|T|=m\). Lower/lower and compatible lower/proper-upper normal pairs are perpendicular. A lower/global pair has normal cosine \(-1/\sqrt m\). Taking supplementary interior angles gives exactly the multiset in the Finding section. For each size \(t\le n-1\), the number of proper upper/proper upper ridges with larger facet \(U_T\) is \(\binom mt(2^t-2)\); each \(U_T\) adds one ridge against \(G\), giving \(\binom mt(2^t-1)\) obtuse ridges. Compatible lower/proper-upper incidences number \((m-t)\binom mt\). Lower/lower pairs number \(\binom m2\); lower/global pairs number \(m\). This proves the exact classification and counts, including the case \(n=2\), when the proper upper/upper sum is empty.

**3. Rigorous asymptotic dominance and the logarithmic threshold.** Put \(k=n-1\) and \(B=\binom mk\). Since \(k\to\infty\) and \(k=o(m)\), the ratio of consecutive binomial coefficients in the range \(1\le t\le k\) is bounded above by \(k/(m-k+1)=o(1)\) when moving from \(t\) to \(t-1\). Therefore
\[
\sum_{t=1}^{k}\binom mt =B(1+o(1)),\qquad
\sum_{t=1}^{k}(m-t)\binom mt=mB(1+o(1)),
\]
with the extra term \(\binom m2=o(mB)\). Likewise the ratios of successive terms \(2^t\binom mt\) are bounded by \(k/(2(m-k+1))=o(1)\). As \(2^k\to\infty\),
\[
O_{m,n}=2^k B(1+o(1)),\qquad R_{m,n}=mB(1+o(1)),\qquad
\frac{O_{m,n}}{R_{m,n}}=\frac{2^{n-1}}m(1+o(1)).
\]
Moreover, \(A_{m,n}/(R_{m,n}+O_{m,n})\to0\). Thus the respective probabilities of an obtuse and a right ridge converge to \(\rho/(1+\rho)\) and \(1/(1+\rho)\), with the evident interpretations at zero and infinity. The transition occurs when \(2^{n-1}\) is of order \(m\), equivalently \(n=\log_2m+O(1)\).

**4. Limiting obtuse angles.** Among obtuse ridges, the proportion whose larger facet is the proper upper facet \(U_T\) with \(|T|=k\) is \(1-o(1)\): smaller-size contributions are down by \(O(k/m)\) and upper/global contributions are down by \(O(2^{-k})\). Conditional on this dominant class and on its larger set \(T\), the smaller set \(S\) is uniform over the \(2^k-2\) nonempty proper subsets of \(T\). Consequently \(|S|\) has the \(\operatorname{Bin}(k,1/2)\) law conditioned to lie between \(1\) and \(k-1\). Its ratio to \(k\) tends to \(1/2\) in probability, yielding the second atom \(\pi-\arccos(1/\sqrt2)=3\pi/4\). The binomial central limit theorem gives
\[
\sqrt{k}\left(\frac{|S|}{k}-\frac12\right)
\xrightarrow{\mathrm d}N\!\left(0,\frac14\right).
\]
The angle map \(h(u)=\pi-\arccos\sqrt u\) has \(h'(1/2)=1\). By the delta method and \(n/k\to1\), the displayed conditional normal law follows. Since all excluded obtuse classes have probability \(o(1)\) even after conditioning, they do not affect this weak limit. Combining with the right-angle exact atom proves the weak two-point limit, including when \(\rho=0\) or \(\infty\).

## Verification
The independent finite checker `verify_sparse_angles.py` uses only the Python 3 standard library. It explicitly generates vertices by ordered supports, independently computes every tight facet equation, confirms exactly \(m\) incident facets per vertex, and compares the observed entire facet-pair incidence set to the predicted ridge set. For every predicted ridge it independently constructs its integer outward normal vectors and checks the squared cosine and angle type exactly using integer arithmetic. It compares the three angle-class counts with the closed formulas. Fourteen cases \(4\le m\le8\), \(2\le n\le\min(5,m-2)\) passed, comprising 17,218 vertex occurrences and 6,789 ridge incidences. Large-dimension count ratios are additionally evaluated from the exact formulas. Execute: `python verify_sparse_angles.py`. These finite computations do **not** establish either the all-dimensional theorem or the asymptotic law, which follow from the proof above.

## Relationship to prior work
Heuer and Striker introduced partial permutohedra and established their defining inequalities and facets, first publicly posted December 17, 2020 [1]. Behrend et al. proved the complete vertex, facet and face-poset classification, including the chain-of-subsets structure [2]. Those combinatorial ingredients are **not** claimed as original; they are indispensable inputs. The claim here is the complete Euclidean ridge-angle multiplicity measure for the **sparse** range \(n\le m-2\), and especially its logarithmic right/obtuse crossover and conditional normal law. A published generalized-parking-function-polytope theorem supplies a different ridge-angle spectrum and a \(3/8\)-variance Gaussian limit for the full positive-parameter parking-family; its facet regime corresponds to \(n\ge m-1\) for partial permutohedra and cannot be applied to the sparse range [3,4]. Published analyses of partial-permutohedron edge lengths and Gaussian widths similarly concern other metric invariants. The assertion is not that prior face enumeration fails to imply the combinatorial ridge counts: the new question and answer are the actual Euclidean angular law and its sparse-parameter phase transition.

## Limitations
The geometric law is specific to the standard coordinate realization and uniformly chosen ridges, not area-weighted ridge curvature. The finite formulas also agree at \(n=m-1\) with the already known classical parking-polytope spectrum [3]: the permitted upper sizes are \(1,\ldots,m-2,m\), and the global facet still meets each coordinate lower facet. At \(n\ge m\) the global facet instead requires all coordinates to be positive, so the \(m\) acute ridges from lower/global incidences are no longer present. The asymptotic results address only the sparse regime \(n\to\infty\), \(n=o(m)\). The normal limit is conditional on a rare class when \(\rho=0\). Priority remains provisional: an unindexed paper, a more general geometric criterion not detected by the source comparisons, or an already-computed tabulation could contain equivalent results.

## References
1. D. Heuer and J. Striker, *Partial permutation and alternating sign matrix polytopes*, arXiv:2012.09901 (first public version 2020-12-17), Sections 5.1–5.2, https://arxiv.org/abs/2012.09901.
2. R. E. Behrend, F. Castillo, A. Chavez, A. Diaz-Lopez, L. Escobar, P. E. Harris and E. Insko, *Partial permutohedra*, arXiv:2207.14253 (first public version 2022-07-28), Propositions 2.7, 2.8, 3.5 and Theorem 3.6, https://arxiv.org/abs/2207.14253.
3. *Universal dihedral-angle spectra and Gaussian ridge law for generalized parking-function polytopes*, Resultary, 2026-11-17, https://github.com/Resultary/2026/blob/main/2026/11/17/SCOPE-universal-dihedral-angle-spectra-and-gaussian-ridge-law-for-gene--676f0e5f85c3/RESULT.md.
4. R. E. Behrend, *Ehrhart polynomials of partial permutohedra*, arXiv:2403.06975 (first public version 2024-03-11), introduction on the parking-function and stellohedral regimes, https://arxiv.org/abs/2403.06975.
