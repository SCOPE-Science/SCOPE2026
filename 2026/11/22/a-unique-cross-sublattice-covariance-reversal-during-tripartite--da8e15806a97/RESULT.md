# A unique cross-sublattice covariance reversal during tripartite dimer adsorption

## Finding

On the balanced complete tripartite graph \(K_{n,n,n}\), perform irreversible dimer deposition. Give each cross-part edge an independent Poisson attempt clock of rate \(1/n\); an attempt is accepted only if both endpoints are still vacant. Let \(V_i^{(n)}(t)\) be the number of vacant sites in part \(i\in\{1,2,3\}\) at physical time \(t\ge0\), with all sites initially vacant. For every fixed finite \(T>0\), as \(n\to\infty\),

\[
\left(\frac{V_1^{(n)}(t)-nu(t)}{\sqrt n},\frac{V_2^{(n)}(t)-nu(t)}{\sqrt n},\frac{V_3^{(n)}(t)-nu(t)}{\sqrt n}\right)_{0\le t\le T}
\Longrightarrow (Y_1(t),Y_2(t),Y_3(t))_{0\le t\le T},
\qquad u(t)=\frac1{1+2t},
\]

in the Skorokhod path topology. The limit is a centered continuous Gaussian process with covariance matrix

\[
\Sigma(t)=v_{\mathrm{com}}(t)\frac{\mathbf1\mathbf1^{\mathsf T}}3
+v_{\mathrm{diff}}(t)\left(I-\frac{\mathbf1\mathbf1^{\mathsf T}}3\right),
\quad v_{\mathrm{com}}=\frac23(u-u^4),\quad
v_{\mathrm{diff}}=\frac{u}{2}\log(1+2t).
\]

Moreover, the actual finite-system covariances converge after division by \(n\). For each pair of distinct parts,

\[
\boxed{\lim_{n\to\infty}\frac{\operatorname{Cov}(V_i^{(n)}(t),V_j^{(n)}(t))}{n}
=\Gamma(t)=\frac{4\bigl(1-(1+2t)^{-3}\bigr)-3\log(1+2t)}{18(1+2t)}.}
\]

There is exactly one strictly positive time \(t_*\) at which \(\Gamma\) vanishes: \(t_*=(y_*-1)/2=1.347345267068\ldots\), where \(y_*>1\) uniquely solves \(3\log y=4(1-y^{-3})\). The covariance is strictly positive for \(0<t<t_*\) and strictly negative for \(t>t_*\). At \(t=0\), it is zero. Consequently, at each fixed time strictly away from \(0,t_*\), sufficiently large finite systems have the same covariance sign. The claim does not assert an exactly universal finite-size transition time.

## Assumptions and scope

For each integer \(n\ge1\), the graph has three disjoint labeled parts of \(n\) vertices each, with an edge precisely between vertices in different parts. Each unordered edge gets independent rate-\(1/n\) Poisson attempts. A successful dimer permanently occupies the two endpoints; unsuccessful attempts change no state. Edge clocks may keep running after an unsuccessful attempt without affecting the law. Time \(t\) is physical time under this normalization, **not** the accepted-deposition index or a terminal jamming time. The process starts empty of dimers. The theorem concerns fixed, finite times as \(n\to\infty\), not the limits \(t\to\infty\) and \(n\to\infty\) jointly. An occupied count \(n-V_i^{(n)}\) has the same cross-class covariance as the corresponding vacant count.

## Proof

Write \(X_n=V^{(n)}/n\), and let \(e_i\) be the coordinate basis. From state \(V=(a,b,c)\), each pair of parts \(i<j\) has exactly \(V_iV_j\) eligible edges, so its accepted jumps have rate \(V_iV_j/n\) and change \(V\) by \(\ell_{ij}=-e_i-e_j\). Thus the generator of \(X_n\) is

\[
\mathcal L_n h(x)=n\sum_{i<j}x_ix_j\bigl[h(x+\ell_{ij}/n)-h(x)\bigr].
\]

Its drift is \(f_i(x)=-x_i\sum_{j\ne i}x_j\), and local martingale covariance density for \(\sqrt n X_n\) is

\[
B(x)=\sum_{i<j}x_ix_j\ell_{ij}\ell_{ij}^{\mathsf T}.
\]

These are bounded Lipschitz polynomials on the compact cube \([0,1]^3\), the jumps are bounded by \(\sqrt2/n\), and the initial condition is deterministic. The Poisson time-change construction, Doob's maximal inequality and Gronwall's lemma first give uniform-on-compact probability convergence of \(X_n\) to the unique ODE solution \(\dot x=f(x)\). By symmetry, that solution is \(x(t)=u(t)\mathbf1\), where \(\dot u=-2u^2\) and \(u(0)=1\).

For completeness, let \(M_n(t)=X_n(t)-X_n(0)-\int_0^t f(X_n(s))\,ds\). Its jumps have magnitude at most \(\sqrt2/n\) and its predictable matrix bracket is \(n^{-1}\int_0^t B(X_n(s))\,ds\). Therefore the martingale functional central limit theorem gives convergence of \(\sqrt n M_n\) to a continuous Gaussian martingale with bracket \(\int_0^t B(u(s)\mathbf1)\,ds\). Taylor expansion of the drift and the same moment bounds give convergence of the fluctuation process to the unique solution of

\[
dY(t)=J(t)Y(t)\,dt+u(t)\sum_{i<j}\ell_{ij}\,dW_{ij}(t),\quad
J(t)=Df(u\mathbf1)=-u(t)(I+\mathbf1\mathbf1^{\mathsf T}),\quad Y(0)=0,
\]

for independent standard Brownian motions \(W_{ij}\). The bounded-jump martingale fourth-moment inequality and Gronwall yield \(\sup_n\mathbb E\sup_{s\le T}\|\sqrt n(X_n(s)-u(s)\mathbf1)\|^4<\infty\) for fixed \(T\). This supplies uniform integrability of products of fluctuations and hence the asserted convergence of normalized finite-system covariances (not just convergence in law).

At the symmetric trajectory, \(B(u\mathbf1)=u^2(I+\mathbf1\mathbf1^{\mathsf T})\). Put \(P=\mathbf1\mathbf1^{\mathsf T}/3\) and \(Q=I-P\). The common mode of \(J\) has eigenvalue \(-4u\), and its two contrast modes have eigenvalue \(-u\); the noise strengths in these modes are respectively \(4u^2\) and \(u^2\). Consequently the covariance \(\Sigma=\mathbb E[YY^{\mathsf T}]\) satisfies \(\dot\Sigma=J\Sigma+\Sigma J^{\mathsf T}+B\), and \(\Sigma(0)=0\). Writing \(\Sigma=v_{\mathrm{com}}P+v_{\mathrm{diff}}Q\) yields the two scalar equations

\[
\dot v_{\mathrm{com}}=-8uv_{\mathrm{com}}+4u^2,\qquad
\dot v_{\mathrm{diff}}=-2uv_{\mathrm{diff}}+u^2,\qquad
v_{\mathrm{com}}(0)=v_{\mathrm{diff}}(0)=0.
\]

Integrating factors \((1+2t)^4\) and \((1+2t)\) give exactly the two functions in the finding. Since the off-diagonal entries of \(P,Q\) are \(1/3,-1/3\), their difference gives \(\Gamma=(v_{\mathrm{com}}-v_{\mathrm{diff}})/3\).

Finally, with \(y=1+2t\), the sign of \(\Gamma\) is the sign of \(H(y)=4(1-y^{-3})-3\log y\). Here \(H(1)=0\), \(H'(y)=3(4-y^3)/y^4\), and \(H(y)\to-\infty\) as \(y\to\infty\). Hence \(H\) strictly increases until \(4^{1/3}\), then strictly decreases to negative infinity, crossing zero exactly once above \(1\). This proves all sign and uniqueness claims.

## Verification

The standalone `verify_fluctuation.py` independently reconstructs the drift Jacobian and noise matrix from the three jump vectors, differentiates the proposed covariance formula exactly using SymPy, checks the matrix Lyapunov differential equation and initial condition, and verifies the unique positive root numerically. The standalone `verify_master_equation.py` does not use the Gaussian-process derivation: it constructs the full finite-state Markov generator on \((n+1)^3\) vacant-count triples and propagates the initial point mass by a sparse matrix exponential for \(n\in\{4,8,12,16\}\) at three positive times. It checks mass conservation, positivity and convergence of exact finite-state covariances to the stated scaling function. The finite-size checks corroborate, but are not substitutes for, the all-size martingale argument.

Run from the directory containing the two supplied scripts with Python 3, NumPy, SciPy and SymPy installed:

```bash
python verify_fluctuation.py
python verify_master_equation.py
```

## Relationship to prior work

Irreversible random sequential adsorption has a long literature, including Pippenger's 1989 treatment of graph adsorption. Fusco, Gallo, Petri and Rovere (arXiv:cond-mat/0103582, first public 28 March 2001) analyze dimer deposition with diffusion on a two-dimensional square lattice; their full arXiv text treats a different geometry and does not provide this three-block covariance law. Cieśla and Barbasz (2013) calculate coverage, kinetics and density fluctuation properties of continuum trimer and hexamer adsorption, not the present cross-class finite-time covariance. Penrose and Sudbury (2005) obtain normal approximations for dimer deposition on graph sequences of uniformly bounded maximum degree (their Theorems 7 and 10) and an exact one-dimensional dimer variance (Theorem 11). Neither applies to the graph sequence here, whose degrees equal \(2n\), or supplies three-component cross-part covariances. Kurtz's density-dependent Markov-chain limits supply the general stochastic limit mechanism used in the proof, **not an independently new central limit theorem**. A published result entitled *The sharp \(7/8\) random-edge matching ratio on dense complete tripartite graphs* treats the same adsorption skeleton at the deterministic fluid/matching-efficiency level; its public search description does not assert the cross-class fluctuation formula. Its full result text could not be retrieved during comparison. The new claim is restricted to the explicitly solved covariance and its unique sign switch; the general fluid equations and limit theorem are credited as prior tools.

## Limitations

This theorem is about three balanced complete parts, equal independent rate-\(1/n\) edge attempts, irreversible dimers, deterministic fully vacant start, and fixed finite physical times. It does not characterize the late jamming window, terminal vacancy counts, unbalanced part sizes, or arbitrary heterogeneous deposition rates. General density-dependent Markov theory underlies the Gaussian limit; novelty concerns the model-specific covariance formula and sign-switch classification. An unindexed or inaccessible equivalent specialized calculation remains possible. Independent historical-priority verification has not been performed.

## References

1. C. Fusco, P. Gallo, A. Petri, M. Rovere, *Random sequential adsorption and diffusion of dimers and k-mers on a square lattice*, arXiv:cond-mat/0103582 (first posted 2001-03-28), https://arxiv.org/abs/cond-mat/0103582.
2. N. Pippenger, *Random Sequential Adsorption on Graphs*, SIAM Journal on Discrete Mathematics 2 (1989), 393–401, https://doi.org/10.1137/0402034.
3. T. G. Kurtz, *Strong approximation theorems for density dependent Markov chains*, Stochastic Processes and their Applications 6 (1978), 223–240, https://doi.org/10.1016/0304-4149(78)90020-0.
4. M. Cieśla, J. Barbasz, *Random sequential adsorption of trimers and hexamers*, Journal of Molecular Modeling 19 (2013), 5423–5427, https://doi.org/10.1007/s00894-013-2031-5.
5. *The sharp \(7/8\) random-edge matching ratio on dense complete tripartite graphs*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-the-sharp-7-8-random-edge-matching-ratio-on-dense-complete-tripa--38fa8766b226.
6. M. D. Penrose, A. Sudbury, *Exact and approximate results for deposition and annihilation processes on graphs*, Annals of Applied Probability 15 (2005), 853–889, arXiv:math/0503519 (posted 2005-03-24), https://arxiv.org/pdf/math/0503519.
