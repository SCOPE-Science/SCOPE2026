# Sixfold phase signature of nearly maximal triangles on an ellipse

## Finding

Fix an ellipse with semiaxes \(a\ge b>0\) along the coordinate axes, and independently sample three boundary points uniformly by Euclidean arclength. Their eccentric anomalies \(\Theta_1,\Theta_2,\Theta_3\in[0,2\pi)\) satisfy \(X_j=(a\cos\Theta_j,b\sin\Theta_j)\). Write \(T\) for their unsigned Euclidean triangle area, \(T_*=3\sqrt3\,ab/4\), and \(E_\varepsilon=\{(T_*-T)/(ab)<\varepsilon\}\). Throughout this result \(a,b\) are fixed as \(\varepsilon\downarrow0\). Define the squared-axis anisotropy
\[
q=\frac{a^2-b^2}{a^2+b^2}\in[0,1),\qquad
D_q(\theta)=1-\frac{3q^2}{4}-\frac{q^3}{4}\cos(6\theta),\qquad
J_q=\int_0^{2\pi}\sqrt{D_q(\theta)}\,d\theta.
\]
**The marked phase law:** under conditioning on \(E_\varepsilon\), the first labelled point's eccentric anomaly converges in total variation to the density
\[
\boxed{g_q(\theta)=\frac{\sqrt{D_q(\theta)}}{J_q}}\quad (0\le\theta<2\pi).
\]
The limit is uniform if and only if \(a=b\). For noncircular ellipses all nonconstant Fourier modes of order below six vanish, while the sixth is strictly negative. It has exactly six strict maxima when noncircular, at \(\theta=(2j+1)\pi/6\), and six minima at \(\theta=j\pi/3\), modulo \(2\pi\).

**Sharp shape inversion:** the single sixth Fourier moment \(M_6(q)=\int_0^{2\pi}\cos(6\theta)g_q(\theta)\,d\theta\) is continuous and strictly decreasing from \(0\) to \(-1/3\) as \(q\) increases from \(0\) to \(1\). Hence \(M_6\) uniquely determines \(a/b=\sqrt{(1+q)/(1-q)}\). More explicitly the phase-density extrema determine
\[
R_q=\frac{\max g_q}{\min g_q}=\sqrt{\frac{1+\delta_q}{1-\delta_q}},\qquad
\delta_q=\frac{q^3}{4-3q^2},\qquad
\delta_q=\frac{R_q^2-1}{R_q^2+1}.
\]
The small-anisotropy inverse is only cube-root stable: \(M_6(q)=-q^3/16+O(q^5)\) and \(R_q-1=q^3/4+O(q^5)\).

**Local marked shape law:** with probability one for all sufficiently small \(\varepsilon\) on \(E_\varepsilon\), there is a unique branch \(\Sigma\in\{+,-\}\). For \(\Sigma=+\) write
\[
\Theta_2=\Theta_1+2\pi/3+\sqrt\varepsilon\,U_\varepsilon,\quad
\Theta_3=\Theta_1+4\pi/3+\sqrt\varepsilon\,V_\varepsilon
\pmod{2\pi};
\]
for \(\Sigma=-\), interchange the two offsets \(2\pi/3\) and \(4\pi/3\) in these expressions. Then the joint law of \((\Theta_1,\Sigma,U_\varepsilon,V_\varepsilon)\), conditioned on \(E_\varepsilon\), converges in total variation to the independent product of density \(g_q\), a fair sign \(\Sigma\), and uniform Lebesgue probability on
\[
\mathcal E=\left\{(u,v)\in\mathbb R^2:\frac{\sqrt3}{4}(u^2-uv+v^2)<1\right\}.
\]
In particular, \((T_*-T)/(ab\varepsilon)\) conditioned on \(E_\varepsilon\) converges to uniform measure on \([0,1]\), independent of the limiting phase.

For calibration the *scalar* rare-area coefficient is
\[
\Pr(E_\varepsilon)=K(q)\varepsilon+o(\varepsilon),\qquad
K(q)=\frac{16\pi}{3}\frac{J_q}{I_q^3},\qquad I_q=\int_0^{2\pi}\sqrt{1-q\cos(2\theta)}\,d\theta.
\]
Its general density-correlation form is already covered by the prior literature on \(U\)-max geometric statistics; **the scalar asymptotic is not asserted to be novel**. An equivalent explicit evaluation using the complete elliptic integral of the second kind \(\mathsf E(m)=\int_0^{\pi/2}\sqrt{1-m\sin^2t}\,dt\) is
\[
K(q)=\frac\pi3\frac{\sqrt{1-3q^2/4+q^3/4}}{(1+q)^{3/2}}
\frac{\mathsf E\big(2q^3/(4-3q^2+q^3)\big)}{\mathsf E\big(2q/(1+q)\big)^3}.
\]
Thus \(K(0)=4/(3\pi)\), \(\lim_{q\uparrow1}K(q)=\pi/12\), and \(K(q)=\frac4{3\pi}(1-3q^2/16+O(q^4))\) near circularity. The limit \(q\uparrow1\) is taken *after* the small-deficit limit; no uniform two-parameter crossover is claimed.

## Assumptions and scope

Points are independent, sampled from normalized Euclidean boundary arclength, not uniform eccentric anomaly. Every asymptotic conditions on a fixed genuine ellipse \(a\ge b>0\). \(T\) is the ordinary unsigned Euclidean area of the three-point convex hull. \(\Theta_1\) is the anomaly of the **labelled** first point, defined with the ellipse center and principal axes fixed. Branch and deviations are measurable and uniquely defined once \(\varepsilon\) is sufficiently small. The phase reconstruction is an identification statement *within this anomaly-parametrized model*, not a claim that an unknown ellipse's eccentric anomaly can be measured without its parametrization.

## Proof

1. **The extrema and their local Hessian.** The affine map \((x,y)\mapsto(ax,by)\) multiplies triangle area by \(ab\). For three cyclically ordered angles on the unit circle, write their positive gaps as \(d_1,d_2,d_3\), summing to \(2\pi\). The area divided by \(ab\) is \(2\prod_{j=1}^3\sin(d_j/2)\). Strict concavity of \(\log\sin x\) on \((0,\pi)\) makes \(d_1=d_2=d_3=2\pi/3\) the only maximum-gap triple. Fixing \(\Theta_1=\theta\), the two labelled orientations are the two branches stated above. Put \(u=\Theta_2-\theta-2\pi/3\), \(v=\Theta_3-\theta-4\pi/3\) on the positive branch. Taylor expansion of \(\frac12[\sin(2\pi/3+u)+\sin(2\pi/3+v-u)+\sin(2\pi/3-v)]\) gives
\[
\frac{T_*-T}{ab}=\frac{\sqrt3}{4}(u^2-uv+v^2)+O((|u|+|v|)^3).
\]
The other branch has the same form. Since the set of maximizers is a compact pair of closed curves and the quadratic form is positive definite, for small enough \(\varepsilon\) the entire event \(E_\varepsilon\) lies in the two disjoint branch tubes with \(|u|+|v|\le C\sqrt\varepsilon\). The ellipse \(\mathcal E\) has Lebesgue area \(8\pi/3\), obtained from determinant \(9/64\) of its quadratic-form matrix.

2. **Arclength density, strong marked limit, and the known scalar coefficient.** Write \(A=(a^2+b^2)/2\) and \(q=(a^2-b^2)/(a^2+b^2)\). The speed of eccentric anomaly is \(s(\theta)=\sqrt A\sqrt{1-q\cos2\theta}\). Thus the sampling density is \(p_q(\theta)=\sqrt{1-q\cos2\theta}/I_q\). In either branch the joint density in the coordinates \((\theta,u,v)\) is \(p_q(\theta)p_q(\theta+2\pi/3+u)p_q(\theta+4\pi/3+v)\). After \(u=\sqrt\varepsilon U\), \(v=\sqrt\varepsilon V\), it converges uniformly on the bounded support tubes to \(p_q(\theta)p_q(\theta+2\pi/3)p_q(\theta+4\pi/3)\), with the event indicator converging almost everywhere to \(\mathbf1_{\mathcal E}(U,V)\). Dominated convergence gives \(L^1\) convergence of the unnormalized, rescaled densities; their integral is positive and therefore the normalized conditional laws converge in total variation. Both branches have equal limiting mass. The scalar probability is \(2(8\pi/3)\varepsilon\int p_q(\theta)p_q(\theta+2\pi/3)p_q(\theta+4\pi/3)\,d\theta+o(\varepsilon)\). The uniform-ellipse law for the local displacements also gives the independent uniform limiting normalized deficit by the fact that its quadratic radius has uniform area fraction.

3. **Sixfold exact factorization.** The elementary identity
\[
\prod_{j=0}^2\big(1-q\cos(x+2\pi j/3)\big)
=1-\frac34q^2-\frac14q^3\cos(3x)
\]
with \(x=2\theta\) yields \(p_q(\theta)p_q(\theta+2\pi/3)p_q(\theta+4\pi/3)=\sqrt{D_q(\theta)}/I_q^3\). Positivity is explicit because \(\min D_q=(1-q)(1+q/2)^2>0\). Integrating establishes the displayed conditional phase density and coefficient. Writing \(D_q=(1-3q^2/4)(1-\delta_q\cos6\theta)\) yields the six extrema and the ratio formula. Standard one-dimensional complete-elliptic-integral substitutions give the stated closed form for \(K(q)\) and its endpoint and small-anisotropy expansions.

4. **Strict invertibility of the sixth harmonic.** Set \(X=\cos6\Theta\) under density proportional to \(\sqrt{1-\delta X}\), where \(0\le\delta<1\). Differentiation of normalized expectations gives
\[
\frac{d}{d\delta}\mathbb E_\delta X
=-\frac12\operatorname{Cov}_\delta\!\left(X,\frac{X}{1-\delta X}\right)<0.
\]
The covariance is strictly positive because \(x/(1-\delta x)\) is strictly increasing on \([-1,1]\) and \(X\) is nondegenerate; equivalently use an independent-copy expression for covariance. Also \(\delta_q=q^3/(4-3q^2)\) strictly increases from zero to one. Hence \(M_6(q)\) is strictly decreasing. Taylor expansion at zero gives \(M_6(q)=-q^3/16+O(q^5)\). At \(q\uparrow1\), dominated convergence gives \(g_q\to |\sin3\theta|/4\) in \(L^1\), and direct integration gives \(M_6\to-1/3\). The density-extrema inversion and axis-ratio formula follow algebraically.

## Verification

The attached standalone `check.py` evaluates \(K(q)\) and \(M_6(q)\) by independent quadrature of their defining integrals, checks the circle constant and monotone numerical samples, and compares the predicted rare-area probabilities and sixth-angle moments with independent arclength-rejection Monte Carlo samples at four anisotropies. Run `python check.py` with NumPy and SciPy installed. A separate tighter-threshold diagnostic is described in `VERIFICATION.md`. None of these finite calculations supplies the analytic proof.

## Relationship to prior work

Koroleva and Nikitin (2013), building on Lao and Mayer, developed maximum-area random-circle-polygon extremal theory. Nikitin and Polevaya's 2019 original article, including its Lemma 1 and ellipse application, **already supplies the unmarked one-triangle area-deficit coefficient in general three-angle-density form**. Nikitin and Simarova (2020) provide additional general smooth-kernel \(U\)-max extremal laws. The present marked phase distribution is an enrichment of that known scalar asymptotic, not a competing rederivation. Its explicit sixfold ellipse factorization, strict sixth-Fourier-moment inversion, and independent uniform local displacement limit constitute the assessed claim; the general scalar rare-area order and coefficient are prior coverage. No claim is made about maxima over growing samples, which the earlier studies treat.

## Limitations

This is a fixed-three-point conditional law on a fixed nondegenerate ellipse. The phase variable assumes a known principal-axis eccentric-anomaly coordinate. Inference from the sixth harmonic loses sensitivity cubically near the circle. The flattening ellipse \(b\downarrow0\) is only a sequential limit of the coefficient and limiting phase. The general principle that a product of sampling densities weights maximizing phases is already present in the cited literature; the novelty assessment concerns the explicitly resolved, rigorously invertible sixfold angular signature and total-variation marked law. Literature overlap cannot establish exhaustive priority, and independent validation has not been performed.

## References

1. E. V. Koroleva and Ya. Yu. Nikitin, *U-max-Statistics and Limit Theorems for Perimeters and Areas of Random Polygons*, arXiv:1301.1360, initial public posting 2013-01-07. https://arxiv.org/abs/1301.1360
2. Ya. Yu. Nikitin and T. A. Polevaya, *Limit theorems for areas and perimeters of random inscribed and circumscribed polygons*, Zap. Nauchn. Sem. POMI 486 (2019), 200–213, esp. Lemma 1 and ellipse application. https://ftp.pdmi.ras.ru/pub/publicat/znsl/v486/p200.pdf
3. Ya. Yu. Nikitin and E. N. Simarova, *Generalized Limit Theorems for U-max Statistics*, arXiv:2010.04460, initially public 2020-10-09. https://arxiv.org/abs/2010.04460
