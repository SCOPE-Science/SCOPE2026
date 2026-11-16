# Sharp checkerboard Hermite sampling and dimension-free optimal derivative design

## Finding

Let \(d\ge2\), let \(PW_{\pi}^{d}\) denote the complex \(L^2(\mathbb R^d)\) Paley–Wiener space with Fourier support in \([-\pi,\pi]^d\), and let
\[
\Lambda=\{n\in\mathbb Z^d:\textstyle\sum_j n_j\equiv0\pmod2\}.
\]
For any real Euclidean-unit vector \(v\in\mathbb R^d\), gain \(\gamma>0\), and complex offset \(c\in\mathbb C\), measure the critically dense two-channel data
\[
\mathcal S_{v,\gamma,c}f=\bigl(f(n),\ c f(n)+\gamma D_v f(n)\bigr)_{n\in\Lambda},\qquad D_v=\sum_{j=1}^d v_j\partial_{x_j}.
\]
Put
\[
L=\|v\|_1,\quad s=\min_{\varepsilon\in\{-1,1\}^{d}}|v\cdot\varepsilon|,\quad
Q=(\operatorname{Re}c)^2+\bigl(|\operatorname{Im}c|+\gamma\pi L/2\bigr)^2,
\]
and for \(0\le z\le L\) set
\[
T_z=2+2Q+\frac{\gamma^2\pi^2z^2}{2},\qquad
\lambda_{\pm}(z)=\frac{T_z\pm\sqrt{T_z^2-4\gamma^2\pi^2z^2}}{4}.
\]
The **exact optimal squared analysis-frame bounds**, in the unweighted physical-sample norm, are
\[
\boxed{A(v,\gamma,c)=\lambda_-(s),\qquad B(v,\gamma,c)=\lambda_+(L).}
\]
Consequently \(\mathcal S_{v,\gamma,c}\) is bounded below, hence admits stable full-bandwidth reconstruction, **if and only if** \(s>0\). If \(s=0\), the operator has a nonzero infinite-dimensional nullspace, for every \(\gamma>0\) and \(c\in\mathbb C\).

Moreover, among **all** real unit directions, all positive gains, and all complex scalar offsets, the unique optimal choices, up to coordinate permutation and sign, are
\[
\boxed{v=\pm e_j,\quad c=0,\quad\gamma=\sqrt2/\pi.}
\]
They simultaneously yield
\[
\boxed{A_*=1-1/\sqrt2,\qquad B_*=1+1/\sqrt2,\qquad
\kappa(\mathcal S)_*=\sqrt{B_*/A_*}=1+\sqrt2.}
\]
Every other admissible design has strictly larger analysis-operator condition number. In particular the global optimal conditioning is independent of dimension.

The singular hyperplanes also have a **sharp quadratic stability law**: along any nonsingular sequence of unit directions for which \(s\downarrow0\), with \(\gamma,c\) fixed and \(v\to v_0\), one has
\[
A(v,\gamma,c)\sim\frac{\gamma^2\pi^2}{4(1+Q_0)}s^2,\quad Q_0=(\operatorname{Re}c)^2+\bigl(|\operatorname{Im}c|+\gamma\pi\|v_0\|_1/2\bigr)^2.
\]

## Assumptions and scope

The Fourier transform is \(\widehat f(\omega)=\int_{\mathbb R^d}f(x)e^{-i\omega\cdot x}\,dx\); Plancherel gives \(\|f\|_2^2=(2\pi)^{-d}\int_{[-\pi,\pi]^d}|\widehat f(\omega)|^2\,d\omega\). All derivatives are classical and bounded, since the Fourier transform has compact support. Data have the squared norm
\[
\|\mathcal Sf\|^2=\sum_{n\in\Lambda}\left(|f(n)|^2+|c f(n)+\gamma D_v f(n)|^2\right).
\]
The condition number is the quotient of the largest and smallest nonzero singular values of this full analysis operator, and is infinite for noninjective designs. The first channel has fixed unit gain; the second channel may contain any complex zero-order term \(c\), but only a real first-order direction \(v\) of Euclidean norm one and a positive real derivative gain \(\gamma\) are optimized. There is no claim about arbitrary filters, general full-rank lattices, different passbands, or other derivative orders.

## Proof

**1. Two-alias Plancherel decomposition.** The subgroup \(\Lambda\) has index two, and its annihilator on the frequency torus is \(\{0,\pi(1,\ldots,1)\}\). Outside a set of measure zero, every frequency \(\omega\in[-\pi,\pi]^d\) belongs to a unique pair \((\omega_-,\omega_+)\), congruent modulo \(2\pi\mathbb Z^d\), with separation \(\omega_+-\omega_-=\pi\varepsilon\), \(\varepsilon\in\{-1,1\}^d\), up to swapping. Parameterize their midpoint by \(u=(\omega_-+\omega_+)/2\in[-\pi/2,\pi/2]^d\). Orthogonality of the parity sublattice reduces the two-channel sample energy to the integral of the squares of the following \(2\times2\) matrix applied to the two Fourier amplitudes:
\[
M_{\varepsilon,u}=\frac1{\sqrt2}\begin{pmatrix}
1&1\\
c+i\gamma(v\cdot u-\pi v\cdot\varepsilon/2)&c+i\gamma(v\cdot u+\pi v\cdot\varepsilon/2)
\end{pmatrix}.
\]
The input integral has the ordinary Euclidean two-amplitude norm. Thus the essential infimum and supremum of the eigenvalues of \(M_{\varepsilon,u}^*M_{\varepsilon,u}\) are the exact squared sampling bounds; this is a unitary fiber statement, not an approximation by finite samples.

**2. Exact extreme fibers.** Write \(m=v\cdot u\) and \(z=|v\cdot\varepsilon|\). The eigenvalues of the squared Gram are
\[
\frac{T\pm\sqrt{T^2-4\gamma^2\pi^2z^2}}4,\quad
T=2+2|c+i\gamma m|^2+\gamma^2\pi^2z^2/2.
\]
This follows from the unscaled matrix's squared Frobenius norm \(T\) and squared determinant \(\gamma^2\pi^2z^2\). For each fixed sign vector, the midpoint variable \(m\) ranges over the *whole* interval \([-\pi L/2,\pi L/2]\). The maximum of \(|c+i\gamma m|^2\) on this interval is exactly \(Q\), attained at an endpoint in the closure. For fixed \(z\), increasing \(T\) strictly decreases the smaller eigenvalue and strictly increases the larger one. Consequently the sharp global lower and upper extrema both use this maximal midpoint term. Endpoints are essential extrema because nearby open frequency sets have positive measure.

**3. Minimizing and maximizing over aliases.** Holding \(Q\) fixed and writing \(w=z^2\), the two unscaled eigenvalues solve \(\mu^2-T_w\mu+\gamma^2\pi^2w=0\), where \(T_w=2+2Q+\gamma^2\pi^2w/2\). The smaller root is strictly below \(2\) and the larger root strictly above \(2\): these inequalities follow from the first row's squared norm \(2\), the second row's nonzero center term, and the min–max principle. Differentiating the quadratic identity shows the smaller root increases strictly and the larger root increases strictly with \(w\). All possible \(z\) are the finitely many values \(|v\cdot\varepsilon|\); their minimum is \(s\) and maximum is \(L\). This proves the displayed exact bounds. If \(s=0\), the determinant vanishes on an entire positive-measure alias cell, giving an infinite-dimensional kernel; if \(s>0\), the continuous fiber singular values are uniformly positive, and fiberwise inversion gives stable reconstruction.

**4. Dominance of coordinate directions and scalar-free channels.** Every real unit vector obeys \(L=\|v\|_1\ge1\), with equality exactly at the signed coordinate vectors. Rademacher averaging gives
\[
2^{-d}\sum_{\varepsilon\in\{-1,1\}^d}(v\cdot\varepsilon)^2=\|v\|_2^2=1,
\]
so \(s\le1\). For fixed \(\gamma\), the lower bound strictly decreases as \(Q\) or \(L\) increases and strictly increases as \(s\) increases; the upper bound strictly increases with \(Q\) and \(L\). The maximal midpoint term \(Q\) is uniquely minimized over \(c\in\mathbb C\) at \(c=0\). Thus, for each fixed gain, every non-coordinate direction or nonzero offset has strictly worse lower and upper bounds than \((v,c)=(e_j,0)\). In particular its condition number is strictly greater, and singular designs have infinite condition number.

**5. Collision asymptotics.** As \(s\to0\), expand the smaller root at the positive trace \(T_0=2+2Q\). The leading term is \(\gamma^2\pi^2s^2/(2T_0)\), and continuity of \(Q\) along \(v\to v_0\) gives the displayed sharp quadratic law. The remainder is of higher order because the discriminant is analytic at this strictly positive trace.

**6. Exact optimal gain.** On a coordinate direction with \(c=0\), put \(q=\gamma^2\pi^2>0\). The two sharp Gram eigenvalues are the roots
\[
A_q,B_q=\frac{2+q\mp\sqrt{(2+q)^2-4q}}4.
\]
Their ratio is uniquely minimized when the positive quantity \((2+q)/\sqrt q=\sqrt q+2/\sqrt q\) is minimized, namely when \(q=2\). Substitution gives \(A_*=1-1/\sqrt2\), \(B_*=1+1/\sqrt2\), and \(\sqrt{B_*/A_*}=1+\sqrt2\). All uniqueness assertions follow from the strict steps above.

## Verification

The standalone Python/NumPy script `verify_bounds.py` independently constructs complex fiber matrices for 6,720 randomly sampled choices of dimension, direction, derivative gain, scalar offset, alias sign, and frequency midpoint. It checks that their Gram eigenvalues remain within the asserted exact sharp bounds, and checks the optimal constants at coordinate directions by direct arithmetic. The checker also verifies 5,760 endpoint fibers and compares directly with a finite 8-by-8 torus model, independently testing normalization. Its successful run reports `CHECK_OK random_fibers= 6720 endpoint_fibers= 5760`, `CHECK_OK minimax`, and `CHECK_OK cyclic_torus=8x8`. These finite numerical checks support but do not establish the universal theorem, which follows from Steps 1–6. The script uses only standard Python and NumPy.

## Relationship to prior work

General one-dimensional Hermite and Fourier-multiplier interpolation has a long history, including Vaaler and Littmann. Gardeazabal-Gutiérrez and Sousa (2025/2026), Theorem 1 and Sections 3.3–3.4, provide a multiplier-matrix invertibility criterion and derivative sampling on a single integer line; the one-dimensional criterion is an antecedent, not a claim of novelty here. Ghosh, Mulleti, and Seelamantula (2026) give a general multidimensional polyphase method with derivative channels and uniform singular-value criteria, which likewise supplies the underlying framework. What is asserted here is the **explicit sharp all-direction bound, signed-subset-sum failure criterion, and global minimax direction/gain/offset design on the index-two checkerboard**, including the dimension-independent optimum; those quantitative design conclusions are not present in the accessible theorem summaries. Existing published studies of finite-group parity-check Fourier sampling and discrete-lattice dynamical sampling address distinct finite-frequency or evolution operators. Their standard character-annihilator ideas are credited rather than claimed new.

## Limitations

The result is restricted to the cube passband, the index-two even-sum sublattice, a value channel plus one first-order real-direction differential channel, and Euclidean sample noise weighting as specified. The optimization does not extend by assertion to anisotropic bandwidths, arbitrary linear differential operators, adaptive measurements, or higher-order sampling. Published full text of the October 2026 motivating work was not accessible in this comparison; its abstract and section-level descriptions were inspected, and possible equivalent formulas in older generalized sampling literature remain a priority risk. No independent mathematical audit has been performed.

## References

1. R. Ghosh, S. Mulleti, C. S. Seelamantula, *Multichannel Sampling and Reconstruction in Multidimensional Shift-Invariant Spaces*, arXiv:2610.36142v1, first public 2026-10-26, https://arxiv.org/abs/2610.36142 .
2. I. Gardeazabal-Gutiérrez, M. Sousa, *Dynamical sampling, derivatives, and interpolation formulas in the Paley–Wiener space*, arXiv:2506.16195v1 (first public 2025-06-19), v2 full text https://arxiv.org/html/2506.16195v2 .
3. *Critical-density lattice dynamical sampling and the silver-ratio instability*, published research note, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-critical-density-lattice-dynamical-sampling-and-the-silver-ratio--06e6e4ce4ac1 .
4. *Exact alias spectra and the binary Nyquist boundary for parity-check Fourier sampling*, published research note, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-alias-spectra-and-the-binary-nyquist-boundary-for-parity-c--75b261de521c .
