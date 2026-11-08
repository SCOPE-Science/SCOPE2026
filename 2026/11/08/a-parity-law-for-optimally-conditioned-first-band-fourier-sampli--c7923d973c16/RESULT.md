# A parity law for optimally conditioned first-band Fourier sampling on ternary spheres

## Finding
For every integer \(d\ge4\), write \(G=\mathbb F_3^d\) and let
\[
S_j=\{x\in G:\; x_1^2+\cdots+x_d^2=j\text{ in }\mathbb F_3\},\qquad j=0,1,2.
\]
Let \(H_1\) be the \((2d+1)\)-dimensional space of complex functions spanned by the constant character and the \(2d\) nontrivial coordinate characters \(x\mapsto\exp(\pm2\pi i x_r/3)\). Restrict these characters to \(S_j\) with **uniform probability measure on that sphere**. Denote their Gram operator by \(K_{d,j}\) and its squared spectral condition number (largest eigenvalue divided by the smallest) by \(\kappa_{d,j}\), taking \(+\infty\) if singular.

**Sharp radius-selection theorem.** For each \(d\ge4\), exactly one of the three radii minimizes \(\kappa_{d,j}\):
\[
\boxed{j_*(d)=0\text{ if }d\text{ is even};\qquad j_*(d)=1\text{ if }d\text{ is odd}.}
\]
The exact sharp minimum has three closed forms. For even \(d\), set \(X=3^{d/2}\); for odd \(d\), set \(X=3^{(d-1)/2}\), \(s=(-1)^{(d-1)/2}\), and \(R=\sqrt{8d+1}\). Then
\[
\boxed{\displaystyle
\min_{j=0,1,2}\kappa_{d,j}=
\begin{cases}
\dfrac{X+3}{X+2-2d},&d\equiv0\pmod4,\\[4pt]
\dfrac{X-2+2d}{X-3},&d\equiv2\pmod4,\\[4pt]
\dfrac{2X+s+R}{2X+s-R},&d\text{ odd}.
\end{cases}}
\]
All three Gram operators are positive definite except \(K_{4,2}\), whose nullity is one. When \(d\) is even, the optimal radius-zero Gram operator has only **two** distinct eigenvalues, one with multiplicity \(2d\) and one with multiplicity one.

Moreover, a complete spectrum for **each** radius is available without diagonalizing large matrices. Define
\[
N_e(j)=\sum_{\substack{0\le r\le e\\r\equiv j\;(\mathrm{mod}\,3)}}\binom er2^r,\quad
 g=\frac{N_{d-1}(j)-N_{d-1}(j-1)}{N_d(j)},\quad
 h=\frac{N_{d-2}(j)-2N_{d-2}(j-1)+N_{d-2}(j-2)}{N_d(j)},
\]
with subscripts in \(\mathbb Z/3\mathbb Z\). The entire spectrum (including coincidences and multiplicities) is
\[
\boxed{\operatorname{spec}(K_{d,j})=
\{1-g\}^{[d]}\cup\{1+g-2h\}^{[d-1]}
\cup\operatorname{spec}\!\begin{pmatrix}
1&\sqrt{2d}\,g\\\sqrt{2d}\,g&1+g+2(d-1)h
\end{pmatrix}.}
\]
Here the exponent in square brackets denotes multiplicity.

## Assumptions and scope
Fix \(\omega=\exp(2\pi i/3)\) and the orthonormal character set \(E=\{0,\pm e_1,\ldots,\pm e_d\}\) under uniform probability measure on \(G\). The matrix of conditional restriction is \((K_{d,j})_{a,b}=|S_j|^{-1}\sum_{x\in S_j}\omega^{(b-a)\cdot x}\), indexed by \(a,b\in E\). Thus the columns are normalized in the **ambient** cube, whereas sampling uses conditional sphere measure. This choice does not affect \(\kappa\): multiplying the sphere measure by a common positive factor rescales all eigenvalues equally. The claim does **not** concern the full character table, higher Fourier degrees, a general odd prime-power field, or anisotropic quadratic forms. The integer \(d=4\) is included and is the only singular boundary case in the stated range.

## Proof
**1. Exact character and counting identities.** Since \(x^2=1\) for both nonzero elements of \(\mathbb F_3\), \(Q(x)\) is simply the number of nonzero coordinates reduced modulo three. Character orthogonality gives the roots-of-unity filter
\[
N_e(j)=\frac{3^e+2\Re\bigl(\omega^{-j}(i\sqrt3)^e\bigr)}{3},\qquad |S_j|=N_d(j).
\]
Condition on one coordinate being zero versus nonzero. The conditional mean of either nontrivial one-coordinate character is \(g\), as displayed above, because the sum of its values on the two nonzero symbols equals \(-1\). Conditioning on two distinct coordinates gives \(h\), since the four nonzero-symbol choices sum to \(+1\). Thus the Gram entries are \(1\) on the diagonal, \(g\) between the constant and any coordinate character or between opposite characters on one coordinate, and \(h\) between characters on two distinct coordinates. There are no other cases.

**2. Invariant subspaces.** For each coordinate, take the difference of its two character basis vectors. These \(d\) orthogonal differences are eigenvectors of eigenvalue \(1-g\). The sums of the two character vectors at each coordinate, subject to their \(d\) coefficients summing to zero, form a \((d-1)\)-dimensional eigenspace of eigenvalue \(1+g-2h\). The orthogonal complement is spanned by the constant vector and the normalized sum of all \(2d\) coordinate vectors. The Gram matrix there is exactly the displayed \(2\)-by-\(2\) block. This proves the full spectral law and its multiplicities for every \(d,j\).

**3. Exact parameters.** For even \(d\), put \(X=3^{d/2}\), \(s=(-1)^{d/2}\), \(a=s/(X+2s)\), \(b=s/(X-s)\). Substitution in the roots-of-unity filter gives
\[
(g,h)_{j=0}=(-a,-a),\quad
(g,h)_{j=1}=(-b,2b),\quad
(g,h)_{j=2}=(2b,-b).
\]
At radius zero the eigenvalues are \(1+a\) (multiplicity \(2d\)) and \(1-2da\) (multiplicity one). Hence its condition number is the first or second boxed expression, according to \(s=+1\) or \(s=-1\). At radius two the exact ratios are
\[
\kappa_{d,2}=
\begin{cases}
(X+3)/(X-1-2d),&s=+1,\\
(X+1+2d)/(X-3),&s=-1,
\end{cases}
\]
where the first is infinite at \(d=4\). Each strictly exceeds \(\kappa_{d,0}\).

At radius one the smaller/larger Rayleigh quotients on the known invariant spaces bound the condition number from below:
\[
\kappa_{d,1}\ge
\begin{cases}
\dfrac{1+(4d-5)b}{1-5b}=\dfrac{X+4d-6}{X-6},&s=+1,\\[5pt]
\dfrac{1-5b}{1+(4d-5)b}=\dfrac{X+6}{X+6-4d},&s=-1.
\end{cases}
\]
All denominators are positive. Cross-multiplication against \(\kappa_{d,0}\) leaves, respectively,
\[
(2d-1)X-8d^2+20d+6>0,\qquad
(2d-1)X+8d^2-20d-6>0.
\]
For the first inequality, \(d=4\) is direct, and \(d\ge8\) has \(X\ge4d\). The second is immediate for \(d\ge6\). Thus radius zero is the unique optimum in every even dimension.

For odd \(d=2k+1\), set \(X=3^k\), \(s=(-1)^k\), \(R=\sqrt{8d+1}\), and \(Q=\sqrt{4d^2-4d+9}\). The roots-of-unity identity gives
\[
(g,h)_{j=0}=(s/X,-s/X),\quad
(g,h)_{j=1}=(-s/(X+s),0),\quad
(g,h)_{j=2}=(0,s/(X-s)).
\]
The entire radius-one spectrum has extreme eigenvalues \((2X+s\pm R)/(2(X+s))\), with all other levels strictly between them. This yields the third boxed formula. The other two condition numbers evaluate to
\[
\kappa_{d,2}=
\begin{cases}(X+2d-3)/(X-3),&s=+1,\\ (X+3)/(X+3-2d),&s=-1,\end{cases}
\]
\[
\kappa_{d,0}=
\begin{cases}2(X+3)/(2X+3-2d-Q),&s=+1,\\ (2X+2d-3+Q)/(2(X-3)),&s=-1.\end{cases}
\]
All relevant denominators are positive for \(d\ge5\). To compare the three radii without approximations, note \(Q>2d-1\). If \(s=+1\), then
\[
\kappa_{d,0}>\frac{X+3}{X+2-2d}>\kappa_{d,2},
\]
where the final cross-product difference equals \(X+4d^2-10d-3>0\). Also \(\kappa_{d,1}<\kappa_{d,2}\) is equivalent to
\[
R(X+d-3)<d(2X+1).
\]
At \(d=5\) this follows from \(\sqrt{41}<7\); at every \(d\ge9\) in this parity class, \(R<d\) and \(X>d-4\). Thus radius one is optimal if \(s=+1\).

If \(s=-1\), \(R\le d+1\) and \(X>d\) for every \(d\ge7\). The inequality \(\kappa_{d,1}<\kappa_{d,2}\) is equivalent to
\[
R(X+3-d)<d(2X-1),
\]
which follows from \(R\le d+1\) since the remaining positive difference is \((d-1)X+d^2-3d-3\). Finally,
\[
\kappa_{d,0}>\frac{X+2d-2}{X-3}>\kappa_{d,1};
\]
the latter inequality follows after cross-multiplication from \((2d+1)(2X-1)>R(2X+2d-5)\), whose difference remains at least \(2d(X-d)+d+4>0\) when \(R\) is replaced by its upper bound \(d+1\). Hence radius one is the unique optimum for odd \(d\).

**4. Positivity and boundary.** The formulas above show that all denominators defining the finite condition numbers are positive and therefore all spectra are positive, except at \(d=4,j=2\): there the eigenvalue \(1-2d/(3^{d/2}-1)=0\) appears exactly once. In particular, \(K_{d,j}\) is nonsingular in all other stated cases. This completes the proof.

## Verification
Run `python CHECK.py` with Python 3 and NumPy installed. The checker constructs the actual complex Fourier character matrices on every sphere for dimensions four through eight, independently diagonalizes their Gram matrices, and compares the entire eigenvalue lists with the analytical block formula. It also tests the exact root-of-unity counting formula, the optimal radius, the expressions for sharp condition numbers, and nonnegativity across dimensions four through forty-four. The packaged run prints `CHECK_OK assertions= 463 max_d_direct=8 max_d_formulas=44`. These finite tests are corroborative; the proof covers every integer dimension at least four.

## Relationship to prior work
Pham and Xue (2026) establish sharp spherical \(L^p\to L^4\) Fourier extension estimates in odd dimensions and discuss sparse Fourier recovery, but not the exact first-coordinate-character Gram spectra or the minimization of their condition numbers across all three radii. Iosevich, Koh, Lee, Pham and Shen study sharp extension estimates for zero- and nonzero-radius finite-field spheres, rather than this finite-dimensional sampling-design objective.

Published spectral calculations for **one** \(q\)-ary Hamming-weight shell yield degree-one Fourier-band compression spectra and a forced null direction; their results do not directly classify the union of Hamming weights in one residue class modulo three, nor optimize over its three classes. A separate published calculation treats split quadratic cones with first-band characters, which are not the diagonal ternary spheres equipped with this particular coordinate-character band. The counting and symmetry ingredients are standard; the global, strict parity-dependent optimum and its sharp condition numbers are the distinct assertion here. The closest published calculations and the cited papers were compared by their claims and operators, not merely their titles.

## Limitations
Only the specific complete first-degree coordinate-character band is optimized. No assertion is made for other finite fields, higher interaction degrees, arbitrary subsets of a sphere, adjustable sampling weights, or the full-space nonlinear Fourier extension norm. The singularity at \(d=4,j=2\) is an exact finite boundary, not a stability claim under perturbation. General character-sum and association-scheme technology may lead to alternative or historically earlier formulations; priority beyond the inspected sources is not established independently. No independent mathematical audit has been conducted.

## References
1. T. Pham and B. Xue, *Sharp spherical \(L^p\to L^4\) extension estimates over finite fields in odd dimensions*, arXiv:2610.29664v1, first submitted 2026-10-21. https://arxiv.org/html/2610.29664v1
2. A. Iosevich, D. Koh, S. Lee, T. Pham and C.-Y. Shen, *On Restriction Estimates for the Zero Radius Sphere over Finite Fields*, Canadian Journal of Mathematics, 2020. https://www.cambridge.org/core/journals/canadian-journal-of-mathematics/article/on-restriction-estimates-for-the-zero-radius-sphere-over-finite-fields/BD04A06192620C6B701E44B560F81F6A
3. *Exact q-ary Hamming-shell Fourier concentration and the arithmetic tightness criterion*, public research record, 2026-10-11, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-q-ary-hamming-shell-fourier-concentration-and-the-arithmet--89a15e26e594
4. *An all-degree spectral law for Fourier sampling on q-ary Hamming spheres*, public research record, 2026-10-11, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-an-all-degree-spectral-law-for-fourier-sampling-on-q-ary-hamming--f3d01cadaa90
5. *Exact first-band Fourier concentration on split quadratic cones over odd finite fields*, public research record, 2026-10-11, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-first-band-fourier-concentration-on-split-quadratic-cones--dbf8fa8aec40
