# Rank-one Rota–Baxter systems on square-zero local algebras: incidence strata and a complete finite-field census

## Finding

Let \(k\) be any field, let \(m\ge 2\), and let \(A=k1\oplus V\) be the commutative unital associative algebra with \(\dim_k V=m\) and \(V^2=0\). An ordered pair of \(k\)-linear maps \((R,S)\), each of vector-space rank at most one, is a *Rota–Baxter system* when, for all \(x,y\in A\),
\[
R(x)R(y)=R(R(x)y+xS(y)),\qquad
S(x)S(y)=S(R(x)y+xS(y)).
\]
Put \(\tau:A\to k\) for the scalar-part homomorphism, and let \(\ell_R=\operatorname{im}R\), \(\ell_S=\operatorname{im}S\) whenever the maps are nonzero. The following cases are exhaustive, disjoint and sufficient.

1. Both maps are zero.
2. Exactly one map, denoted \(T\), is nonzero. Either \(\ell_T=k1\), with no further restriction on \(T\), or \(\ell_T\subset V\) and \(T(\ell_T)=0\).
3. Both maps are nonzero, and exactly one has image \(k1\). If the radical-image map is \(T\), it has a nonzero eigenvalue \(\rho\in k^\times\) on its one-dimensional image, and the scalar-image map must equal \(-\rho\tau(\cdot)1\). Conversely, every such pair is a system, in either ordering.
4. Both maps are nonzero and have images in \(V\). Then the system condition is equivalent to
\[
R(\ell_R+\ell_S)=S(\ell_R+\ell_S)=0.
\]
In particular, both nonzero maps cannot both have scalar image. In case 4 the four compositions \(R^2,S^2,RS,SR\) all vanish.

For a prime power \(q\), put \(L_m(q)=(q^m-1)/(q-1)\). The exact seven-category census over \(\mathbb F_q\) is
\[
\begin{array}{c|c}
\text{category}&\text{number}\hline
(R,S)=(0,0)&1\\
\operatorname{rank}R=1,\ S=0&q^{m+1}-1+L_m(q)(q^m-1)\\
R=0,\ \operatorname{rank}S=1&q^{m+1}-1+L_m(q)(q^m-1)\\
\ell_R=k1,\ \ell_S\subset V&q^m(q^m-1)\\
\ell_R\subset V,\ \ell_S=k1&q^m(q^m-1)\\
\ell_R=\ell_S\subset V&L_m(q)(q^m-1)^2\\
\ell_R,\ell_S\subset V,\ \ell_R\ne\ell_S&L_m(q)(L_m(q)-1)(q^{m-1}-1)^2.
\end{array}
\]
Therefore the number of ordered pairs of rank at most one is exactly
\[
\boxed{\mathcal N_m(q)=1+2\bigl(q^{m+1}-1+L_m(q)(q^m-1)\bigr)
+2q^m(q^m-1)+L_m(q)(q^m-1)^2
+L_m(q)(L_m(q)-1)(q^{m-1}-1)^2.}
\]
For \(m=2\), this gives \(\mathcal N_2(2)=90\), \(\mathcal N_2(3)=565\) and \(\mathcal N_2(4)=2062\); for \(m=3\) it gives \(\mathcal N_3(2)=962\).

The two nonzero radical/radical loci with equal versus distinct image lines are geometrically irreducible *locally closed strata* of dimensions \(3m-1\) and \(4m-4\), respectively. Their dimensions are unequal in favor of the equal-line stratum at \(m=2\), equal at \(m=3\), and unequal in favor of distinct lines for every \(m\ge4\). **No assertion is made that these strata are irreducible components of the full reduced operator variety.**

## Assumptions and scope

All maps are \(k\)-linear, and rank means vector-space rank. No hypothesis on field characteristic, perfection or algebraic closure is required for the classification. The finite-field count concerns *labeled ordered pairs* of linear operators, not conjugacy classes. For the incidence geometry claim, irreducibility and dimensions are taken after extension to an algebraic closure, for the reduced locally closed rank-one strata. The formula also remains true at the boundary \(m=1\) (with an empty distinct-line stratum), although the geometric transition statement assumes \(m\ge2\).

## Proof

**Step 1: image-line rigidity.** Write a nonzero rank-one map as \(R(x)=\phi(x)u\) with \(u\ne0\) and \(\phi\ne0\). Choosing \(x,y\) with \(\phi(x)\phi(y)\ne0\), the first Rota–Baxter-system identity forces \(u^2\in ku\). The same argument applies to the generator of \(\operatorname{im}S\). For \(u=a1+w\) with \(w\in V\), if \(a\ne0\) then comparing scalar and radical parts in \(u^2=\lambda u\) gives \(\lambda=a\) and \(2aw=aw\), hence \(w=0\) in every characteristic. If \(a=0\), then \(u\in V\), so \(u^2=0\). Thus every nonzero image is either the scalar line \(k1\) or a radical line.

**Step 2: one nonzero map.** For \(S=0\), the equation becomes \(R(x)R(y)=R(R(x)y)\). If \(R(x)=\phi(x)1\), it holds for arbitrary \(\phi\). If \(R(x)=\phi(x)w\) with \(w\in V\setminus\{0\}\), using \(wx=\tau(x)w\) gives \(\phi(w)=0\) as the necessary and sufficient condition. Interchanging the equations proves the same statement for \(R=0\).

**Step 3: nonzero scalar/radical pairs.** Write \(R(x)=\phi(x)1\), \(S(x)=\psi(x)w\), with \(w\in V\setminus\{0\}\). The first identity gives \(\phi(w)=0\); the second gives
\[
0=\psi(y)\bigl(\phi(x)+\tau(x)\psi(w)\bigr)w.
\]
Since \(\psi\ne0\), this is equivalent to \(\phi=-\psi(w)\tau\); because \(R\ne0\), one has \(\psi(w)\ne0\). The first condition then follows automatically. If instead \(R(x)=\phi(x)w\), \(S(x)=\psi(x)1\), the first identity reduces to
\[
0=\phi(x)\bigl(\tau(y)\phi(w)+\psi(y)\bigr)w,
\]
so \(\psi=-\phi(w)\tau\), with \(\phi(w)\ne0\); the second identity is automatic. If both image lines are scalar, the first identity forces \(\phi(x)\psi(y)=0\) for every \(x,y\), impossible when both functionals are nonzero. This proves case 3 and excludes the remaining scalar/scalar case.

**Step 4: two radical-image maps.** Write \(R(x)=\phi(x)w\) and \(S(x)=\psi(x)z\) with \(w,z\in V\setminus\{0\}\). Both left sides vanish. The two right sides equal zero for all \(x,y\) precisely when
\[
\phi(x)\tau(y)\begin{pmatrix}\phi(w)\\\psi(w)\end{pmatrix}
+\tau(x)\psi(y)\begin{pmatrix}\phi(z)\\\psi(z)\end{pmatrix}=0.
\]
Set \(\alpha=\phi(1)\), \(\beta=\psi(1)\) and let \(L=\phi|_V\), \(M=\psi|_V\). Taking \(x\in V,y=1\) shows that if \(L\ne0\), the first vector must vanish. Taking \(x=1,y\in V\) shows that if \(M\ne0\), the second vector must vanish. If both restrictions are nonzero, both vectors therefore vanish. If \(L\ne0,M=0\), the first vanishes and the \(x=y=1\) equation forces the second to vanish because \(\beta\ne0\). The case \(L=0,M\ne0\) is symmetric using \(\alpha\ne0\). If \(L=M=0\), both vectors vanish directly. Thus in every case \(\phi(w)=\phi(z)=\psi(w)=\psi(z)=0\), which is also sufficient by the displayed equation. This is exactly the asserted common-image-span annihilation criterion.

**Step 5: finite-field counts.** There are \(L_m(q)\) radical image lines. For a chosen radical line, a rank-one map into that line with the line in its kernel has \(q^m-1\) choices of nonzero functional (since \(\dim A/\ell=m\)). A scalar-image rank-one map has \(q^{m+1}-1\) choices. For a chosen radical line \(\ell\), the condition that a map \(T:A\to\ell\) have nonzero eigenvalue on \(\ell\) allows \((q-1)q^m\) maps; multiplication by \(L_m(q)\) gives \(q^m(q^m-1)\) in each mixed ordering. For two equal radical lines, the two functionals have \((q^m-1)^2\) choices. For two distinct ordered radical lines, there are \(L_m(q)(L_m(q)-1)\) choices of lines and each map's functional vanishes on their two-dimensional span, giving \((q^{m-1}-1)^2\) choices. All categories are disjoint, so summing gives the displayed formula.

**Step 6: incidence dimensions.** A single radical line varies in \(\mathbb P(V)\), of dimension \(m-1\); the pair of nonzero rank-one maps annihilating it is a nonzero-vector locus in two vector bundles each of rank \(m\). This equal-line locus is geometrically irreducible of dimension \((m-1)+2m=3m-1\). Distinct ordered lines vary in the irreducible open complement of the diagonal in \(\mathbb P(V)^2\), of dimension \(2(m-1)\); each map's fiber has dimension \(m-1\), so that locus is geometrically irreducible of dimension \(2(m-1)+2(m-1)=4m-4\). Comparing dimensions proves the transition. These are strata, not a claimed full component decomposition.

## Verification

The standalone source `roba_pair_check.py` enumerates **all** ordered pairs of rank-at-most-one endomorphisms over each requested field, reconstructs the original algebra multiplication, and independently checks both defining identities on every ordered pair of basis elements. It does not reject maps based on the stated classification before checking the identities. The seven-category counts are compared to their closed formulas only after successful direct testing. The field \(\mathbb F_4\) is realized by the irreducible polynomial \(X^2+X+1\), not by arithmetic modulo four. Exact exhaustive checks passed for \((q,m)=(2,1),(3,1),(5,1),(2,2),(3,2),(4,2),(2,3)\); all listed tests enumerate complete endomorphism-pair spaces; the exact tested-pair totals are printed in `CHECKER_OUTPUT.txt`. The general proof, not finite testing, establishes the universal statement.

Replay from the directory containing `roba_pair_check.py` by running `python roba_pair_check.py 2:1 3:1 5:1 2:2 3:2 4:2 2:3`. The expected final marker is `ROTA_BAXTER_SYSTEM_RANK_ONE_ORIGINAL_IDENTITIES_OK`. `CHECKER_OUTPUT.txt` records the actual seven checks.

## Relationship to prior work

Tomasz Brzeziński introduced Rota–Baxter systems in the March 17, 2015 preprint [1]. Definition 2.1 contains exactly the two identities used here. Its Lemma 2.3 and Example 2.4 construct pairs from module-linearity and orthogonal multipliers, and Corollary 2.7 constructs associated associative and pre-Lie products. Those results are credited. They do **not** give the all-rank-at-most-one classification, its seven-category finite-field count, or the image-line incidence transition. For example, when \(m\ge3\), choose linearly independent \(e_1,e_2,e_3\in V\) and set \(R(e_3)=e_1\), \(S(e_3)=e_2\), all other basis values zero. It satisfies the new classification, yet neither operator is multiplication by an algebra element, since each vanishes on \(1\) but is nonzero.

The prior single-operator Rota–Baxter classifications [2] and earlier work on square-zero local algebras overlap the diagonal specialization \(R=S\). Such diagonal results are not independently claimed as new. They do not enumerate general non-diagonal pairs, including the mixed scalar/radical branches. Full-text and record searches found no decisive theorem covering the joint result; absence of a located theorem is not an independence certificate.

## Limitations

This theorem concerns the rank-at-most-one *pair* locus on split commutative square-zero local algebras. It does not classify arbitrary higher-rank systems, noncommutative trivial extensions, simultaneous conjugacy classes, the complete reduced irreducible-component structure, or nonreduced scheme multiplicities. The geometric dimensions refer to the stated locally closed strata only. The self-review is not an independent audit, and historical publication priority has residual uncertainty.

## References

[1] T. Brzeziński, *Rota-Baxter systems, dendriform algebras and covariant bialgebras*, arXiv:1503.05073v1, publicly submitted 2015-03-17, https://arxiv.org/abs/1503.05073 ; Journal of Algebra 460 (2016), 1–25, DOI:10.1016/j.jalgebra.2016.04.018. In particular Section 2, Definition 2.1, Lemma 2.3, Example 2.4, Proposition 2.5 and Corollary 2.7.

[2] S. Zheng, L. Guo, M. Rosenkranz, *Classification of Rota-Baxter operators on semigroup algebras of order two and three*, arXiv:1402.3702v1 (2014-02-15), https://arxiv.org/abs/1402.3702 ; Communications in Algebra 47 (2019), 3094–3116, https://pmc.ncbi.nlm.nih.gov/articles/PMC7083595/ . This concerns single Rota–Baxter operators rather than arbitrary two-map systems.
