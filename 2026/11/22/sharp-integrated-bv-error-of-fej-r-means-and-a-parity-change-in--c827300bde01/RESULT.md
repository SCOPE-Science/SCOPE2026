# Sharp integrated BV error of Fejér means and a parity change in extremal rigidity

## Finding
Let \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\) carry unnormalized arc-length measure \(dx\). For each integer \(n\ge1\), define the Fejér density and positive convolution operator by
\[
K_n(t)=\frac{1}{2\pi n}\left(\frac{\sin(nt/2)}{\sin(t/2)}\right)^2,
\qquad (T_nf)(x)=\int_{-\pi}^{\pi}K_n(t)f(x-t)\,dt.
\]
The density is defined at removable singularities by continuity and has integral one. With \(|Df|(\mathbb T)\) the distributional Jordan variation, the *exact* induced approximation-error seminorm is
\[
\boxed{C_n:=\sup_{0<|Df|(\mathbb T)<\infty}\frac{\|T_nf-f\|_{L^1(\mathbb T)}}{|Df|(\mathbb T)}
=\frac\pi2-\frac4\pi\sum_{\substack{1\le k<n\\k\ \mathrm{odd}}}\frac{1-k/n}{k^2}.}
\]
For each fixed \(n\), equality holds **if and only if** (up to a.e. changes) \(f\) is a nonconstant two-level function whose higher level occupies an arc of length \(\pi\), with arbitrary rotation and interchange of levels.

For a nonconstant indicator of a single arc of length \(\ell\), put \(d=\min\{\ell,2\pi-\ell\}\). Its error divided by its variation is
\[
C_n(d)=d-\frac{d^2}{2\pi}-\frac2\pi\sum_{k=1}^{n-1}\frac{(1-k/n)(1-\cos(kd))}{k^2},\qquad 0<d\le\pi.
\]
It is strictly increasing on \((0,\pi)\). If \(\delta=\pi-d\downarrow0\), its deficit from the optimum has the *different exact leading orders*
\[
\boxed{C_n-C_n(\pi-\delta)=
\begin{cases}
\displaystyle \frac{\delta^2}{2\pi n}+O_n(\delta^4),& n\text{ odd},\\[5pt]
\displaystyle \frac{n\delta^4}{48\pi}+O_n(\delta^6),& n\text{ even}.
\end{cases}}
\]
Finally, with Euler's constant \(\gamma\), the sharp all-degree error has a parity-separated asymptotic expansion:
\[
\boxed{C_n=\frac{2}{\pi n}\bigl(\log(2n)+\gamma+1\bigr)
+\frac{1}{\pi n^3}\begin{cases}-1/3,&n\text{ even},\\2/3,&n\text{ odd},\end{cases}
+O(n^{-5}).}
\]

## Assumptions and scope
All functions are real-valued elements of periodic \(BV(\mathbb T)\), understood up to a.e. equality. Total variation counts the jump at the periodic seam as well as interior jumps. Norms in the statement use **unnormalized** Lebesgue arc length \(dx\) on a circle of circumference \(2\pi\). The density \(K_n\) is normalized so that \(\int_\mathbb T K_n=1\); consequently \(T_n1=1\). An arc is a connected proper interval of the circle, identified modulo null sets. All equality classifications assume \(|Df|>0\). The \(O_n\) remainders allow a constant depending on fixed \(n\), whereas the final \(O(n^{-5})\) concerns integer \(n\to\infty\).

## Proof
**1. An arc leakage identity.** More generally, let \(K\in L^1(\mathbb T)\) be an even, nonnegative probability density and set \(T_Kf=K*f\). If \(A\subset\mathbb T\) is an arc of length \(0<\ell<2\pi\), positivity gives \(0\le T_K\mathbf1_A\le1\). The integral of the absolute error over \(A\) equals the mass leaking from \(A\) to its complement; equality of incoming and outgoing mass gives
\[
\frac{\|T_K\mathbf1_A-\mathbf1_A\|_1}{2}
=\int_A\int_{A^c}K(x-y)\,dy\,dx
=2\int_0^\pi K(t)\min\{t,\ell,2\pi-\ell\}\,dt.
\]
The last equality follows by translating the arc and counting the length of \(A\setminus(A+t)\). On writing \(d=\min\{\ell,2\pi-\ell\}\le\pi\), let
\[
Q_K(d)=2\int_0^\pi K(t)\min\{t,d\}\,dt.
\]
Then \(Q_K'(d)=2\int_d^\pi K(t)\,dt\ge0\) for \(0<d<\pi\). If \(K>0\) a.e., it is strictly positive and only half-circles maximize \(Q_K\).

**2. Reduction of all BV inputs and equality rigidity.** By the coarea formula for real periodic BV functions, for almost every level \(s\) the superlevel set \(E_s=\{f>s\}\) is a finite union of disjoint arcs, and
\[
|Df|(\mathbb T)=\int_{\mathbb R}\operatorname{Per}(E_s)\,ds.
\]
The layer-cake formula, linearity and the triangle inequality imply
\[
\|T_Kf-f\|_1\le\int_{\mathbb R}\|T_K\mathbf1_{E_s}-\mathbf1_{E_s}\|_1\,ds.
\]
For a set comprising \(r\) disjoint arcs, splitting its indicator into arc indicators gives an error at most \(2rQ_K(\pi)=\operatorname{Per}(E_s)Q_K(\pi)\). Thus the global sharp norm is at most \(Q_K(\pi)\), attained by any half-circle indicator. If \(K>0\) a.e., a union of two or more arcs has *strictly* smaller error than the sum of their separate errors: indeed the latter counts positive kernel flux between distinct components as leakage although their union does not. For one arc of non-half length, Step 1 is strict. Therefore global equality for nonconstant \(f\) forces almost every nontrivial superlevel to be a half-circle. Because these superlevels are nested and all have length \(\pi\), they coincide up to null sets. Hence \(f\) has exactly two levels on complementary half-circles. This also proves sufficiency.

**3. Exact Fejér formula and arc profile.** The familiar finite Fourier expansion is
\[
K_n(t)=\frac1{2\pi}\left(1+2\sum_{k=1}^{n-1}(1-k/n)\cos(kt)\right).
\]
Integrating \(2tK_n(t)\) over \([0,\pi]\), and using \(\int_0^\pi t\cos(kt)dt=((-1)^k-1)/k^2\), proves the displayed exact \(C_n\). Alternatively, integrating the kernel over two arcs produces
\[
C_n(d)=d-\frac{d^2}{2\pi}-\frac2\pi\sum_{k=1}^{n-1}(1-k/n)\frac{1-\cos(kd)}{k^2}.
\]
The Fejér kernel has only finitely many zeros, so the strict inequality and the complete BV equality classification in Steps 1–2 apply even though the density need not decrease radially.

**4. A parity change in extremal rigidity.** Differentiating the arc identity yields \(C_n'(d)=2\int_d^\pi K_n(t)dt\) and \(C_n''(d)=-2K_n(d)\). Thus, for \(\delta>0\),
\[
C_n-C_n(\pi-\delta)=2\int_0^\delta(\delta-u)K_n(\pi-u)\,du.
\]
For odd \(n\), the explicit sine quotient gives \(K_n(\pi-u)=1/(2\pi n)+O_n(u^2)\), producing the quadratic term. For even \(n\), the kernel vanishes to second order at the antipode, with \(K_n(\pi-u)=nu^2/(8\pi)+O_n(u^4)\); since \(\int_0^\delta(\delta-u)u^2du=\delta^4/12\), the deficit is \(n\delta^4/(48\pi)+O_n(\delta^6)\).

**5. The logarithmic law and parity-dependent cubic term.** Let \(m=\lfloor n/2\rfloor\), \(S_m=\sum_{j=0}^{m-1}(2j+1)^{-1}\), and \(R_m=\sum_{j=m}^{\infty}(2j+1)^{-2}\). The exact norm equals
\[
C_n=\frac4\pi\left(R_m+\frac{S_m}{n}\right).
\]
Euler–Maclaurin expansion of the harmonic sums gives
\[
S_m=\frac12\log(4m)+\frac\gamma2+\frac1{48m^2}+O(m^{-4}),
\qquad R_m=\frac1{4m}-\frac1{48m^3}+O(m^{-5}).
\]
Substitution first for \(n=2m\) and then for \(n=2m+1\), expanding \(\log(n-1)\) in the latter case, gives the two displayed cubic coefficients. In both parities the nominal even inverse powers cancel, and the stated remainder is \(O(n^{-5})\) using the next standard Euler–Maclaurin terms.

## Verification
A standalone Python program, `verify_fejer_bv.py`, independently compares the Fourier arc formula with direct kernel quadrature, tests strict half-circle maximality, measures the parity-dependent quadratic/quartic deficits, tests the two cubic asymptotics, and performs Fourier-grid checks on independent periodic multijump inputs. These are finite numerical corroborations, not substitutes for Steps 1–5. Run using `python verify_fejer_bv.py` with NumPy and SciPy available. The exact result itself requires neither software nor a computational certificate.

## Relationship to prior work
López-Bonilla, Vidal Beltrán and Yalja Montiel (2007) give the standard Fejér and Dirichlet kernel formulas and a kernel identity; their inspected four-page paper does not evaluate the sharp periodic BV-to-integrated-error coefficient or its equality and parity rigidity. Nochetto and Salgado (first posted 2012-11-05) construct a variation-diminishing finite-element interpolant and give approximation estimates in another setting, not this Fejér operator. Gaubert and Qu (first posted 2013-02-21) give a Dobrushin coefficient for Hopf's oscillation seminorm of Markov maps, not the norm of \(T_n-I\) from BV variation to \(L^1\). Kravitz and Steinerberger (2020) optimize discrete derivative smoothing in \(\ell^2\), a different norm and operator family.

Two close published research results were compared by statement. *Exact optimal two-jump Poisson leakage and its logarithmic boundary law* (2026-11-01) concerns the Poisson semigroup and one binary two-jump family; its strictly positive antipodal kernel yields quadratic arc rigidity and does not give Fejér's even-degree **quartic** rigidity or its finite-degree harmonic constant. *The sharp Lipschitz contraction deficit of Fejér means* (2026-10-26) concerns \(\operatorname{Lip}(T_nf)/\operatorname{Lip}(f)\), rather than \(\|(T_n-I)f\|_1/|Df|\). Neither implication gives the theorem here. Classical approximation-kernel texts may nevertheless contain equivalent integrated-error constants or moment identities; the result is not claimed independently priority-certified.

## Limitations
The result applies only to real periodic one-dimensional BV functions, to the ordinary nonnegative Fejér kernel, and to unnormalized integrated \(L^1\) approximation error. It does not assert analogous rigidity for Dirichlet partial sums, higher-order Cesàro transforms, weights, or multidimensional data. The coarea reduction establishes the full equality classification only because the kernel is positive almost everywhere. The exact finite sum could conceivably appear under an alternate name in older harmonic-analysis literature, which remains a priority risk.

## References
1. J. López-Bonilla, S. Vidal Beltrán and J. Yalja Montiel, *A note on Dirichlet and Fejér kernels*, Revista de Matemática: Teoría y Aplicaciones 14 (2007), 101–104, DOI:10.15517/rmta.v14i1.283. https://doi.org/10.15517/rmta.v14i1.283 (publication year verified; exact initial public day not verified).
2. R. H. Nochetto and A. J. Salgado, *A Total Variation Diminishing Interpolation Operator and Applications*, arXiv:1211.1069v1, first posted 2012-11-05. https://arxiv.org/abs/1211.1069.
3. S. Gaubert and Z. Qu, *Dobrushin ergodicity coefficient for Markov operators on cones, and beyond*, arXiv:1302.5226v1, first posted 2013-02-21. https://arxiv.org/abs/1302.5226.
4. N. Kravitz and S. Steinerberger, *The smoothest average: Dirichlet, Fejér and Chebyshev*, arXiv:2007.13700v1, first posted 2020-07-27. https://arxiv.org/abs/2007.13700.
5. *Exact optimal two-jump Poisson leakage and its logarithmic boundary law*, published 2026-11-01. https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-exact-optimal-two-jump-poisson-leakage-and-its-logarithmic-bound--5a5f88c645ff.
6. *The sharp Lipschitz contraction deficit of Fejér means*, published 2026-10-26. https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-the-sharp-lipschitz-contraction-deficit-of-fej-r-means--8aa63d6abf65.
