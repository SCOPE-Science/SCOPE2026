# Period-two geometric weights: singular Weyl law and contrast rigidity for Cesàro averaging

## Finding

For \(0<q<1\) and \(u,v>0\), define the complex Hilbert space
\[
H_{q;u,v}=\left\{x=(x_j)_{j\ge1}:\sum_{j\ge1}q^j d_j|x_j|^2<\infty\right\},
\qquad d_{2k+1}=u,\quad d_{2k+2}=v,
\]
and the ordinary Cesàro operator \((Cx)_j=j^{-1}\sum_{i=1}^j x_i\). Put \(a=\sqrt{u/v}\) and \(\Delta_q(\theta)=\sqrt{1+q^2-2q\cos\theta}\). Its decreasing singular values satisfy the **indexed infinite-dimensional law**
\[
\lim_{n\to\infty}n\,s_n(C)=\mathcal K_q(a),\qquad
\mathcal K_q(a)=\frac1{4\pi}\int_0^{2\pi}
 \frac{\sqrt{2+q(a^2+a^{-2})+2\Delta_q(\theta)}}{\Delta_q(\theta)}\,d\theta.
\]
The constant is strictly increasing in \(a^2+a^{-2}\), minimal exactly at \(a=1\), invariant under \(a\mapsto1/a\), and unbounded as \(a\to\infty\). Thus, at fixed \(q\), the singular tail uniquely determines the absolute alternating log-contrast \(|\log(u/v)|\). Yet the spectrum is **independent of contrast**:
\[
\sigma(C)=\{0\}\cup\{1/j:j=1,2,\ldots\}.
\]
For every \(p>0\), membership in the Schatten class \(\mathcal S_p\) holds exactly when \(p>1\), and
\[
\lim_{N\to\infty}\frac1{\log N}\sum_{n=1}^N s_n(C)=\mathcal K_q(a).
\]
A more microscopic distinction is present: the two singular-value branches of the explicit period-two Bloch matrix coincide at some quasi-momentum if and only if \(u=v\); then their sole crossing occurs at \(\theta=\pi\). For unequal weights, their separation at \(\theta=\pi\) is exactly
\[
\frac{\sqrt q}{1+q}\left|a-a^{-1}\right|.
\]

## Assumptions and scope

All assertions hold for arbitrary positive \(u,v\), with no requirement that the original weight sequence decrease monotonically. The limit is at fixed \(q,u,v\) as the singular-value index tends to infinity. The spectral and singular-value assertions refer to the bounded operator on the indicated Hilbert space. Interchanging \(u,v\) leaves the displayed leading singular coefficient unchanged, but no equality of complete finite-index singular sequences is asserted. In the neutral case \(u=v\), the coefficient becomes the classical scalar integral \((2\pi)^{-1}\int_0^{2\pi}|1-\sqrt q\,e^{i\phi}|^{-1}d\phi\); this already-known subcase is **not** the new contribution.

## Proof

**1. Conjugation and compactness.** The unitary map to ordinary \(\ell^2\) is \((Ux)_j=q^{j/2}\sqrt{d_j}\,x_j\). The conjugate \(A=UCU^{-1}\) has entries
\[
A_{ji}=\mathbf1_{i\le j}\frac{q^{(j-i)/2}}{j}\sqrt{\frac{d_j}{d_i}}.
\]
Writing \(r=\sqrt q\), this is a product of the compact diagonal operator \(\operatorname{diag}(1/j)\) with the bounded lower-triangular convolution \((r^{j-i}\sqrt{d_j/d_i})_{j\ge i}\). Boundedness follows from geometric summability and uniform bounds on \(\sqrt{d_j/d_i}\); compactness follows by diagonal finite-rank truncation.

**2. Two-cell Bloch symbol.** Pair indices \(2k+1,2k+2\), \(k\ge0\). Removing the first paired block changes the operator by finite rank. On all remaining rows the diagonal multipliers \(1/(2k+1)\) and \(1/(2k+2)\) can be replaced by \(1/(2k)\), since the replacement error is a trace-class diagonal operator composed with a bounded Toeplitz matrix: its diagonal entries are \(O(k^{-2})\). The resulting operator, up to trace-class terms and the harmless shift of the block origin, is \(\tfrac12 D B_F\), where \(D\) has block diagonal entries \(k^{-1}I_2\), and \(B_F\) is the semi-infinite block Toeplitz operator with absolutely summable coefficients and symbol
\[
F_q(z)=\frac1{1-qz}\begin{pmatrix}1& ar z\\r/a&1\end{pmatrix},\qquad |z|=1.
\]
The two off-diagonal entries encode, respectively, the first lag from an even input to an odd output and the zero-lag transfer from an odd input to an even output. The factor \(1/2\) is essential: one block represents two original indices.

**3. The compact Toeplitz Weyl lemma.** If \(F\) is a continuous matrix-valued symbol with absolutely summable Fourier coefficients, and \(B_F\) its semi-infinite block Toeplitz operator on \(\ell^2(\mathbb N;\mathbb C^d)\), then
\[
\lim_{t\downarrow0}t\,\#\{j:s_j(DB_F)>t\}
=\frac1{2\pi}\int_0^{2\pi}\|F(e^{i\theta})\|_*\,d\theta,
\qquad D=\operatorname{diag}(k^{-1}I_d)_{k\ge1},
\]
where \(\|\cdot\|_*\) denotes the sum of matrix singular values. Here is a proof, to fix the normalization and avoid assuming a finite-section limit implies an infinite-operator assertion. Approximate \(F\) in uniform matrix norm by a band-limited Fourier polynomial \(F_M\). The singular-number ideal inequality \(s_j(DB)\le\|B\|s_j(D)\) bounds the discarded-symbol contribution by \(\limsup_{t\downarrow0}tN(t;D(B_F-B_{F_M}))\le d\|B_F-B_{F_M}\|\), which vanishes as \(M\to\infty\). For fixed \(M\), rows/columns with block index below \(t^{-1/2}\) give rank \(o(t^{-1})\), while blocks above \(R/t\) have operator norm at most \(t\|B_{F_M}\|/R\). Partition the remaining indices into multiplicative intervals of relative width \(\delta\). Deleting cross-interval couplings has rank \(O(M\delta^{-1}\log(1/t))=o(t^{-1})\); replacing the diagonal \(1/k\) inside each interval by its left-end value changes the counting coefficient by \(O(\delta\|B_{F_M}\|)\) via the same ideal inequality. Each interval now contains a constant multiple of a large finite block Toeplitz section. Replace that banded section by its block circulant counterpart at rank cost \(O(M)\). The circulant's singular values are exactly those of \(F_M(e^{2\pi i\ell/L})\) across the \(L\) Fourier nodes, hence their empirical distribution tends to the symbol distribution. Summing over multiplicative intervals gives
\[
\int_0^\infty\frac1{2\pi}\int_0^{2\pi}
\sum_{j=1}^d\mathbf1_{s_j(F_M(e^{i\theta}))>x}\,d\theta\,dx
=\frac1{2\pi}\int_0^{2\pi}\|F_M(e^{i\theta})\|_*\,d\theta.
\]
Taking \(t\downarrow0\), \(\delta\downarrow0\), \(R\) sufficiently large and then \(M\to\infty\) proves the lemma. Finite-rank changes and trace-class changes have \(tN(t)\to0\), by standard singular-number counting inequalities, and so do not change this limit. If \(tN(t)\to\kappa>0\), inversion of the decreasing counting function yields \(ns_n\to\kappa\).

**4. Coefficient and contrast.** The two singular values of \(F_q(e^{i\theta})\) satisfy
\[
\|F_q\|_F^2=\frac{2+q(a^2+a^{-2})}{\Delta_q(\theta)^2},\qquad
|\det F_q|=\frac1{\Delta_q(\theta)}.
\]
The identity \(\|F_q\|_*^2=\|F_q\|_F^2+2|\det F_q|\) yields the integral in the finding, after multiplication by \(1/2\). Differentiation of its positive integrand with respect to \(a^2+a^{-2}\) gives a strictly positive derivative. Because \(a^2+a^{-2}=2\cosh(\log(u/v))\), the asymptotic coefficient recovers \(|\log(u/v)|\) uniquely, while the leading term grows linearly in \(\max(a,a^{-1})\). For \(a=1\), a scalar even/odd Fourier folding identity gives the usual unmodulated integral.

**5. Bloch branches and contrast detection.** The first and second columns of the numerator of \(F_q(z)\) have squared lengths \(1+q/a^2\) and \(1+qa^2\), and inner product \(r(az+a^{-1})\). Equal singular values require orthogonal columns of equal length, forcing \(a=1\) and then \(z=-1\). At \(z=-1\), the singular-value difference squared is \(\|F_q\|_F^2-2|\det F_q|=q(a-a^{-1})^2/(1+q)^2\), giving the claimed splitting.

**6. Spectrum and Schatten consequences.** Any eigenvector with first nonzero coordinate at \(m\) must have eigenvalue \(1/m\) by triangularity. Conversely \(x_j=\mathbf1_{j\ge m}\binom{j-1}{m-1}\) is an eigenvector for \(1/m\), and belongs to the Hilbert space because its polynomial growth is dominated by \(q^j\). Compactness therefore gives precisely the stated spectrum. Finally \(s_n\sim\mathcal K_q(a)/n\) implies the exact Schatten threshold and logarithmic singular-value average.

## Verification

The accompanying \`checker.py\` reconstructs finite truncations and their exact bidiagonal inverses at rational parameters; checks the Bloch nuclear-norm and branch-splitting identities; verifies symmetry and strict contrast ordering; and compares finite-section singular values at ranks \(50,100,200\) with the independent integral coefficient. The checks are finite corroboration only; the general statement rests on the counting-function proof above. A fixed-parameter numerical truncation cannot establish the asymptotic limit by itself.

## Relationship to prior work

Albanese, Bonet and Ricker (first published August 19, 2015) establish compactness and spectral properties for Cesàro operators on weighted \(\ell^p\) spaces, not the period-two contrast-sensitive singular-number Weyl coefficient. The classical generalized Cesàro/Rhaly operator corresponds to the **unmodulated** case after unitary conjugation; it has long-known compactness and eigenvalues. Tilli's block Toeplitz singular-value distribution is an important general background principle, explicitly acknowledged and recovered by the finite-section part of the proof, but does not itself provide the stated infinite-operator ordered-singular-number limit or its contrast reconstruction. The scalar \(u=v\) high-rank law was previously obtained and is not claimed here as a new result. Published statements about periodically **row**-modulated unweighted Rhaly operators concern distinct (generally noncompact) operators and do not imply the two-sided periodic diagonal similarity studied here.

## Limitations

The result provides a leading \(o(1/n)\) law without a quantitative remainder for unequal weights; it does not recover the phase (odd-versus-even ordering) of the periodic contrast, and does not assert finite-index spectral equality under swapping \(u,v\). The result is specific to strictly two-periodic positive modulation and \(0<q<1\); it does not cover arbitrary almost-periodic weights or the boundary \(q=1\). General GLT and block Toeplitz literature may encode stronger distributional machinery; equivalence to an unlocated specialized indexed singular-number result remains a historical risk.

## References

- A. A. Albanese, J. Bonet, W. J. Ricker, “Spectrum and compactness of the Cesàro operator on weighted \(\ell_p\) spaces,” *Journal of the Australian Mathematical Society* **99** (2015), 287–314, DOI: 10.1017/S1446788715000221; first online August 19, 2015. In particular Introduction and Section 4.
- P. Tilli, “A note on the spectral distribution of Toeplitz matrices,” *Linear and Multilinear Algebra* **45** (1998), 147–159, DOI: 10.1080/03081089808818584. Background on matrix-valued finite Toeplitz distributions.
- S. Serra-Capizzano, “Generalized locally Toeplitz sequences: spectral analysis and applications to discretized partial differential equations,” *Linear Algebra and its Applications* **366** (2003), 371–402, DOI: 10.1016/S0024-3795(02)00504-9. Background on variable-coefficient singular distributions.
- M. Yıldırım and N. Durna, “The spectrum and some subdivisions of the spectrum of discrete generalized Cesàro operators on \(\ell_p\),” *Journal of Inequalities and Applications* **2017**, 193, DOI: 10.1186/s13660-017-1464-2; full open text used to distinguish known eigenvalue results from singular-number results.
