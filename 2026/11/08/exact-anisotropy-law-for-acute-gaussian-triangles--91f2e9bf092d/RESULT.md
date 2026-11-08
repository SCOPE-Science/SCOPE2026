# Exact anisotropy law for acute Gaussian triangles

## Finding
Let \(X_1,X_2,X_3\) be independent points in the Euclidean plane with common Gaussian law \(N(\mu,\Sigma)\), where \(\Sigma\) is positive definite. Define the covariance anisotropy \(R=\lambda_{\max}(\Sigma)/\lambda_{\min}(\Sigma)\ge1\), and let \(A(R)\) denote the probability that their triangle is acute.

For \(q_R(\theta)=1+(R-1)\cos^2\theta\), the complete anisotropy law is
\[
A(R)=\frac{18}{\pi}\int_0^{\pi/2}\frac{q_R(\theta)}{\sqrt{(1+3q_R(\theta))(R+3q_R(\theta))}}\,d\theta-2.
\]
It is strictly decreasing as \(R\) increases from \(1\) to infinity, with \(A(1)=1/4\), strictly positive values at finite \(R\), and limit zero. Its exact local and elongated asymptotics are
\[
A(R)=\frac14-\frac9{256}(R-1)^2+O((R-1)^3)\qquad(R\downarrow1),
\]
\[
A(R)=\frac{\sqrt3}{\pi}\frac{\log R}{R}+O(R^{-1})\qquad(R\to\infty).
\]
The logarithmic coefficient and the quadratic susceptibility are thus exact. The theorem gives a complete strict shape ordering of these Gaussian triangle models by a single covariance aspect ratio.

## Assumptions and scope
All three vertices are independent and identically distributed under one nondegenerate *planar* Gaussian law; the same (arbitrary) mean is allowed. Angles and distances are Euclidean. Right and degenerate triangles have probability zero. The spectral ratio \(R\) involves covariance **eigenvalues**, not standard deviations. Common translations, orthogonal transformations, and positive scales leave \(A\) unchanged, so diagonalization and division by \(\lambda_{\min}\) reduce to \(\Sigma=\operatorname{diag}(R,1)\). The result covers every finite \(R\ge1\); the limit \(R=\infty\) is not a nonsingular Gaussian model.

## Proof
**1. Reduce an obtuse angle to two independent quadratic forms.** Let \(U=X_2-X_1\) and \(V=X_3-X_1\). Then \(U+V\) and \(U-V\) are independent centered Gaussian vectors, with covariance matrices \(6\Sigma\) and \(2\Sigma\). The identity \(4U\cdot V=\|U+V\|^2-\|U-V\|^2\) gives
\[
\Pr(U\cdot V<0)=\Pr(Q_2>3Q_1),
\]
where \(Q_1,Q_2\) are independent copies of \(RZ_1^2+Z_2^2\), with independent standard normal \(Z_1,Z_2\). The events that the three distinct triangle angles are obtuse are disjoint except for null sets, and their probabilities agree by exchangeability. Thus \(A(R)=1-3\Pr(Q_2>3Q_1)\).

**2. Integrate the Gaussian radii.** In polar coordinates \(Q_j=H_jq_R(\Theta_j)\), where the angles are independent uniform variables on \([0,2\pi)\), independent of iid \(\chi^2_2\) radial variables \(H_j\). Since \(\chi^2_2\) has an exponential law,
\[
\Pr(Q_2>3Q_1\mid\Theta_1,\Theta_2)=\frac{q_R(\Theta_2)}{q_R(\Theta_2)+3q_R(\Theta_1)}.
\]
The standard angular integral
\[
\frac1{2\pi}\int_0^{2\pi}\frac{d\phi}{1+3u+(R-1)\cos^2\phi}
=\frac1{\sqrt{(1+3u)(R+3u)}}
\]
for \(u>0\) gives
\[
\Pr(Q_2>3Q_1)=1-\frac2\pi\int_0^{\pi/2}\frac{3q_R(\theta)}{\sqrt{(1+3q_R(\theta))(R+3q_R(\theta))}}\,d\theta.
\]
Substitution into \(A=1-3\Pr(Q_2>3Q_1)\) yields the asserted formula.

**3. Prove strict monotonicity without differentiating the elliptic integral.** Put \(S=\cos^2\Theta_1\) and \(T=\cos^2\Theta_2\). These are iid with the \(\operatorname{Beta}(1/2,1/2)\) law. Symmetrizing the conditional probability under \(S\leftrightarrow T\) gives the exact identity
\[
A(R)=\frac14-\frac94\,\mathbb E\left[
\frac{(q_R(S)-q_R(T))^2}
{3q_R(S)^2+10q_R(S)q_R(T)+3q_R(T)^2}
\right],
\]
where here \(q_R(s)=1+(R-1)s\) for \(s\in[0,1]\). Indeed,
\[
\frac12\left(\frac{b}{b+3a}+\frac{a}{a+3b}\right)-\frac14
=\frac{3(a-b)^2}{4(3a^2+10ab+3b^2)}.
\]
For fixed distinct \(s,t\), the absolute logarithm of \(q_R(s)/q_R(t)\) grows strictly in \(R>1\): its derivative has the sign of \(s-t\), since
\[
\frac{d}{dR}\log\frac{1+(R-1)s}{1+(R-1)t}
=\frac{s-t}{(1+(R-1)s)(1+(R-1)t)}.
\]
Writing \(z=a/b+b/a\ge2\), the displayed rational deficit equals \((z-2)/(3z+10)\), which grows strictly with \(z\). As \(\Pr(S\ne T)=1\), the expectation is strictly increasing and \(A\) strictly decreases for \(R>1\). The case \(R=1\) gives \(A(1)=1/4\). The Gaussian law has a positive density everywhere, and acute triangles form a nonempty open set of triples, so \(A(R)>0\) at each finite \(R\).

**4. Compute the isotropic quadratic coefficient.** Write \(\delta=R-1\). The denominator in the symmetrized deficit is \(16+O(\delta)\) uniformly for \(s,t\in[0,1]\), while its numerator is \(\delta^2(s-t)^2\). The arcsine law has \(\mathbb E S=1/2\) and \(\operatorname{Var}(S)=1/8\), so \(\mathbb E(S-T)^2=1/4\). Hence
\[
\frac14-A(1+\delta)=\frac94\frac{\delta^2}{16}\frac14+O(\delta^3)
=\frac9{256}\delta^2+O(\delta^3).
\]

**5. Establish the sharp large-anisotropy logarithm.** Set \(\varepsilon=1/R\), let \(x\in(0,1)\) have arcsine density \(w(x)=1/(\pi\sqrt{x(1-x)})\), and define \(y=x+\varepsilon(1-x)\). The integral in Step 2 becomes \(J(\varepsilon)=\mathbb E f_{\varepsilon}(x)\) for
\[
f_{\varepsilon}(x)=\frac{y}{\sqrt{(\varepsilon+3y)(1+3y)}}.
\]
At \(\varepsilon=0\),
\[
J(0)=\frac2{\pi\sqrt3}\int_0^{\pi/2}\frac{\cos\theta}{\sqrt{1+3\cos^2\theta}}\,d\theta=\frac29.
\]
On \(x\ge\varepsilon\), Taylor's theorem, uniformly for \(0<\varepsilon\le x\le1\), gives
\[
f_{\varepsilon}(x)-f_0(x)=\varepsilon f_0(x)L(x)+O(\varepsilon^2x^{-3/2}),
\]
where
\[
L(x)=\frac1{3x}-\frac12-\frac{3(1-x)}{2(1+3x)}.
\]
The derivative remainder bound follows by twice differentiating the elementary function: on \(\varepsilon\le x\), its two denominator factors are uniformly comparable to \(x\) and \(1\), and its second \(\varepsilon\)-derivative is \(O(x^{-3/2})\). Against \(w(x)\), that remainder integrates to \(O(\varepsilon)\). On \(0<x<\varepsilon\), both \(f_{\varepsilon}\) and \(f_0\) are \(O(\sqrt\varepsilon)\), while the arcsine mass is \(O(\sqrt\varepsilon)\), contributing another \(O(\varepsilon)\). Finally, as \(x\downarrow0\),
\[
f_0(x)L(x)w(x)=\frac1{3\sqrt3\pi x}+O(1),
\]
so integration over \([\varepsilon,1]\) yields
\[
J(\varepsilon)-\frac29=\frac{\varepsilon\log(1/\varepsilon)}{3\sqrt3\pi}+O(\varepsilon).
\]
Because \(A(R)=9J(1/R)-2\), the final asymptotic follows. The coefficient is exact; no finite computation is used to infer the logarithm.

## Verification
A standalone script `verify.py` tests the independent one- and two-angular-integral formulas; compares both with direct simulation of \(1{,}200{,}000\) Gaussian vertex triples over six covariance ratios; checks three near-isotropic coefficients; and compares the high-anisotropy numerical tail with its exact limiting coefficient over three scales. It prints `VERIFY_OK` on success. Reproduce with Python, NumPy and SciPy by executing `python verify.py`. The proof above does not rely on finite quadrature, Monte Carlo, or numerical asymptotic fitting.

## Relationship to prior work
The classical isotropic probability \(A(1)=1/4\) and the associated uniform triangle shape-hemisphere model are established in Edelman and Strang (2015); these facts are background, not new contributions. A 2013 Baylor educational demonstration uses a correlated planar Gaussian model and asks how triangular acuteness changes as the correlation approaches extreme values, but no exact strict-ordering formula was available in the retrieved excerpt. The present claim concerns **nonisotropic** Gaussian vertices, gives an explicit probability integral, proves a strict global anisotropy ordering, and derives both sharp asymptotic regimes. The 2017 Anderson study of the triangle shape sphere treats different conditional shape categories, not this covariance-deformation problem. None of these cited material statements logically entails the new monotonic comparison or logarithmic coefficient without new calculations. Published-index searches and broad mathematical literature searches did not locate a covering theorem; this is a provisional originality assessment, not a claim of historical completeness.

## Limitations
The results apply to three independent Gaussian planar vertices with common covariance and to exact probabilities. They do not address arbitrary elliptically contoured non-Gaussian vertex laws, nonidentical covariances, higher-dimensional Euclidean angles, or finite-sample estimation. No claim is made that the one-dimensional integral is elementary or that all earlier sources on nonisotropic random triangles were accessible. The 2013 educational page could be read only from a retrieved dated excerpt when its full site returned a gateway error.

## References
1. A. Edelman and G. Strang, *Random Triangle Theory with Geometry and Applications*, arXiv:1501.03053, first posted 2015-01-09. In particular, Sections 2.3 and 3.1–3.3 establish the isotropic Gaussian shape model and acute probability. https://arxiv.org/abs/1501.03053
2. *Random triangles*, BaylorISMs educational demonstration, dated 2013-04-23. Its public excerpt discusses correlated Gaussian vertex coordinates and varies their correlation. https://blogs.baylor.edu/baylorisms/2013/04/23/random-triangles/
3. E. Anderson, *Alice in Triangleland: Lewis Carroll's Pillow Problem and Variants Solved on Shape Space of Triangles*, arXiv:1711.11492, first posted 2017-11-30; especially Sections 5–8. https://arxiv.org/abs/1711.11492
4. E. W. Weisstein, *Gaussian Triangle Picking*, MathWorld; historical summary of isotropic Gaussian acute probabilities and the dimensional formulas attributed to earlier literature. https://mathworld.wolfram.com/GaussianTrianglePicking.html
