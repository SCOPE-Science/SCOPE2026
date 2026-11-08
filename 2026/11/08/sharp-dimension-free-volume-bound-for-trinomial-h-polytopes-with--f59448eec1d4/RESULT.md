# Sharp dimension-free volume bound for trinomial \(h^*\)-polytopes with final coefficient two

## Finding

Let \(k\ge2\), \(a\ge1\) be integers. For any full-dimensional lattice polytope \(P\) with Ehrhart numerator
\[
h^*_P(t)=1+a t^k+2t^{2k},
\]
its normalized volume is at most \(12\), or equivalently \(a\le9\). The bound is sharp for **every** \(k\ge2\): examples with \(a=9\) exist in dimension \(3k-1\). The result closes the optimal volume bound for the final-coefficient-two slice of the dimension-free question in Tsuchiya (2026).

## Assumptions and scope

A lattice polytope means a convex polytope with integral vertices, full-dimensional in its affine lattice. Its Ehrhart series is \(h^*_P(t)/(1-t)^{d+1}\), and its normalized volume is \(h^*_P(1)=d!\operatorname{vol}_{\mathrm{Euclidean}}(P)\). Integers \(a\ge1\) and \(k\ge2\) are arbitrary; dimension and lattice embedding are unrestricted. The theorem is only for the leading coefficient exactly \(2\) and exponents \(k,2k\), not arbitrary trinomial numerators.

## Proof

**1. Group reduction.** Since \(h^*_1=0\), the polytope is an empty lattice simplex. Write \(G=\Lambda_P\subset(\mathbb R/\mathbb Z)^{d+1}\) for its finite simplex group. The height \(\mathrm{ht}(g)\), the sum of coordinate representatives in \([0,1)\), equals \(k\) for all nonzero \(g\) except two distinct elements \(x,y\), for which it equals \(2k\). Also \(|G|=a+3\), the normalized volume. Proposition 4.3 of Tsuchiya (2026) proves that the upper-height elements generate the group, \(G=\langle x,y\rangle\), and that their orders satisfy \(\varphi(\operatorname{ord}x),\varphi(\operatorname{ord}y)\le4\). Thus both orders belong to
\[
\mathscr D=\{2,3,4,5,6,8,10,12\}.
\]
Consequently \(|G|\le144\), and the fundamental theorem of finite abelian groups gives \(G\cong C_m\times C_n\) with \(m\mid n\), \(mn\le144\).

**2. Spectral obstruction.** Scale heights by \(k\): \(f(0)=0\), \(f(g)=1\) for \(g\ne0,x,y\), and \(f(x)=f(y)=2\). For any coordinate character \(\chi:G\to\mathbb R/\mathbb Z\), its contribution to \(\mathrm{ht}(g)+\mathrm{ht}(-g)\) is \(1_{\chi(g)\ne0}\). For a nontrivial complex character \(\psi\) of \(G\), the Fourier transform of that indicator is \(-|\ker\chi|\) if \(\psi\) is trivial on \(\ker\chi\), and zero otherwise. It is therefore nonpositive. On the other hand, direct Fourier transformation of \(k[f(g)+f(-g)]\) gives
\[
2k\bigl(\operatorname{Re}\psi(x)+\operatorname{Re}\psi(y)-1\bigr).
\]
Thus every nontrivial character satisfies the necessary exact restriction
\[
\operatorname{Re}\psi(x)+\operatorname{Re}\psi(y)\le1. \tag{S}
\]

**3. Finite exhaustive obstruction with rational arithmetic.** The accompanying `verify.py` visits *every* \(m\mid n\) with \(12<mn\le144\), every two distinct elements \(x,y\) whose orders lie in \(\mathscr D\), and every nontrivial character of \(C_m\times C_n\). The checker proves a violation of (S) by an exact rational lower bound whenever possible. For \(0\le z<1/2\), write \(X=(44/7)z\), and let
\[
T_{19}(X)=\sum_{j=0}^{19}\frac{(-1)^jX^{2j}}{(2j)!}.
\]
The classical bounds \(223/71<\pi<22/7\), together with the possible denominators at most \(144\), show that \(X\le\pi\). As cosine decreases on \([0,\pi]\) and the alternating-series tail after the negative 19th term is positive, \(\cos(2\pi z)\ge T_{19}(X)\). At \(z=1/2\), cosine is exactly \(-1\). All these lower bounds are fractions, not floating-point estimates.

Out of **46,223** element-pairs above order \(12\), the exact character screen rules out **46,135**. The remaining 88 pairs occur only in three groups: \(C_2\times C_8\) (16 pairs), \(C_4\times C_4\) (48 pairs), and \(C_3\times C_6\) (24 pairs). Enumerating every injective endomorphism, the checker proves that each of those sets is precisely one automorphism orbit, represented by
\[
(C_2\times C_8;(0,1),(1,2)),\quad
(C_4\times C_4;(0,1),(1,0)),\quad
(C_3\times C_6;(0,1),(1,1)).
\]

**4. Exact dual obstructions for the three survivors.** Each group is equipped in `verify.py` with an explicit rational coefficient vector \(v=(v_g)_{g\ne0}\). For each representative pair \(x,y\), it verifies by exact fraction operations that
\[
\sum_{g\ne0}v_g\,[1+1_{g=x}+1_{g=y}]=-1,
\qquad
\sum_{g\ne0}v_g\,\{\chi(g)\}\ge0
\]
for **every** character \(\chi:G\to\mathbb R/\mathbb Z\), where braces denote the fractional representative in \([0,1)\). But each group-coordinate map of a simplex is one of these characters. Therefore the second inequality would force
\[
\sum_{g\ne0}v_g\,\mathrm{ht}(g)=\sum_{\text{coordinates }i}\sum_{g\ne0}v_g\,\{\chi_i(g)\}\ge0,
\]
whereas the prescribed heights yield the left side \(-k<0\). This contradiction is invariant under group automorphisms. All 88 remaining pairs are impossible. Thus \(|G|\le12\), giving \(a+3\le12\) and \(a\le9\).

**5. Sharpness.** Example 4.5 of Tsuchiya (2026) constructs for every \(b\ge2\) and \(k\ge1\) a lattice simplex of dimension \(3k-1\) with numerator \(1+(3b+3)t^k+b t^{2k}\) and normalized volume \(4(b+1)\). Taking \(b=2\) gives \(1+9t^k+2t^{2k}\) and volume \(12\), for every \(k\ge2\).

## Verification

Run `python3 verify.py` using Python 3.9+ and no third-party libraries. It reports `EXACT_VERIFICATION_PASS`, 46,223 tested element pairs, 46,135 spectral exclusions, 88 exact-dual exclusions, and automorphism orbit sizes 16, 48, 24. The classification is finite **and exhaustive** because the group and order bounds from Proposition 4.3 are mathematical premises, not a computational cutoff imposed on an unbounded problem. The checker uses `fractions.Fraction` for every numerical inequality and enumerates the complete character and automorphism sets. Its rational witness vectors and loops are included, not externally hosted.

## Relationship to prior work

Tsuchiya (2026) establishes \(|G|\le(8b^2)^b\) in this regime and poses the determination of the optimal bound depending only on \(b\). His Example 4.5 gives the lower bound \(4(b+1)\). At \(b=2\), the present upper bound \(12\) meets his lower construction and therefore completely resolves this fixed-leading-coefficient case. The 2015 Higashitani–Nill–Tsuchiya classification treats palindromic (Gorenstein) trinomial numerators; the present non-palindromic cases include \(a=9\) and are not a consequence of that special classification. The new contribution is the sharpness proof via the character screen and three rational separating witnesses, not the source's group bound or its examples.

## Limitations

The proof uses Tsuchiya's Proposition 4.3 for the group-generation and element-order reduction. It does not supply a sharp bound for \(b\ge3\), a classification of all equality simplices, or a theorem for general trinomial exponents. The finite verification is a fully specified exact arithmetic certificate; it should be independently rerun for further assurance. Historical priority is assessed against the inspected sources and indexed mathematical records, not guaranteed against all unpublished or unindexed literature. Independent mathematical audit has not been performed.

## References

1. A. Tsuchiya, *Scott-type inequalities for trinomial \(h^*\)-polynomials*, arXiv:2610.35287, first public version 2026-10-26. Proposition 4.3, Example 4.5, and Question 4.6. https://arxiv.org/abs/2610.35287
2. A. Higashitani, B. Nill, A. Tsuchiya, *Gorenstein polytopes with trinomial \(h^*\)-polynomials*, arXiv:1503.05685, 2015. https://arxiv.org/abs/1503.05685
