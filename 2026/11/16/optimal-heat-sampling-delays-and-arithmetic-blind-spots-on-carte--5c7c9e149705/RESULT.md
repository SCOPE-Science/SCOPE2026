# Optimal heat-sampling delays and arithmetic blind spots on Cartesian graph strips

## Finding
Let \(d\ge1\) and \(m\ge2\) be integers. On the Cartesian graph \(G_{d,m}=\mathbb Z^d\square P_m\), use the **combinatorial** graph Laplacian \(L\) (unit conductances), and observe at a fixed transverse vertex \(a\in\{0,\ldots,m-1\}\), for every base cell \(n\in\mathbb Z^d\), the heat samples
\[
y_k(n)=(e^{-k\tau L}f)(n,a),\qquad k=0,\ldots,p-1,\quad\tau>0.\]
Here \(p\) is the number of temporal observations per cell and \(f\) is an arbitrary element of \(\ell^2(G_{d,m})\). Set \(g=\gcd(2a+1,m)\). The measurement operator has Fourier-fiber rank exactly
\[
\boxed{\min\left\{p,m-\frac{g-1}{2}\right\}.}
\]
Thus all signals are stably recoverable **if and only if** \(g=1\) and \(p\ge m\). In particular, one endpoint sensor and exactly \(m\) snapshots always suffice; fewer snapshots cannot suffice for an arbitrary signal.

For endpoint sampling with exactly \(m\) snapshots, put
\[
\mu_j=2-2\cos(\pi j/m),\quad 0\le j<m,\qquad C_m=\frac{m(m-1)}2.
\]
The worst-fiber square-root information determinant (the minimum absolute measurement determinant over all longitudinal Fourier frequencies) is
\[
\boxed{\mathcal D_{d,m}(\tau)=W_m e^{-4d C_m\tau}
\prod_{0\le i<j<m}\left(e^{-\tau\mu_i}-e^{-\tau\mu_j}\right),}
\]
where \(W_m=m^{-1/2}\prod_{j=1}^{m-1}\bigl(\sqrt{2/m}\cos(\pi j/(2m))\bigr)>0\). For each \(d,m\), this quantity has a **unique** maximum at the positive solution \(\tau_{d,m}\) of
\[
\boxed{\sum_{0\le i<j<m}
\frac{\mu_j-\mu_i}{e^{\tau_{d,m}(\mu_j-\mu_i)}-1}
=2dm(m-1)+\sum_{0\le i<j<m}\mu_i.}
\]
For \(m=2\), including the smallest two-rail ladder, this optimum is already finite:
\[
\boxed{\tau_{d,2}=\tfrac12\log\left(1+\tfrac1{2d}\right).}
\]

There is also an exact wide-strip limit. Define \(\mu(u)=2-2\cos(\pi u)\) and
\[
I(t)=\int_0^1\int_u^1
\frac{\mu(v)-\mu(u)}{e^{t(\mu(v)-\mu(u))}-1}\,dv\,du,
\]
with diagonal value \(1/t\). For every fixed integer \(d\ge1\), let \(s_d>0\) denote the **unique** solution of
\[
\boxed{I(s_d)=2d+1-\frac4{\pi^2}.}
\]
Then, as \(m\to\infty\),
\[
\boxed{\tau_{d,m}=s_d+\frac{c_d}{m}+O_d(m^{-2}),\qquad
c_d=-\frac{2d+2-1/(2s_d)}{I'(s_d)}>0.}
\]
For \(d=1\), \(s_1\approx0.168232381922\) and \(c_1\approx0.058731801423\). In addition, as \(d\to\infty\),
\[
\boxed{s_d=\frac1{4d+2}+\frac1{24(2d+1)^3}+O(d^{-5}).}
\]
These are determinant-optimal *uniform* observation delays; they do not purport to maximize the smallest frame bound or optimize nonuniform time grids.

## Assumptions and scope
The finite path \(P_m\) has vertices \(0,\ldots,m-1\), joined by edges \(a\sim a+1\). The base \(\mathbb Z^d\) has nearest-neighbor edges in each coordinate. \(L\) is the usual degree-minus-adjacency operator on \(\ell^2(G_{d,m})\); it is **not** the normalized Laplacian. Measurements are raw point values with no spatial or temporal rescaling. The measurement objective is the essential infimum of the absolute determinant of the \(m\)-by-\(m\) Fourier-fiber analysis matrix at a fixed endpoint, equivalently the square root of the worst-fiber Gram determinant. In an equal-noise model, maximizing it maximizes the worst-fiber information volume within this design class.

The transverse observation location \(a\) is fixed for every cell and time; all base cells are sampled. The rank and stable-recovery criterion allow arbitrary \(p\ge1\). The D-optimal statement uses precisely \(p=m\) and \(a=0\) (the reflected endpoint is identical). All limits with \(m\to\infty\) hold for each **fixed** \(d\); the displayed large-\(d\) expansion concerns the subsequent limit of the limiting constant \(s_d\).

## Proof
**1. Fourier and path spectral reduction.** Let \(\theta\in[-\pi,\pi]^d\). The unitary Fourier transform in the base variables diagonalizes the base Laplacian with scalar symbol
\[
\lambda(\theta)=2\sum_{r=1}^d(1-\cos\theta_r),\qquad 0\le\lambda(\theta)\le4d.
\]
The transverse path Laplacian has simple eigenvalues \(\mu_j\) above and an orthonormal eigenbasis
\[
v_0(a)=m^{-1/2},\qquad
v_j(a)=\sqrt{2/m}\cos\bigl(\pi j(a+1/2)/m\bigr),\quad1\le j<m.
\]
The eigenvalue equation at interior and endpoint vertices follows directly from the cosine addition formula; orthonormality follows by finite cosine orthogonality (or direct summation of the displayed products). Therefore the Fourier-fiber observation matrix, with \(p\) rows, has entries
\[
U_{kj}^{(a)}(\theta,\tau)=v_j(a)e^{-k\tau(\lambda(\theta)+\mu_j)},
\qquad 0\le k<p,\;0\le j<m.
\]
It factors as an invertible diagonal row matrix \(\operatorname{diag}(e^{-k\tau\lambda(\theta)})\), followed by a temporal Vandermonde matrix with nodes \(e^{-\tau\mu_j}\) and column amplitudes \(v_j(a)\). These nodes are distinct for every \(\tau>0\).

**2. Exact arithmetic visibility and complete stable recovery.** An amplitude \(v_j(a)\), for \(j>0\), vanishes exactly when \(j(2a+1)=m(2\ell+1)\) for some integer \(\ell\). Write \(g=\gcd(2a+1,m)\), \(2a+1=gA\), \(m=gB\), with \(A,B\) coprime. Since \(2a+1\) and \(g\) are odd, so is \(A\). The zero indices are exactly \(j=Bq\) for odd \(q\in\{1,3,\ldots,g-2\}\), and number \((g-1)/2\). All remaining columns are weighted distinct-node Vandermonde columns, so their rank with \(p\) rows is \(\min\{p,m-(g-1)/2\}\), independent of \(\theta\).

If this rank is less than \(m\), a fixed nonzero kernel vector multiplied by any nonzero square-integrable base Fourier function gives an invisible signal, so sampling is not injective. If rank is \(m\), necessarily \(g=1\) and \(p\ge m\). The finite Vandermonde matrix has a positive least singular value; the row scaling stays between \(e^{-4d(p-1)\tau}\) and one uniformly over \(\theta\). Plancherel therefore gives uniform positive upper and lower frame bounds and stable recovery of every \(\ell^2\) signal. This proves necessity and sufficiency, not just fiberwise injectivity.

**3. Sharp frame endpoints and determinant.** For \(a=0\) and \(p=m\), all column amplitudes \(w_j=v_j(0)\) are positive. Write \(V(\tau)_{kj}=w_j e^{-k\tau\mu_j}\) and \(D_z=\operatorname{diag}(e^{-k\tau z})\). The fiber matrix is \(U(\theta)=D_{\lambda(\theta)}V\). If \(0\le z_1\le z_2\le4d\), then
\[
V^*D_{z_2}^2V\preceq V^*D_{z_1}^2V.
\]
Hence the exact lower and upper frame bounds are respectively \(\lambda_{\min}(V^*D_{4d}^2V)\) and \(\lambda_{\max}(V^*V)\). Equality at the extremal frequencies holds in the essential-infimum/supremum sense by continuity. The Vandermonde determinant and \(\sum_{k=0}^{m-1}k=C_m\) give the displayed formula for \(\mathcal D_{d,m}\) and show its worst fiber is \(\theta=(\pi,\ldots,\pi)\).

**4. A unique optimal delay at every width.** Define \(\Delta_{ij}=\mu_j-\mu_i>0\). The logarithm of \(\mathcal D_{d,m}\), up to an additive constant, is
\[
\ell(\tau)=-4dC_m\tau-
\tau\sum_{i<j}\mu_i+
\sum_{i<j}\log(1-e^{-\tau\Delta_{ij}}).
\]
Its derivative is the difference of the two sides of the boxed finite stationarity equation, and its second derivative is
\[
\ell''(\tau)=-\sum_{i<j}\frac{\Delta_{ij}^2e^{\tau\Delta_{ij}}}
{(e^{\tau\Delta_{ij}}-1)^2}<0.
\]
Thus \(\ell'\) decreases strictly from \(+\infty\) at zero to \(-4dC_m-\sum_{i<j}\mu_i<0\) at infinity. There is precisely one stationary point, necessarily the unique global maximizer. When \(m=2\), \(\mu_0=0\), \(\mu_1=2\), and the equation reduces to \(2/(e^{2\tau}-1)=4d\), yielding the elementary formula. The longitudinal high-frequency penalty supplies a finite optimum even for two vertical modes.

**5. Wide-strip limit, including its first correction.** Let \(u_i=i/m\), \(\mu_i=\mu(u_i)\), and set \(F_t(z)=z/(e^{tz}-1)\), continuously extended by \(F_t(0)=1/t\). Dividing the stationarity equation by \(m^2\) and applying triangular Riemann sums gives, uniformly for \(t\) in compact positive intervals,
\[
\frac1{m^2}\sum_{i<j}F_t(\mu_j-\mu_i)\longrightarrow I(t),\qquad
\frac1{m^2}\sum_{i<j}\mu_i\longrightarrow
J:=\int_0^1(1-u)\mu(u)du=1-\frac4{\pi^2}.
\]
The function \(I\) is continuous and strictly decreasing from \(+\infty\) to zero, since \(F_t(z)\) has these properties for every fixed \(z\ge0\). Therefore the limiting equation \(I(s_d)=2d+J\) has exactly one positive root and the finite roots converge to it by monotone bracketing.

For completeness, the needed **two-term triangular summation estimate**, for every smooth \(h\) on \(\{0\le u\le v\le1\}\), is
\[
\sum_{0\le i<j<m}h(u_i,u_j)
=m^2\iint_{u<v}h(u,v)\,du\,dv
+\frac m2\left[\int_0^1h(0,v)dv-\int_0^1h(u,1)du-\int_0^1h(u,u)du\right]+O_h(1).
\]
To verify it, first apply the ordinary trapezoidal Euler summation formula to the inner sum over \(j=i+1,\ldots,m-1\), then to the outer sum over \(i\); smoothness gives a uniform bounded total remainder. Apply this with \(h_t(u,v)=F_t(\mu(v)-\mu(u))\). The first two boundary integrals coincide because \(\mu(1-u)=4-\mu(u)\); the diagonal integral equals \(1/t\). Uniformly for \(t\) in compact subsets of \((0,\infty)\),
\[
\sum_{i<j}F_t(\mu_j-\mu_i)=m^2I(t)-\frac m{2t}+O_t(1).
\]
Similarly, ordinary Euler summation applied to \((1-u)\mu(u)\) and \(\mu(u)\) yields
\[
\sum_{i<j}\mu_i=m^2J-2m+O(1).
\]
Substituting into the stationarity equation gives
\[
I(\tau_{d,m})-(2d+J)+\frac{2d+2-1/(2\tau_{d,m})}{m}=O_d(m^{-2}).
\]
Since \(I'(s_d)<0\), the mean-value theorem and a Taylor expansion give the asserted \(m^{-1}\) correction and \(O_d(m^{-2})\) remainder. To prove its coefficient is positive, note the elementary inequality \(z/(e^{tz}-1)\ge1/t-z/2\) for \(z\ge0\). At \(t_0=1/[4(d+1)]\), since \(0\le\mu(v)-\mu(u)\le4\),
\(I(t_0)\ge 1/(2t_0)-1=2d+1>2d+1-4/\pi^2\).
Thus \(s_d>t_0\), implying \(2d+2-1/(2s_d)>0\) and hence \(c_d>0\).

**6. High-dimensional longitudinal asymptotics.** Uniformly for \(0\le z\le4\) and sufficiently small positive \(t\), the Bernoulli expansion gives
\(F_t(z)=t^{-1}-z/2+tz^2/12+O(t^3)\), with the remainder uniform in \(z\). Direct integration over \(0<u<v<1\) shows \(\iint(\mu(v)-\mu(u))=8/\pi^2\) and \(\iint(\mu(v)-\mu(u))^2=2\). Therefore
\[
I(t)=\frac1{2t}-\frac4{\pi^2}+\frac t6+O(t^3).
\]
Solving \(I(s_d)=2d+1-4/\pi^2\) by the unique-root equation, with \(Q=2d+1\), gives \(s_d=(2Q)^{-1}+(24Q^3)^{-1}+O(Q^{-5})\). This is the displayed large-\(d\) formula.

## Verification
The accompanying standard-library `CHECK.py` independently reconstructs finite path eigenvector equations and orthogonality, checks the complete arithmetic blind-mode counts, compares direct Gaussian-elimination determinants with the Fourier/Vandermonde product, brackets the unique finite optimizer across widths and base dimensions, and evaluates selected continuum roots. Running `python3 CHECK.py` from the package returns `VERIFY_OK 5663 supplementary_assertions`. High-precision independent quadrature of the exact integral equation gives the quoted \(d=1\) numerical constants. Finite computations support but do not establish the infinite-width and all-dimension assertions: those follow from the analytic argument above.

## Relationship to prior work
Bulai, Cabrelli, Cordero, Molter and Saliani, *Dynamical Sampling in Graph Paley–Wiener Spaces*, arXiv:2609.25472v1 (first publicly submitted September 21, 2026), treat graph spectral sampling, lattice Fourier analysis, and numerical examples on finite paths. The presently established claim concerns the full signal space on **infinite Cartesian strips**, an exact arithmetic visibility criterion, the sharp worst-fiber information determinant, the uniquely optimal raw heat-sampling interval, and its first-order wide-strip correction. The full text of that motivating manuscript was inaccessible through the available lawful routes, so any overlap beyond its published abstract remains a specific priority risk.

The full text of Aldroubi, Cabrelli, Krishtal and Molter, *Dynamical Sampling: A Survey* (2026), gives the general finite-dimensional eigenvector-visibility and frame-of-iterates criteria. Those imply qualitative recovery once the strip is fiberized, but do not supply this strip's arithmetic rank formula or sharp worst-fiber optimization and continuum correction. Published mathematical results entitled *Optimal heat-sampling intervals on normalized paths: a bandwidth crossover* and *Universal endpoint optimality for dynamical sampling on normalized paths* solve related finite **normalized-path** questions. Their path operators, objectives and limiting formulas are not the claimed \(\mathbb Z^d\square P_m\) **combinatorial-Laplacian** worst-fiber design; the additional longitudinal high-frequency penalty changes even the two-mode existence of a finite optimum. The earlier techniques and elementary Vandermonde identities are not claimed as new. A published arithmetic-spectrum two-observable delay theorem likewise concerns a different confluent-Vandermonde model, rather than this path-eigenvalue limit.

## Limitations
The optimization is restricted to one fixed endpoint rail, uniform sampling times, all base cells, and exactly one temporal measurement per transverse mode. It does not compare arbitrary nonuniform clocks, alternative sensor mixes, randomized sampling, or the smallest frame eigenvalue. The stability bounds are exact spectral-matrix formulas rather than elementary radicals for arbitrary width. Continuum approximations are asymptotic in transverse width at fixed longitudinal dimension. The spectral visibility factorization uses the combinatorial graph Laplacian; replacing it by the normalized Laplacian of the nonregular strip changes the model. The motivating preprint's inaccessible complete text and possible older equivalent Cartesian-product observability formulas remain bibliographic risks. No independent mathematical audit is asserted.

## References
1. I. M. Bulai, C. Cabrelli, E. Cordero, U. Molter and S. Saliani, *Dynamical Sampling in Graph Paley–Wiener Spaces*, arXiv:2609.25472v1 (2026-09-21), https://arxiv.org/abs/2609.25472.
2. A. Aldroubi, C. Cabrelli, I. Krishtal and U. Molter, *Dynamical Sampling: A Survey*, La Matematica 5, article 37 (2026), https://doi.org/10.1007/s44007-026-00215-y.
3. *Optimal heat-sampling intervals on normalized paths: a bandwidth crossover*, published mathematical record (2026-11-01), available in the published-finding corpus public mathematical results collection.
4. *Universal endpoint optimality for dynamical sampling on normalized paths*, published mathematical record (2026-10-11), available in the published-finding corpus public mathematical results collection.
5. *A universal optimal observation horizon for arithmetic-spectrum flows*, published mathematical record (2026-10-11), available in the published-finding corpus public mathematical results collection.
