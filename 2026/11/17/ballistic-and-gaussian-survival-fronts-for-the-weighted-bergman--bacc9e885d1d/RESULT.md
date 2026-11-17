# Ballistic and Gaussian survival fronts for the weighted-Bergman completely positive map

## Finding

For the normal unital completely positive map \(\Psi_w\) associated by Panja with every admissible radial weighted Bergman space, every compact operator is norm-stable under iteration, but the restriction to the compact ideal has norm one at every iterate. Finite-rank projection decay has an exact pure-birth survival interpretation, an explicit finite spectral expansion, and a universal ballistic threshold. For every beta weight \(w_\alpha(z)=(\alpha+1)(1-|z|^2)^\alpha\), \(\alpha>-1\), that threshold has a Gaussian window with explicit variance and logarithmic mean correction.

Write \(\omega_n=\int_{\mathbb D}|z|^{2n}w(z)\,dA(z)\), \(\rho=\omega_1\in(0,1)\), and \(r_k=\rho\omega_k/\omega_{k+1}\). Then \(r_0=1\), \(r_k\searrow\rho\), and \(0<r_k<1\) for \(k\ge1\). Let \(e_k=z^k/\sqrt{\omega_k}\), and let \(P_N\) project onto \(\operatorname{span}\{e_0,\ldots,e_N\}\).

**Compact decay without uniform decay.** For every compact \(K\), \(\|\Psi_w^m(K)\|\to0\), yet \(\|\Psi_w^m|_{\mathcal K}\|=1\) for every integer \(m\ge0\). The finite corner \(P_N\mathcal B(P_N H)P_N\) is invariant, and the spectral radius of the restricted map equals \(1-r_N\), including the value zero for \(N=0\).

**Exact finite-rank survival law.** Let \(X_0=0\) and, conditional on \(X_m=k\), let \(X_{m+1}=k+1\) with probability \(r_k\), and \(X_{m+1}=k\) otherwise. Then for all integers \(m,N\ge0\),
\[
\|\Psi_w^m(P_N)\|=\mathbb P(X_m\le N)
=\sum_{j=0}^N\left(\prod_{\substack{0\le i\le N\\i\ne j}}\frac{r_i}{r_i-r_j}\right)(1-r_j)^m.
\]
Here \(0^0=1\) when \(m=0\). For fixed \(N\ge1\) the sharp finite-window decay constant is
\[
\lim_{m\to\infty}\frac{\|\Psi_w^m(P_N)\|}{(1-r_N)^m}
=\prod_{j=0}^{N-1}\frac{r_j}{r_j-r_N}\in(0,\infty).
\]
Moreover, \(X_m/m\to\rho\) almost surely; consequently, for any integer sequence \(N_m\ge0\) with \(N_m/m\to v\), the norms tend to zero when \(v<\rho\) and to one when \(v>\rho\). No universal assertion is made at \(v=\rho\) for arbitrary admissible weights.

**Gaussian critical window for beta weights.** For \(w_\alpha(z)=(\alpha+1)(1-|z|^2)^\alpha\), \(\alpha>-1\), put \(\rho=1/(\alpha+2)\). For every real \(s\), with \(N_m=\lfloor \rho m+s\sqrt{\rho(1-\rho)m}\rfloor\),
\[
\lim_{m\to\infty}\|\Psi_{w_\alpha}^m(P_{N_m})\|=\Phi(s),
\]
where \(\Phi\) is the standard normal distribution function; the formula applies for all sufficiently large \(m\) so that \(N_m\ge0\). The associated pure-birth chain satisfies the sharper drift relation
\[
\mathbb E X_m=\rho m+\frac{1-\rho}{\rho}\log m+o(\log m).
\]

## Assumptions and scope

The weight \(w\ge0\) is an integrable radial function on the open unit disk, normalized by \(\int_{\mathbb D}w\,dA=1\), with positive mass in every annulus meeting the unit circle. The measure \(dA\) is normalized planar area measure. Its moment sequence is strictly log-convex and \(\omega_{n+1}/\omega_n\nearrow1\), as established for admissible weights. The Hilbert space \(H=A_w^2(\mathbb D)\) uses the orthonormal monomial basis \((e_k)_{k\ge0}\).

Let \(S\) be multiplication by the coordinate, \(S'=S(S^*S)^{-1}\), and let \(Q_j\) project onto \(\overline{\operatorname{span}}\{e_j,e_{j+1},\ldots\}\). Panja's normal unital completely positive map is
\[
\Psi_w(X)=\rho\left[S'^*XS'+\sum_{j\ge1}(\delta_{j-1}-\delta_j)Q_jXQ_j\right],
\qquad \delta_j=\frac{\omega_j}{\omega_{j+1}},\quad\rho=\frac1{\delta_0}.
\]
The series converges in norm for each bounded operator. Its restriction to \(\mathcal K(H)\) is considered with operator norm, not Schatten or trace norm. The finite-corner algebra is a finite-dimensional invariant subspace but the restriction need not be unital. The stochastic chain has state space \(\mathbb N_0\) with no absorbing state.

## Proof

**1. Matrix units and invariant finite corners.** For \(E_{ij}=|e_i\rangle\langle e_j|\), the Cauchy-dual shift identity \(S'e_k=\sqrt{\omega_k/\omega_{k+1}}e_{k+1}\) and the tail projections yield
\[
\Psi_w(E_{ij})=(1-r_{\min(i,j)})E_{ij}
+\mathbf1_{\{i,j\ge1\}}\sqrt{r_{i-1}r_{j-1}}\,E_{i-1,j-1}.
\]
Indeed, \(\rho\sum_{1\le\ell\le\min(i,j)}(\delta_{\ell-1}-\delta_\ell)=1-\rho\delta_{\min(i,j)}\). Thus \(\Psi_w\) preserves every finite corner and is triangular there, with diagonal \(1-r_{\min(i,j)}\). Strict log-convexity of the moments gives \(r_0>r_1>\cdots>\rho\), hence the largest diagonal modulus on the \(N\)-corner is \(1-r_N<1\). This is its exact spectral radius. Every matrix unit decays to zero under powers of that finite-dimensional restriction. Finite-rank operators are norm-dense in \(\mathcal K(H)\), and the UCP map is contractive in operator norm, so \(\|\Psi_w^m(K)\|\to0\) for every compact \(K\). The same matrix-unit identity also proves invariance of the compact ideal.

**2. Diagonal stochastic representation and operator norm.** For any bounded scalar sequence \(f\),
\[
(\Psi_w(\operatorname{diag}f))_{kk}
=(1-r_k)f(k)+r_k f(k+1).
\]
Iterating gives the pure-birth Markov operator. In particular, \(\Psi_w^m(P_N)\) is a positive diagonal contraction with entry \(\mathbb P_k(X_m\le N)\) at state \(k\). Coupling chains started at \(k\le\ell\) using the same uniforms preserves their order: at a strict gap, jumps of size at most one cannot reverse it, and coincident chains make identical choices. Hence the supremal diagonal entry is the one started at zero, proving the norm identity. Because \(X_m\le m\) when started at zero, \(\|\Psi_w^m(P_m)\|=1\), establishing \(\|\Psi_w^m|_{\mathcal K}\|=1\) for every \(m\).

**3. Exact finite spectral expansion and sharp constant.** For each \(j\ge0\), the holding time \(G_j\) at state \(j\) is an independent geometric random variable on \(\{1,2,\ldots\}\) with success probability \(r_j\). The first hitting time of \(N+1\) is \(\tau_N=\sum_{j=0}^N G_j\). Therefore
\[
\sum_{m\ge0}\mathbb P(\tau_N>m)z^m
=\frac{1-\prod_{j=0}^N[r_j z/(1-(1-r_j)z)]}{1-z}.
\]
Partial-fraction decomposition using the distinct \(r_j\) produces precisely the coefficients in the claimed finite sum. For \(N\ge1\), set \(T=\sum_{j=0}^{N-1}G_j\), \(\lambda=1-r_N\in(0,1)\). Then
\[
\lambda^{-m}\mathbb P(\tau_N>m)
=\lambda^{-m}\mathbb P(T>m)+\mathbb E[\lambda^{-T}\mathbf1_{\{T\le m\}}].
\]
The first term tends to zero, because each preceding geometric variable has smaller tail ratio \(1-r_j<\lambda\), and the second tends to
\[
\mathbb E\lambda^{-T}=\prod_{j=0}^{N-1}\frac{r_j}{r_j-r_N},
\]
which is finite and strictly positive. This proves the sharp constant.

**4. Universal ballistic speed.** Let independent uniforms \((U_t)\) drive the chain through \(X_{t+1}=X_t+\mathbf1_{\{U_t\le r_{X_t}\}}\), and let \(Y_m=\sum_{t<m}\mathbf1_{\{U_t\le\rho\}}\). Since \(r_k\ge\rho\), \(X_m\ge Y_m\), and \(Y_m/m\to\rho\) almost surely. Thus \(X_m\to\infty\), and \(r_{X_m}\to\rho\) almost surely. The bounded martingale differences \(\mathbf1_{\{U_t\le r_{X_t}\}}-r_{X_t}\) obey the martingale strong law, while Cesàro averaging gives \(m^{-1}\sum_{t<m}r_{X_t}\to\rho\). Therefore \(X_m/m\to\rho\) almost surely. The two strict-side limits of the projection norm follow by convergence in probability and the norm-survival identity.

**5. Gaussian window and logarithmic mean.** For the beta weight, elementary beta integration gives \(\omega_n=\binom{n+\alpha+1}{n}^{-1}\), \(\rho=1/(\alpha+2)\), and
\[
r_k=\rho+\frac{1-\rho}{k+1}.
\]
Use the same uniforms to couple the pure-birth chain with the binomial chain \(Y_m\) above. The nonnegative difference \(D_m=X_m-Y_m\) has conditional increment mean \((1-\rho)/(X_t+1)\), so
\[
\mathbb E D_m\le(1-\rho)\sum_{t=0}^{m-1}\mathbb E\frac1{Y_t+1}
=\frac{1-\rho}{\rho}\sum_{t=0}^{m-1}\frac{1-(1-\rho)^{t+1}}{t+1}
=O_\rho(\log(m+1)).
\]
Consequently \(D_m/\sqrt m\to0\) in \(L^1\). The elementary binomial central limit theorem and Slutsky's lemma give
\[
\frac{X_m-\rho m}{\sqrt{\rho(1-\rho)m}}\ \Longrightarrow\ N(0,1),
\]
and hence the asserted Gaussian survival window. Finally, the ballistic law and \(X_t\ge Y_t\) imply
\[
t\,\mathbb E\frac1{X_t+1}\longrightarrow\frac1\rho.
\]
To justify uniform integrability, on \(\{Y_t\ge\rho t/2\}\) the integrand \(t/(X_t+1)\) is bounded by \(2/\rho\), while a binomial exponential lower-tail bound makes \(t\mathbb P(Y_t<\rho t/2)\to0\). Thus \(\mathbb E D_m=(1-\rho)\sum_{t<m}\mathbb E[1/(X_t+1)]\sim(1-\rho)\rho^{-1}\log m\), proving the stated logarithmic mean correction.

## Verification

The matrix-unit and generating-function identities give complete exact calculations; they are valid for all permitted weights and integer parameters. The compact-ideal argument uses operator-norm density, not mere pointwise convergence of matrix coefficients. The ballistic limit is an almost-sure martingale law. The Gaussian window is justified by an explicit \(O(\log m)\) coupling bound, not by finite simulations. A standalone finite exact-rational checker, `CHECK.py`, compares pure-birth transition recurrences against the spectral coefficient formula for four rational parameter choices and seven projection sizes, and verifies a binomial reciprocal-moment identity. It reports `BERGMAN_CP_BIRTH_DIAGNOSTICS_OK 466` on successful execution. These finite tests are supplementary, not proofs of the infinite-dimensional or asymptotic assertions.

## Relationship to prior work

Panja (arXiv:2611.09731v1) constructs the map \(\Psi_w\), proves normal complete positivity and unitality, identifies its harmonic Toeplitz fixed space, and excludes nonzero compact harmonic Toeplitz operators. Those results, particularly the definition and matrix model, are foundational here and are not claimed as new. The present statement describes powers of this specific map on the compact ideal, sharp finite-rank power norms, and their ballistic and Gaussian transition geometry. The general study by Fidaleo, Ottomano and Rossi (arXiv:2110.06743v1) discusses spectral and transient parts of completely positive dynamics but does not furnish this map-specific projection survival law or its explicit Gaussian scaling. The independent geometric-waiting-time and binomial tools are classical; their use alone is not claimed as a new probability theorem.

## Limitations

The result concerns Panja's exact weighted-Bergman map, not arbitrary unital completely positive maps or arbitrary Toeplitz symbols. Universal ballistic speed applies to every admissible radial weight, but the Gaussian critical window and logarithmic correction are asserted only for the beta-weight family. For an arbitrary admissible weight, the critical regime \(N_m/m\to\rho\) may need additional moment hypotheses. The exact finite-corner spectral radius is not a uniform spectral gap; indeed uniform compact-ideal power decay fails. Priority against all potentially equivalent formulations of the diagonal Markov process has not been independently certified.

## References

1. S. Panja, *Toeplitz operators with bounded harmonic symbols on weighted Bergman spaces are the fixed points of a normal unital completely positive map*, arXiv:2611.09731v1 (first submitted 2026-11-06), https://arxiv.org/html/2611.09731v1 .
2. F. Fidaleo, F. Ottomano, S. Rossi, *Spectral and ergodic properties of completely positive maps and decoherence*, arXiv:2110.06743v1 (2021), https://arxiv.org/html/2110.06743v1 .
3. Standard facts used explicitly: geometric holding-time generating functions, the strong law for bounded martingale differences, and the binomial central limit theorem.
