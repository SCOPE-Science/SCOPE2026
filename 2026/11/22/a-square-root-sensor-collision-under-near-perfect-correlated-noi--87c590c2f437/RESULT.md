# A square-root sensor collision under near-perfect correlated noise in two-mode heat sensing

## Finding

Consider the first two spatial Dirichlet modes of a one-dimensional heat field, with unknown initial coefficients \(c_1,c_2\), observed at two freely chosen points. The two unit-variance Gaussian observation errors have a **fixed** correlation \(\rho\in[0,1)\), independent of the selected positions. Let \(\mathcal E(\rho)\) denote the maximum, over all ordered pairs \((x,y)\in[0,1]^2\), of the minimum eigenvalue of the Fisher information matrix for \((c_1,c_2)\).

Put \(\varepsilon=1-\rho\) and
\[
\theta_*=\arccos\sqrt{3/8},\qquad x_*=\theta_*/\pi.
\]
As \(\varepsilon\downarrow0\), the **global** optimum satisfies
\[
\boxed{\mathcal E(1-\varepsilon)=\frac{25}{16}-\frac{75}{16}\varepsilon+o(\varepsilon).}
\]
For **every** globally optimal pair, after exchanging its sites and possibly reflecting both around \(1/2\),
\[
\boxed{\frac{x+y}{2}=x_*+o(\sqrt\varepsilon),\qquad
 |x-y|=\frac{\sqrt{5\varepsilon}}\pi+o(\sqrt\varepsilon).}
\]
Thus optimal sensors are distinct for each \(\rho<1\), but collide at one of the two maximum-sensitivity points as correlation approaches one. No uniqueness of the finite-\(\rho\) global maximizer is asserted.

For comparison, among reflection-paired sites \(y=1-x\), the exact optimum for **every** \(0\le\rho<1\) is
\[
\boxed{\mathcal E_{\rm refl}(\rho)=\frac{3+5\rho}{2(1+\rho)^2},}
\]
which tends to \(1\). Hence optimizing without the reflection restriction increases the limiting worst-direction information by a factor \(25/16\).

## Assumptions and scope

The initial field is \(f(z)=c_1\sin(\pi z)+c_2\sin(2\pi z)\) for \(z\in[0,1]\), with Dirichlet boundaries and no other unknown coefficients. Equivalently, it is the initial state of the heat equation \(u_t=u_{zz}\), before temporal attenuation; both measurements are made at the same observation time zero. The data are
\[
Y=(f(x),f(y))^{\mathsf T}+\xi,\qquad
\operatorname{Cov}(\xi)=\begin{pmatrix}1&\rho\\\rho&1\end{pmatrix}.
\]
Correlation is an experimental **pair-level constant**, not a function of \(|x-y|\); it remains fixed while locations are optimized. One interpretation is a shared additive calibration error combined with independent measurement errors, where \(\xi_i=\sqrt\rho\,Z_{\mathrm{common}}+\sqrt{1-\rho}\,Z_i\) with independent standard Gaussian variables. The information criterion is \(\lambda_{\min}(X^{\mathsf T}\Sigma^{-1}X)\), where rows of \(X\) are the two sine-mode evaluation vectors. The point \(\rho=1\) is excluded because \(\Sigma\) becomes singular. Site order and simultaneous reflection are immaterial to the information eigenvalues.

## Proof

Write \(s=\pi x\), \(t=\pi y\), \(a(v)=(\sin v,\sin 2v)^{\mathsf T}\), and \(\varepsilon=1-\rho\). The exact information decomposition is
\[
M_\varepsilon(s,t)=\frac{[a(s)+a(t)][a(s)+a(t)]^{\mathsf T}}{2(2-\varepsilon)}+
\frac{[a(s)-a(t)][a(s)-a(t)]^{\mathsf T}}{2\varepsilon}.
\]
Existence of a maximizer follows from compactness. Coincident sites give a rank-one matrix, hence cannot maximize, since distinct interior sites give a positive definite matrix.

For distinct \(s,t\), let \(d=a(s)-a(t)\) and define the squared distance of the origin from the affine line through the two evaluation vectors by
\[
D(s,t)=\frac{\det(a(s),a(t))^2}{\|d\|^2}.
\]
Taking the Rayleigh quotient of \(M_\varepsilon\) in a unit direction orthogonal to \(d\) yields
\[
\lambda_{\min}(M_\varepsilon(s,t))\le\frac{2D(s,t)}{2-\varepsilon}.
\]
Since \(\det(a(s),a(t))=\det(a(s),a(t)-a(s))\), the elementary determinant bound gives
\[
D(s,t)\le\min\{\|a(s)\|^2,\|a(t)\|^2\}\le L:=\frac{25}{16}.
\]
Indeed, with \(u=\cos^2v\),
\[
\|a(v)\|^2=(1-u)(1+4u)=L-4(u-3/8)^2.
\]
The two and only two maximizers are \(\theta_*\) and \(\pi-\theta_*\). If a sequence of distinct pairs has \(D\to L\), both endpoints must approach these two locations. They cannot approach opposite ones: the line joining \(a(\theta_*)\) and \(a(\pi-\theta_*)\) has squared distance \(\sin^2\theta_*=5/8<L\). Therefore both endpoints of any such sequence coalesce at the *same* maximizer.

Set \(m=(s+t)/2\), \(\delta=t-s\), \(u=\cos^2 m\), \(v=\cos^2(\delta/2)\). Trigonometric sum-and-difference identities yield the exact chord formula
\[
D(m,\delta)=\frac{4(1-u)(u-v)^2}{u+4(2u-1)^2v}.
\]
The denominator is positive in a neighborhood of the collision points. Direct differentiation at \(u=3/8,v=1\) gives \(D=L\), \(D_u=0\), \(D_{uu}=-56\), and \(D_v=35/8\). Since \((\cos^2m)'\) at \(m=\theta_*\) has squared value \(15/16\) and \(v=1-\delta^2/4+O(\delta^4)\),
\[
D(m,\delta)=L-\frac{105}{4}(m-\theta_*)^2-\frac{35}{32}\delta^2
+o((m-\theta_*)^2+\delta^2).
\]
The reflected collision point has the same expansion after reflecting coordinates.

For a lower bound, use \(m=\theta_*\) and \(\delta^2=5\varepsilon+\varepsilon^{3/2}\), with \(s=m-\delta/2,t=m+\delta/2\). At \(\theta_*\), the vectors \(A=a(\theta_*)\) and \(A'=a'(\theta_*)\) are perpendicular, with \(\|A\|^2=25/16\), \(\|A'\|^2=5/8\), and \(A\cdot A''=-35/8\). In the orthonormal basis along \(A,A'\), direct Taylor expansion of the exact information decomposition gives a first diagonal entry
\[
\frac{25}{16}-\frac{75}{16}\varepsilon+O(\varepsilon^{3/2}),
\]
a second diagonal entry \(25/16+(5/16)\sqrt\varepsilon+O(\varepsilon)\), and off-diagonal entries \(O(\varepsilon)\). The eigenvalue gap is of order \(\sqrt\varepsilon\), so the smaller eigenvalue equals the first entry plus \(O(\varepsilon^{3/2})\). Consequently,
\[
\mathcal E(1-\varepsilon)\ge L-\frac{75}{16}\varepsilon+o(\varepsilon).
\]

Choose any maximizing pair at each \(\varepsilon\). The lower bound and the chord upper bound force \(D\to L\), hence its endpoints coalesce at one of the two indicated maxima. After reflection, write \(h=m-\theta_*\). The chord expansion, the upper bound, and the lower bound force \(h^2+\delta^2=O(\varepsilon)\). Along any subsequence with \(\delta^2/\varepsilon\to g\), the information matrix tends to
\[
AA^{\mathsf T}+\frac g2A'A'^{\mathsf T},
\]
whose eigenvalues are \(25/16\) and \(5g/16\). Because the optimal smaller eigenvalue tends to \(25/16\), necessarily \(g\ge5\). On the other hand, the chord upper expansion and the lower benchmark imply
\[
\frac{105}{4}h^2+\frac{35}{32}\delta^2
\le\frac{175}{32}\varepsilon+o(\varepsilon),
\]
so \(\limsup\delta^2/\varepsilon\le5\). Thus \(\delta^2/\varepsilon\to5\) and \(h^2/\varepsilon\to0\). Substitution into the chord upper bound gives \(\mathcal E(1-\varepsilon)\le L-(75/16)\varepsilon+o(\varepsilon)\), matching the lower bound. Conversion from angles to physical positions proves the asserted collision and midpoint limits for **every** maximizing pair.

Finally, for reflection-paired sites put \(u=\cos^2(\pi x)\). The information matrix is diagonal, with entries \(2(1-u)/(1+\rho)\) and \(8u(1-u)/(1-\rho)\). For \(0\le\rho<1\), the maximum of their minimum occurs exactly when they agree, at \(u=(1-\rho)/[4(1+\rho)]\); monotonicity on either side gives the stated explicit reflected optimum.

## Verification

Run `python verify.py` in an environment with `numpy`, `sympy` and `scipy` as specified in `requirements.txt`. The script checks exact symbolic factorization and chord derivatives, 2,500 independently evaluated chord identities, and supplementary global numerical searches at four positive correlations. The verified output is in `verification_output.txt`. The analytical argument above, not the finite numerical searches, establishes the global and asymptotic statements. In particular, no discrete-grid search is used as a uniqueness certificate.

## Relationship to prior work

Attia and Constantinescu (2020, arXiv:2007.14476) provide general optimal-design formulations with correlated observation errors, together with advection-diffusion sensor-placement experiments; the inspected full text does not supply this two-harmonic fixed-pair E-optimal asymptotic or its square-root collision constant. Liu, Gao and Zhou (2019, arXiv:1910.02539) study a different R-optimality criterion for multi-response regression. Dette, Pepelyshev and Zhigljavsky (2013, arXiv:1303.2863) derive broad universally optimal *approximate least-squares* designs for certain covariance kernels, including cosine regression; their infinite-measure setting and optimization functional do not imply the present exact two-read GLS E-optimal result. Holland-Letz, Dette and Pepelyshev (2011) develop a correlated-observation geometric c-optimality theory, not the two-direction minimax eigenvalue objective. These distinctions do not establish absolute historical novelty.

## Limitations

This is an asymptotic classification as \(\rho\uparrow1\), not a closed finite-correlation global phase diagram. It assumes the error correlation stays constant when sensors move, which is unlike common spatial correlation kernels. It treats two simultaneous readings of exactly two Dirichlet harmonics, unit marginal error variances, a known correlation and the GLS Fisher metric. It does not cover unknown correlation, additional modes, time-dependent sensing, spatially varying covariance, instrument minimum spacing, or a claim about information at the singular endpoint \(\rho=1\). Independence of this finding from all older specialized exact-design literature has not been externally certified.

## References

1. A. Attia and E. Constantinescu, *Optimal Experimental Design for Inverse Problems in the Presence of Observation Correlations*, arXiv:2007.14476, first posted 2020-07-28. https://arxiv.org/abs/2007.14476
2. P. Liu, L. Gao and J. Zhou, *R-optimal designs for multi-response regression models with multi-factors*, arXiv:1910.02539, 2019. https://arxiv.org/abs/1910.02539
3. H. Dette, A. Pepelyshev and A. Zhigljavsky, *Optimal design for linear models with correlated observations*, arXiv:1303.2863, 2013. https://arxiv.org/abs/1303.2863
4. T. Holland-Letz, H. Dette and A. Pepelyshev, *A geometric characterization of optimal designs for regression models with correlated observations*, Journal of the Royal Statistical Society B 73 (2011), 239–252. https://pmc.ncbi.nlm.nih.gov/articles/PMC3106301/
5. S. I. Watson and Y. Pan, *Evaluation of combinatorial optimisation algorithms for c-optimal experimental designs with correlated observations*, Statistics and Computing 33 (2023), article 112. https://doi.org/10.1007/s11222-023-10280-w
