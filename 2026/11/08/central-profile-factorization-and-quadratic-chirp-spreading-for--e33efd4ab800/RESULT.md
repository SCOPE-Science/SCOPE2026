# Central-profile factorization and quadratic-chirp spreading for finite Heisenberg spectrograms

## Finding
Let \(q\) be any odd prime power, \(n\geq1\), and \(N=q^{2n+1}\). For the explicitly defined coordinate-modulated, right-translated short-time Fourier transform on the finite Heisenberg group, the self-transform of any nonzero central-profile window has **exact support**
\[
\big|\operatorname{supp}V_g g\big|=(N-q)r^2+a,
\]
where \(r\) is the number of nonzero one-dimensional Fourier coefficients of its central profile and \(a\) is the number of nonzero entries in that profile's one-dimensional ambiguity function. This identity includes all nontrivial central profiles, without a support or nonvanishing hypothesis.

For the nondegenerate quadratic central profile \(U(z)=\psi(\alpha z^2+\beta z)\), \(\alpha\ne0\), the nonzero spectrogram values have exactly two magnitudes: \(q\) coefficients of modulus \(1\) and \((N-q)q^2\) coefficients of modulus \(1/q\). The remaining \(N^2-q-(N-q)q^2\) coefficients vanish. Its normalized spectrogram entropy is exactly
\[
\log N+2\left(1-\frac qN\right)\log q.
\]
The same normalized central chirp under coordinatewise *abelian* translations has only \(N\) nonzero self-transform coefficients, all of modulus \(1\), and entropy \(\log N\). Therefore the explicit noncommutative spreading excess is \(2(1-q/N)\log q\).

## Assumptions and scope
Work over the finite field \(\mathbb F_q\) of odd order. Fix a nontrivial additive character \(\psi:\mathbb F_q\to\mathbb C\), and write \(H=\mathbb F_q^n\times\mathbb F_q^n\times\mathbb F_q\). Endow \(H\) with the Heisenberg multiplication
\[
(x,y,z)(a,b,c)=(x+a,y+b,z+c+\tfrac12(x\cdot b-y\cdot a)).
\]
Here \(\tfrac12\) means the multiplicative inverse of \(2\) in the field; the dot products are the standard bilinear pairings. Thus \(|H|=N\). Coordinates of \(H\) are used only to define modulation, and the group operation is used for right translation.

For a nonzero function \(U:\mathbb F_q\to\mathbb C\), set \(E=\sum_z|U(z)|^2\) and the unit-norm window
\[
g(x,y,z)=\frac{U(z)}{q^n\sqrt E}.
\]
For \(u\in H\) and a coordinate modulation frequency \(\xi=(P,Q,W)\in\mathbb F_q^{2n+1}\), define
\[
V_g g(u,\xi)=\sum_{(x,y,z)\in H}g(x,y,z)\overline{g((x,y,z)u^{-1})}\,\psi(-P\cdot x-Q\cdot y-Wz).
\]
The sign and normalization conventions are part of the assertion; the transform is not an irreducible-representation coefficient transform. Write
\[
\widehat U(k)=\sum_{z\in\mathbb F_q}U(z)\psi(-kz),\qquad
A_U(c,W)=\sum_zU(z)\overline{U(z-c)}\psi(-Wz).
\]
Let \(r=|\{k:\widehat U(k)\ne0\}|\) and \(a=|\{(c,W):A_U(c,W)\ne0\}|\). All sums and supports are over the full finite groups indicated.

## Proof
**1. Translate the central variable.** Inversion in the displayed two-step group gives \(u^{-1}=(-a,-b,-c)\). Consequently, if \(u=(a,b,c)\), then
\[
(x,y,z)u^{-1}=(x-a,y-b,z-c-\ell_{a,b}(x,y)),\qquad
\ell_{a,b}(x,y)=\tfrac12(x\cdot b-y\cdot a).
\]
After inserting the central profile, the coefficient is
\[
V_g g(u,\xi)=\frac1{q^{2n}E}\sum_{x,y,z}U(z)\overline{U(z-c-\ell_{a,b}(x,y))}\psi(-P\cdot x-Q\cdot y-Wz).
\]

**2. Central translations.** When \((a,b)=0\), the horizontal character sums are zero unless \(P=Q=0\). At \(P=Q=0\), the \(q^{2n}\) horizontal terms cancel the normalization, leaving precisely
\[
V_g g((0,0,c),(P,Q,W))=\begin{cases}A_U(c,W)/E,&P=Q=0,\\0,&\text{otherwise}.\end{cases}
\]
In total, these \(q\) translation rows contribute exactly \(a\) nonzero coefficients.

**3. Noncentral translations and factorization.** Fix \((a,b)\ne0\). Then \(\ell_{a,b}\) is a nonzero linear functional on \(\mathbb F_q^{2n}\), and each fiber has cardinality \(q^{2n-1}\). Summation along its kernel vanishes unless \((P,Q)\) is proportional to its defining covector, that is,
\[
(P,Q)=(\lambda b/2,-\lambda a/2)
\]
for a *unique* \(\lambda\in\mathbb F_q\). In this case the Fourier sum over \((x,y)\) is \(q^{2n-1}\) times the sum over the scalar \(h=\ell_{a,b}(x,y)\). Substitute \(w=z-c-h\) and separate the sums:
\[
\begin{aligned}
V_g g((a,b,c),(\lambda b/2,-\lambda a/2,W))
&=\frac1{qE}\sum_{h,z}U(z)\overline{U(z-c-h)}\psi(-\lambda h-Wz)\\
&=\frac{\psi(\lambda c)}{qE}\left(\sum_zU(z)\psi(-(W+\lambda)z)\right)
\left(\sum_w\overline{U(w)}\psi(\lambda w)\right)\\
&=\frac{\psi(\lambda c)}{qE}\widehat U(W+\lambda)\overline{\widehat U(\lambda)}.
\end{aligned}
\]
For each noncentral translation there are precisely \(r\) eligible values of \(\lambda\), and for each such value precisely \(r\) values of \(W\). Hence each contributes \(r^2\) nonzero coefficients. The number of noncentral translations is \(N-q\), proving the exact support formula.

**4. Quadratic specialization.** If \(U(z)=\psi(\alpha z^2+\beta z)\) and \(\alpha\ne0\), then \(E=q\). Completing the square, or expanding the squared modulus and summing first over one variable, proves \(|\widehat U(k)|^2=q\) for *every* \(k\): the cross sum has only the diagonal term because \(2\alpha\ne0\). Thus \(r=q\). The identity
\[
U(z)\overline{U(z-c)}=\psi(2\alpha cz-\alpha c^2+\beta c)
\]
shows that \(A_U(c,W)=0\) except at \(W=2\alpha c\), where its magnitude is \(q\). Thus \(a=q\), and all \(q\) nonzero central-row coefficients have modulus \(1\). The factorization in step 3 has numerator magnitude \(q\) and denominator \(qE=q^2\), so each of the \((N-q)q^2\) noncentral nonzero coefficients has modulus \(1/q\). This proves the complete two-tier support and amplitudes; in particular \(\sum|V_g g|^2=N\).

**5. Moments and entropy.** For every real \(s>0\), direct counting gives
\[
\sum_{u,\xi}|V_g g(u,\xi)|^s=q+(N-q)q^{2-s}.
\]
Define a probability distribution on all \(N^2\) STFT coordinates by \(\mathsf P(u,\xi)=|V_g g(u,\xi)|^2/N\), taking \(0\log0=0\). The two kinds of nonzero atoms have probabilities \(1/N\) and \(1/(Nq^2)\), respectively. Computing \(-\sum\mathsf P\log\mathsf P\) yields \(\log N+2(1-q/N)\log q\). Under abelian coordinatewise translation the profile difference depends on \(c\), not \(\ell_{a,b}\). Every one of the \(N\) translation rows then has exactly one nonzero vertical Fourier coefficient, of modulus \(1\); its entropy is \(\log N\). This proves the comparison.

## Verification
The standalone `CHECK.py` performs exact cyclotomic-integer coefficient and squared-modulus comparisons for all \(N^2\) STFT coordinates at five prime-field parameter choices, including horizontal dimension \(n=2\). It then tests the arbitrary-profile factorization independently through direct complex summation for every STFT coordinate at field orders \(3\) and \(5\). All checks passed. This finite test suite checks normalization, zero geometry, and amplitudes but is **not** a proof over arbitrary prime powers or dimensions. The general proof is steps 1–5.

## Relationship to prior work
The motivating preprint by Dabra, Dasgupta, and Gulia (arXiv:2608.20952, first posted 2026-08-21) treats noncommutative Heisenberg-group STFT uncertainty, including entropy inequalities, in a continuous setting. The present result uses a distinctly specified finite-field coordinate-modulation transform and proves exact coefficients, support, and entropy for central-profile windows. Führ and Oussa (arXiv:2201.08654; 2023 journal publication) study phase retrieval for irreducible nilpotent-group representations, including the finite Heisenberg Schrödinger representation; that transform and its reconstruction questions differ from the regular-coordinate-modulated transform defined here. The elementary one-dimensional Fourier and Gauss-sum identities employed in the proof are classical and not asserted to be novel.

## Limitations
The result is specific to right translations and *coordinatewise additive* modulations on the finite Heisenberg group, with a window constant in horizontal coordinates. It does not assert an optimal uncertainty inequality over all windows, phase retrieval, or equivalence with an operator-valued noncommutative Fourier transform. The numerical checker covers prime fields only; the proof covers all odd prime powers. Earlier formulations of an equivalent central-profile factorization may exist in finite-group or noncommutative Gabor literature and warrant independent specialist comparison.

## References
1. A. Dabra, A. Dasgupta, P. Gulia, *Uncertainty Principles for the Short-Time Fourier Transform on the Heisenberg Group*, arXiv:2608.20952 (first public version 2026-08-21), https://arxiv.org/abs/2608.20952.
2. H. Führ, V. Oussa, *Phase retrieval for nilpotent groups*, arXiv:2201.08654 (2022); *Journal of Fourier Analysis and Applications* **29** (2023), 47, https://doi.org/10.1007/s00041-023-10031-5.
3. A. Poria, A. Dasgupta, *Uncertainty principles for the short-time Fourier transform on the lattice*, arXiv:2204.05886 (2022), https://arxiv.org/abs/2204.05886.
