# A slope-sensitive shattering phase transition for zero-padded Sturmian factors

## Finding

**Theorem.** Let \(w\) be any one-sided binary Sturmian word of irrational slope \(\alpha\in(0,1)\), with symbol \(1\) having frequency \(\alpha\). For every nonempty finite factor \(u=u_0\cdots u_{L-1}\) of \(w\), let \(E(u)=\{j:0\le j<L,\ u_j=1\}\subseteq\mathbb N_0\), interpreted as an infinite binary word with zeros beyond its length. Let \(\mathcal F_\alpha=\{E(u):u\text{ is a finite factor of }w\}\). Then

\[
\operatorname{VCdim}(\mathcal F_\alpha)=
\begin{cases}2,&0<\alpha<\tfrac12,\\3,&\tfrac12<\alpha<1.\end{cases}
\]

More precisely, every singleton and the empty support are shattered. For \(0<\alpha<1/2\), a two-element support \(\{i,j\}\), \(i<j\), is shattered if and only if
\[\lVert(j-i)\alpha\rVert<\alpha,\qquad
\lVert x\rVert=\min_{r\in\mathbb Z}|x-r|,\]
and no support of size at least three is shattered. For \(1/2<\alpha<1\), every two-element support is shattered, no support of size four or more is shattered, and a three-element support \(i<j<k\) is shattered if and only if the following four sets all have nonempty interior in \(\mathbb T=\mathbb R/\mathbb Z\):
\[
J_i\cap J_j\setminus J_k,\quad
J_i\setminus(J_j\cup J_k),\quad
J_j\setminus(J_i\cup J_k),\quad
\mathbb T\setminus(J_i\cup J_j\cup J_k),
\]
where \(A_r=\{x\in\mathbb T:\{x+r\alpha\}<\alpha\}\) is the one-symbol arc and \(J_r=\mathbb T\setminus A_r\) is its short complementary arc.

Consequently, if \(P_N\) denotes the number of shattered pairs supported in \(\{0,\dots,N-1\}\), then
\[
P_N=\begin{cases}
\displaystyle\sum_{d=1}^{N-1}(N-d)\mathbf1_{\{\lVert d\alpha\rVert<\alpha\}},&\alpha<\tfrac12,\\
\binom N2,&\alpha>\tfrac12,
\end{cases}
\qquad
\lim_{N\to\infty}\frac{P_N}{\binom N2}=
\begin{cases}2\alpha,&\alpha<\tfrac12,\\1,&\alpha>\tfrac12.
\end{cases}
\]
This is an exact description of the entire shattered-support family, not only its maximum cardinality. The ordinary *equal-length-window/mask* VC dimension is two at both slopes, a distinct earlier result; the additional unit is caused by permitting a factor to end before the largest queried coordinate.

## Assumptions and scope

A one-sided Sturmian word is an aperiodic binary word of factor complexity \(L+1\) at length \(L\). By its classical irrational mechanical-word representation, its factor language equals that obtained by coding an irrational circle rotation of angle \(\alpha\) with a half-open interval of length \(\alpha\). Either lower or upper boundary convention and any intercept yield the same finite factor language. The theorem concerns factor sets with the *same coordinate origin*, and factors are allowed to have different lengths: positions beyond a factor's last coordinate are regarded as zero. Thus it is specifically the variable-length VC dimension of Johnson's binary-string set family, not the mask dimension of fixed-length windows. Because \(\alpha\) is irrational, \(\alpha=1/2\) is excluded.

For any finite query support, the orbit of an irrational rotation is dense. Thus every nonempty open phase cell occurs in some factor of \(w\). Conversely, every phase trace produced at an arc boundary coincides with the trace of a neighboring open cell, by the uniform half-open convention. This allows all shattering decisions to be made using nonempty *interior* of phase intersections, without exceptional intercept dependence.

## Proof

**1. Exact trace structure.** Write the mechanical coding of coordinate \(r\) as \(\mathbf1_{A_r}(x)\), where \(x\) ranges over a dense forward orbit in \(\mathbb T\). For a factor of length \(L\), the observed bit at position \(r\) is \(\mathbf1_{A_r}(x)\) if \(r<L\) and zero otherwise. Hence on ordered support \(i_1<\cdots<i_s\), the positive bits are obtained by restricting a rotation phase to an initial prefix of the queried coordinates. In particular, a trace whose last queried bit is one must be witnessed by a factor long enough to include *every* queried coordinate and hence by the ordinary arc arrangement.

**2. Pairs.** Take \(i<j\). The zero-zero trace exists using a factor ending before \(j\): if \(i=0\), choose a one-symbol factor beginning with zero; if \(i>0\), choose a one-symbol factor, which is zero at both queried positions. The one-zero trace exists using a factor of length \(i+1\) with symbol one at \(i\). Both zero-one and one-one require a factor reaching \(j\), and are equivalent respectively to \(A_j\setminus A_i\) and \(A_j\cap A_i\) having nonempty interior. All distinct translates of a proper half-open arc differ in both directions, so the former always holds. For \(\alpha<1/2\), the latter holds precisely when the circular separation \(\lVert(j-i)\alpha\rVert\) is strictly smaller than \(\alpha\); for \(\alpha>1/2\), two arcs of length \(\alpha\) always intersect in an open set. Density of the irrational rotation supplies witnesses. At small slope a suitable pair exists because the dense orbit has a nonzero return to circular distance less than \(\alpha\).

**3. No triples at small slope.** If \(\alpha<1/2\), consider \(i<j<k\). To shatter them, the four traces with bit one at \(k\) must be realized by the pair of indicators \(\mathbf1_{A_i},\mathbf1_{A_j}\) on the interval \(A_k\) of length \(\alpha\). The intersection of two circular arcs of length less than one half is either empty or a single interval. In the coordinate chart identifying \(A_k\) with an ordinary open interval, each \(A_i\cap A_k\) and \(A_j\cap A_k\) is a proper initial segment or a proper terminal segment of that interval: two equal-length short arcs can overlap only from one end. Two such end-anchored subintervals cannot realize all four pairs \(00,01,10,11\): same-end segments are nested, and opposite-end segments cannot have both a gap and overlap. Thus no triple is shattered. Heredity rules out all larger supports.

**4. All pairs, but no quadruples, at large slope.** The pair result already gives all pairs. For any four ordered indices \(i<j<k<\ell\), all eight assignments to the first three coordinates with final bit one would have to occur in the arc \(A_\ell\), which is an interval on cutting the circle at its endpoints. The three preceding arc indicators have at most six internal discontinuity positions, hence at most seven open cells on that interval. At shared boundary points, uniform half-open indicators take the same values as one adjacent open cell, never producing a new isolated trace. Eight different assignments are therefore impossible. Heredity excludes larger supports.

**5. Exact large-slope triple criterion.** For \(i<j<k\), the four traces with final bit zero occur automatically: the zero-zero trace is obtained from a short factor; the one-zero trace from a factor ending immediately after \(i\); and the zero-one and one-one traces from factors ending immediately after \(j\), since \(A_j\setminus A_i\) and \(A_j\cap A_i\) both have open interior. For final bit one, the factor must extend through \(k\). As a zero at \(r\) is equivalent to membership in \(J_r\), the patterns \((0,0,1),(0,1,1),(1,0,1),(1,1,1)\) are available exactly when, respectively, the four regions in the statement have nonempty interior. These conditions are also sufficient by density of the rotation orbit.

**6. A shattered triple exists at every large slope.** Set \(\beta=1-\alpha<1/2\). By density of the translates \(J_r\), choose \(i<j\) so that the two short arcs \(J_i,J_j\) overlap with a positive displacement \(\varepsilon<\min\{\beta,\alpha-\beta\}\). Their union is a connected circular arc of length \(\beta+\varepsilon<\alpha\), and the two differences and their intersection have nonempty interiors. The complementary arc has length \(\alpha-\varepsilon>\beta\), so by density choose \(k>j\) with \(J_k\) wholly inside that complementary arc. Then the four triple regions in the criterion are all nonempty. Steps 4 and 5 prove that the VC dimension is exactly three.

**7. Pair-density statement.** The exact formula follows from Step 2 by grouping pairs according to their difference \(d\). The irrational sequence \(\{d\alpha\}\) is equidistributed; the interval union \((0,\alpha)\cup(1-\alpha,1)\) has total length \(2\alpha\). Standard weighted Cesàro summation, with weights \(N-d\), gives the claimed normalized limit.

## Verification

A separate dependency-free Python verifier `verify.py` enumerates rational mechanical rotations and their *all-length suffix-truncations*, and independently determines fixed-window and zero-padded shattering using exact rational phase-cell geometry. The eight test cases, including \(233/610\) and \(377/610\) at a twelve-coordinate horizon, yielded **7,808 agreement checks** for supports of sizes zero through four; every case passed. These finite rational tests check the criterion and truncation bookkeeping, but do not establish the theorem for irrational slopes. The all-irrational arguments are Steps 1–7 above.

For the slope \(\alpha=(\sqrt5-1)/2>1/2\), the support \(\{0,2,4\}\) is explicitly shattered. In the order \(000,001,010,011,100,101,110,111\), witnesses \((t,L)\), meaning an \(L\)-symbol factor beginning at offset \(t\), are \((0,1),(0,5),(2,3),(2,5),(1,1),(8,5),(1,3),(4,5)\), respectively, using the mechanical coding \(w_t=\mathbf1_{\{\{(t+1)\alpha\}<\alpha\}}\). Every factor is nonempty.

Reproduce the finite comparison with `python verify.py` (Python standard library only).

## Relationship to prior work

M.-P. Muller (2005) established that Sturmian words have mask/sliding-window VC dimension two, according to the accessible published abstract. That result is explicitly **not** claimed new. H. Johnson (arXiv:2101.06490, initially public January 16, 2021), Section 2, defines the variable-length factor VC dimension and proves it differs from sliding-window dimension by at most one, and Section 4 poses the question of whether a Sturmian word could have infinite dimension. Combining Muller's fixed-window result with Johnson's inequality already gives the finite upper bound three; finiteness alone is therefore not presented as an original consequence here. The contribution assessed is the exact *slope dichotomy*, all-support geometric classification, and resulting pair-density spectrum, which are not implications of those coarse bounds.

Related published work on Sturmian words includes Fici et al. (2016) on abelian powers and other combinatorial properties of their factors. A semantic search of published mathematical finding records for Sturmian shattering, irrational rotation, masks, and finite factors found adjacent work on shift conjunctions and binary pattern constraints, not an equivalent all-support theorem. These searches cannot establish absolute priority. The complete text of Muller's 2005 preprint was not obtainable during this assessment, creating an explicit historical-overlap risk.

## Limitations

The result concerns binary Sturmian factor languages with **symbol-one frequency \(\alpha\)**, and the specific zero-padded variable-length factor notion. It does not characterize the Littlestone dimension, arbitrary finite binary words, general low-complexity subshifts, or non-Sturmian rotation codings. The criterion for large-slope shattered triples is geometric rather than a closed formula for their number at a finite horizon. The reproducible finite tests use rational rotations solely as checks; no finite enumeration proves the irrational all-order claim. While primary source inspection and semantic searches found no implication covering the exact theorem, the unavailable Muller full text and unindexed alternate terminology are residual novelty risks. No independent audit is asserted.

## References

1. H. R. Johnson, *Binary strings of finite VC dimension*, arXiv:2101.06490 (first posted 2021-01-16), https://arxiv.org/abs/2101.06490 . Definition of variable-length VC dimension, Propositions 1–3, Corollary 1, and Section 4.
2. M.-P. Muller, *Suites de Sturm, complexité et dimension de Vapnik-Chervonenkis*, preprint (2005), https://hal.science/hal-00129709 ; accessible abstract at https://www.researchgate.net/publication/228966434_Suites_de_Sturm_complexite_et_dimension_de_Vapnik-Chervonenkis . Earlier sliding-window/mask dimension two.
3. J.-P. Allouche, *Surveying some notions of complexity for finite and infinite sequences*, survey (2012), https://paperzz.com/doc/6978862/surveying-some-notions-of-complexity-for-finite-and-infin... ; bibliography includes Muller (2005).
4. G. Fici et al., *Abelian powers and repetitions in Sturmian words*, *Theoretical Computer Science* (2016), https://doi.org/10.1016/j.tcs.2016.04.039 . Sturmian factor-language context.
