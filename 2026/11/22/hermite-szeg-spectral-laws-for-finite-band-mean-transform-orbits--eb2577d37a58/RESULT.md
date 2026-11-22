# Hermite–Szegő spectral laws for finite-band mean-transform orbits

## Finding

Let \(Ue_j=e_{j+1}\) be the bilateral shift on \(\ell^2(\mathbb Z)\). Let \(A=A^*\ne0\) be a matrix of finite support (all but finitely many matrix entries vanish) satisfying \(\|A\|<1\). Fix \(0<q<1\), put \(T=U(I+A)\), and define the normalized weighted arithmetic mean transform by
\[
\mathcal M_q(S)=(1-q)V|S|+q|S|V,
\]
where \(S=V|S|\) is its canonical polar decomposition. Define \(T_k=\mathcal M_q^{\circ k}(T)\), including \(T_0=T\), and write \(A_k=U^*T_k-I\).

For each integer \(h\), put \(a_h(j)=\langle Ae_j,e_{j+h}\rangle\) and \(M_{s,h}=\sum_{j\in\mathbb Z}j^s a_h(j)\), with \(j^0=1\). The **cancellation order** \(r\) is the least nonnegative integer for which some \(M_{r,h}\ne0\). This order exists and is finite because the supported diagonal coefficient sequences are finite and \(A\ne0\). Put
\[
\sigma_k=\sqrt{kq(1-q)},\qquad
\phi(x)=(2\pi)^{-1/2}e^{-x^2/2},\qquad
H_r(x)=(-1)^r\phi(x)^{-1}\phi^{(r)}(x),
\]
and define the nonzero real trigonometric polynomial
\[
P_r(e^{i\theta})=\frac1{r!}\sum_{h\in\mathbb Z}M_{r,h}e^{ih\theta}.
\]
Reality follows from selfadjointness and the vanishing of the lower moments.

**Theorem.** For each fixed \(0<p<\infty\), with the Schatten quasi-norm convention when \(p<1\),
\[
\boxed{\lim_{k\to\infty}\sigma_k^{(r+1)p-1}
\|T_k-U\|_{\mathcal S_p}^p
=\left(\int_{\mathbb R}|H_r(x)\phi(x)|^p\,dx\right)
\left(\frac1{2\pi}\int_0^{2\pi}|P_r(e^{i\theta})|^p\,d\theta\right).}
\]
The operator norm has the separately sharp limit
\[
\boxed{\lim_{k\to\infty}\sigma_k^{r+1}\|T_k-U\|
=\|H_r\phi\|_{L^\infty(\mathbb R)}\|P_r\|_{L^\infty(\mathbb T)}.}
\]
For any continuous function \(F\) with compact support disjoint from zero, the entire *nonzero signed spectral cloud* obeys
\[
\boxed{\lim_{k\to\infty}\frac1{\sigma_k}
\sum_{\lambda\in\operatorname{spec}(A_k)\setminus\{0\}}
F(\sigma_k^{r+1}\lambda)
=\int_{\mathbb R}\frac1{2\pi}\int_0^{2\pi}
F\bigl(H_r(x)\phi(x)P_r(e^{i\theta})\bigr)\,d\theta\,dx.}
\]
On the left, eigenvalues are counted with finite multiplicity; the zero eigenvalue is excluded. In particular \(T_k\to U\) in operator norm. Its difference converges to zero in \(\mathcal S_p\) exactly when \(p>1/(r+1)\), has a positive finite limiting quasi-norm at equality, and has divergent \(\mathcal S_p\) quasi-norm when \(0<p<1/(r+1)\). All constants displayed are positive and finite.

**Concrete noncommutative example.** Take \(0<\varepsilon<1/\sqrt2\) and let \(A\) have the only nonzero matrix entries \(\langle Ae_0,e_1\rangle=\langle Ae_1,e_0\rangle=\varepsilon\) and \(\langle Ae_1,e_2\rangle=\langle Ae_2,e_1\rangle=-\varepsilon\). Then \(\|A\|=\sqrt2\varepsilon<1\), \(r=1\), and \(P_1(e^{i\theta})=-2\varepsilon\cos\theta\). At \(q=1/2\),
\[
\lim_{k\to\infty}\sigma_k^2\|T_k-U\|=\frac{2\varepsilon}{\sqrt{2\pi e}},\qquad
\lim_{k\to\infty}\sigma_k\|T_k-U\|_{\mathcal S_1}
=\frac{4\varepsilon}{\pi}\sqrt{\frac2\pi},
\]
and, for every integer \(k\ge0\),
\[
\|T_k-U\|_{\mathcal S_2}^2
=\frac{4\varepsilon^2}{k+1}\frac{\binom{2k}{k}}{4^k}.
\]
This example has cancellation of the zeroth moments on both offdiagonals, but nonzero first moments and a genuine two-sided Fourier symbol.

## Assumptions and scope

The Hilbert space is complex and separable. The perturbation \(A\) is a fixed finite-support selfadjoint matrix, not necessarily diagonal, and \(I+A\) is strictly positive. The weighting parameter \(q\) is fixed strictly between zero and one. The theorem is for the large positive iteration index \(k\), without any simultaneous dependence of \(q\), \(A\), or \(p\) on \(k\). Schatten ideals with \(0<p<1\) are quasi-Banach ideals; this convention is essential for the critical value below one. The spectrum in the counting formula is that of the compact selfadjoint \(A_k\), not of the nonnormal operator \(T_k\).

## Proof

**1. Exact iteration.** Since \(I+A>0\), the polar part of \(T\) is \(U\). Positive convex combinations preserve strict positivity, so induction gives
\[
T_k=U(I+A_k),\qquad
A_k=\sum_{t=0}^k\binom{k}{t}q^t(1-q)^{k-t}U^{-t}AU^t.
\]
In particular \(A_k=A_k^*\) is finite rank, has the same finite diagonal bandwidth as \(A\), and \(\|T_k-U\|_{\mathcal S_p}=\|A_k\|_{\mathcal S_p}\) for every Schatten exponent.

**2. Local Gaussian moment expansion, with a global tail bound.** Let \(p_k(t)=\binom{k}{t}q^t(1-q)^{k-t}\) for \(0\le t\le k\), zero elsewhere, and let \(b_{k,h}(n)=\langle A_ke_n,e_{n+h}\rangle\). Then
\[
b_{k,h}(n)=\sum_j a_h(j)p_k(j-n).
\]
For fixed \(h\) the Fourier inversion formula is
\[
b_{k,h}(n)=\frac1{2\pi}\int_{-\pi}^{\pi}
 e^{int}(1-q+qe^{it})^k\sum_j a_h(j)e^{-ijt}\,dt.
\]
The last finite Laurent sum has a zero of order at least \(r\) at \(t=0\) and its first possible nonzero Taylor coefficient is \((-it)^r M_{r,h}/r!\). With \(n=-kq+\sigma_k x+O(1)\), set \(t=u/\sigma_k\); the central Gaussian limit of the characteristic function and Fourier inversion yield, locally uniformly in real \(x\),
\[
\sigma_k^{r+1} b_{k,h}(n)
\longrightarrow \frac{M_{r,h}}{r!}H_r(x)\phi(x).
\]
When \(M_{r,h}=0\), the limit is zero. This local limit is uniform over all finitely many active diagonals.

Here a quantitative tail control is also necessary: for every sufficiently large \(k\), every integer \(n\), and every active \(h\),
\[
\left|\sigma_k^{r+1}b_{k,h}(n)\right|
\le C\exp\left(-c\frac{|n+kq|}{\sigma_k}\right)
\]
with constants depending only on \(q,A\). To see this, shift the periodic entire Fourier integrand vertically by \(\operatorname{sgn}(n+kq)/\sigma_k\). The phase and binomial factor contribute \(\exp(-|n+kq|/\sigma_k+O(1))\); on the shifted contour, the binomial factor also contributes \(\exp(-c k\sin^2(t/2))\), while the finite Laurent sum is bounded by \(C(|t|+\sigma_k^{-1})^r\) near zero. Gaussian integration then supplies the factor \(\sigma_k^{-r-1}\), and the remaining arc is exponentially small. This bound is valid uniformly even outside the central binomial region.

**3. The slowly varying band symbol.** Let \(B_k=\sigma_k^{r+1}A_k\) and \(f_r(x)=H_r(x)\phi(x)\). The previous step says that along each fixed diagonal and in the \(\sigma_k\)-wide central window, \(B_k\) has entries \(f_r((n+kq)/\sigma_k)M_{r,h}/r!+o(1)\), uniformly on bounded rescaled windows. The global tail bound makes the contribution of \(|(n+kq)/\sigma_k|>R\) vanish in normalized \(\mathcal S_p^p\) as \(R\to\infty\), for every \(p>0\). Indeed, for a matrix with a fixed finite bandwidth, \(\|E\|_{\mathcal S_p}^p\le C_{p,A}\sum_{n,h}|E_{n+h,n}|^p\), using the quasi-triangle inequality if \(p\le1\) and ordinary triangle inequality otherwise.

Fix a central window and partition it into blocks of length \(\ell_k\), where \(\ell_k\to\infty\) and \(\ell_k/\sigma_k\to0\). Only \(O(\sigma_k/\ell_k)\) sites near block boundaries participate in cross-block entries, so their normalized \(\mathcal S_p^p\) contribution is \(O(1/\ell_k)\). Each remaining block differs, in operator norm by \(o(1)\), from the finite Hermitian Toeplitz section with coefficients \(f_r(x_{\rm block})M_{r,h}/r!\). By expanding powers and counting closed finite-band walks, the eigenvalue distribution of such a Toeplitz section approaches the circle distribution of \(f_r(x_{\rm block})P_r(e^{i\theta})\). Polynomial approximation then gives the same assertion for \(|\cdot|^p\), for all \(p>0\). Summing blocks as a Riemann sum and removing the tail yields
\[
\frac1{\sigma_k}\operatorname{Tr}|B_k|^p
\longrightarrow \int_{\mathbb R}|f_r(x)|^p\,dx
\frac1{2\pi}\int_0^{2\pi}|P_r(e^{i\theta})|^p\,d\theta.
\]
The same block moment argument first proves the signed spectral test formula for polynomials vanishing at zero. For continuous \(F\) supported away from zero, approximate \(F(t)/t^2\) uniformly by polynomials on a fixed interval containing the bounded spectra, then multiply by \(t^2\). The uniformly bounded normalized second moments justify passing to \(F\). This establishes the signed spectral formula and all finite \(p\) laws.

**4. Sharp operator norm.** For an upper bound, use a partition of unity by smoothly overlapping diagonal cutoffs of length \(\ell_k\), with sum of their squares equal to identity. Because \(B_k\) has fixed bandwidth, the difference between \(B_k\) and the sum of its localized compressions has norm \(O(\ell_k^{-2})\) times a uniform coefficient bound (the error on an edge is half the sum of squared differences of cutoffs). Each compressed piece is within \(o(1)\) in norm of the constant-symbol Toeplitz operator with coefficient \(f_r(x)\), whose norm does not exceed \(|f_r(x)|\|P_r\|_\infty\). Cauchy–Schwarz with the squared partition shows \(\limsup\|B_k\|\le\|f_r\|_\infty\|P_r\|_\infty\). For the reverse inequality, use long finite wave packets centered at a maximizing \(x\), with Fourier frequency approaching a maximizing angle of \(|P_r|\). On each packet the coefficients vary by \(o(1)\), so its Rayleigh quotient tends to \(f_r(x)P_r(e^{i\theta})\). This proves the sharp norm law.

**5. Example and cutoff.** For the three-site example, the supported upper diagonal has coefficients \((\varepsilon,-\varepsilon)\), so \(M_{0,1}=0\), \(M_{1,1}=-\varepsilon\), with the conjugate relation on the lower diagonal. Thus \(r=1\) and \(P_1=-2\varepsilon\cos\theta\). The Gaussian and circle integrals give the stated norm and trace-norm limits. At \(q=1/2\), the upper diagonal of \(A_k\) is \(\varepsilon(p_k(j)-p_k(j+1))\), up to a reversal of its indexing. Hence
\[
\operatorname{Tr}(A_k^2)=2\varepsilon^2\sum_j(p_k(j)-p_k(j+1))^2
=\frac{4\varepsilon^2}{k+1}\frac{\binom{2k}{k}}{4^k},
\]
by Vandermonde convolution. Finally, the positive finite limiting constants imply the stated trichotomy directly from the exponent \(1-(r+1)p\).

## Verification

The accompanying `checker.py` verifies the exact three-site Hilbert–Schmidt identity for several finite iteration indices using independent tridiagonal eigensolvers and binomial coefficient formulas, and compares the scaled operator, Hilbert–Schmidt and trace norms with the three analytical limits. The infinite-index assertions are established by the preceding proof; finite numerical tests alone cannot certify them.

## Relationship to prior work

Chabbabi, Curto and Mbekhta (2018) define mean transforms and derive a general binomial conjugation identity; Jung, Ko and Lee (2020) give the weighted-mean iteration formula and norm convergence results for monotone unilateral shifts. These iteration identities are background, not claimed here. Barbarino and Garoni (2018) develop general locally Toeplitz spectral-symbol machinery. The present result identifies the **specific finite-moment Hermite symbol** arising under bilateral conjugation of arbitrary finite-band selfadjoint defects and proves a sharp two-parameter phase diagram of all Schatten quasi-norms, including the endpoint \(p<1\), the signed spectral cloud, and the operator norm. The result is compatible with general local Toeplitz theory but does not claim novelty of that framework or of Gaussian local limit methods.

## Limitations

The perturbation must have finite matrix support, and \(q\) must remain in a fixed compact subset of \((0,1)\) as the iteration count tends to infinity (the theorem itself fixes one \(q\)). No extension to infinitely supported, time-varying or non-selfadjoint perturbations is proved. The normalized signed eigenvalue law is stated only for tests supported away from zero because the number of tiny eigenvalues grows faster than the central effective rank. All novelty assessments are provisional pending independent literature and mathematical scrutiny, especially for possible operator-theoretic specializations of generalized locally Toeplitz results.

## References

1. F. Chabbabi, R. E. Curto and M. Mbekhta, *The Mean Transform and the Mean Limit of an Operator*, first public 9 December 2018, arXiv:1812.03499v1, https://arxiv.org/abs/1812.03499.
2. S. Jung, E. Ko and M.-J. Lee, *On the Iterated Mean Transforms of Operators*, Mathematical Inequalities & Applications 23 (2020), 597–610, doi:10.7153/mia-2020-23-49, https://files.ele-math.com/articles/mia-23-49.pdf.
3. G. Barbarino and C. Garoni, *Normal Form for GLT Sequences, Functions of Normal GLT Sequences, and Spectral Distribution of Perturbed Normal Matrices*, first public 22 May 2018, arXiv:1805.08708v1, https://arxiv.org/abs/1805.08708.
4. A. Basak, E. Paquette and O. Zeitouni, *Regularization of Non-normal Matrices by Gaussian Noise: the Banded Toeplitz and Twisted Toeplitz Cases*, first public 30 November 2017, arXiv:1712.00042, https://arxiv.org/abs/1712.00042.
