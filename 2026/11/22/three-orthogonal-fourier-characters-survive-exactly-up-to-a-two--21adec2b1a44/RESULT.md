# Three orthogonal Fourier characters survive exactly up to a two-to-one mass imbalance on a tetrahedron

## Finding
Let \(x_1,x_2,x_3,x_4\in\mathbb R^3\) be affinely independent, let \(a,b>0\) with \(2a+2b=1\), and define the positive atomic probability measure
\[
\mu=a(\delta_{x_1}+\delta_{x_2})+b(\delta_{x_3}+\delta_{x_4}).
\]
Let \(\mathcal O(\mu)\) denote the maximum number of pairwise orthogonal distinct functions among the real-frequency Fourier characters \(e_\xi(x)=e^{2\pi i\langle\xi,x\rangle}\) in \(L^2(\mu)\). Then the exact capacity is
\[
\mathcal O(\mu)=
\begin{cases}
4,&a=b=1/4,\\
3,&\tfrac12\le a/b\le2\text{ and }a\ne b,\\
2,&a/b<\tfrac12\text{ or }a/b>2.
\end{cases}
\]
Moreover, whenever \(\tfrac12\le a/b\le2\), a three-character orthogonal family can be chosen at frequencies \(\{0,\xi,2\xi\}\) (and is maximum when \(a\ne b\)). When \(a=b\), the same frequency also gives an orthogonal basis \(\{e_{k\xi}:0\le k<4\}\). Thus both the maximal packing number and the existence of a single-frequency character progression are independent of the tetrahedron's shape.

## Assumptions and scope
The measure is supported on precisely four points of affine rank three; no periodic lattice is imposed on frequencies. All weights are strictly positive and are normalized to total mass one. The two equal-mass pairs are indexed as \(x_1,x_2\) and \(x_3,x_4\); any relabelling into two equal-mass pairs yields the same assertion. Orthogonality is with respect to the complex Hilbert inner product in \(L^2(\mu)\). The count concerns orthogonal Fourier characters, not arbitrary orthogonal vectors of \(L^2(\mu)\), nor spectra of infinite self-affine convolutions.

## Proof
**Step 1: all relative phase configurations are realizable.** Since the vectors \(x_2-x_1,x_3-x_1,x_4-x_1\) form a basis of \(\mathbb R^3\), for any four unit complex numbers \(z_j\) there is a real frequency \(\xi\) with
\[
 e^{2\pi i\langle\xi,x_j-x_1\rangle}=z_j/z_1\qquad(2\le j\le4).
\]
Choose real arguments of \(z_j/z_1\) and solve the corresponding invertible real \(3\times3\) linear system. Therefore a Fourier character has phases \(z_1,z_2,z_3,z_4\) at the sites, up to a common phase that does not affect orthogonality. In particular, \(\{e_{k\xi}:0\le k<m\}\) is orthonormal exactly when \(\sum_jw_jz_j^r=0\) for every integer \(1\le r<m\), where \(w=(a,a,b,b)\).

**Step 2: universal upper bounds.** If \(m\) characters are pairwise orthonormal, their weighted value columns form a \(4\times m\) matrix \(V\) satisfying \(V^*V=I_m\), whose \(j\)-th row has squared norm \(mw_j\). Since \(VV^*\) is an orthogonal projection, its diagonal entries are at most one. Thus
\[
 mw_j\le1\quad\text{for all }j.
\]
For \(m=3\), this demands \(a,b\le1/3\), equivalent to \(\tfrac12\le a/b\le2\) because \(a+b=1/2\). For \(m=4\), all four inequalities force \(a=b=1/4\). No five characters can be orthogonal in the four-dimensional Hilbert space.

**Step 3: two orthogonal characters always exist.** Take \(z=(1,-1,1,-1)\), so \(\sum_jw_jz_j=0\) for every \(a,b>0\). Step 1 realizes this phase vector, proving \(\mathcal O(\mu)\ge2\).

**Step 4: construct an orthogonal triple throughout the closed admissible interval.** Suppose \(\tfrac12\le a/b\le2\). Choose angles \(\theta\in[0,\pi/2]\), \(\phi\in[\pi/2,\pi]\) by
\[
 \cos\theta=\sqrt{\frac b{2a}},\qquad
 \cos\phi=-\sqrt{\frac a{2b}},
\]
and set \(z=(e^{i\theta},e^{-i\theta},e^{i\phi},e^{-i\phi})\). Both square roots are at most one exactly in the claimed weight regime. Directly,
\[
\begin{aligned}
\sum_jw_jz_j&=2a\cos\theta+2b\cos\phi=0,\\
\sum_jw_jz_j^2&=2a(2\cos^2\theta-1)+2b(2\cos^2\phi-1)\\
&=2\bigl((b-a)+(a-b)\bigr)=0.
\end{aligned}
\]
Step 1 now supplies \(\xi\) such that \(1,e_\xi,e_{2\xi}\) are mutually orthonormal. The endpoint ratios are included, even though one pair of assigned phase values coincides.

**Step 5: four orthogonal characters when the masses are uniform.** For \(a=b=1/4\), the construction gives \(\theta=\pi/4\) and \(\phi=3\pi/4\). Consequently the four phases are the four fourth roots of \(-1\), arranged in some order; their power sums vanish for powers one, two, and three. Therefore \(\{e_{k\xi}:0\le k<4\}\) is an orthonormal basis. Steps 2–5 establish all cases and the arithmetic-progression assertion.

## Verification
The independent-of-shape reduction uses an invertible affine difference matrix, and no computation of that matrix is needed to establish existence. The supplementary standalone `checker.py` evaluates the stated closed-form phase construction for 1,001 evenly spaced ratios in the entire closed interval \([1/2,2]\), verifies the resulting weighted \(3\times3\) Gram matrix, tests the four-character uniform case, and checks representative exterior ratios and two-character examples. All tests passed when executed from the included source file. These finite diagnostics are not substituted for the universal analytic proof above.

## Relationship to prior work
Li and Wang (published 29 July 2026) analyze maximal mutually orthogonal exponentials for a class of **infinite**, uniformly weighted four-digit self-affine measures in \(\mathbb R^3\), using their Fourier-mask zero sets and rational dilation assumptions. Their Theorem 2 and Corollary 1 neither assert nor imply the exact nonuniform, **four-atomic** phase diagram here. Classical finite spectral-measure theory explains why four orthogonal exponentials force equal atom masses; it does not by itself furnish the explicit three-character arithmetic-progression construction throughout the sharp nonuniform interval. Work on maximal orthogonal systems for Lebesgue-measure cubes studies a different measure and a different distinction (inclusion-maximal versus complete systems). The distinction between maximum cardinality and maximal-by-inclusion is retained here.

## Limitations
No claim is made for arbitrary four positive weights lacking the two-pair symmetry, for affinely dependent support, for frequencies restricted to a lattice, or for the number of inclusion-maximal incomplete sets. The row-norm obstruction is standard; the exact attainability result is limited to this natural one-parameter two-orbit family. There may be earlier equivalent weighted trigonometric-quadrature or partial complex-Hadamard formulations that were not indexed by the searches reported in the review.

## References
1. Y.-Q. Li and Z.-M. Wang, *The Number of Orthogonal Exponential Functions of a Class of Self-Affine Measures in \(\mathbb R^3\)*, **Axioms** 15 (2026), 563; first publicly posted 29 July 2026. https://doi.org/10.3390/axioms15080563 .
2. M. N. Kolountzakis, N. Lev and M. Matolcsi, *Maximality and completeness of orthogonal exponentials on the cube*, arXiv:2410.12387, initially submitted 2024; https://arxiv.org/abs/2410.12387 .
3. P. E. T. Jorgensen and S. Pedersen, *Dense analytic subspaces in fractal \(L^2\)-spaces*, **J. Anal. Math.** 75 (1998), 185–228; cited as foundational spectral-measure context, not as a source of this threshold.
