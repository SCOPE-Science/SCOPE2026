# Sharp Gaussian smoothing threshold for nontrivial positive Fourier twins

## Finding

Let \(\phi_t(x)=(2\pi t)^{-1/2}\exp[-x^2/(2t)]\). For every real \(t>0\), set
\[
f_t(x)=\frac{\phi_t(x)+5\phi_t(x-1)+6\phi_t(x-2)}{12},\qquad
g_t(x)=\frac{3\phi_t(x)+7\phi_t(x-1)+2\phi_t(x-2)}{12}.
\]
Both densities have strictly nonzero Fourier transforms along the real axis, the same full Fourier intensity, and are inequivalent under translations and reflected translations. Define \(Q(t)=\frac{25}{6}e^{1/t}\). There is exactly one \(t_*\in(1/4,1/3)\) satisfying
\[
(t_*-1/4)(Q(t_*)-4)=1,
\qquad t_*=0.2548339622562053983\ldots.
\]
Both densities are globally log-concave precisely for \(t\ge t_*\) and both are uniformly strongly log-concave precisely for \(t>t_*\). At equality \(f_{t_*}\) has two separate points of vanishing log-density curvature. Centering and scaling each distribution to unit variance gives two distinct, non-reflected probability densities with the same Fourier intensity, converging to the standard Gaussian in \(C^k\) on every compact set for all finite \(k\), with their log-Hessians converging uniformly on the whole line to \(-1\).

## Assumptions and scope

Fourier transform is \(\widehat h(\xi)=\int_{\mathbb R}e^{-i\xi x}h(x)\,dx\); Fourier intensity means \(|\widehat h(\xi)|^2\) for all real \(\xi\). Log-concave means \((\log h)''\le0\) everywhere. Uniformly strongly log-concave means there exists a constant \(\kappa>0\) such that \((\log h)''\le-\kappa\) everywhere. Translations and reflected translations are the usual ambiguities of real positive Fourier phase retrieval. No uniqueness claim about other possible partners is made.

## Proof

**1. Fourier ambiguity and inequivalence.** With \(z=e^{-i\xi}\), the discrete coefficient polynomials factor as
\[
12e^{t\xi^2/2}\widehat f_t(\xi)=(1+2z)(1+3z),\qquad
12e^{t\xi^2/2}\widehat g_t(\xi)=(1+2z)(3+z).
\]
For \(|z|=1\), \(|1+3z|=|3+z|\). Thus their intensities agree everywhere. The factors have no unit-circle roots and \(|1+2z|\ge1\), \(|1+3z|\ge2\); so neither transform vanishes for real \(\xi\). The discrete means are respectively \(17/12\) and \(11/12\); both variances are \(59/144\), while the third centered moments are \(-145/864\) and \(17/864\). Gaussian convolution preserves third cumulants. These third moments are neither equal nor opposite, excluding both translations and reflected translations. The common variance permits the same standardization factor.

**2. An exact three-location curvature optimization.** For a general positive triple \((a,b,c)\) on \(\{0,1,2\}\), the conditional distribution of the latent location given the observed value \(x\) has probabilities proportional to \(a,be^{-1/(2t)}e^{x/t},ce^{-2/t}e^{2x/t}\). After scaling the positive parameter this is proportional to \((1,\lambda u,u^2)\), where
\[
\lambda=\frac b{\sqrt{ac}}e^{1/(2t)},\qquad u>0.
\]
Differentiating the Gaussian mixture gives the *exact identity*
\[
(\log h)''(x)=-\frac1t+\frac{\operatorname{Var}(J\mid x)}{t^2},\qquad J\in\{0,1,2\}.
\]
Put \(z=u+u^{-1}\ge2\). A direct calculation yields
\[
\operatorname{Var}(J\mid x)=\frac{\lambda z+4}{(z+\lambda)^2}.
\]
Differentiation with respect to \(z\) therefore gives the sharp global maximum
\[
M(\lambda)=\begin{cases}
\frac{2}{\lambda+2},&0<\lambda\le4,\\
\frac{\lambda^2}{4(\lambda^2-4)},&\lambda\ge4.
\end{cases}
\]
The maximum occurs at \(z=2\) for \(\lambda\le4\), and at \(z=\lambda-8/\lambda>2\) for \(\lambda>4\). The function \(M\) is strictly decreasing. Hence the \(f_t\) triple, for which \(\lambda_f=(5/\sqrt6)e^{1/(2t)}\), has larger worst-case posterior variance than the \(g_t\) triple, for which \(\lambda_g=(7/\sqrt6)e^{1/(2t)}\). Therefore both are log-concave if and only if \(t\ge M(\lambda_f)\), and both are uniformly strongly log-concave if and only if the inequality is strict.

**3. The single sharp transition.** For \(t\le1/4\), \(M(\lambda)>1/4\) and log-concavity fails. On \((1/4,1/3]\), \(\lambda_f>4\) and the condition is equivalent to \(F(t):=(t-1/4)(Q(t)-4)\ge1\), with \(Q(t)=\lambda_f^2=(25/6)e^{1/t}\). Here \(F(1/4)=0\) as a right limit and \(F(1/3)>1\). Moreover
\[
F'(t)=Q(t)\frac{(t-1/2)^2}{t^2}-4>0
\quad\text{for } 1/4<t\le1/3,
\]
because \(Q(t)\ge(25/6)e^3>80\) and \((t-1/2)^2/t^2\ge1/4\). Exactly one crossing occurs. For \(t\ge1/3\) as long as \(\lambda_f\ge4\), \(M(\lambda_f)\le1/3\le t\). Once \(\lambda_f\le4\), necessarily \(t>1/2\), while \(M(\lambda_f)\le2/(2+5/\sqrt6)<1/2\). Thus no second crossing is possible. At \(t=t_*\), \(\lambda_f>4\) and the maximizing \(z>2\) has two reciprocal positive solutions \(u\), giving two distinct zero-curvature points; \(g_t\) has strictly negative log curvature.

**4. Near-Gaussian shape control.** After subtracting each mean and dividing by the common standard deviation \(s_t=\sqrt{t+59/144}\), both laws become mixtures of normal variables with variance \(t/s_t^2\to1\) and means of order \(1/s_t\to0\). Differentiation under the finite mixture gives convergence of densities and all derivatives on compact sets. The rescaled log-Hessian equals \(s_t^2(\log h_t)''\), and the posterior-variance identity bounds it, *uniformly in position*, between \(-s_t^2/t\) and \(-s_t^2/t+s_t^2/t^2\). Both bounds tend to \(-1\). Distinctness after centering follows from the two unequal-in-magnitude third centered moments, which become nonzero and remain neither equal nor opposite under common scaling.

## Verification

All algebraic identities and moments have a standard-library exact-arithmetic checker in `CHECK.py`. It verifies the positive coefficient vectors, coefficient-product autocorrelation, central cumulants, and formula for the conditional variance and its derivative using rational symbolic identities evaluated by coefficient comparison. The transcendental threshold's existence and uniqueness and the global log-concavity classification are proved above; numerical root values are illustrative, not proof.

## Relationship to prior work

Novikov and Xu (2026) establish a general finite-difference construction for Fourier phase-retrieval ambiguities with compactly supported seeds. The two-factor ambiguity here uses that classical root-reflection mechanism, not a claim to have discovered root flipping. The additional statement proved here is an *exact Gaussian smoothing threshold* for a positive probability-density pair and the persistence of its ambiguity under arbitrarily strong near-Gaussian shape regularity. This conclusion is not a theorem in their compact-seed setting, although extending their algebra to Gaussian seeds is immediate; the main priority risk is an unlocated equivalent Gaussian-mixture log-concavity classification. Xia and Xu (2026) study Fourier retrieval for unions of intervals rather than positive Gaussian mixtures. Sparse phase retrieval papers and Gaussian-basis reconstruction work give complementary generic-uniqueness or reconstruction results.

## Limitations

This is a sharp statement for a particular nontrivial three-Gaussian homometric pair, not a characterization of all Gaussian mixtures, all log-concave laws, or all Fourier-phase fibers. The example is deliberately elementary in its root-flipping component, and its originality depends on the exact shape-regularity transition and its inverse-problem interpretation. An older equivalent formula under statistical Gaussian-mixture terminology may exist. No independent scientific audit or publication-priority certification has been performed.

## References

- R. Novikov and T. Xu, *On phase retrieval for continuous and discrete Fourier transforms*, arXiv:2604.25662, first public April 28, 2026. https://arxiv.org/abs/2604.25662
- R. Xia and T. Xu, *Fourier Phase Retrieval for Finite Unions of Intervals*, arXiv:2606.19855, first public June 18, 2026. https://arxiv.org/abs/2606.19855
- R. Trahan III and D. Hyland, *Phase retrieval of images using Gaussian radial bases*, Applied Optics 52 (2013), 8627–8633, DOI 10.1364/AO.52.008627.
- J. Ranieri, A. Chebira, Y. M. Lu, and M. Vetterli, *Phase Retrieval for Sparse Signals: Uniqueness Conditions*, arXiv:1308.3058.
