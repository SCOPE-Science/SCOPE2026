# A cubic boundary-layer spectral law for nested-disk Toeplitz commutators on the bianalytic Bergman space

## Finding
Let \(\mathbb D\subset\mathbb C\) be the unit disk, let \(d\mu=dA/\pi\) be normalized area, and let \(\mathcal A_2^2\) be the **full** unweighted bianalytic Bergman space. For \(0<q<1\), write \(D_q=\{z\in\mathbb D:|z|^2\le q\}\) and
\[
T_q=P_2M_{\mathbf 1_{D_q}}\big|_{\mathcal A_2^2},
\]
where \(P_2\) is the orthogonal projection onto \(\mathcal A_2^2\). For every pair of distinct parameters \(q,r\in(0,1)\), put
\[
\kappa_n(q,r)=\sqrt{(n+1)(n+3)}\,(n+2)^2(1-q)(1-r)|r-q|(qr)^{n+1},\qquad n=0,1,\ldots.
\]
The skew-adjoint commutator \(K_{q,r}=[T_q,T_r]\) has nonzero eigenvalues \(\pm i\kappa_n(q,r)\), one of each sign for every \(n\ge0\). Its singular values are **exactly** \(\kappa_n(q,r)\), each repeated twice, and its kernel is one-dimensional. For fixed distinct cutoffs, it lies in every Schatten class \(\mathcal S_p\), \(p>0\).

Fix distinct \(a,b>0\) and let \(q_\varepsilon=e^{-a\varepsilon}\), \(r_\varepsilon=e^{-b\varepsilon}\). Define the nonzero continuum profile
\[
G_{a,b}(u)=ab|a-b|\,u^3e^{-(a+b)u},\qquad u\ge0.
\]
For every real \(p>0\), the complete sharp Schatten-mass limit is
\[
\boxed{\lim_{\varepsilon\downarrow0}\varepsilon\|K_{q_\varepsilon,r_\varepsilon}\|_{\mathcal S_p}^p
=2\int_0^\infty G_{a,b}(u)^p\,du
=\frac{2\Gamma(3p+1)[ab|a-b|]^p}{[p(a+b)]^{3p+1}}.}
\]
Furthermore,
\[
\boxed{\lim_{\varepsilon\downarrow0}\|K_{q_\varepsilon,r_\varepsilon}\|=
\frac{27ab|a-b|}{e^3(a+b)^3}.}
\]
Although \(T_{q_\varepsilon}\to I\) and \(T_{r_\varepsilon}\to I\) strongly, their commutator does **not** approach zero in operator norm. For example,
\[
\lim_{\varepsilon\downarrow0}\varepsilon\|K_{q_\varepsilon,r_\varepsilon}\|_{\mathcal S_1}
=\frac{12ab|a-b|}{(a+b)^4}.
\]
Among all positive distinct rates \(a,b\), the limiting operator norm is maximized precisely when \(a/b=2+\sqrt3\) or \(a/b=2-\sqrt3\), and its sharp value is \(3\sqrt3/(2e^3)\).

## Assumptions and scope
The Hilbert space is \(\mathcal A_2^2=\{f\in L^2(\mathbb D,d\mu):\partial_{\bar z}^2 f=0\}\) with the distributional derivative condition. It includes the analytic subspace and is **not** the true-order-two orthogonal complement. The area normalization is essential to the displayed orthonormal basis, but not to the Toeplitz operators under an equivalent constant rescaling of the Hilbert norm. The cutoffs are concentric disks whose parameters are their **squared** radii; boundary circles have zero measure. All asymptotic statements hold for fixed \(a,b,p\), with \(a,b>0\), \(a\ne b\). For \(0<p<1\), Schatten expressions are quasi-norms. There is no assertion of uniformity as \(a\), \(b\), or \(p\) varies with \(\varepsilon\).

## Proof
**1. Complete Fourier decomposition.** Every bianalytic function has the form \(f_0(z)+\bar zf_1(z)\), where both coefficients are analytic. Orthogonal angular sectors consist of a one-dimensional sector \(\mathbb C\bar z\) of frequency \(-1\) and, for each \(n\ge0\), the span of \(z^n\) and \(z^{n+1}\bar z\). In the sector \(n\ge0\), put \(t=|z|^2\). The radial probability law is \((n+1)t^n\,dt\), \(0\le t\le1\). Its mean and variance are
\[
\mu_n=\frac{n+1}{n+2},\qquad
\sigma_n^2=\frac{n+1}{(n+2)^2(n+3)}.
\]
The two vectors
\[
u_n(z)=\sqrt{n+1}\,z^n,\qquad
v_n(z)=\sqrt{n+1}\,z^n\frac{|z|^2-\mu_n}{\sigma_n}
\]
are orthonormal, and the collection \(\{\sqrt2\,\bar z\}\cup\{u_n,v_n:n\ge0\}\) is an orthonormal basis of \(\mathcal A_2^2\). Radial Toeplitz operators preserve each sector.

**2. Exact compression matrices.** Write \(d=1-q\) and \(g_n=\sqrt{(n+1)(n+3)}\). Direct integration of the truncated zeroth, first and second beta moments under \((n+1)t^n\,dt\) gives the matrix of \(T_q\) on \(\operatorname{span}\{u_n,v_n\}\):
\[
A_n(q)=q^{n+1}\begin{pmatrix}
1&-g_nd\\
-g_nd&1-2d+(n+2)^2d^2
\end{pmatrix}.
\]
For instance, its off-diagonal entry is \((n+1)\int_0^q t^n(t-\mu_n)\,dt/\sigma_n=-g_ndq^{n+1}\). The diagonal entries follow by integrating \(1\) and \((t-\mu_n)^2/\sigma_n^2\); no asymptotic approximation is used here. The frequency \(-1\) compression is scalar, so it contributes zero to the commutator.

**3. Paired exact spectrum.** For any two real symmetric matrices \(\begin{pmatrix}x&y\\y&z\end{pmatrix}\) and \(\begin{pmatrix}X&Y\\Y&Z\end{pmatrix}\), the upper-right commutator entry is \(Y(x-z)+y(Z-X)\). Substituting the two matrices above and simplifying gives
\[
[A_n(q),A_n(r)]
=g_n(n+2)^2(1-q)(1-r)(r-q)(qr)^{n+1}
\begin{pmatrix}0&1\\-1&0\end{pmatrix}.
\]
A real skew-symmetric matrix \(c\begin{pmatrix}0&1\\-1&0\end{pmatrix}\) has eigenvalues \(\pm i|c|\) and singular values \(|c|,|c|\). Thus the displayed blocks exhaust the nonzero spectral data. For distinct \(q,r\), every coefficient is nonzero; the frequency \(-1\) sector alone forms the kernel. Exponential decay in \(n\) proves \(K_{q,r}\in\mathcal S_p\) for all \(p>0\).

**4. Boundary scaling and all Schatten powers.** With \(u=\varepsilon(n+1)\), elementary expansions give, uniformly when \(u\) ranges over any compact interval in \((0,\infty)\),
\[
\kappa_n(q_\varepsilon,r_\varepsilon)
=G_{a,b}(u)+o(1).
\]
Indeed \(1-e^{-a\varepsilon}\sim a\varepsilon\), \(|e^{-a\varepsilon}-e^{-b\varepsilon}|\sim|a-b|\varepsilon\), \(g_n(n+2)^2\sim n^3\), and \((q_\varepsilon r_\varepsilon)^{n+1}=e^{-(a+b)u}\) exactly. For \(0<\varepsilon\le1\), the global inequalities \(1-e^{-c\varepsilon}\le c\varepsilon\), \(|e^{-a\varepsilon}-e^{-b\varepsilon}|\le|a-b|\varepsilon\), and \(g_n\le n+2\) show that
\[
0\le\kappa_n(q_\varepsilon,r_\varepsilon)
\le ab|a-b|\,(u+\varepsilon)^3e^{-(a+b)u}.
\]
For each fixed \(p>0\), this has an integrable \(p\)-th power as a function of \(u\), uniformly in \(\varepsilon\le1\); the near-zero region contributes vanishing total mass in the scaled Riemann sum and the exponential bound controls the tail. Consequently
\[
\varepsilon\sum_{n\ge0}\kappa_n(q_\varepsilon,r_\varepsilon)^p
\longrightarrow\int_0^\infty G_{a,b}(u)^p\,du.
\]
The multiplicity two and the gamma integral establish the stated Schatten limit for every \(p>0\). The same local convergence and global bound imply convergence of the suprema, since \(G_{a,b}\) tends to zero at both endpoints and has its unique positive maximum at \(u=3/(a+b)\). This gives the operator-norm constant. The strong convergence \(T_{q_\varepsilon}\to I\) follows from \(\mathbf1_{D_{q_\varepsilon}}\to1\) almost everywhere, uniform contractivity of multiplication and projection, and dominated convergence in \(L^2\). Thus both products converge strongly to \(I\) and their commutator strongly to zero.

**5. Sharp rate optimization.** Let \(t=a/(a+b)\). The norm coefficient is \(27e^{-3}t(1-t)|2t-1|\). Setting \(w=|2t-1|\in(0,1)\), this becomes \(27e^{-3}w(1-w^2)/4\). Its sole interior maximum is attained at \(w=1/\sqrt3\), yielding \(3\sqrt3/(2e^3)\) and the two stated rate ratios. The endpoint values are zero, so the maximum is global.

## Verification
The standalone `CHECK.py` evaluates the three truncated moments using exact rational arithmetic and checks the displayed two-by-two matrix and commutator identities independently for several indices and rational disk cutoffs. It also compares computed complete finite spectral sums with the analytic Schatten and norm limits in several small-scale regimes. Run `python3 CHECK.py` with Python 3's standard library. These finite checks support the calculations but do not establish infinite-dimensional completeness, norm convergence, or asymptotics; those are proved above.

## Relationship to prior work
Barrera-Castelán, Maximenko and Ramos-Vazquez (2020, Sections 7–8) establish the general Jacobi-block representation of radial Toeplitz operators on polyanalytic Bergman spaces, and their 2023 paper describes the corresponding generated operator algebras for fixed boundary-regular symbols. Those structural results are used here; the novel asserted statement is the **exact nested-cutoff commutator spectrum together with its simultaneous two-rate, all-Schatten boundary law**. The known smooth-symbol boundary-jet theorem concerns fixed \(C^3\) radial amplitudes with high-frequency \(n^{-3}\) commutators, whereas these moving discontinuous cutoffs generate \(\varepsilon^{-1}\) equally-sized spectral modes. The known analytic Bergman disk-cutoff commutator involves one cutoff and coordinate multiplication and has vanishing operator norm. An analogous bianalytic **Fock** disk-pair result concerns Gaussian radial moments and a different fixed-cutoff spectral law; it does not imply the beta-moment Bergman boundary transition. A 2025 study by Shi, Li, Zhang and Lu concerns commutativity in the two-analytic setting, but its full text was unavailable for a complete priority comparison.

## Limitations
The exact theorem is for the **full unweighted order-two** disk space, two concentric sharp indicators, and fixed distinct positive boundary rates. It does not treat general radial weights, higher polyanalytic order, nonconcentric disks, or the coalescing-rate regime \(a-b\to0\) with \(\varepsilon\). Earlier generic block formulas make the finite-dimensional integration possible, so historical priority for particular cutoff identities remains uncertain. Published search and self-review are not independent validation.

## References
1. R. M. Barrera-Castelán, E. A. Maximenko, G. Ramos-Vazquez, *Radial operators on polyanalytic weighted Bergman spaces*, arXiv:2009.14301 (first public 29 September 2020), https://arxiv.org/abs/2009.14301 .
2. R. M. Barrera-Castelán, E. A. Maximenko, G. Ramos-Vazquez, *C*-algebras generated by radial Toeplitz operators on polyanalytic weighted Bergman spaces*, arXiv:2306.06231 (first public 9 June 2023), https://arxiv.org/abs/2306.06231 .
3. Y. Shi, Y. Li, B. Zhang, Y. Lu, *Commuting Toeplitz Operators on the 2-analytic Bergman Space*, Acta Mathematica Sinica **41** (2025), 1855–1867, DOI:10.1007/s10114-025-3195-5 (abstract and bibliographic information only inspected).
4. *A universal boundary-jet law for noncommuting radial poly-Bergman Toeplitz operators*, publicly available research note (2026); comparison restricted to its smooth-symbol theorem.
5. *Gamma boundary layer and Schatten phase transitions for Bergman disk-cutoff commutators*, publicly available research note (2026); comparison restricted to analytic Bergman coordinate commutators.
6. *A sharp noncommutativity constant for nested-disk concentration in the bianalytic Fock space*, publicly available research note (2026); comparison restricted to the Gaussian Fock-space theorem.
