# A sharp moment transition for unoversampled Gaussian Nyström projection near rank one

## Finding
For a two-column matrix with singular values \(1\) and \(h\), an unoversampled **one-vector right Gaussian sketch** has an exact, unexpectedly nonuniform error law. Even with arbitrarily many independent left Gaussian measurements, its root-mean-square error is proportional to \(\sqrt h\), whereas the optimal rank-one error is \(h\). One may draw fresh sketches for every step; the following is an exact one-step statement.

For \(k\ge3\), the squared Frobenius risk is **exactly**
\[
\mathbb E\|Z_h-\widehat Z_h\|_F^2=\frac{k-1}{k-2}h,\qquad 0<h<1.
\]
With only one or two left measurements this expectation is infinite. All fractional moments have a sharp transition at exponent one, described below.

## Assumptions and scope
Fix integers \(m\ge2\) and \(k\ge1\), orthonormal columns \(u,v\in\mathbb R^m\), and real \(0<h<1\). Define \(Z_h=ue_1^\top+hve_2^\top\in\mathbb R^{m\times2}\). Draw mutually independent standard real Gaussian \(\Omega\in\mathbb R^{2\times1}\) and \(\Psi\in\mathbb R^{m\times k}\). The generalized Nyström approximation is
\[
\widehat Z_h=(Z_h\Omega)(\Psi^\top Z_h\Omega)^\dagger\Psi^\top Z_h.
\]
Here \(\dagger\) denotes the Moore–Penrose inverse, and rank-one truncation leaves \(\widehat Z_h\) unchanged. The one-column sampled vector is almost surely nonzero and the left denominator has full column rank almost surely. Let \(T_h=\|Z_h-\widehat Z_h\|_F\).

Take independent \(\Theta\sim\mathrm{Uniform}([0,\pi/2])\), \(\xi\sim N(0,1)\), and \(W_k\sim\chi^2_k\). Then
\[
T_h\stackrel{d}{=}\frac{h}{\sqrt{\cos^2\Theta+h^2\sin^2\Theta}}\sqrt{1+\frac{\xi^2}{W_k}}.
\]
For all real \(q>0\), the \(q\)-th moment is finite exactly when \(q<k\), and for \(q<k\) equals
\[
\mathbb E T_h^q=B_{q,k}\frac{2h^q}{\pi}\int_0^{\pi/2}\frac{d\theta}{(\cos^2\theta+h^2\sin^2\theta)^{q/2}},
\quad B_{q,k}=\frac{\Gamma((k+1)/2)\Gamma((k-q)/2)}{\Gamma(k/2)\Gamma((k+1-q)/2)}.
\]
The constants in the complete asymptotics as \(h\downarrow0\) are
\[
\mathbb ET_h^q\sim\begin{cases}
 B_{q,k}\dfrac{\Gamma((1-q)/2)}{\sqrt\pi\,\Gamma(1-q/2)}h^q,&0<q<1,\\[6pt]
 \dfrac{2B_{1,k}}\pi h\log(4/h),&q=1<k,\\[6pt]
 B_{q,k}\dfrac{\Gamma((q-1)/2)}{\sqrt\pi\,\Gamma(q/2)}h,&1<q<k.
\end{cases}
\]
At \(q=1\), the more precise exact formula is \(\mathbb ET_h=(2B_{1,k}/\pi)hK(\sqrt{1-h^2})\), with \(K\) the complete elliptic integral of the first kind. In particular, for \(k\ge3\),
\[\mathbb ET_h^2=\frac{k-1}{k-2}h.\]

## Proof
Put \(q_h=Z_h\Omega/\|Z_h\Omega\|_2\), let \(v_h\) be its orthogonal unit complement in the two-dimensional column space of \(Z_h\), and write \(R_h=(I-q_hq_h^\top)Z_h=v_ha_h^\top\). The decomposition
\[
 Z_h-\widehat Z_h=R_h-q_h(\Psi^\top q_h)^\dagger\Psi^\top R_h
\]
has orthogonal column-space summands. Therefore
\[
T_h^2=\|R_h\|_F^2\left(1+\frac{((\Psi^\top q_h)^\top\Psi^\top v_h)^2}{\|\Psi^\top q_h\|_2^4}\right).
\]
Conditional on \(\Omega\), the two vectors \(G=\Psi^\top q_h\) and \(H=\Psi^\top v_h\) are independent standard normal vectors in \(\mathbb R^k\). Conditional on \(G\), their scalar product is \(G^\top H=\|G\|\xi\), where \(\xi\) is standard normal and independent of \(\|G\|^2=W_k\sim\chi_k^2\). Rotational invariance makes the multiplicative factor independent of \(\Omega\).

Writing \(\Omega=(\omega_1,\omega_2)^\top\), direct orthogonal projection gives
\[
\|R_h\|_F^2=h^2\frac{\omega_1^2+\omega_2^2}{\omega_1^2+h^2\omega_2^2}.
\]
The Gaussian direction is uniform on the circle, proving the distributional formula. The ratio \(\xi/\sqrt{W_k}\) has density
\[
\frac{\Gamma((k+1)/2)}{\sqrt\pi\,\Gamma(k/2)}(1+t^2)^{-(k+1)/2},\quad t\in\mathbb R.
\]
Integrating \((1+t^2)^{q/2}\) against this density gives the gamma quotient \(B_{q,k}\) for \(q<k\), and a divergent tail integral when \(q\ge k\). Independence gives the moment formula.

For \(q<1\), dominated convergence applies after division by \(h^q\), since \(\cos^{-q}\theta\) is integrable. The elementary beta integral gives the stated constant. For \(q>1\), substitute \(s=(\pi/2-\theta)/h\) near the angular singularity and use an integrable majorant to obtain \(h^{1-q}\) times \(\int_0^\infty(1+s^2)^{-q/2}ds\); the complement is lower order. The beta integral yields the second constant. At \(q=1\), the angular integral is \(K(\sqrt{1-h^2})\sim\log(4/h)\). At \(q=2\), the angular integral is exactly \(\pi/(2h)\), by \(s=\tan\theta\), while \(B_{2,k}=(k-1)/(k-2)\), proving the identity for all \(h\).

For each fixed pair of sketches, \(T_h/h\) converges almost surely to the finite random variable \(\sqrt{1+(\omega_2/\omega_1)^2}\sqrt{1+\xi^2/W_k}\), because \(\omega_1\ne0\) almost surely. This does not imply convergence of its second moments: rare right-sketch directions concentrate the risk near \(\omega_1=0\).

## Verification
Run \(\texttt{python3 verify.py}\) with Python's standard library. The script compares the explicit two-by-two generalized Nyström matrix with the independent projection formula for seeded Gaussian samples, checks the exact \(q=2\) angular integral by quadrature, and tests gamma factors and representative asymptotic regimes. These finite checks complement, rather than replace, the exact proof.

The matrix path \(Z(t)=ue_1^\top+tve_2^\top\) is the exact solution of \(\dot Z=ve_2^\top\), \(Z(0)=ue_1^\top\). Its vector field is constant and hence globally Lipschitz with constant zero. An exact-data generalized Nyström projection at \(t=h\) has precisely the stated distribution. This is an idealized one-step observation; no global trajectory convergence claim is made.

## Relationship to prior work
Lam–Ceruti–Kressner (arXiv:2409.06384, first version 2024) introduce randomized low-rank Runge–Kutta integration with generalized Nyström compression and prove moment estimates under positive Gaussian sketch oversampling. Their framework and projection formula are credited, and this example lies outside the published right-oversampling regime. Nakatsukasa (arXiv:2009.11392) develops stabilized generalized Nyström analysis, including oblique-projection reasoning and Gaussian inverse factors; the distributional mechanism itself is not claimed new. Kressner–Lam (arXiv:2302.12761) establish mean-square oversampled generalized Nyström estimates; their displayed assumptions involve larger right and left sketch sizes than the one-vector regime here. Classical Gaussian range-finder estimates likewise assume oversampling when taking relevant expectations. The added claim is the **complete exact error-moment and singular-value-gap phase diagram in the unoversampled one-vector regime**, including the identity \(\mathbb ET_h^2=((k-1)/(k-2))h\) and its dynamical one-step interpretation.

## Limitations
This theorem treats independent real Gaussian sketches, one sampled right direction, two nonzero singular values, the unstabilized exact-arithmetic pseudoinverse, and Frobenius error at one step. It does not assert the same law for structured sketches, positive right oversampling, finite-precision pseudoinverses, repeated Runge–Kutta steps, or arbitrary matrix spectra. The moment constants follow from the stated special geometry and are not general lower bounds for all rank-one approximation schemes. Overlap with equivalent classical angular or Gaussian ratio identities remains possible despite literature comparison.

## References
Lam, Ceruti, and Kressner, “Randomized low-rank Runge–Kutta methods,” arXiv:2409.06384 (first posted 10 September 2024), https://arxiv.org/abs/2409.06384.
Nakatsukasa, “Fast and stable randomized low-rank matrix approximation,” arXiv:2009.11392, https://arxiv.org/abs/2009.11392.
Kressner and Lam, “Randomized low-rank approximation of parameter-dependent matrices,” arXiv:2302.12761, https://arxiv.org/abs/2302.12761.
Halko, Martinsson, and Tropp, “Finding structure with randomness,” SIAM Review 53 (2011), 217–288, https://arxiv.org/abs/0909.4061.