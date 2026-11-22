# Unique worst-direction one-point sensing of the first two heat modes

## Finding
Let \(K=\begin{pmatrix}a&b\\b&c\end{pmatrix}\) be any real symmetric positive-definite \(2\times2\) matrix. For a point \(x\in[0,1]\), define the two-mode information matrix
\[
G_K(x)=\operatorname{diag}(\sin\pi x,\sin 2\pi x)\,K\,\operatorname{diag}(\sin\pi x,\sin 2\pi x).
\]
There are **exactly two** global maximizers of \(\lambda_{\min}(G_K(x))\): \(x_K\in(0,1/2)\) and \(1-x_K\). A globally convergent one-dimensional characterization uses \(u_K=\cos^2(\pi x_K)\): it is the **unique** minimizer on \(0<u<1\) of
\[
\Phi_K(u)=\frac{1}{(ac-b^2)(1-u)}\lambda_{\max}\begin{pmatrix}c&|b|/(2\sqrt u)\\|b|/(2\sqrt u)&a/(4u)\end{pmatrix}.
\]
Furthermore \(\log\Phi_K(e^z/(1+e^z))\) is **strictly convex** on the whole real line. Thus this two-mode spatial E-optimal design has no spurious interior local optima after logit reparameterization, for every positive-definite temporal information matrix.

For the heat dynamics on \((0,1)\) with Dirichlet endpoints, normalized diffusivity \(1/\pi^2\), and initial state \(v(x,0)=\alpha_1\sin(\pi x)+\alpha_2\sin(2\pi x)\), continuously observe \(v(x,t)\) at one spatial location over \([0,T]\), \(T>0\). The information entries are
\[
a_T=\frac{1-e^{-2T}}2,\qquad b_T=\frac{1-e^{-5T}}5,\qquad c_T=\frac{1-e^{-8T}}8.
\]
For its optimal \(u_T\),
\[
\lim_{T\downarrow0}u_T=\frac{\sqrt5-1}{4},\qquad
\lim_{T\to\infty}u_T=u_\infty,
\]
where \(u_\infty\) is the unique root in \((0,1)\) of
\[
50u^3+19u^2+4u-9=0\qquad(u_\infty=0.42563099964867\ldots).
\]
Consequently the left-optimal spatial point changes between the sharp limits \(0.312376431107\ldots\) and \(0.273760552610\ldots\) as the horizon changes. This is a statement about limits, **not** an assertion of monotonic motion for all horizons.

## Assumptions and scope
The two modal amplitudes have the standard Euclidean norm, and the observation-energy norm is \(L^2(0,T)\) for the heat specialization. There is a single fixed spatial point observed over a continuous time interval, not an optimized finite collection of temporal samples. \(K\) may arise from any two real linearly independent temporal profiles \(f_1,f_2\), via \(K_{ij}=\int f_i(t)f_j(t)\,dt\); positivity is the only hypothesis needed for the general uniqueness claim. No measurement-noise prior or temporal normalization is assumed. The common \(\sqrt2\) normalization of the sine eigenfunctions multiplies the entire information matrix by \(2\) without changing the design.

## Proof
**1. Exact information matrix.** Reflecting \(x\mapsto1-x\) preserves both eigenvalues because \(\sin(\pi x)\) is unchanged and \(\sin(2\pi x)\) changes sign. For \(0<x<1/2\), set \(u=\cos^2(\pi x)\). The elementary sine identities give
\[
G_K(x)=(1-u)\begin{pmatrix}a&2b\sqrt u\\2b\sqrt u&4cu\end{pmatrix}.
\]
Its determinant is \(4(ac-b^2)u(1-u)^2\), positive exactly for \(0<u<1\). At \(u=0\) (the midpoint) and \(u=1\) (the endpoints), the smallest eigenvalue is zero. Hence every optimizer is interior.

**2. Inversion and the strict convexity certificate.** Put \(\Delta=ac-b^2>0\). Matrix inversion followed, if necessary, by an orthogonal diagonal sign change gives
\[
\lambda_{\min}(G_K(x))^{-1}=\Phi_K(u)
=\lambda_{\max}\!\left[\frac1{\Delta(1-u)}
\begin{pmatrix}c&|b|/(2\sqrt u)\\|b|/(2\sqrt u)&a/(4u)\end{pmatrix}\right].
\]
Let \(z=\log(u/(1-u))\). Except for positive constant factors, the entries of the symmetric, entrywise nonnegative matrix are
\[
f_{11}(z)=1+e^z,\quad
f_{12}(z)=(1+e^z)^{3/2}e^{-z/2},\quad
f_{22}(z)=(1+e^z)^2e^{-z}.
\]
Their logarithmic second derivatives are, respectively, \(s(z)\), \(3s(z)/2\), and \(2s(z)\), where \(s(z)=e^z/(1+e^z)^2>0\). On each compact \(z\)-interval, all nonzero entries therefore enjoy a **common positive strict log-convexity margin**. For each nonnegative unit vector \(w\), its Rayleigh quadratic form is a positive sum of these entries with nonnegative coefficients. Hölder's inequality preserves this common strict margin under summation. Since an entrywise nonnegative symmetric matrix has a nonnegative maximizing eigenvector, taking the supremum of these Rayleigh forms preserves the same strict margin. Hence \(z\mapsto\log\Phi_K(e^z/(1+e^z))\) is strictly convex, including the diagonal case \(b=0\). As \(z\to+\infty\), the top-left diagonal entry diverges, and as \(z\to-\infty\), the bottom-right diverges. A unique finite minimizing logit, and therefore a unique \(u_K\in(0,1)\), follows. Reflection gives exactly two physical locations.

**3. Heat specialization and the short-horizon limit.** The heat modes decay as \(e^{-t}\) and \(e^{-4t}\). Their Gram matrix has the stated entries and \(\Delta_T>0\) by strict Cauchy–Schwarz. Writing \(\Lambda_T(u)\) for the smaller information eigenvalue yields the stable identity
\[
\Lambda_T(u)=\frac{8u(1-u)\Delta_T}{a_T+4c_Tu+\sqrt{(a_T-4c_Tu)^2+16b_T^2u}}.
\]
Taylor expansion gives \(\Delta_T=3T^4/4+O(T^5)\). It follows uniformly on \(u\in[0,1]\) that
\[
T^{-3}\Lambda_T(u)\longrightarrow \frac{3u(1-u)}{1+4u}.
\]
The limiting function has its unique maximum at \(u_0=(\sqrt5-1)/4\), obtained from \(1-2u-4u^2=0\). Uniform convergence on the compact design interval and uniqueness of the finite-horizon optimizers imply \(u_T\to u_0\).

**4. Infinite-horizon limit.** As \(T\to\infty\), \((a_T,b_T,c_T)\to(1/2,1/5,1/8)\), and the information matrices converge uniformly on \([0,1]\), so the unique maximizers converge to the unique optimizer of the limiting problem. There \(\Delta=9/400\). Write its characteristic polynomial for an eigenvalue \(\ell\) as \(F(\ell,u)=\ell^2-S(u)\ell+P(u)\), with \(S=(1-u)(1/2+u/2)\), \(P=9u(1-u)^2/100\). At an interior optimum of the simple smaller eigenvalue, \(F=\partial_uF=0\). Eliminating \(\ell\) gives the necessary equation \(50u^3+19u^2+4u-9=0\). Its derivative is \(150u^2+38u+4>0\) for \(u\ge0\), and it changes sign between zero and one. The unique interior optimizer must therefore equal the stated root.

## Verification
Run `python verify.py` with `sympy` installed. It checks the exact resultant identity and short-horizon coefficient, plus 20,610 finite numerical inequalities and inverse identities over ten horizons. These computations are supplementary: the all-matrix strict convexity and global uniqueness are proved analytically above. The actual standalone source, not an external log, is included with this result.

## Relationship to prior work
Geshkovski and Zuazua (2021) analyze finite-dimensional scalar actuator design through a Brunovský-form change of coordinates; their optimization is over unconstrained actuator directions with a different cost reduction, not the spatial sine profile or the stated time-dependent point-sensor E-design. Privat, Trélat and Zuazua (2014) optimize positive-measure observation domains with random-initial-data averaging, which eliminates modal cross terms; the present one-point worst-direction information retains those terms. Wolf, Moura and Krstić (2012) optimize a modal amplitude observability criterion via numerical sensor placement, not the integrated two-mode Gramian's minimum eigenvalue. Kang and Xu (2013) use minimum Gramian eigenvalues to discuss partial observability but do not optimize this precise location. These distinctions identify different mathematical objectives; they are not proofs of absolute publication priority.

## Limitations
Only the first two sine modes are covered by the spatial claim. The finite-horizon result does not assert monotonic motion in time, and does not extend the unique-minimum theorem to higher Fourier modes, multiple sensors, temporally discrete samples, spatially varying diffusivity, or nonlinear/uncertain dynamics. The general positive-definite matrix theorem requires the specified two sine sensing gains. Relevant broader literature or a previously implicit application of log-convex Perron-root theory may contain equivalent uniqueness conclusions; the priority comparison is not an independent audit.

## References
1. B. Geshkovski and E. Zuazua, *Optimal actuator design via Brunovsky's normal form*, arXiv:2108.05629, first posted 12 August 2021. https://arxiv.org/abs/2108.05629
2. Y. Privat, E. Trélat and E. Zuazua, *Optimal shape and location of sensors for parabolic equations with random initial data*, arXiv:1403.6445, first posted 25 March 2014. https://arxiv.org/abs/1403.6445
3. P. Wolf, S. Moura and M. Krstić, *On Optimizing Sensor Placement for Spatio-Temporal Temperature Estimation in Large Battery Packs*, CDC 2012. https://ecal.studentorg.berkeley.edu/pubs/CDC12-PDESensorPlacementBatts.pdf
4. W. Kang and L. Xu, *Partial Observability and Its Consistency for Linear PDEs*, IFAC NOLCOS 2013. https://skoge.folk.ntnu.no/prost/proceedings/nolcos-2013/papers/0011.pdf
5. J. A. Burns and T. L. Herdman, *Optimal Sensor Placement for Observer Design*, IFAC-PapersOnLine 54(9), 446–451 (2021), DOI:10.1016/j.ifacol.2021.06.102. https://doi.org/10.1016/j.ifacol.2021.06.102
