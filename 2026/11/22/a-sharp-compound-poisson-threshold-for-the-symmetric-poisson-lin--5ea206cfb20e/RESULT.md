# A sharp compound-Poisson threshold for the symmetric Poisson–Lindley distribution

## Finding

Let \(X_\theta\) have the symmetric Poisson–Lindley (SPL) distribution of Chesneau, Chakraborty, Bakouch and Karakaya (2023), with \(\theta>0\) and
\[
 \Pr(X_\theta=k)=\frac{\theta^2(\theta+2+|k|)}{(\theta^3+4\theta^2+6\theta+2)(1+\theta)^{|k|}},\qquad k\in\mathbb Z.
\]
Write \(r=(1+\theta)^{-1}\). Let \(r_*\) be the unique root in \((0,1)\) of
\[
 P(r)=3r^5+2r^4+6r^3-r-2=0,
\]
and set \(\theta_*=r_*^{-1}-1=0.482487738319200658\ldots\). Then **the SPL law is infinitely divisible under ordinary addition (as a distribution on the real line, equivalently here by compound-Poisson convolution on \(\mathbb Z\)) if and only if \(\theta\ge\theta_*\)**, or equivalently \(0<r\le r_*\).

More precisely, for \(0<r<r_0\), the characteristic function has a negative numerator cosine coefficient; for the whole interval \(0<r<r_\mathrm{z}\) it is positive on the real line. Here \(r_0\) is the unique positive root of \(2r^3+r^2-1=0\), and \(r_\mathrm{z}=0.67513087056664607088\ldots\) is the unique root in \((0,1)\) of \(r^3+3r^2-r-1=0\). In particular, \(r_*<r_\mathrm{z}\). For \(r_*<r<r_\mathrm{z}\), the characteristic function is everywhere **strictly positive**, yet the distribution is **not** infinitely divisible; at \(r=r_\mathrm{z}\) it vanishes at angle \(\pi\), and beyond that it is negative at angle \(\pi\).

On the infinitely divisible side, put
\[
 a=\frac{1+r}{r},\quad A=a(1-r^4)-4r^2,\quad
 B=2r\big[(1+r^2)-a(1-r^2)\big],\quad
 s=\frac{B}{A+\sqrt{A^2-B^2}}.
\]
Then \(-r<s\le r\), and the **exact bilateral Lévy masses** are
\[
 \boxed{\quad \nu_\theta(\{n\})=\nu_\theta(\{-n\})
 =\frac{2r^n+(-1)^{n+1}s^n}{n},\qquad n=1,2,\ldots\quad}.
\]
They are positive and summable. Thus \(X_\theta\) is a sum of a Poisson-distributed number of independent signed integer jumps, with the displayed positive jump intensities. At \(r=r_*\), one has \(s=r\), and no individual Lévy mass vanishes.

## Assumptions and scope

The parameter is any finite real \(\theta>0\); no zero-inflation parameter, location shift, truncation or separate positive-side Poisson–Lindley convolution is included. The displayed mass function is normalized and symmetric on all of \(\mathbb Z\). Infinite divisibility means arbitrarily fine additive iid convolution roots; the proof uses the standard fact that a symmetric infinitely divisible distribution supported on \(\mathbb Z\) has a symmetric compound-Poisson representation with nonnegative masses on \(\mathbb Z\setminus\{0\}\). No assertion about the stronger property of self-decomposability is made.

## Proof

**1. Exact characteristic function.** Let \(c=\theta^2/(\theta^3+4\theta^2+6\theta+2)\), \(r=(1+\theta)^{-1}\), and \(a=\theta+2=(1+r)/r\). Then the mass is \(c(a+|k|)r^{|k|}\). The Poisson kernel and its radial derivative give
\[
 \sum_{k\in\mathbb Z}r^{|k|}e^{ikt}
 =\frac{1-r^2}{D(t)},\qquad
 D(t)=1-2r\cos t+r^2,
\]
so, after applying \(a+r\partial_r\),
\[
 \phi_\theta(t)=c\,\frac{A+B\cos t}{D(t)^2},
 \quad A=a(1-r^4)-4r^2,\quad
 B=2r\big[(1+r^2)-a(1-r^2)\big].
\]
The series is absolutely convergent and \(\phi_\theta(0)=1\). Direct factorization yields
\[
 A+B=-\frac{(r-1)^2}{r}(r^3-r^2-r-1)>0,\qquad
 A-B=-\frac{(r+1)^2}{r}(r^3+3r^2-r-1).
\]
The latter cubic has exactly one positive zero \(r_\mathrm{z}\in(0,1)\), by Descartes' rule and sign change. If \(r\ge r_\mathrm{z}\), then \(\phi_\theta(\pi)\le0\), whereas the characteristic function of a symmetric infinitely divisible lattice law is everywhere positive. Such parameters are therefore excluded.

**2. Canonical cosine logarithm in the zero-free phase.** For \(0<r<r_\mathrm{z}\), the factorizations show \(A>|B|\) and \(A>0\). The uniquely defined \(s\in(-1,1)\) in the finding obeys
\[
 \frac BA=\frac{2s}{1+s^2},\qquad
 A+B\cos t=\frac A{1+s^2}(1+s e^{it})(1+s e^{-it}).
\]
Expanding the absolutely convergent logarithmic Fourier series, including the denominator \(D(t)^2\), and using \(\phi_\theta(0)=1\), gives
\[
 \log\phi_\theta(t)=\sum_{n=1}^\infty c_n(\cos(nt)-1),\qquad
 c_n=\frac{4r^n+2(-1)^{n+1}s^n}{n}.
\]
The lattice Lévy–Khintchine characterization says that infinite divisibility is equivalent to \(c_n\ge0\) for every positive integer \(n\). Here this holds **exactly** when \(|s|\le r\): if \(s<0\), every coefficient has numerator \(4r^n-2|s|^n\); if \(s\ge0\), the odd coefficients are positive and every even coefficient has numerator \(4r^n-2s^n\). Whenever \(|s|>r\), sufficiently large even indices have a strictly negative coefficient. Conversely \(|s|\le r\) gives strictly positive coefficients for all indices, with summable total mass. Half of \(c_n\) is the positive Lévy mass at each of \(\pm n\).

**3. The algebraic phase boundary.** The map \(s\mapsto2s/(1+s^2)\) is strictly increasing on \((-1,1)\). Its comparisons with \(\pm r\) are therefore exactly the comparisons of \(B(1+r^2)\) with \(\pm2rA\). Two identities give
\[
 B(1+r^2)+2rA=2r(1-r^2)^2>0,
\]
\[
 B(1+r^2)-2rA=2\big(3r^5+2r^4+6r^3-r-2\big)=2P(r).
\]
Thus the lower bound \(s>-r\) always holds in the zero-free phase, while \(s\le r\) holds exactly when \(P(r)\le0\). Descartes' rule of signs and the endpoint values \(P(0)=-2\), \(P(1)=8\) show that \(P\) has exactly one positive root \(r_*\in(0,1)\). At \(r=r_\mathrm{z}\), one has \(A=B>0\), whence \(2P(r_\mathrm{z})=A(1-r_\mathrm{z})^2>0\); therefore \(r_*<r_\mathrm{z}\). Combining the cases establishes the complete threshold and the strict positivity of the Lévy masses at equality.

**4. A finite rational witness in the zero-free nondivisible region.** At \(r=27/40\), equivalently \(\theta=13/27\), exact arithmetic gives
\[
 A=\frac{9942253}{69120000},\quad B=\frac{2263}{16000},\quad
 A-B=\frac{166093}{69120000}>0.
\]
For \(t_0=41/50\),
\[
 B(1+t_0^2)-2t_0A=\frac{5544383}{8640000000}>0,
 \qquad t_0^4-2r^4=\frac{29546783}{800000000}>0.
\]
The monotonic transformation therefore gives \(s>t_0\), and \(c_4=(4r^4-2s^4)/4<0\). This explicit **fourth-harmonic obstruction** shows that a zero-free characteristic function need not imply infinite divisibility. It is only an example; the full converse was proved by the all-index Fourier argument.

## Verification

The standalone `check_spl_divisibility.py` reproduces the Poisson-kernel rational identity, normalization, two boundary factorizations, the \(P\)-comparison identities, rational isolation brackets for both positive roots, the exact nondivisible witness, and independently summed characteristic-function samples. Exact symbolic algebra is used for structural identities and the rational witness; finite numerical samples are corroboration, not substitutes for the infinite Fourier-series proof. The root values are
\[
 r_*=0.67454183542439917437\ldots,\qquad
 r_\mathrm{z}=0.67513087056664607088\ldots.
\]

## Relationship to prior work

Chesneau, Chakraborty, Bakouch and Karakaya (2023) introduce precisely this SPL mass in their Eq. (1.1), give mixtures and transforms, and explicitly list discrete decomposability among future developments (p. 299). Their log-concavity criterion \(\theta\ge\sqrt2-1\) is a different property: throughout \(\sqrt2-1\le\theta<\theta_*\), the SPL law is log-concave but not infinitely divisible. The threshold and bilateral Lévy intensities here are not stated in that paper. Earlier symmetric discrete double-Lindley models use related linear-geometric kernels. The Poisson–Lindley difference distribution is instead the difference of two independent nonnegative Poisson–Lindley variables, not the symmetrically normalized single Poisson–Lindley mass in the present theorem. A separate additive perturbation of the discrete Laplace model was also published in 2022. General compound-Poisson theory supplies the conceptual criterion; none of the accessible claims directly specifies the sharp SPL quintic boundary. The literature-priority comparison remains qualified by incomplete access to related 2022 full texts.

## Limitations

The result pertains only to the original, symmetric, non-zero-inflated SPL distribution; the zero-inflated regression and translated variants of the source are not classified. No simulation, estimation optimality, thinning self-decomposability, multivariate construction or separate probability-of-zero boundary is asserted. The literature comparison is limited to the sources discussed and does not establish global priority.

## References

1. C. Chesneau, S. Chakraborty, H. S. Bakouch and K. Karakaya, “A new symmetric distribution on integers with applications in data modeling and zero inflated regression,” *Journal of Statistics and Management Systems* 26 (2023), 291–308, DOI: https://doi.org/10.47974/JSMS-865; full text: https://tarupublications.com/journals/jsms/volume/26/issue/2/a-new-symmetric-distribution-on-integers-with-applications-in-data-modeling-and-zero-inflated-regression/pdf (pp. 293–299, 306–308 inspected).
2. C. Chesneau, H. S. Bakouch, L. Tomy and G. Veena, “A new discrete distribution on integers: Analytical and applied study on stock exchange and flood data,” *Journal of Statistics and Management Systems* 25 (2022), 1899–1917, DOI: https://doi.org/10.1080/09720510.2021.1995199 (metadata/abstract accessible; full text not verified).
3. H. S. Salinas, H. S. Bakouch, S. R. Bapat et al., “Discrete Asymmetric Double Lindley Distribution on Z: Theory, Likelihood Inference, and Applications,” *Symmetry* 18 (2026), 533, DOI: https://doi.org/10.3390/sym18030533 (abstract and publicly indexed summary inspected).
4. C. Chesneau, H. S. Bakouch, L. Tomy and G. Veena, “The Poisson-Lindley difference model with application to discrete stock price change,” *International Journal of Modelling and Simulation* 43 (2023), 406–415, first online 13 June 2022, DOI: https://doi.org/10.1080/02286203.2022.2086422 (abstract available; full text not verified).
5. S. R. Bapat, H. S. Bakouch and C. Chesneau, “A distribution on ℤ via perturbing the Laplace distribution with applications to finance and health data,” *Stat* 12 (2023), e535, first published 22 December 2022, DOI: https://doi.org/10.1002/sta4.535 (abstract available; full text not verified).
6. The classical lattice Lévy–Khintchine / compound-Poisson representation for infinitely divisible laws on \(\mathbb Z\); used as background theory rather than claimed here as a new result.
