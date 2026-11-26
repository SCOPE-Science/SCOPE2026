# Universal radial fluctuations and a sharp Gaussian crossover for random zonogon area

## Finding

For independent isotropically directed planar segments with positive i.i.d. lengths, the normalized isoperimetric deficit has a universal, explicitly computable non-Gaussian limiting distribution. The limiting distribution depends on the length law only through its second moment, although the perimeter has a distinct, asymptotically independent Gaussian fluctuation when the length variance is positive. The finite-sample deficit variance is exact. When the lengths approach one at the critical standard-deviation scale \(n^{-1/2}\), the centered area undergoes a complete crossover from this non-Gaussian law to an independent Gaussian convolution.

Precisely, let \(\Theta_i\) be independent uniform variables on \([0,\pi)\) and let \(R_i>0\) be i.i.d., independent of the directions, with \(r=\mathbb E R_i>0\) and \(q=\mathbb E R_i^2<\infty\). For every integer \(n\ge2\), set
\[
Z_n=\sum_{i=1}^n[0,R_i(\cos\Theta_i,\sin\Theta_i)],\quad
A_n=\operatorname{Area}(Z_n),\quad P_n=\operatorname{Perimeter}(Z_n),\quad
D_n=\frac{P_n^2/(4\pi)-A_n}{n}.
\]
For independent unit-mean exponential variables \(E_k\), define the almost-surely finite variable
\[
S=\frac2\pi\sum_{k=1}^{\infty}\frac{E_k}{4k^2-1}.
\]
Then
\[
D_n\ \xrightarrow{d}\ qS,\qquad \mathbb E D_n=\frac q\pi.
\]
Its Laplace transform is explicit: for \(t\ge0\), writing \(a^2=1-2t/\pi\), the continuous analytic interpretation is
\[
\mathbb E e^{-tS}=\prod_{k=1}^{\infty}\left(1+\frac{2t}{\pi(4k^2-1)}\right)^{-1}
=\frac{a}{\sin(\pi a/2)}.
\]
For \(t>\pi/2\), the last quotient is real and equals \(b/\sinh(\pi b/2)\), where \(b=\sqrt{2t/\pi-1}\); at \(t=\pi/2\) its value is \(2/\pi\). In particular,
\[
\mathbb ES=\frac1\pi,\qquad \operatorname{Var}(S)=\frac{\pi^2-8}{4\pi^2}>0.
\]
If \(m_4=\mathbb E R_i^4<\infty\), the **exact** finite-size variance is
\[
\boxed{\operatorname{Var}(D_n)=\frac{m_4-q^2}{\pi^2 n}+\frac{n-1}{n}\frac{q^2(\pi^2-8)}{4\pi^2}.}
\]
Thus the first two moments converge to those of \(qS\). With \(\sigma^2=q-r^2>0\), the normalized perimeter fluctuation is independent of the limiting deficit:
\[
\left(D_n,\frac{P_n-2nr}{2\sigma\sqrt n}\right)
\xrightarrow{d}(qS,G),\qquad G\sim N(0,1),\quad G\perp S.
\]
When \(\mathbb E R_i^3<\infty\), the additional exact covariance identity is
\[
\operatorname{Cov}(D_n,P_n)=\frac2\pi\bigl(\mathbb E R_i^3-rq\bigr),
\]
independent of \(n\), despite the limiting independence after perimeter normalization.

There is a sharp triangular-array area crossover. Let \(\xi_i\) be i.i.d. bounded real variables, independent of the angles, with \(\mathbb E\xi_i=0\) and \(\mathbb E\xi_i^2=1\). For each \(n\) put \(R_{n,i}=1+\sigma_n\xi_i\) with \(\sigma_n\ge0\), \(\sigma_n\to0\), and \(R_{n,i}>0\) for all sufficiently large \(n\). Set \(s_n=\sqrt n\sigma_n\), \(G_n=n^{-1/2}\sum_i\xi_i\), and
\[
B_n=\frac{A_n-n(n-1)/\pi}{n}.
\]
The limiting deficit and the radial central-limit variable are jointly independent, and the following **exact identity** holds for every sufficiently large \(n\):
\[
B_n=\frac1\pi-D_n+\frac{2s_n}{\pi}G_n+\frac{\sigma_n^2}{\pi}G_n^2.
\]
Consequently, if \(s_n\to\tau\in[0,\infty)\),
\[
\boxed{(B_n,G_n)\xrightarrow{d}
\left(\frac1\pi-S+\frac{2\tau}{\pi}G,\ G\right),\quad G\perp S.}
\]
For finite \(\tau\), the limiting centered-area variance is \((\pi^2-8)/(4\pi^2)+4\tau^2/\pi^2\). Moreover, writing \(X_\tau=1/\pi-S+2\tau G/\pi\), its third centered moment is
\[
\mathbb E[(X_\tau-\mathbb E X_\tau)^3]
=-2\sum_{k\ge1}\left(\frac{2}{\pi(4k^2-1)}\right)^3<0.
\]
Thus the limiting centered-area law is strictly non-Gaussian for **every finite** \(\tau\), even after Gaussian convolution. It follows independently from the exact finite-sample identity, valid for the triangular array with \(q_n=1+\sigma_n^2\),
\[
\operatorname{Var}(A_n)=\binom n2\left(\frac{q_n^2}{2}-\frac4{\pi^2}\right)
+\frac{4n(n-1)(n-2)}{\pi^2}\sigma_n^2.
\]
When \(s_n\to\infty\) while \(\sigma_n\to0\), the alternative normalization gives \(B_n/s_n\xrightarrow{d}2G/\pi\). The boundary \(\sigma_n\asymp n^{-1/2}\) is therefore the precise crossover between the second-order shape fluctuation and first-order radial-size fluctuation.

## Assumptions and scope

The directions are isotropic **unoriented** directions, so all angles are modulo \(\pi\). Lengths are strictly positive almost surely, independently sampled across segments and independently of their directions. All formulas use Euclidean area and Euclidean perimeter, not a randomly sampled support-line or chord length. Translation of the generators does not affect either functional. Fixed-law distributional convergence requires a finite second radial moment; the exact variance additionally requires a fourth moment. The perimeter central limit is nondegenerate only for positive radial variance. The triangular-array assertion assumes bounded, standardized radial marks, with nonnegativity of all resulting lengths eventually; no identical distribution across different rows is required.

## Proof

**1. Deterministic Fourier representation.** For \(Z_n\), the planar zonotope formula gives \(P_n=2\sum_iR_i\) and
\[
A_n=\sum_{1\le i<j\le n}R_iR_j|\sin(\Theta_i-\Theta_j)|.
\]
The absolutely and uniformly convergent Fourier expansion
\[
|\sin u|=\frac2\pi-\frac4\pi\sum_{k\ge1}\frac{\cos(2ku)}{4k^2-1}
\]
and the identity \(\sum_{k\ge1}(4k^2-1)^{-1}=1/2\) imply, after pairing off diagonal terms,
\[
\boxed{D_n=\frac2{\pi n}\sum_{k\ge1}\frac{|\sum_iR_i e^{2ik\Theta_i}|^2}{4k^2-1}.}\tag{1}
\]
All summands are nonnegative, and interchanging finite generator sums with the absolutely convergent Fourier expansion is justified. This also proves the isoperimetric nonnegativity directly and fixes the normalization.

**2. Exact moments.** Conditional on all radii, each squared Fourier sum in (1) has conditional mean \(\sum_iR_i^2\). For distinct positive Fourier frequencies, their squared moduli have conditional covariance zero: expanding both squared moduli, isotropic angular integration annihilates every term except the separate diagonal products, as distinct frequencies cannot share the same nonzero balanced exponent. For a fixed frequency, direct pair expansion gives
\[
\operatorname{Var}\!\left(\left|\sum_iR_i e^{2ik\Theta_i}\right|^2\bigg|R_1,\ldots,R_n\right)
=2\sum_{i<j}R_i^2R_j^2.
\]
The exact spectral sums
\[
\sum_{k\ge1}\frac1{4k^2-1}=\frac12,\qquad
\sum_{k\ge1}\frac1{(4k^2-1)^2}=\frac{\pi^2-8}{16}
\]
now yield \(\mathbb E[D_n\mid R_1,\dots,R_n]=(\sum_iR_i^2)/(\pi n)\), and
\[
\operatorname{Var}(D_n\mid R_1,\dots,R_n)
=\frac{\pi^2-8}{2\pi^2n^2}\sum_{i<j}R_i^2R_j^2.
\]
Total expectation and total variance give the displayed unconditional formulas. Conditional centering also gives the exact covariance with \(P_n\), since \(P_n\) is measurable with respect to the radii.

**3. Universal law and joint independence.** For every fixed integer \(K\), the multivariate central limit theorem applied to the real and imaginary parts of \(R_i e^{2ik\Theta_i}\), \(1\le k\le K\), gives independent circular complex Gaussian limits \(H_k\) with \(\mathbb E|H_k|^2=q\). Hence \(|H_k|^2/q\) are independent unit exponentials. The contribution to (1) from \(k>K\) has expectation bounded by \(2q\sum_{k>K}(4k^2-1)^{-1}/\pi\), uniformly in \(n\); Markov's inequality lets \(K\to\infty\) after \(n\to\infty\). This proves \(D_n\xrightarrow{d}qS\). If \(m_4<\infty\), the exact finite-\(n\) variance identifies second-moment convergence. The Euler sine product
\[
\prod_{k\ge1}\left(1-\frac{z^2}{4k^2}\right)=\frac{\sin(\pi z/2)}{\pi z/2}
\]
with \(z^2=1-2t/\pi\) evaluates the Laplace transform, including its continuous and hyperbolic branches. If \(\sigma>0\), append the centered radial coordinate \(R_i-r\) to the finite Fourier vector in the multivariate CLT. Every cross-covariance is zero because \(\mathbb E e^{2ik\Theta_i}=0\). The resulting joint Gaussian blocks are independent, and the same uniform tail argument proves the joint perimeter–deficit independence.

**4. Critical triangular array.** Since \(\sigma_n\to0\) and \(\xi_i\) are bounded, the difference between the Fourier sums with radii \(1+\sigma_n\xi_i\) and the unit-radius sums has normalized second moment \(\sigma_n^2\) at each frequency. The nonnegative Fourier representation and the uniform \(k\)-tail bound show that \(D_n\) has the same limiting shape law as for unit radii, jointly with \(G_n\). Independence follows already at each \(n\) for the unit-radius Fourier sums and the marks, and then by the difference estimate. Expanding the exact identity \(A_n=(\sum_iR_{n,i})^2/\pi-nD_n\) and using \(\mathbb E A_n=n(n-1)/\pi\) gives the displayed equation for \(B_n\). The ordinary CLT gives \(G_n\xrightarrow{d}G\). For bounded \(s_n\), the term \(\sigma_n^2G_n^2/\pi\) tends to zero in probability; for \(s_n\to\infty\), dividing the exact identity by \(s_n\) leaves only \(2G_n/\pi\), because \(\sigma_n^2 G_n^2/s_n=(\sigma_n/\sqrt n)G_n^2\to0\). Slutsky's theorem establishes all three regimes. To justify the displayed finite-\(\tau\) variance without assuming uniform integrability from weak convergence alone, expand the double-sum area directly: disjoint generator pairs are independent, the diagonal-pair variance is \(q_n^2/2-4/\pi^2\), and each distinct pair of edges sharing one generator has covariance \(4\sigma_n^2/\pi^2\). Summing those pair classes yields the exact area variance given above, which has the asserted limit after division by \(n^2\). Finally, independent exponential variables have centered third moment two, while the independent centered normal has third moment zero. The exponential series converges in \(L^3\) by Minkowski's inequality because its nonnegative coefficients are summable. Hence the independent centered third cumulants can be summed absolutely, giving the strict negative third centered moment and hence the non-Gaussian character for every finite \(\tau\). This is a complete proof for all stated parameter ranges, not a finite-sample extrapolation.

## Verification

Run `python3 verify.py` with the Python 3 standard library. The script constructs zonotope areas independently by ordered-generator accumulation and by pairwise determinants; checks the deterministic Fourier identity with a positive tail bound; checks the sine-product Laplace expression and rational spectral sums; and tests exact finite-size moments and the three scaling regimes with reproducible Monte Carlo samples. Its successful output terminates with `ALL_RADIAL_UNIVERSALITY_AND_CROSSOVER_CHECKS_PASSED`. The analytical equalities and limit justifications above, rather than Monte Carlo confidence, provide the proof.

## Relationship to prior work

Schneider, *Random zonotopes and valuations* (arXiv:2202.06774, first posted 14 February 2022), proves expectation formulas for zonotope valuations and a generic nondegenerate central limit theorem. The area expansion here agrees with those first-moment foundations but extracts a non-Gaussian **perimeter-cancelled** second-order law, an exact finite variance, and a length-variance crossover not supplied by that central limit theorem. Joós and Lángi (arXiv:2206.03204, first posted 7 June 2022) study zonotope intrinsic-volume decompositions and deterministic isoperimetric problems. Buffière and Marchal (arXiv:2303.18045, first posted 31 March 2023) analyze a distinct lattice-zonotope sampling model, not independent Haar directions and radial marks. Rahmani, Pinoli and Debayle (2017) study Feret-diameter reconstruction by random zonotopes with controlled directions rather than the present random-generator limit.

An earlier exact **unit-length**, locally direction-biased Fourier deficit law, identified by opaque record `474c5a5f-f684-4deb-8225-2bcddca2d7a3`, already contains the isotropic exponential spectral series and its Laplace transform. Those components are **not claimed as independently new**. The new assessed content is their radial-mark universality, exact all-\(n\) variance and covariance, asymptotic independence from genuine radial perimeter fluctuations, and the sharp Gaussian/non-Gaussian crossover in raw area under triangular-array radial perturbations. The formula for the convolution is not presented as a general result for arbitrary angular biases, which are outside the main hypotheses.

## Limitations

The lengths are direction-independent and have a finite second moment; nonisotropic or direction-dependent length laws, infinite-variance radii, and higher-dimensional zonotopes are not treated. The exact finite variance requires a fourth moment; the limiting law does not. The fixed-length isotropic spectrum is known from the earlier result just identified. Priority of the **combined** radial and crossover statements remains provisional because unindexed equivalent formulations may exist; no independent mathematical audit has been performed. The verifier's finite calculations cannot rule out published stronger theorems or substitute for the infinite proof.

## References

1. R. Schneider, *Random zonotopes and valuations*, arXiv:2202.06774v1 (14 February 2022), https://arxiv.org/abs/2202.06774.
2. A. Joós and Zs. Lángi, *Isoperimetric problems for zonotopes*, arXiv:2206.03204v1 (7 June 2022), https://arxiv.org/abs/2206.03204.
3. T. Buffière and P. Marchal, *Fluctuations of lattice zonotopes and polygons*, arXiv:2303.18045v1 (31 March 2023), https://arxiv.org/abs/2303.18045.
4. S. Rahmani, J.-C. Pinoli and J. Debayle, *Description of the symmetric convex random closed sets as zonotopes from their Feret diameters*, Modern Stochastics: Theory and Applications 3 (2016), online 3 January 2017, doi:10.15559/16-VMSTA70.
5. Earlier exact fixed-length angular-perturbation deficit law: opaque record `474c5a5f-f684-4deb-8225-2bcddca2d7a3` (the isotropic spectral-series case is prior work).
