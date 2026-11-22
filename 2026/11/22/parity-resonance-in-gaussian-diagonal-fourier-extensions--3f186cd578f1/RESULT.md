# Parity resonance in Gaussian diagonal Fourier extensions

## Finding

Let \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\), let \(a,b>0\), and consider the stationary positive-definite kernel on \(\mathbb T^2\) having Fourier weights \(c_{m,n}=\exp(-a m^2-b n^2)\). Denote by \(E\) the canonical minimum-reproducing-kernel-norm extension of a function specified on the diagonal circle \(H=\{(t,t):t\in\mathbb T\}\). This initially defined operator extends uniquely to a bounded, bounded-below operator \(L^2(H)\to L^2(\mathbb T^2)\).

Write \(s=a+b\), \(\alpha=b/(a+b)\), and define
\[
\Theta_s(x)=\sum_{j\in\mathbb Z}e^{-s(j-x)^2},\qquad
R_s(x)=\frac{\Theta_{2s}(x)}{\Theta_s(x)^2}.
\]
The complete squared-singular-value sequence, in diagonal-circle Fourier order, is
\[
\boxed{\lambda_k(E^*E)=R_s(\alpha k),\quad k\in\mathbb Z.}
\]
For every \(s>0\), \(R_s\) is even, one-periodic, **strictly decreasing** on \((0,1/2)\), and has a nondegenerate maximum at integers and a nondegenerate minimum at half-integers.

Let \(K_s(\alpha)\) denote the sharp *squared* condition number of \(E\), namely its squared upper singular bound divided by its squared lower singular bound. Then
\[
\boxed{
K_s(\alpha)=
\begin{cases}
\displaystyle \frac{R_s(0)}{R_s(\lfloor q/2\rfloor/q)},&\alpha=p/q\in\mathbb Q\text{ reduced},\\[6pt]
\displaystyle \frac{R_s(0)}{R_s(1/2)},&\alpha\notin\mathbb Q.
\end{cases}}
\]
Here \(q\ge2\) because \(0<\alpha<1\). If \(q\) is even, the lower bound is attained by Fourier modes; for irrational \(\alpha\), it is sharp but never attained. If \(q\) is odd, the optimal lower squared bound is strictly larger than the half-integer bound.

There is a sharp arithmetic localization dichotomy as \(s\to\infty\) with \(\alpha\) fixed:
\[
\boxed{
\lim_{s\to\infty}K_s(\alpha)=
\begin{cases}
1,&\alpha\in\mathbb Q\text{ with odd reduced denominator},\\
2,&\alpha\notin\mathbb Q\text{ or with even reduced denominator}.
\end{cases}}
\]
More precisely, when \(q\ge3\) is odd, \(K_s(\alpha)-1\sim2e^{-s/q}\); for even \(q\) or irrational \(\alpha\), \(K_s(\alpha)=2-8e^{-s}+O(e^{-2s})\).

The spectral counting measures on consecutive Fourier modes have two different kinds of limit: if \(\alpha=p/q\) is reduced rational, they converge to the uniform discrete measure on the \(q\) values \(R_s(j/q)\), counting repetitions; if \(\alpha\) is irrational, they converge weakly to the distribution of \(R_s(U)\) for \(U\) uniform on \([0,1]\). In the irrational case the full spectrum of \(E^*E\) is the interval \([R_s(1/2),R_s(0)]\) although its point eigenvalues constitute only a countable dense subset. The limiting distribution has a density \(2/|R_s'(x_y)|\) at interior \(y\), where \(x_y\in(0,1/2)\) uniquely solves \(R_s(x_y)=y\), and has inverse-square-root singularities at both spectral edges.

## Assumptions and scope

All torus Haar measures are normalized to total mass one. The kernel is \(K((x_1,x_2),(y_1,y_2))=\sum_{m,n\in\mathbb Z}c_{m,n}e^{i[m(x_1-y_1)+n(x_2-y_2)]}\). These sums converge absolutely. The diagonal restricted kernel has Fourier coefficients \(W_k=\sum_m c_{m,k-m}>0\); its RKHS contains every trigonometric polynomial and is dense in \(L^2(H)\). The canonical extension minimizes the **ambient RKHS norm subject to the exact diagonal restriction**; its eventual \(L^2\)-operator norm is measured with normalized Haar measure, not the RKHS norm. Rationality refers to the anisotropy fraction \(\alpha\), not a geometric change to the diagonal subgroup. All limits with \(s\to\infty\) keep \(\alpha\) fixed and choose \(a=s(1-\alpha)\), \(b=s\alpha\).

## Proof

**1. Fourier fibers.** For any trigonometric polynomial \(u(t)=\sum_k u_ke^{ikt}\), the constraints on an ambient extension \(f\) are \(\sum_m\widehat f(m,k-m)=u_k\). Its RKHS squared norm is \(\sum_{m,n}|\widehat f(m,n)|^2/c_{m,n}\). Cauchy–Schwarz gives the unique fiberwise minimum:
\[
\widehat{Eu}(m,k-m)=\frac{c_{m,k-m}}{W_k}u_k.
\]
Consequently, by orthogonality in ambient \(L^2\),
\[
\|Eu\|_{L^2(\mathbb T^2)}^2
=\sum_k |u_k|^2\frac{\sum_m c_{m,k-m}^2}{W_k^2}.
\]
Completing the square, \(a m^2+b(k-m)^2=s(m-\alpha k)^2+(ab/s)k^2\), yields the stated multiplier \(R_s(\alpha k)\). Each multiplier is a collision probability of a positive discrete Gaussian and therefore lies strictly between zero and one. The continuous positive periodic function \(R_s\) has a positive minimum and finite maximum, so the extension uniquely continues to all \(L^2(H)\), bounded above and below.

**2. Exact theta monotonicity.** Split pairs of integers into those with even and odd sums, using \((m-x)^2+(n-x)^2=((m+n-2x)^2+(m-n)^2)/2\). This proves the duplication identity
\[
\Theta_s(x)^2=\Theta_{2s}(0)\Theta_{2s}(x)
+\Theta_{2s}(1/2)\Theta_{2s}(x-1/2).
\]
Thus \(R_s(x)^{-1}=A+B\Theta_{2s}(x-1/2)/\Theta_{2s}(x)\), with \(A=\Theta_{2s}(0)>0\) and \(B=\Theta_{2s}(1/2)>0\). Poisson summation and Jacobi's triple product give, for \(q=e^{-\pi^2/t}\in(0,1)\),
\[
\Theta_t(x)=\sqrt{\pi/t}\prod_{j\ge1}(1-q^{2j})
\bigl(1+2q^{2j-1}\cos(2\pi x)+q^{4j-2}\bigr).
\]
Every nonconstant factor has strictly negative derivative for \(0<x<1/2\), proving that \(\Theta_t\) has strictly negative derivative there. By evenness and periodicity, \(\Theta_t(x-1/2)\) increases strictly on the same interval. Their positive ratio strictly increases, hence \(R_s\) strictly decreases. Differentiating the strictly positive product at the endpoints shows \(\Theta_t''(0)<0\), \(\Theta_t''(1/2)>0\); the ratio formula then gives \(R_s''(0)<0\), \(R_s''(1/2)>0\). These inequalities are strict for each fixed \(t,s>0\).

**3. Arithmetic spectral classification and sharp bounds.** Rational reduced \(\alpha=p/q\) permutes the residues \(k\bmod q\), so its phase set is exactly \(\{j/q:0\le j<q\}\). The farthest distance from integers is \(\lfloor q/2\rfloor/q\), giving the stated minimum by strict monotonicity, and \(k=0\) gives the global maximum. With irrational \(\alpha\), the phases \(\alpha k\bmod1\) are dense and equidistributed. Strict monotonicity makes the lower spectral edge \(R_s(1/2)\) an unattained infimum, whereas \(k=0\) still attains the upper edge. The standard spectral description of a bounded diagonal operator gives the asserted finite-versus-interval spectrum and weak limits of empirical eigenvalue measures. On each open half-circle \(R_s\) is a diffeomorphism onto its value range; change of variables gives density \(2/|R_s'(x_y)|\). The nonzero endpoint second derivatives produce the two inverse-square-root density divergences, with coefficients \(\sqrt{2/|R_s''(0)|}\) at the upper edge and \(\sqrt{2/R_s''(1/2)}\) at the lower edge.

**4. High-localization parity resonance.** At an integer, the unique nearest lattice atom gives \(R_s(0)=1-4e^{-s}+O(e^{-2s})\). At a half-integer, two equal nearest atoms give \(R_s(1/2)=1/2+O(e^{-2s})\). If \(q\) is odd, the extremal phase \(d=(q-1)/(2q)\) has a unique nearest lattice atom and one next-nearest atom with relative mass \(e^{-s/q}\); the other atoms have exponentially smaller relative mass. Hence \(R_s(d)=1-2e^{-s/q}+o(e^{-s/q})\), and the odd-denominator expansion follows. For even \(q\) and irrational \(\alpha\), substituting the half-integer edge instead gives \(K_s=2-8e^{-s}+O(e^{-2s})\). All asymptotics are for each fixed \(\alpha\); uniformity over varying rational denominators is not asserted.

## Verification

The accompanying standalone `checker.py` uses independent finite Gaussian-sum calculations to compare direct Fourier-fiber weights against the theta formula, check the theta duplication identity, test monotonicity, compare rational-residue extrema and examine the large-\(s\) rates. Run `python checker.py` with standard Python 3. The analytic theta product, Weyl equidistribution, and infinite-dimensional Fourier argument, not a finite checker, establish the universal claims.

## Relationship to prior work

Winkle's 2026 work derives the general Fourier-fiber formula for minimal-RKHS-norm extensions on closed subgroups, including operator norm and lower norm characterizations and examples of torus subgroups. Those **general extension identities are prior work**; the contribution claimed here is the explicit **Gaussian phase-order theorem**, its rational denominator parity classification and sharp large-localization law, and the associated atomic-versus-continuous spectral-edge distribution. No claim of a new general subgroup extension principle is made. Jacobi's theta product and Weyl's equidistribution principle are standard inputs. Publicly accessible metadata and abstract of Winkle's manuscript were examined, but the complete manuscript was inaccessible; a duplicate specialized calculation inside it cannot be ruled out.

## Limitations

This result treats positive coordinate-separable Gaussian Fourier weights and the fixed diagonal subgroup in two dimensions. It does not cover arbitrary stationary kernels, general integer-slope subgroups, non-Gaussian spectra, perturbation-robust inversion or the RKHS-to-RKHS restriction norm. The full text of a highly relevant 2026 manuscript was unavailable for comparison, so bibliographic precedence remains a material risk.

## References

1. D. Winkle, *Minimal-Norm Extensions of Stationary Kernels on Subgroups of Locally Compact Abelian Groups and Gaussian Conditioning*, arXiv:2608.04853, first submitted 2026-08-05, https://arxiv.org/abs/2608.04853 (abstract and metadata accessible; main text not verified).
2. NIST Digital Library of Mathematical Functions, §20.5, especially formula 20.5.3 / 20.5.9 (Jacobi's triple product), https://dlmf.nist.gov/20.5 .
3. Classical Weyl equidistribution theorem for irrational rotations of the circle (standard theorem; no specialized attribution claimed).
